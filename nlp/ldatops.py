import gensim
from gensim.utils import simple_preprocess
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
import gensim.corpora as corpora

stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

def get_lda(sents):
    nsents = sents
    ldasents = []
    for i in range(len(nsents)):
        if nsents[i][-1] == ".":
            ldasents.append(nsents[i][:-1])
        else:
            ldasents.append(nsents[i])

    def sent_to_words(sentences):
        for sentence in sentences:
            # deacc=True removes punctuations
            yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
    def remove_stopwords(texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]
    
    data = ldasents
    data_words = list(sent_to_words(data))

    # Create Dictionary
    id2word = corpora.Dictionary(data_words)
    # Create Corpus
    texts = data_words
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    # number of topics
    num_topics = 10
    # Build LDA model
    lda_model = gensim.models.LdaMulticore(corpus=corpus, id2word=id2word, num_topics=num_topics)

    doc_lda = lda_model[corpus]

    tops = []
    prob = []
    for i in range(len(lda_model.print_topics())):
        t = lda_model.print_topics()[i]
        tl = list(t)[1]
        tls = tl.split(" + ")
        for j in range(len(tls)):
            dat = tls[j][:-1].split('*"')
            if dat[1] in tops:
                dex = tops.index(dat[1])
                prob[dex] = prob[dex] + float(dat[0])
            else:
                tops.append(dat[1])
                prob.append(float(dat[0]))

    return tops, prob
