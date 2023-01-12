from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
from random import randint
import csv
import requests
from pprint import pprint


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Для вывода курса валюты из списка\nВоспользуйтесь командой')
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    for line in data['Valute']:
        name = data['Valute'][line]['Name']
        await update.message.reply_text(f'/{line} - {name}')

async def valut(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    msg=update.message.text
    items=msg.split('/')
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    val = data['Valute'][items[1]]['Value']
    await update.message.reply_text(f'{val} руб ')
    log(update, context, val)
