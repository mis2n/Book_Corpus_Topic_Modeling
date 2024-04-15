import string 
import nltk 
# nltk.download('punkt') 
# nltk.download('stopwords') 
# nltk.download('reuters') 
from nltk.corpus import reuters 
from nltk import FreqDist 
from nltk.corpus import stopwords
from nltk import ngrams

def get_grams(sents):
    nsents = sents
    stop_words = set(stopwords.words('english')) 

    string.punctuation = string.punctuation +'"'+'"'+'-'+'''+'''+'—'+',' 
    string.punctuation 
    removal_list = list(stop_words) + list(string.punctuation)+ ['lt','rt']

    for i in range(len(sents)):
        curr = nsents[i].lower()
        if curr[-1] in ".?!,":
            curr = curr[:-1]
        
        currsplit = curr.split(" ")

        rems = []
        for j in range(len(currsplit)):
            if currsplit[j] in removal_list:
                rems.append(j)
        rems.reverse()
        for r in rems:
            del currsplit[r]
        cs = " ".join(currsplit) + "."
        cs = cs.replace(",", "")
        nsents[i] = cs

    unigram=[] 
    bigram=[] 
    trigram=[] 
    tokenized_text=[] 
    for i in range(len(nsents)):
        sentence = nsents[i].strip(".").split()
        for word in sentence:
            unigram.append(word) 
        
        tokenized_text.append(sentence) 
        bigram.extend(list(ngrams(sentence, 2,pad_left=True, pad_right=True))) 
        trigram.extend(list(ngrams(sentence, 3, pad_left=True, pad_right=True)))

    # generate frequency of n-grams 
    freq_uni = FreqDist(unigram)
    freq_bi = FreqDist(bigram) 
    freq_tri = FreqDist(trigram) 

    # generate 25 most frequent unigrams and their probabilites
    uni = freq_uni.most_common(25)

    uni_topics = []
    uni_counts = []
    uni_probs = []

    for i in range(len(uni)):
        uni_topics.append(uni[i][0])
        uni_counts.append(uni[i][1])

    count_tot = sum(uni_counts)
    #print(uni_counts)

    for i in range(len(uni_counts)):
        uni_probs.append(uni_counts[i] / count_tot)

    # generate 25 most frequent bigrams and their probabilites
    bi = freq_bi.most_common(25)

    bi_topics = []
    bi_counts = []
    bi_probs = []

    for i in range(len(bi)):
        grm = ""
        for j in range(2):
            if bi[i][0][j] != None:
                grm += bi[i][0][j] + " "
        bi_topics.append(grm[:-1])
        bi_counts.append(bi[i][1])

    count_tot = sum(bi_counts)
    #print(bi_counts)

    for i in range(len(bi_counts)):
        bi_probs.append(bi_counts[i] / count_tot)

    # generate 25 most frequent trigrams and their probabilites
    tri = freq_tri.most_common(25)

    tri_topics = []
    tri_counts = []
    tri_probs = []

    for i in range(len(tri)):
        grm = ""
        for j in range(3):
            if tri[i][0][j] != None:
                grm += tri[i][0][j] + " "
        tri_topics.append(grm[:-1])
        tri_counts.append(tri[i][1])

    count_tot = sum(tri_counts)
    #print(tri_counts)

    for i in range(len(tri_counts)):
        tri_probs.append(tri_counts[i] / count_tot)

    # Combine all n-grams and probabilities (averaging probabilities)
    all_topics = [uni_topics, bi_topics, tri_topics]
    all_probs = [uni_probs, bi_probs, tri_probs]

    GRAMS = []
    PROBS = []
    COUNTS = []

    for i in range(3):
        ct = all_topics[i]
        cp = all_probs[i]
        for j in range(25):
            if ct[j] not in GRAMS:
                GRAMS.append(ct[j])
                PROBS.append(cp[j])
                COUNTS.append(1)
            else:
                PROBS[j] += cp[j]
                COUNTS[j] += 1

    for i in range(len(PROBS)):
        PROBS[i] = PROBS[i] / max(COUNTS)

    return GRAMS, PROBS