from rank_bm25 import BM25Okapi
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import nltk

# Download stopwords
nltk.download('stopwords')

# Sample Documents
documents = [
    "Enjoy the stunning architecture and vibrant nightlife in Chicago.",
    "Visit Millennium Park for concerts and outdoor activities.",
    "Take a river cruise to see Chicago's skyline."
]

# Sample Query
query = "fun activity in Chicago"

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

# Initialize BM25
bm25 = BM25Okapi(tokenized_docs)

# Calculate BM25 Scores
scores = bm25.get_scores(tokenized_query)

# Rank Documents Based on BM25 Scores
ranked_docs = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)

# Display Results
print("\nBM25 Scores With Library:")
for rank, (doc, score) in enumerate(ranked_docs, start=1):
    print(f"{rank}. Score: {score:.4f} | Document: {doc}")
