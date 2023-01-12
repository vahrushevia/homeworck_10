from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

def log(update: Update, context: ContextTypes, val='-'):
    file = open('log.csv', 'a')
    file.write(f'{datetime.datetime.now().time()},{update.effective_user.first_name},{update.message.text},{val}\n')
    file.close()
