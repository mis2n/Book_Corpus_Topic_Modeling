from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired
from bertopic.representation import MaximalMarginalRelevance

def get_bert(sents):
    #vectorizer_model = CountVectorizer(stop_words="english")
    representation_model = KeyBERTInspired()
    topic_model = BERTopic(representation_model=representation_model)

    topics, probs = topic_model.fit_transform(sents)

    ntops = len(topic_model.get_topics())

    btops = []
    bprob = []
    counts = []

    for i in range(ntops-1):
        ctops = topic_model.get_topic(i)
        for j in range(len(ctops)):
            t, p = ctops[j][0], ctops[j][1]
            if t in btops:
                dex = btops.index(t)
                counts[dex] += 1
                bprob[dex] += p
            else:
                btops.append(t)
                bprob.append(p)
                counts.append(1)

    for i in range(len(bprob)):
        bprob[i] = bprob[i] / counts[i]

    return btops, bprob