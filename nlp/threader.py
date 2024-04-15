import os
import multiprocessing
import random

nthreads = 4
fpath = "/mnt/share/matt/text_files/"
tpath = "/mnt/share/matt/nlp/topics/"

def run_extractor(n):
    #cmnd = "python topics.py " + str(n)
    cmnd = "python fix_spacy.py " + str(n)
    #cmnd = "python summarizer.py " + str(n)
    #print(cmnd)
    os.system(cmnd)

fnames_ = []
for (root, dirs, files) in os.walk(fpath, topdown=True):
    for fname in files:
        fnames_.append(str(os.path.join(root, fname)))

parsed = []
for (root, dirs, files) in os.walk(tpath, topdown=True):
    for fname in files:
        parsed.append(str(os.path.join(root, fname)))

fnames = []
for i in range(len(fnames_)):
    nn = tpath + fnames_[i].split("/")[-1][:-8] + ".dat"
    #if not os.path.isfile(nn): # run only files that don't exist in output dir
    if os.path.isfile(nn): # run only files that DO exist in output dir
        fnames.append(fnames_[i])

random.shuffle(fnames)

numb = len(fnames)
nmax = int(numb / nthreads)

if numb % nthreads == 0:
    remain = 0
if numb % nthreads != 0:
    remain = numb - ((nmax) * nthreads)

i = 0
z = 0
inc = 0
while z < nmax:
    jobs = []
    for i in range(nthreads):
        cfn = fnames[i+inc]
        process = multiprocessing.Process(target=run_extractor, args=([cfn]))
        jobs.append(process)
        i += 1

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    z += 1
    inc += nthreads
    
# print("processing leftovers")

jobs = []
for k in range(remain):
    cfn = fpath + fnames[k+inc]
    print(inc, k, k+inc)
    process = multiprocessing.Process(target=run_extractor, args=([cfn]))
    jobs.append(process)

for j in jobs:
    j.start()

for j in jobs:
    j.join()

