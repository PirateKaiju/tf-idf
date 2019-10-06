from math import log

import re

document_paths = []

sample_doc1 = ""

sample_doc2 = ""

sample_doc3 = ""

def extract_words(document):

    #TODO: TIME EFFICIENT FILTERING
    #Remove numbers, symbols, accents and special characters
    #document = re.sub(r'[^A-Za-z ]+', '', document)
    #Remove line breaks
    document = re.sub(r'\n', ' ', document)
    
    
    words = document.split(" ")
    #for simplicity, its best to convert all words to lowercase
    words = [word.lower() for word in words]

    return words

def calc_frequencies(document):
    #Using dicts to store frequencies
    frequencies = {}

    words = extract_words(document)

    #Used for normalizing the frequencies
    total_words = len(document)

    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    for freq in frequencies.keys():
        if(frequencies[freq] > 0):
            frequencies[freq] = frequencies[freq] / total_words

    
    return frequencies

def normalize_frequencies(frequencies, total_words_in_doc):
    pass

def term_frequency(term, frequencies):
    if term in frequencies:
        return frequencies[term]
    return 0

def inverse_doc_frequency(term, documents):
    idf = 0
    for document in documents:

        words = extract_words(document)
        
        if term in words:
            idf += 1
    
    #avoiding divide by 0
    if idf > 0:
        #idf formula
        return log(float(len(documents)) / idf)
    
    return 0


def tfidf(documents):

    tfidfs = {}
    iddoc = 1 #TODO: CREATE A CLASS FOR DOCUMENT

    #term_frequencies = []

    for document in documents:
        
        words = list(set(extract_words(document))) #Trick to get unique values
        frequencies = calc_frequencies(document)

        actual_tfidfs = []

        for word in words:

            tf = term_frequency(word, frequencies)
            idf = inverse_doc_frequency(word, documents)
            
            tfidf = tf * idf

            #result = (word, tfidf)
            actual_tfidfs.append((word, tfidf))


        tfidfs[iddoc] = actual_tfidfs
        iddoc += 1

    return tfidfs


#print(calc_frequencies(sample_doc))
#print(inverse_doc_frequency("market", [sample_doc, sample_doc2]))

print(tfidf([sample_doc1, sample_doc2, sample_doc3])[2])

#TODO: ACCEPT FILES AS INPUT
