from tkinter import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Sentiment Analysis Function
def analyze_sentiment():
    text = input_text.get("1.0", END).strip()
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        sentiment = "Positive 😀"
    elif compound <= -0.05:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    
    result_label.config(text=f"Sentiment: {sentiment}")

# GUI Setup
root = Tk()
root.title("Simple Sentiment Analyzer")
root.geometry("400x300")
root.configure(bg="lightblue")

title_label = Label(root, text="Sentiment Analyzer", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

input_text = Text(root, height=5, width=40, font=("Arial", 12))
input_text.pack(pady=10)

analyze_button = Button(root, text="Analyze Sentiment", command=analyze_sentiment, font=("Arial", 12), bg="skyblue")
analyze_button.pack(pady=5)

result_label = Label(root, text="Sentiment: ", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)

root.mainloop()
