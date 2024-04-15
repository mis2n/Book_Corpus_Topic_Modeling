import os
import sys
import pandas as pd
from ngrams import *
from ldatops import *
from parse import *
from run_bert import *
from run_spacy import *

pth = sys.argv[1]

bookname = pth.split("/")[-1][:-8]
outfile =  "./topics/" + bookname + ".dat"


try:
    book, sents = preprocess(pth)
    grams, gprobs = get_grams(sents)
    ldatops, ldaprobs = get_lda(sents)
    btops, bprobs = get_bert(sents)
    ents = get_spacy(book)

    topics = []
    probs = []
    counts = []

    for i in range(len(grams)):
        if grams[i] in topics:
            dex = topics.index(grams[i])
            probs[dex] += gprobs[i]
            counts[dex] += 1
        else:
            topics.append(grams[i])
            probs.append(gprobs[i])
            counts.append(1)
            

    for i in range(len(ldatops)):
        if ldatops[i] in topics:
            dex = topics.index(ldatops[i])
            probs[dex] += ldaprobs[i]
            counts[dex] += 1
        else:
            topics.append(ldatops[i])
            probs.append(ldaprobs[i])
            counts.append(1)

    for i in range(len(btops)):
        if btops[i] in topics:
            dex = topics.index(btops[i])
            probs[dex] += bprobs[i]
            counts[dex] += 1
        else:
            topics.append(btops[i])
            probs.append(bprobs[i])
            counts.append(1)

    for i in range(len(probs)):
        probs[i] = probs[i] / counts[i]

    for i in range(25):
        print(topics[i], probs[i])

    ner = []
    for i in range(len(ents)):
        for j in range(len(ents[i])):
            if len(ents[i][j].split(" ")) <=3:
                ner.append(ents[i][j])
    ner = list(set(ner))

    book2 = book.lower()
    book2 = re.sub(r'[^\w\s]', '', book2)

    freqs = []
    for i in range(len(ner)):
        ct = book2.count(ner[i].lower())
        freqs.append(ct)

    sf = sum(freqs)
    for i in range(len(freqs)):
        freqs[i] = freqs[i] / sf

    for i in range(len(ner)):
        print(ner[i], freqs[i])

    
    ners = "|".join(map(str, ner))
    freeks = "|".join(map(str, freqs))
    tops = "|".join(topics)
    pros = "|".join(map(str,probs))
    # ent = "|".join(map(str, ents))

    #print(bookname, tops, pros, ent)

    with open(outfile, 'w', encoding='utf-8') as f:
        f.write("***Title\n")
        f.write(bookname + "\n")
        f.write("\n***Topics\n")
        f.write(tops + "\n")
        f.write("\n***Probabilities\n")
        f.write(pros + "\n")
        f.write("\n***NamedEntities\n")
        f.write(ners + "\n")
        f.write("\n***Frequencies\n")
        f.write(freeks + "\n")
        f.write("\n***EOF\n")
        f.close()

except:
    with open("error.log", 'a+', encoding='utf-8') as f2:
        f2.write(pth + "\n")
        f2.close()