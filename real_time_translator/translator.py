import googletrans

def translat_str(snetence,to_language='ar'):

    # Initial
    translator = googletrans.Translator()
    # Basic Translate
    translation = translator.translate(snetence, dest=to_language)
    translated = f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
    print(translated)
    return translated

if __name__ == "__main__":
    print(translat_str("تفاحة",'en').lower())
    # pass