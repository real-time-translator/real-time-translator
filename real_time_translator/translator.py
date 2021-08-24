import googletrans

def translat_str(snetence,to_language='ar'):
    translator = googletrans.Translator()
    translation = translator.translate(snetence, dest=to_language)
    translated = f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"
    
    # with open('real_time_translator/abc.txt',mode ='w') as file:
    #     file.write(translated)
    # with open('real_time_translator/abc.txt',mode='r') as file: 
    #     translated = file.readlines()
    
    # file = open('real_time_translator/abc.txt','r')
    # translated = file.read()
    print(translated)
    return translated

if __name__ == "__main__":
    print(translat_str("تفاحة",'en'))
    pass