from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token(
    "Запрещено публиковать, требование телеграм").build()

app.add_handler(CommandHandler("start", start))
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
for line in data['Valute']:
    app.add_handler(CommandHandler(line, valut))


app.run_polling()
