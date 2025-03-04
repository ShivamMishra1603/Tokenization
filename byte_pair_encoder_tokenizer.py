import re
import os
from collections import Counter


def pre_process_corpus(corpus):
    corpus = [re.sub(r'[^\x00-\x7F]', '?', tweet) for tweet in corpus]
    all_tweets = " ".join(corpus)
    vocab = set("".join(all_tweets.split()))
    words = [list(word) for word in " ".join(corpus).split()]
    return words, vocab

def get_bigrams(corpus):
    bigrams = []
    for word in corpus:
        bigrams += [(word[i], word[i + 1]) for i in range(len(word) - 1)]
    return bigrams

def update_corpus(corpus, bigram, new_token):
    for i, word in enumerate(corpus):
        new_word = []
        j = 0
        while j < len(word):
            if j < len(word) - 1 and (word[j], word[j + 1]) == bigram:
                new_word.append(new_token)
                j += 2
            else:
                new_word.append(word[j])
                j += 1
        corpus[i] = new_word
    return corpus


def spacelessBPElearn(corpus, max_vocabulary=1000):
    corpus, vocab = pre_process_corpus(corpus)
    vocab_size = len(vocab)
    while vocab_size < max_vocabulary:
        bigrams = get_bigrams(corpus)

        bigram_freq = Counter(bigrams)
        if not bigram_freq:
            print("No more bigrams to merge.")
            break
        most_frequent_bigram, freq = bigram_freq.most_common(1)[0]
        new_token = ''.join(most_frequent_bigram)

        corpus = update_corpus(corpus, most_frequent_bigram, new_token)
        vocab.add(new_token)
        vocab_size = len(vocab)
        if vocab_size%100==0: 
            print(f"Updated vocab size: {vocab_size}")

    return vocab



def spacelessBPETokenize(text, vocab):
    text = re.sub(r'[^\x00-\x7F]', '?', text)
    words = text.split()
    
    tokenized_words = []
    
    for word in words:
        tokens_word = []
        while word:
            for i in range(len(word), 0, -1):
                if word[:i] in vocab:
                    tokens_word.append(word[:i])
                    word = word[i:]
                    break
        
        tokenized_words.extend(tokens_word)
    
    return tokenized_words


if __name__ == "__main__":
    
    current_directory = os.path.dirname(__file__)
    tweets_file_path = os.path.join(current_directory, 'Data/daily547_tweets.txt')

    try:
        with open(tweets_file_path, 'r', encoding='utf-8') as file:
            corpus = file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {tweets_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    
    vocab = spacelessBPElearn(corpus, 5000)
    
    print(f"Final Vocab of size {len(vocab)}")
    print(vocab)

    print("***********************************************************************")

    print("Result of tokenization for first 15 sentences")
    for sentence in corpus[:15]:
        print(spacelessBPETokenize(sentence, vocab))