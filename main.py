from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commans as bc


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.full_name}')


app = ApplicationBuilder().token("5822824684:AAE5lh3S8zzL5d1-mWRbFBszSuNRII3NQns").build()

app.add_handler(CommandHandler("hi", bc.hi_command))
app.add_handler(CommandHandler("time", bc.time_command))
app.add_handler(CommandHandler("help", bc.help_command))
app.add_handler(CommandHandler("sum", bc.sum_command))
app.add_handler(CommandHandler("play", bc.play_command))
app.add_handler(CommandHandler("p", bc.play_continue_command))

print("server-start")
app.run_polling()

# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))

# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()

# from isOdd import isOdd

# print(isOdd(int('1')))
# print(isOdd(int('5')))

# print(isOdd(0))
# print(isOdd(4))