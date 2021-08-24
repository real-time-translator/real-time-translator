import googletrans

def translat_str(snetence,to_lang):

    # Initial
    translator = googletrans.Translator()
    # Basic Translate
    translation = translator.translate( snetence, dest=to_lang)
    translated=f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
    print(translated)

    # with open('abc.txt',mode ='w') as file:     
    #         file.write(translated)

    return translated

if __name__ == "__main__":
    print(translat_str("تفاحة",'en').lower())
    pass