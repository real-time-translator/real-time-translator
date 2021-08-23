from real_time_translator.input_text import input_text_manually, input_text_file
from real_time_translator.input_image import imagetotext
from real_time_translator.input_voice import transcript_from_file, transcript_from_record
from real_time_translator.edit_text import edit_text


def play(choice):
    
    #Render Main Page

    if choice == 'Translate by Text':
        handle_text()
    if choice == 'Translate by Voice':
        handle_voice()
    if choice == 'Translate by File':
        handle_file()



def handle_text(extracted_text='',translated_text=''):
    # Render new page

    print (extracted_text) # On 1st GUI Box
    print (translated_text) # On 2nd GUI Box

    button_selected = ''
    # Event click on Button, so the button variable will change, recursive

    if button_selected == 'Type Your Text':
        extracted_text = input_text_manually()
        handle_file(extracted_text)
    if button_selected == 'Edit Text':
        extracted_text = edit_text(extracted_text)
        # 1st GUI Box gonna updated
        handle_file(extracted_text)
    if button_selected == 'Translate':
        # translated_text = translate(extracted_text) #translate function to be updated
        # 2nd GUI Box gonna updated
        handle_file(extracted_text,translated_text)
    if button_selected == 'Back':
        play()



def handle_voice(extracted_text='',translated_text=''):
    extracted_text = transcript_from_record()
    # Render new page

    print (extracted_text) # On 1st GUI Box
    print (translated_text) # On 2nd GUI Box

    button_selected = ''
    # Event click on Button, so the button variable will change, recursive

    if button_selected == 'Start Recording':
        extracted_text = transcript_from_record()
        handle_file(extracted_text)
    if button_selected == 'Edit Text':
        extracted_text = edit_text(extracted_text)
        # 1st GUI Box gonna updated
        handle_file(extracted_text)
    if button_selected == 'Translate':
        # translated_text = translate(extracted_text) #translate function to be updated
        # 2nd GUI Box gonna updated
        handle_file(extracted_text,translated_text)
    if button_selected == 'Back':
        play()



def handle_file(extracted_text='',translated_text=''):
    # Render new page

    print (extracted_text) # On 1st GUI Box
    print (translated_text) # On 2nd GUI Box

    button_selected = ''
    # Event click on Button, so the button variable will change, recursive
    
    if button_selected == 'Insert a Text':
        path = '' # Input from GUI - Browse from Device
        extracted_text = input_text_file(path)
        handle_file(extracted_text)
    if button_selected == 'Insert an Image':
        path = '' # Input from GUI - Browse from Device
        extracted_text = imagetotext(path)
        handle_file(extracted_text)
    if button_selected == 'Insert an Audio':
        path = '' # Input from GUI - Browse from Device
        extracted_text = transcript_from_file(path)
        handle_file(extracted_text)
    if button_selected == 'Edit Text':
        extracted_text = edit_text(extracted_text)
        # 1st GUI Box gonna updated
        handle_file(extracted_text)
    if button_selected == 'Translate':
        # translated_text = translate(extracted_text) #translate function to be updated
        # 2nd GUI Box gonna updated
        handle_file(extracted_text,translated_text)
    if button_selected == 'Back':
        play()
