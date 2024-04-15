import os
import sys
import datetime
from PyPDF2 import PdfReader

with open("ocr.config", 'r') as f:
    conf = f.readlines()
    f.close()

tpath = conf[3].strip().split("=")[-1]

cfile = sys.argv[1]

fnsplit = cfile.split("/")[-1]
outname = tpath + fnsplit[:-4] + ".txt"

if not os.path.isfile(outname):

    try:
        reader = PdfReader(cfile)

        with open(outname, 'w', encoding='utf-8') as f:
            for i in range(len(reader.pages)):
                pg = reader.pages[i]
                page = pg.extract_text()
                if i == 0:
                    f.write("-P-A-G-E-" + str(i+1) + "\n")
                else:
                    f.write("\n-P-A-G-E-" + str(i+1) + "\n")
                f.write(page)
            f.close()

        with open("textract.log", 'a+', encoding='utf-8') as f:
            f.write(str(datetime.datetime.now()) + " --- " + cfile + " --- SUCCESSFUL\n")
            f.close()

    except:
        with open("textract.log", 'a+', encoding='utf-8') as f:
            f.write(str(datetime.datetime.now()) + " --- " + cfile + " --- FAILED\n")
            f.close()