import re
import os


def regex_word_tokenize(text):
    pattern = r'''
          (?:\#\w+|@\w+)                    # Matches hashtags or @mentions
        | \b(?:[A-Za-z]\.)+[A-Za-z]\b       # Matches capital abbreviations (U.S.A.)
        | \b[a-zA-Z]+(?:'\w+)?\b            # Matches words and contractions (like can't)
        | \d+\.\d+                          # Matches decimal numbers like 5.0
        | \d+                               # Matches whole numbers
        | [.,!?;]                           # Matches common punctuation marks
    '''
    return re.findall(pattern, text, re.VERBOSE)


if __name__ == "__main__":
    
    current_directory = os.path.dirname(__file__)
    tweets_file_path = os.path.join(current_directory, 'data/daily547_tweets.txt')

    try:
        with open(tweets_file_path, 'r', encoding='utf-8') as file:
            file_contents = file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {tweets_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    corpus = file_contents
    for c in corpus[:5]:
        print(c, end= "")
        print(regex_word_tokenize(c))
