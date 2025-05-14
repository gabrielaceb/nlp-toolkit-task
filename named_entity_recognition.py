import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    entities = extract_entities(text)
    print("Named Entities:")
    for ent, label in entities:
        print(f"- {ent} ({label})")