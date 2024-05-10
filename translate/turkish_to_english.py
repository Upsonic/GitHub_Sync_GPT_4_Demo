def turkish_to_english(text):
    print('##active_line4##')
    translator = Translator(from_lang='tr', to_lang='en')
    print('##active_line5##')
    return translator.translate(text)
