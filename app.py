import sys
import os
import traceback
import nltk

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

# Ensure required NLTK packages are downloaded only once
nltk.download('punkt', quiet=True)

try:
    from summarizer import TextSummarizer  # Ensure the correct import

    def main():
        text = input("Enter the text to summarize:\n>>> ")

        try:
            num_sentences = int(input("Enter the number of summary sentences: "))
        except ValueError:
            print("Invalid input. Using default (2 sentences).")
            num_sentences = 2
        
        summarizer = TextSummarizer(text)
        summary = summarizer.summarize(num_sentences)

        print("\nSummary:\n", summary)

    if __name__ == "__main__":
        main()

except Exception as e:
    print("An error occurred:")
    traceback.print_exc()
    input("\nPress Enter to exit...")
