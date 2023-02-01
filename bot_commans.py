from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import matrix as matrix


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.full_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi Приветствие\n/time Время\n/sum Расчет сумм\n/play Игра\n/p Продолжение игры\n/h Список команд')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    sum = 0
    sumText = ""
    for item in msg.split():
        if item!="/sum":
            sum = sum + int(item)
            sumText = sumText + item + '+'
    
    await update.message.reply_text(f'{sumText[0:-1]} = {sum}')

async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Начнем")
    await update.message.reply_text(matrix.outMatrix())
    await update.message.reply_text("Введите: /p [номер]")

async def play_continue_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    text = "*"
    for item in msg.split():
        if item!="/p":
            text = item
    # matrix.play(text)
    await update.message.reply_text(matrix.play(text))
    res = matrix.checkRow()
    if res != "*":
        await update.message.reply_text(f"Победили {res}")
    else:
        await update.message.reply_text("Продолжим: /p [номер]")
