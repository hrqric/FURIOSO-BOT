from telegram import Update
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from furia_bot_responses import requestDetailsMatches, requestLineUp, requestRanking, requestWinStreak, requestNoticias

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Oi! Sou um BOT Furioso! 🤖")

async def partidas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        qtd = int(context.args[0])

    except (IndexError, ValueError):
        qtd = 5

    texto = requestDetailsMatches(qtd)
    await update.message.reply_text(
    texto,
    disable_web_page_preview=True
    )

async def lineup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = requestLineUp()
    await update.message.reply_text(
        texto,
        disable_web_page_preview=True
    )

async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = requestRanking()
    await update.message.reply_text(
        texto,
        disable_web_page_preview=True
    )

async def winstreak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = requestWinStreak()
    await update.message.reply_text(
        texto,
        disable_web_page_preview=True
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        qtd = int(context.args[0])

    except (IndexError, ValueError):
        qtd = 3

    texto = requestNoticias(qtd)
    await update.message.reply_text(
    texto,
    disable_web_page_preview=True
    )

    

if __name__ == '__main__':

    load_dotenv()
    BOT_TOKEN = os.getenv("TOKEN")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("partidas", partidas))
    app.add_handler(CommandHandler("lineup", lineup))
    app.add_handler(CommandHandler("ranking", ranking))
    app.add_handler(CommandHandler("winrate", winstreak))
    app.add_handler(CommandHandler("winstreak", winstreak))
    app.add_handler(CommandHandler("news", news))

    print("bot ta rodando...")
    app.run_polling()


