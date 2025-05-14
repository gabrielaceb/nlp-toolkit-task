from textblob.classifiers import NaiveBayesClassifier

train_data = [
    ('The food was great!', 'Food'),
    ('Terrible service at the restaurant.', 'Service'),
    ('Lovely ambiance and setting.', 'Ambiance'),
    ('The waiter was rude.', 'Service'),
    ('Fantastic dessert selection.', 'Food'),
    ('Chairs were uncomfortable.', 'Ambiance')
]

classifier = NaiveBayesClassifier(train_data)

def classify_text(text):
    return classifier.classify(text)

if __name__ == "__main__":
    text = input("Enter a review: ")
    category = classify_text(text)
    print(f"Predicted category: {category}")


