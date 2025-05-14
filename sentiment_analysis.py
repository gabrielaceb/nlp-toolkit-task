# sentiment_analysis.py
from textblob import TextBlob

def analyse_sentiment(text):
    blob = TextBlob(text)
    return {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }

if __name__ == "__main__":
    text = input("Enter a sentence to analyse: ")
    result = analyse_sentiment(text)
    print(f"Polarity: {result['polarity']}, Subjectivity: {result['subjectivity']}")
