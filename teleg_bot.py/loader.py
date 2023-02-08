# import os
# os.system('cls')
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from bot_commands import *
# TOKEN = "6032914868:AAGncpyujLNA7fukoyVhyFgvY7ELv0DIDeE"


# app = ApplicationBuilder().token(TOKEN).build()
# print("Server start")
# app.add_handler(CommandHandler("hello", hello))
# app.add_handler(CommandHandler("go", go))
# app.add_handler(CommandHandler("sum", sum))
# app.run_polling()
# print("Server stop")

from aiogram import Bot, Dispatcher

bot = Bot('6032914868:AAGncpyujLNA7fukoyVhyFgvY7ELv0DIDeE')
dp = Dispatcher(bot)






# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# app = ApplicationBuilder().token("6032914868:AAGncpyujLNA7fukoyVhyFgvY7ELv0DIDeE").build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()