from deep_translator import GoogleTranslator

print("Welcome to CodeAlpha Language Translator")
print("Type 'exit' to quit.")

while True:
    text = input("Enter text to translate: ")
    if text.lower() == "exit":
        print("Bye bye! Have a great day.")
        break

    target_lang = input("Translate to (e.g., 'fr' for French, 'hi' for Hindi, 'es' for Spanish): ")
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        print(f"Translated Text: {translated}")
    except Exception as e:
        print(f"Error: {e}")