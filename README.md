# nlp_code

<h1>CSCI 6350 - Selected Topics in Artificial Intelligence: Natural Language Processing - Spring 2024</h1>
<h1>Source Code and Data Results for Term Project</h1>
<h2>Matthew I. Swindall</h2>
<h2>Middle Tennessee State University</h2>

<p>
Directory Details
<ul>
<li>nlp_code/
<li>    nlp/			Source code for the NLP process
<li>        topics/				Output files for the NLP process are saved to this directory
<li>        Demonstration.ipynb		A Jupyter notebook to demonstrates the individual python modules developed for this project
<li>        ldatops.py			Python model written to perform topic extraction using Latend Dirichlet Association
<li>        ngrams.py			Python model written to perform topic extraction using N-gram models
<li>        parse.py			Python model written to perform pre-processing of text files
<li>        run_bert.py			Python model written to perform topic extraction using BERTopic
<li>        run_spacy.py			Python model written to perform Named Entity Recognition using the spaCy library
<li>        topics.py			Main Python module that performs all NER and topic extraction. Executed as < python topics.py path_to_pdf_file >
<li>    ocr/			Source code for the OCR process
<li>        output/				OCR and text extraction files will be output to this directory
<li>        pdf_samples/			A small sample of books (PDF files) from the corpus
<li>        tmp/				Directory for temporary, single page PDF files. Necessary for the OCR process. If dir is deleted, OCR will fail
<li>        extractor.py			Program that extracts text from PDF files after the OCR process. Executed as < python extractor path_to_pdf_file >
<li>        pdf_ocr.py			Program that performs OCR on a given PDF file. Executed as < python pdf_ocr.py path_to_pdf_file >
<li>        ocr.config			A configuration file with path details. Current paths are relative
<li>    text_files/				Text files extracted from pdf files after the OCR process
<li>    topics/				Text files produced as an imtermediate step of processing. One file for each book containing the model outputs
<li>    Project_Results_formatted.xlsx	Results from topics and named enteties extraction from book corpus. Formatted for easier inspection
<li>    Project_Results.csv			Results from topics and named enteties extraction from book corpus
<li>    requirements.txt			Python dependencies
<li>    setup.sh				Bash script that install necessary dependencies (Except for Tesseract) Executed as < ./setup.sh >
<li>    README.md				This file
</ul>
</p>