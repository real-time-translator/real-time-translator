from warnings import filters

from telegram import update
from real_time_translator.translator import *
import telegram
from telegram.ext import Updater , CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater(token='1931148200:AAGK0N9WLdxD34WT71o2WIStSvQ2NW38LWU', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="use /language to choose the language you want to translate to ")

to_lang='English'

def language(update, context,args=None):
    # print(update.massage.text)

    try:
        global to_lang
        to_lang = update.message.text.split()[1] # [1:] is to get rid of the / in id
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Translate To {to_lang} ")

    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"invald entart see /help")


def massage(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=translat_str(update.message.text))

def audio(updata,context):
    print('ok')
    # context.bot.send_message(chat_id=update.effective_chat.id, text='update.message.text')




start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
language_handler = CommandHandler('language', language,pass_args=True)

massage_handler = MessageHandler(Filters.text & (~Filters.command), massage)
audio_handler=MessageHandler(Filters.audio,audio)

dr=dispatcher
dr.add_handler(start_handler)
dr.add_handler(help_handler)
dr.add_handler(language_handler)
dr.add_handler(massage_handler)
dr.add_handler(audio_handler)
updater.start_polling()

# bot = telegram.Bot(token='1931148200:AAGK0N9WLdxD34WT71o2WIStSvQ2NW38LWU')
# print(bot.getUpdates()[0])
