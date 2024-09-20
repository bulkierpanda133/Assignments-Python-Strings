import re
import time
def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]

    highlighted_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = re.sub(rf'\b{keyword}\b', keyword.upper(), review, flags=re.IGNORECASE)
        highlighted_reviews.append(review)

    return highlighted_reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

highlighted_reviews = highlight_keywords(reviews)

for review in highlighted_reviews:
    print(review)

time.sleep(4)

#Task 2: Sentiment Tally
import string

def sentiment_tally(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
    positive_count = 0
    negative_count = 0

    for review in reviews:
        words = review.lower().split()
        for word in words:
            cleaned_word = word.strip(string.punctuation)
            if cleaned_word in positive_words:
                positive_count += 1
            elif cleaned_word in negative_words:
                negative_count += 1

    return positive_count, negative_count


reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]


positive_count, negative_count = sentiment_tally(reviews)
print(f"Positive words count: {positive_count}, Negative words count: {negative_count}")

 
 
time.sleep(4)
 #Task 3: Review Summary

def review_summary(review, length=30):
    if len(review) <= length:
        return review
    else:
        summary = review[:length]
        last_space = summary.rfind(' ')
        if last_space == -1:
            return summary + "…"
        else:
            return review[:last_space] + "…"

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for review in reviews:
    print(review_summary(review))
