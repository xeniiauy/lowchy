# lowchy
Silly discord math bot 
# 🤖 Discord Math Bot

A fun little Discord bot built with `discord.py` that can greet users and answer simple math questions using slash commands!

## 📦 Features

- `/lowchi` — Replies with a friendly mention.
- `/math question: What is 5 + 3` — Answers the math question and explains the result if asked.

## 🚀 Getting Started

### Requirements
- Python 3.8+
- `discord.py` with slash command support (or use `py-cord`)

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/discord-math-bot.git
   cd discord-math-bot

2. Create ``.env`` file that stores your discord bot token as:
   ```env
   DISCORD_TOKEN=your-discord-bot-token-here

> [!WARNING]
> NOTE: Never commit your ``.env`` file to version control, as it will expose your bot token. It will automatically be ignored via ``.gitignore``.

3. Install dependencies by running:
   ```bash
   pip install -r requirements.txt
