# 🧐 BG3 AI Voting Bots

This project contains a collection of AI-powered Discord bots based on companions from *Baldur’s Gate 3*. Each bot represents a unique character — Shadowheart, Karlach, Astarion, Gale, Wyll, and Lae'zel — and participates in voting sessions to help drive group decisions during a custom BG3 campaign run by the Dungeon Master (DM).

## 🎯 Purpose

The goal is to bring roleplay and personality-driven chaos to the party's choices. These bots simulate the opinions and behavior of their in-game counterparts, voting on Discord polls with unique logic and personality flair.

## 🤖 Bots Included

Each bot is modeled after a BG3 companion and uses AI to "think" before voting:

* **🖤 ShadowheartBot** – Mysterious, logical, and occasionally sarcastic.
* **🔥 KarlachBot** – Chaotic good energy, driven by emotion.
* **🧙‍♂️ AstarionBot** – Arrogant, stylish, and morally flexible.
* **🧙 GaleBot** – Intellectual and verbose, with an eye toward arcane balance.
* **🔪 WyllBot** – Heroic and morally grounded, but dramatic.
* **⚔️ Lae'zelBot** – Blunt, aggressive, and honor-bound.

## 🛠️ Features

* **Personality-Driven Voting**: Each bot makes choices based on character traits and context.
* **On-Demand Launching**: Bots are only activated when needed via a launcher script.
* **Poll Participation**: Bots scan for Discord polls in a specific channel and cast votes accordingly.
* **ChatGPT Integration**: Uses OpenAI’s API to simulate personalities and decisions.
* **Modular Setup**: Bots are organized in separate folders, each encapsulating its own logic.

## 🧪 How It Works

1. The DM posts a poll in Discord.
2. Bots fetch the latest poll, interpret the options, and "discuss" internally.
3. Each bot makes a decision based on its logic and sends its vote via the Discord API.
4. Votes are cast, results are logged (optionally), and drama ensues.

## 🚀 Usage

### Prerequisites

* Python 3.8+
* OpenAI API key
* Discord bot tokens for each character
* Installed dependencies: `discord.py`, `openai`, `python-dotenv`, etc.

### Running Bots

Each bot is run individually by navigating to its folder and executing:

```bash
python bot.py
```

Or use the unified launcher to start all bots:

```bash
python launcher.py
```

### Environment Setup

Each bot typically has its own `.env` file within its folder:

```
DISCORD_TOKEN=your_token_here
OPENAI_API_KEY=your_openai_key
```

## 📁 Project Structure

```
bg3-bots/
├── astarion/
│   ├── bot.py
│   ├── prompt.py
│   └── .env
├── shadowheart/
│   ├── bot.py
│   ├── prompt.py
│   └── .env
├── karlach/
│   ├── bot.py
│   ├── prompt.py
│   └── .env
├── gale/
│   ├── bot.py
│   ├── prompt.py
│   └── .env
├── wyll/
│   ├── bot.py
│   ├── prompt.py
│   └── .env
├── laezel/
│   ├── bot.py
│   ├── prompt.py
│   └── .env
├── bot_launcher.py
└── README.md
```

## 🎮 Customization

Want to add more bots or change personalities?

* Copy an existing bot folder
* Modify the `prompt.py` to reflect the new personality
* Update the `.env` file with the appropriate bot token and settings
* (Optional) Update `bot_launcher.py` if using a launcher

## 🧠 Future Ideas

* Log conversation snippets from each bot
* Create "party debates" before voting
* Integrate dice rolls for chaotic decisions
* Add visuals or voice messages to increase immersion

🙌 Credits
Created by Braxton Tillman, inspired by the characters of *Baldur’s Gate 3*. Bots powered by OpenAI, running in Discord via `discord.py`.

