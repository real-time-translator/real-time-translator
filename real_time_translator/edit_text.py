import readline

def edit_text(old_text, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(old_text) #Input gonna change to GUI
   finally:
      readline.set_startup_hook()


if __name__ == '__main__':
    old_text = "This is a test"
    edited_text = edit_text("", old_text)
    print(edited_text)