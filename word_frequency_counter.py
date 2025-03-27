import argparse
from collections import Counter

def count_word_frequency(file_path):
    """Read a text file and counts the frequency of each word."""
    try: 
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        words = text.split()
        word_count = Counter(words)
        
        print("Word Frequency Count:")
        for word, count in word_count.most_common():
            print(f"{word}: {count}")    
    
    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Word Frequency Counter")
    parser.add_argument("file", type=str, help="Path to the text file")
    args = parser.parse_args()

    count_word_frequency(args.file)

