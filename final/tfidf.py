import utils
import operator
import csv
from datetime import datetime

def generate_tfidf_data(file):
    with open(file) as f:
        csvreader = csv.reader(f)
        texts = [row[0] for row in csvreader]

    tfidf, corpus, dictionary = utils.score_keyphrases_by_tfidf(texts, candidates='chunks')

    return (tfidf, corpus, dictionary)

def score_keyphrases_by_tfidf(texts, candidates='chunks'):
    # extract candidates from each text in texts, either chunks or words
    if candidates == 'chunks':
        boc_texts = [extract_candidate_chunks(text) for text in texts]
    elif candidates == 'words':
        boc_texts = [extract_candidate_words(text) for text in texts]
    # make gensim dictionary and corpus
    dictionary = gensim.corpora.Dictionary(boc_texts)
    corpus = [dictionary.doc2bow(boc_text) for boc_text in boc_texts]
    # transform corpus with tf*idf model
    tfidf = gensim.models.TfidfModel(corpus)

    return tfidf, corpus, dictionary

if __name__ == '__main__':
    startTime = datetime.now()
    tfidf, corpus, dictionary = generate_tfidf_data('./corpus-abstracts.csv')
    utils.save_obj({'corpus':corpus, 'tfidf': tfidf, 'dictionary': dictionary}, './tfidf-chunks')
    print datetime.now() - startTime
