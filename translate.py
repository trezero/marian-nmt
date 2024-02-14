from transformers import MarianMTModel, MarianTokenizer

def translate(text_to_translate, model_name='Helsinki-NLP/opus-mt-en-es'):
    # Load the tokenizer and model
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Prepare the text for translation
    translated = tokenizer(text_to_translate, return_tensors="pt", padding=True)

    # Translate the text
    translated_text = model.generate(**translated)

    # Decode and print the translated text
    print("Original:", text_to_translate)
    print("Translated:", tokenizer.decode(translated_text[0], skip_special_tokens=True))

if __name__ == "__main__":
    text_to_translate = "This is a test sentence. my name is Jason Perr, and I love to go spearfishing"
    translate(text_to_translate)
