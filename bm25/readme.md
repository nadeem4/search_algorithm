
# **BM25 Search Ranking Algorithm Implementation**

This repository provides a clean and efficient implementation of the **BM25 (Best Matching 25)** algorithm using the **`rank_bm25`** library. BM25 is widely used in search engines to rank documents based on their relevance to a given search query. The implementation includes key preprocessing steps such as **stopword removal** and **stemming** to ensure accuracy and improve the effectiveness of the search ranking.

---

## **Table of Contents**

1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Explanation of the Code](#explanation-of-the-code)
4. [Why Does the Score Differ Between Implementations?](#why-does-the-score-differ-between-implementations)
5. [Conclusion](#conclusion)
6. [License](#license)

---

## **Introduction**

BM25 is a ranking function used in search engines to estimate the relevance of documents to a user's query. This repository provides an implementation of BM25 using the `rank_bm25` library, which simplifies the process by abstracting away many of the complexities associated with the algorithm.

This project also focuses on demonstrating **why scores may differ** when comparing different BM25 implementations (manual vs. library-based), and how **text preprocessing** plays a vital role in the final results.

---

## **Usage**

Once the dependencies are installed, you can run the BM25 implementation as follows:

1. Run the main BM25 script:
    ```bash
    python bm25_library.py
    ```

This will display the BM25 scores for a set of documents based on the query.

### **Sample Output:**

```
BM25 Scores With Library:
1. Score: 0.5108 | Document: Visit Millennium Park for concerts and outdoor activities.
2. Score: 0.1127 | Document: Enjoy the stunning architecture and vibrant nightlife in Chicago.
3. Score: 0.1127 | Document: Take a river cruise to see Chicago's skyline.
```

```
BM25 Scores Without Library:
1. Score: 0.9808 | Document: Visit Millennium Park for concerts and outdoor activities.
2. Score: 0.4700 | Document: Enjoy the stunning architecture and vibrant nightlife in Chicago.
3. Score: 0.4700 | Document: Take a river cruise to see Chicago's skyline.
```

---

## **Explanation of the Code**

The BM25 implementation using `rank_bm25` includes the following steps:

1. **Tokenization:** Each document and the query are tokenized using regular expressions. Tokenization breaks text into individual words while removing punctuation.
2. **Stopword Removal:** Common words (e.g., "the", "and", "in") that do not contribute to relevance are removed using NLTK's stopword list.
3. **Stemming:** Words are reduced to their root forms (e.g., "activities" becomes "activ") using NLTK’s Porter Stemmer.
4. **BM25 Scoring:** The `rank_bm25` library automatically computes BM25 scores based on the term frequency and inverse document frequency.
5. **Ranking:** Documents are ranked in descending order based on their BM25 scores, with the most relevant document appearing at the top.

---

## **Why Does the Score Differ Between Implementations?**

When comparing BM25 scores from a **manual implementation** to the ones generated using the **`rank_bm25` library**, the scores may differ due to the following reasons:

### 1. **Preprocessing Differences**
   - **Stopword Removal:** If stopwords are not removed in a manual implementation, they can affect the term frequencies and relevance calculations. In contrast, the `rank_bm25` library may not handle stopwords by default unless preprocessed properly.
   - **Stemming:** Stemming reduces words to their root forms (e.g., "activities" → "activ"). Without stemming, different forms of the same word are treated as separate terms, affecting term frequency and document frequency calculations.

### 2. **Tokenization Differences**
   - The way text is tokenized (i.e., splitting text into words) can also lead to differences. Inconsistent handling of punctuation, case sensitivity, or possessive forms (e.g., "Chicago's" vs. "Chicago") can cause variations in term counts and thus BM25 scores.

### 3. **IDF Calculation**
   - Slight variations in how the **Inverse Document Frequency (IDF)** is calculated in manual implementations vs. the library can also lead to differences in final scores. The library applies smoothing techniques and may handle edge cases differently, such as when terms appear in all or none of the documents.

### **Key Takeaway:**
   - To ensure consistency between manual and library-based implementations, it’s critical to use the **same preprocessing steps** (tokenization, stopword removal, stemming) in both approaches.

---

## **Conclusion**

The `rank_bm25` library offers a highly efficient and streamlined way to calculate BM25 scores without manually handling the underlying mechanics like document frequencies, inverse document frequencies, and scoring. However, **preprocessing steps** such as **tokenization**, **stopword removal**, and **stemming** play a crucial role in ensuring accurate and consistent results.

Understanding the differences in preprocessing and how they affect BM25 scores helps clarify why scores might vary between implementations and ensures better control over the search ranking process.

Feel free to modify and experiment with the code to suit your specific search ranking needs, and remember that consistent preprocessing is key to accurate search results!

---

