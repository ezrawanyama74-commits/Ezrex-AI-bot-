import logging
import sys
import psutil
import time
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("=== EZRA WANYAMA: SMARTPHONE SCIENTIST BOT ===")
TOKEN = input("1. Enter your Telegram Bot Token: ").strip()
MINI_APP_URL = input("2. Enter your Mini App Web URL (https://...): ").strip()

if not TOKEN or not MINI_APP_URL:
    print("\n❌ Error: Token and URL are both required!")
    sys.exit(1)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

START_TIME = time.time()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    
    welcome_text = (
        f"🧪 *WELCOME TO THE SMARTPHONE SCIENTIST PORTAL* 🧪\n\n"
        f"Greetings {user_first_name}!\n"
        f"I am *Ezra Wanyama*, guiding students and developers to master remote tech opportunities, "
        f"free online education, and mobile development directly from smartphones.\n\n"
        f"💡 *Commands You Can Use:*\n"
        f"▫️ /jobs - Latest remote entry-level roles\n"
        f"▫️ /learn - Free high-income skill pathways\n"
        f"▫️ /termux - Termux setup guide for developers\n"
        f"▫️ /status - Check Termux server stats\n"
        f"▫️ /about - Learn about Ezra Wanyama"
    )

    # Permanent Action Buttons
    menu_keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="🚀 Launch Full Mini App", web_app=WebAppInfo(url=MINI_APP_URL))],
            [KeyboardButton(text="💼 Latest Jobs"), KeyboardButton(text="🎓 Free Courses")],
            [KeyboardButton(text="⚡ Termux Tools"), KeyboardButton(text="📊 Bot Status")]
        ],
        resize_keyboard=True
    )

    inline_keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="🌐 Open Scientist Web Portal", web_app=WebAppInfo(url=MINI_APP_URL))]]
    )

    await update.message.reply_text(
        text=welcome_text,
        parse_mode="Markdown",
        reply_markup=inline_keyboard
    )
    
    await update.message.reply_text(
        text="👇 Select an option or use the menu below:",
        reply_markup=menu_keyboard
    )

async def jobs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jobs_text = (
        "💼 *SMARTPHONE SCIENTIST: ENTRY-LEVEL REMOTE JOBS*\n"
        "───────────────────────────────\n\n"
        "1. *Remote Data Entry & QA Tester*\n"
        "   └ 💰 $12 - $18/hr • No Experience Required\n"
        "2. *Junior Web Scraping Assistant*\n"
        "   └ 💰 $15 - $22/hr • Python / Termux Basics\n"
        "3. *Virtual Assistant & Chat Support*\n"
        "   └ 💰 $10 - $15/hr • Smartphone Friendly\n\n"
        "📲 *Open the Mini App to view direct application links & full scraped list!*"
    )
    
    inline_keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="🚀 Apply via Mini App", web_app=WebAppInfo(url=MINI_APP_URL))]]
    )
    await update.message.reply_text(jobs_text, parse_mode="Markdown", reply_markup=inline_keyboard)

async def learn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    learn_text = (
        "🎓 *SMARTPHONE SCIENTIST: ONLINE EDUCATION*\n"
        "───────────────────────────────\n\n"
        "▫️ *Python for Mobile Devs:* Master coding on Termux\n"
        "▫️ *Web Scraping & Automation:* Auto-fetch remote jobs\n"
        "▫️ *AI Prompt Engineering:* Monetize smartphone AI tools\n"
        "▫️ *Freelance Remote Work:* Build an international profile\n\n"
        "Access free curated roadmaps inside the Mini App!"
    )
    
    inline_keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="📚 Explore Courses", web_app=WebAppInfo(url=MINI_APP_URL))]]
    )
    await update.message.reply_text(learn_text, parse_mode="Markdown", reply_markup=inline_keyboard)

async def termux_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    termux_text = (
        "⚡ *TERMUX SCIENTIST TOOLKIT*\n"
        "───────────────────────────────\n"
        "Quick setup commands to build apps on your smartphone:\n\n"
        "1️⃣ *Update Core Packages:*\n"
        "`pkg update && pkg upgrade -y`\n\n"
        "2️⃣ *Install Python & Git:*\n"
        "`pkg install python git -y`\n\n"
        "3️⃣ *Install Scraping Tools:*\n"
        "`pip install requests beautifulsoup4`\n\n"
        "4️⃣ *Run Bot in Background:*\n"
        "`nohup python bot.py > bot.log 2>&1 &`"
    )
    await update.message.reply_text(termux_text, parse_mode="Markdown")

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ram = psutil.virtual_memory()
    uptime_seconds = int(time.time() - START_TIME)
    
    status_text = (
        "📊 *TERMUX SERVER STATUS*\n"
        "───────────────────────────────\n"
        f"🟢 *Bot State:* Active\n"
        f"⏱️ *Uptime:* {uptime_seconds // 3600}h {(uptime_seconds % 3600) // 60}m {uptime_seconds % 60}s\n"
        f"🧠 *RAM Usage:* {ram.percent}%\n"
        f"💾 *Available RAM:* {ram.available // (1024 * 1024)} MB\n"
        f"📱 *Host Engine:* Termux Android Environment"
    )
    await update.message.reply_text(status_text, parse_mode="Markdown")

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "💼 Latest Jobs":
        await jobs_command(update, context)
    elif text == "🎓 Free Courses":
        await learn_command(update, context)
    elif text == "⚡ Termux Tools":
        await termux_command(update, context)
    elif text == "📊 Bot Status":
        await status_command(update, context)

if __name__ == '__main__':
    print("\nConnecting to Telegram servers...")
    
    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .connect_timeout(30.0)
        .read_timeout(30.0)
        .write_timeout(30.0)
        .pool_timeout(30.0)
        .build()
    )
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jobs", jobs_command))
    app.add_handler(CommandHandler("learn", learn_command))
    app.add_handler(CommandHandler("termux", termux_command))
    app.add_handler(CommandHandler("status", status_command))
    
    # Handle button clicks
    from telegram.ext import MessageHandler, filters
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    
    print("✅ Ezra Wanyama Bot is live and upgraded! Press CTRL+C to stop.")
    app.run_polling()
