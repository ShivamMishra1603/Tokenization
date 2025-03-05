# Tokenization

This repository contains code that implements two different tokenization techniques: **Regular Expression-based Word Tokenizer** and **Byte Pair Encoding (BPE)**. These tokenizers are useful in various natural language processing (NLP) tasks, such as text preprocessing, machine learning, and deep learning. 

The repository provides two Python scripts:
1. `regex_word_tokenizer.py`: Implements word tokenization using regular expressions.
2. `byte_pair_encoder_tokenizer.py`: Implements tokenization using the Byte Pair Encoding algorithm, which is often used in subword tokenization for machine learning applications.

---

## Table of Contents

- [Tokenization](#tokenization)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Setup](#setup)
  - [Scripts Overview](#scripts-overview)
    - [1. `regex_word_tokenizer.py`](#1-regex_word_tokenizerpy)
      - [Key Functions:](#key-functions)
      - [Example Regex Pattern:](#example-regex-pattern)
    - [2. `byte_pair_encoder_tokenizer.py`](#2-byte_pair_encoder_tokenizerpy)
      - [Key Functions:](#key-functions-1)
      - [Example Workflow:](#example-workflow)
  - [Usage](#usage)
    - [1. `regex_word_tokenizer.py` Usage](#1-regex_word_tokenizerpy-usage)

---

## Introduction

Tokenization is the process of splitting a sequence of text into smaller chunks, called tokens. In NLP, tokens can be words, subwords, or characters. Tokenization is an essential step in preparing data for machine learning and deep learning models.

This repository provides two types of tokenizers:
1. **Regular Expression-based Word Tokenizer**: Uses regex patterns to identify words, hashtags, mentions, punctuation, and numbers in text. This tokenizer is ideal for handling typical word tokenization in plain text.
   
2. **Byte Pair Encoding (BPE)**: A subword tokenization method that starts by considering each character in the corpus as a separate token. It then iteratively merges the most frequent character pairs into a new token. This technique is widely used in modern NLP tasks to handle rare or unseen words by representing them as subword units. BPE helps in reducing vocabulary size and handling out-of-vocabulary words effectively.

---

## Setup

Before running the scripts, ensure that you have Python 3.x installed on your system.

1. Clone the repository:

    ```bash
    git clone https://github.com/ShivamMishra1603/Tokenization.git
    cd Tokenization
    ```

2. Install necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Scripts Overview

### 1. `regex_word_tokenizer.py`

This script implements a word tokenization function using regular expressions. It splits text into various token types like:
- Words (including contractions like "can't")
- Hashtags (e.g., `#example`)
- Mentions (e.g., `@username`)
- Punctuation (e.g., `.,!?;`)
- Numbers (both whole numbers and decimal numbers)

#### Key Functions:
- **`regex_word_tokenize(text)`**: Tokenizes a given text using a defined regular expression pattern.

#### Example Regex Pattern:
- Matches hashtags or mentions: `(?:\#\w+|\@\w+)`
- Matches capital abbreviations: `\b(?:[A-Za-z]\.)+[A-Za-z]\b`
- Matches words and contractions: `\b[a-zA-Z]+(?:'\w+)?\b`
- Matches decimal numbers: `\d+\.\d+`
- Matches whole numbers: `\d+`
- Matches common punctuation marks: `[.,!?;]`

---

### 2. `byte_pair_encoder_tokenizer.py`

This script implements the **Byte Pair Encoding (BPE)** algorithm, which is useful for subword tokenization. It iteratively merges the most frequent pair of characters (or subword tokens) in the corpus until a predefined vocabulary size is reached. The resulting vocabulary is then used for tokenizing input text into subword units.

#### Key Functions:
- **`pre_process_corpus(corpus)`**: Preprocesses the corpus by replacing non-ASCII characters with `?`, splits text into words, and builds an initial vocabulary.
- **`get_bigrams(corpus)`**: Extracts all bigrams (pairs of consecutive characters) from the corpus.
- **`update_corpus(corpus, bigram, new_token)`**: Updates the corpus by merging the given bigram into a new token.
- **`spacelessBPElearn(corpus, max_vocabulary)`**: Learns subword vocabulary using BPE and returns the resulting vocabulary.
- **`spacelessBPETokenize(text, vocab)`**: Tokenizes the input text based on the learned BPE vocabulary.

#### Example Workflow:
1. **Learning BPE vocabulary**: The corpus is processed to create a vocabulary of subword units by iteratively merging frequent character pairs.
2. **Tokenizing text**: The learned vocabulary is then used to tokenize input text into subword tokens.

---

## Usage

### 1. `regex_word_tokenizer.py` Usage

This script reads a file containing tweets (`daily547_tweets.txt`), tokenizes the first 5 lines using regular expressions, and prints the tokenized output.

To run it:
```bash
python regex_word_tokenizer.py
