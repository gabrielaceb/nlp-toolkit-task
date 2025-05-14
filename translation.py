from googletrans import Translator

def translate_text(text, src='fr', dest='en'):
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

if __name__ == "__main__":
    text = input("Enter text in French to translate: ")
    translated = translate_text(text)
    print(f"Translation: {translated}")

