# Mr Jaanu Bot

A private Telegram bot built by **@Ijaanu**, designed to fetch and send media from restricted or private Telegram posts using just the message link — powered with a secure login system and hosted 24/7 on Koyeb.

---

## Features

- **Restricted Post Access**: Download from private or restricted Telegram channels using post links.
- **Session-Based Login**: Users can log in with their own Telegram session for secure use.
- **Admin-Only Access**: Fully private — only you or allowed users can access the bot.
- **Multi-Message Support**: Fetch multiple posts at once using "from - to" message link format.
- **Bot Message Links Supported**: Grab content even from bot chats using `/b/botusername/1234`.
- **Hosted 24/7 on Koyeb**: Your bot stays online, without any manual restarts.

---

## Environment Variables

Configure these variables in your Koyeb deployment settings:

- `API_HASH`: Your API hash from [my.telegram.org](https://my.telegram.org)
- `API_ID`: Your API ID from [my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN`: Your Telegram bot token from [@BotFather](https://t.me/BotFather)
- `ADMINS`: Your Telegram user ID (used for admin features like broadcast)
- `DB_URI`: Your MongoDB connection string from [mongodb.com](https://mongodb.com)
- `ERROR_MESSAGE`: Set to `True` or `False` — toggle detailed error messages

> **Important:** Never upload your API keys or tokens to GitHub. Always keep them secure as environment variables.

---

## Commands

- `/start` – Check if the bot is running
- `/help` – Show usage instructions
- `/login` – Login with your Telegram string session
- `/logout` – Logout your session
- `/cancel` – Cancel any ongoing task
- `/broadcast` – Send a message to all users (Admin only)

---

## Usage Guide

### Public Channels  
Just send the post link(s).

### Private Channels  
If needed, send the **invite link** to the channel first. Then send the post link(s).

### Bot Chats  
Use this format to fetch bot messages:

### Multiple Messages  
Use this format to send a batch of posts:

Example: Get messages from post 100 to 105.

---

## Deployment (Koyeb)

1. Fork or clone this repository.
2. In Koyeb, create a new Python service.
3. Add all required environment variables (see above).
4. Deploy with the included `Procfile`.
5. Enjoy 24/7 uptime — no restarts required.

---

## Disclaimer

This bot is for **private, personal use only**. Any misuse is the sole responsibility of the user.  
Developed with passion by **@Ijaanu**
