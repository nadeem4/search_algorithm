import math
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# Ensure NLTK data is downloaded
import nltk
nltk.download('stopwords')

# Sample Documents
documents = [
    "Enjoy the stunning architecture and vibrant nightlife in Chicago.",
    "Visit Millennium Park for concerts and outdoor activities.",
    "Take a river cruise to see Chicago's skyline."
]

# Sample Query
query = "fun activity in Chicago"

# BM25 Parameters
k1 = 1.5
b = 0.75

# Initialize Stemmer and Stopwords
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Enhanced Tokenizer Function
def tokenize(text, remove_stopwords=True, apply_stemming=True):
    """
    Tokenizes the input text into lowercase words, removes punctuation,
    removes stopwords, and applies stemming.
    """
    # Lowercase and remove punctuation using regex
    tokens = re.findall(r'\b\w+\b', text.lower())
    
    if remove_stopwords:
        tokens = [word for word in tokens if word not in stop_words]
    
    if apply_stemming:
        tokens = [stemmer.stem(word) for word in tokens]
    
    return tokens

# Tokenize all documents and the query
tokenized_docs = [tokenize(doc) for doc in documents]
tokenized_query = tokenize(query)

# Calculate Document Frequencies (DF)
def calculate_df(tokenized_docs):
    """
    Calculates the document frequency for each term in the corpus.
    """
    df = {}
    for doc in tokenized_docs:
        unique_terms = set(doc)
        for term in unique_terms:
            df[term] = df.get(term, 0) + 1
    return df

df = calculate_df(tokenized_docs)
N = len(documents)  # Total number of documents

# Calculate Inverse Document Frequency (IDF)
def calculate_idf(query_terms, df, N):
    """
    Calculates the IDF for each query term using the BM25 formula.
    """
    idf = {}
    for term in query_terms:
        # BM25 IDF formula with smoothing
        if term in df:
            idf_term = math.log(1 + (N - df[term] + 0.5) / (df[term] + 0.5))
        else:
            # If term not in any document, assign maximum IDF
            idf_term = math.log(1 + (N + 0.5) / 0.5)
        idf[term] = idf_term
    return idf

idf = calculate_idf(tokenized_query, df, N)

# Calculate Average Document Length (avgdl)
def calculate_avgdl(tokenized_docs):
    """
    Calculates the average length of documents in the corpus.
    """
    total_length = sum(len(doc) for doc in tokenized_docs)
    return total_length / len(tokenized_docs)

avgdl = calculate_avgdl(tokenized_docs)

# Calculate BM25 Scores
def calculate_bm25_scores(query_terms, tokenized_docs, idf, avgdl, k1, b):
    """
    Calculates the BM25 score for each document given the query terms.
    """
    scores = []
    for doc in tokenized_docs:
        score = 0.0
        doc_len = len(doc)
        for term in query_terms:
            if term in doc:
                tf = doc.count(term)
                numerator = tf * (k1 + 1)
                denominator = tf + k1 * (1 - b + b * (doc_len / avgdl))
                score += idf.get(term, 0) * (numerator / denominator)
        scores.append(score)
    return scores

bm25_scores = calculate_bm25_scores(tokenized_query, tokenized_docs, idf, avgdl, k1, b)

# Rank Documents Based on BM25 Scores
def rank_documents(documents, scores):
    """
    Ranks documents based on their BM25 scores in descending order.
    """
    ranked = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)
    return ranked

ranked_documents = rank_documents(documents, bm25_scores)

# Display Results
print("BM25 Scores Without Library:")
for rank, (doc, score) in enumerate(ranked_documents, start=1):
    print(f"{rank}. Score: {score:.4f} | Document: {doc}")
