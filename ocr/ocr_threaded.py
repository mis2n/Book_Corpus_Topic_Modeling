import os
import sys
import datetime
from PIL import Image
import pandas as pd
import pytesseract
from PyPDF2 import PdfMerger
from pdf2image import convert_from_path, convert_from_bytes

with open("ocr.config", 'r') as f:
    conf = f.readlines()
    f.close()

tpath = conf[2].strip().split("=")[-1]

# files = os.listdir(fpath)

cfile = sys.argv[1]

# print(cfile)

st = datetime.datetime.now()
try:
    fnsplit = cfile.split("/")[-1]
    outname = tpath + fnsplit[:-4] + "_ocr.pdf"
    PIL_objects = convert_from_path(cfile)

    # Perfomr OCR on pdf pages
    pdfs = []
    for j in range(len(PIL_objects)):
        cpdf = pytesseract.image_to_pdf_or_hocr(PIL_objects[j], extension='pdf')
        pdfs.append(cpdf)

    # Build PDF page files, then merge into single PDF
    pdfiles = []

    for k in range(len(pdfs)):
        cfn = "./tmp/" + fnsplit[:-4] + "_merge_" + str(k) + ".pdf"
        pdfiles.append(cfn)
        with open(cfn, 'w+b') as f:
            f.write(pdfs[k])
        f.close()

    merger = PdfMerger()

    for tem in pdfiles:
        merger.append(tem)
        os.remove(tem)

    merger.write(outname)
    merger.close()

    with open("ocr.log", 'a+') as f:
        f.write(str(datetime.datetime.now()) + " --- " + cfile + " --- SUCCESSFUL\n")
        
    fin = datetime.datetime.now()
    with open("timing.log", 'a+') as f:
        f.write(str(fin - st) + "\n")

except:
    with open("ocr.log", 'a+') as f:
        f.write(str(datetime.datetime.now()) + " --- " + cfile + " --- FAILED\n")
