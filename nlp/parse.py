import os
import re
from textblob import TextBlob

def preprocess(path):
    title = path.split("/")[-1][:-8]

    with open(path, 'r', encoding='utf-8') as f:
        text = f.readlines()
        f.close()

    markers = []
    for i in range(len(text)):
        if "-P-A-G-E-" in text[i]:
            markers.append(i)

    pages = []
    for i in range(len(markers)-1):
        st = markers[i]+1
        en = markers[i+1]
        page_a = text[st:en]
        pg = []
        for a in page_a:
            aout = a.strip("\n“”").lstrip().rstrip()
            if len(aout) > 0:
                alnumct = 0
                for k in range(len(aout)):
                    if aout[k].isalnum():
                        alnumct += 1
                if alnumct > 0:
                    pg.append(aout)
        if len(pg) > 1:
            pages.append(pg)
        else:
            pages.append([])

    st = markers[-1]
    page_a = text[st:]
    pg = []
    for a in page_a:
        aout = a.strip("\n“”").lstrip().rstrip()
        if len(aout) > 0:
            alnumct = 0
            for k in range(len(aout)):
                if aout[k].isalnum():
                    alnumct += 1
            if alnumct > 0:
                pg.append(aout)
    if len(pg) > 1:
        pages.append(pg)
    else:
        pages.append([])

    pages_with_title_header = []

    for i in range(len(pages)):
        if len(pages[i]) > 0:
            if title.lower() in pages[i][0].lower():
                pages_with_title_header.append(i)

    contents_pages = []

    for i in range(len(pages)):
        if len(pages[i]) > 0:
            if "contents" in pages[i][0].lower():
                contents_pages.append(i)
    if len(contents_pages) < 1:
        contents_pages.append(-1)

    preface_pages = []

    for i in range(len(pages)):
        if len(pages[i]) > 0:
            if "preface" in pages[i][0].lower():
                preface_pages.append(i)
    if len(preface_pages) < 1:
        preface_pages.append(-1)

    index_pages = []

    for i in range(len(pages)):
        if len(pages[i]) > 0:
            if "index" in pages[i][0].lower():
                index_pages.append(i)
    if len(index_pages) < 1:
        index_pages.append(999999999999999)
            
    modpages = []

    for j in range(len(pages)):
        if j > preface_pages[-1] and j > contents_pages[-1] and j < index_pages[0]:
            pg = ""
            for i in range(len(pages[j])):
                if len(pages[j][i]) > 0:
                    if pages[j][i][-1] == "-":
                        pg = pg + pages[j][i]
                    else:
                        pg = pg + pages[j][i] + " "
            if len(pg) > 0:
                npg = ""
                for i in range(len(pg)):
                    if pg[i] != "-":
                        npg = npg + pg[i]
                    if pg[-1] == "-":
                        npg = npg + ""
            
                modpages.append(npg)

    book = ""
    for mod in modpages:
        book = book + mod

    if len(book) > 1000000:
        book = book[:1000000] #Spacy will only accept text up to 1,000,000 characters

    tb = TextBlob(book)
    book = str(tb.correct())
    book

    book = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff\xad\x0c6§\\\£\Â*_<>""⎫•{}Γ~]', ' ', book)
    book = re.sub(r'\s', ' ', book)
    book = re.sub(r'\s((I{2,}V*X*\.*)|(IV\.*)|(IX\.*)|(V\.*)|(V+I*\.*)|(X+L*V*I*]\.*))\s', ' ', book)
    book = re.sub(r'\s((i{2,}v*x*\.*)|(iv\.*)|(ix\.*)|(v\.*)|(v+i*\.*)|(x+l*v*i*\.*))\s', ' ', book)
    book = re.sub(r'Tue ', 'The ', book)
    book = re.sub(r'\s+', ' ', book)

    sents = book.split('. ')

    for i in range(len(sents)):
        words = sents[i].split(" ")
        caps = []
        for j in range(len(words)):
            if words[j].isupper():
                caps.append(j)
        caps.reverse()
        for k in range(len(caps)):
            words.pop(caps[k])
        s = ' '.join(map(str, words)) + "."
        sents[i] = s
    
    return book, sents

