import googletrans


def translat_str(snetence):

    # Initial
    translator = googletrans.Translator()
    # Basic Translate
    translation = translator.translate( snetence, dest="ar")
    translated=f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
    print(translated)

    # with open('abc.txt',mode ='w') as file:     
    #         file.write(translated)

    return translated

if __name__ == "__main__":
  

    # print(translat_str())
    pass