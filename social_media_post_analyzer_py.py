# -*- coding: utf-8 -*-
"""social media post analyzer.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sqKTPHuuZSmxboKIdJYsS6e5GSle-xbQ
"""

def post_analyze():
    post = "i an very happy because my code is run "

    positive_words = ["happy", "joyful", "excited", "love", "amazing", "great"]
    negative_words = ["sad", "angry", "frustrated", "hate", "terrible", "awful"]

    # Count positive and negative word
    positive_count = 0
    negative_count = 0
    for word in post.split():
        if word.lower() in positive_words:
            positive_count += 1
        elif word.lower() in negative_words:
            negative_count += 1

        # Determine sentiment based on word counts
        if positive_count > negative_count:
            sentiment = "positive"
        elif negative_count > positive_count:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        # Extract keywords (excluding common words)
        common_words = ["the", "a", "is", "of", "and", "to", "in", "that", "it", "on"]
        keywords = [word for word in post.split() if word.lower() not in common_words]
        print(f"Sentiment: {sentiment}")
        print(f"Keywords: {keywords}")
post_analyze()