import spacy

nlp = spacy.load('en_core_web_sm')

def get_spacy(book):
    doc = nlp(book)

    labels = ['ORG', 'GPE', 'PERSON', 'NORP', 'LANGUAGE', 'WORK_OF_ART', 'EVENT']
    ents = [[], [], [], [], [], [], []]

    #list.index(item)

    for label in labels:
        dex = labels.index(label)
        for ent in doc.ents:
            if ent.label_ == label:
                ents[dex].append(ent)#.text, ent.label_)

    for i in range(len(ents)):
        entlist = list(set(ents[i]))
        update = []
        for j in range(len(entlist)):
            res = False
            entity = str(entlist[j])
            for k in range(len(entity)):
                if entity[k].isupper():
                    res = True
            if res == True:
                update.append(entity)
        ents[i] = update

    return ents