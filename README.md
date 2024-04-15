# nlp_code

<h1>CSCI 6350 - Selected Topics in Artificial Intelligence: Natural Language Processing - Spring 2024<\h1>
<h1>Source Code and Data Results for Term Project<\h1>
<h2>Matthew I. Swindall<\h2>
<h2>Middle Tennessee State University<\h2>

<p>
Directory Details

nlp_code/
    nlp/			Source code for the NLP process
        topics/				Output files for the NLP process are saved to this directory
        Demonstration.ipynb		A Jupyter notebook to demonstrates the individual python modules developed for this project
        ldatops.py			Python model written to perform topic extraction using Latend Dirichlet Association
        ngrams.py			Python model written to perform topic extraction using N-gram models
        parse.py			Python model written to perform pre-processing of text files
        run_bert.py			Python model written to perform topic extraction using BERTopic
        run_spacy.py			Python model written to perform Named Entity Recognition using the spaCy library
        topics.py			Main Python module that performs all NER and topic extraction. Executed as < python topics.py path_to_pdf_file >
    ocr/			Source code for the OCR process
        output/				OCR and text extraction files will be output to this directory
        pdf_samples/			A small sample of books (PDF files) from the corpus
        tmp/				Directory for temporary, single page PDF files. Necessary for the OCR process. If dir is deleted, OCR will fail
        extractor.py			Program that extracts text from PDF files after the OCR process. Executed as < python extractor path_to_pdf_file >
        pdf_ocr.py			Program that performs OCR on a given PDF file. Executed as < python pdf_ocr.py path_to_pdf_file >
        ocr.config			A configuration file with path details. Current paths are relative
    text_files/				Text files extracted from pdf files after the OCR process
    topics/				Text files produced as an imtermediate step of processing. One file for each book containing the model outputs
    Project_Results_formatted.xlsx	Results from topics and named enteties extraction from book corpus. Formatted for easier inspection
    Project_Results.csv			Results from topics and named enteties extraction from book corpus
    requirements.txt			Python dependencies
    setup.sh				Bash script that install necessary dependencies (Except for Tesseract) Executed as < ./setup.sh >
    README.md				This file
</p>