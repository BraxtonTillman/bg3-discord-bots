🧠 BG3 AI Voting Bots
This project contains a collection of AI-powered Discord bots based on companions from Baldur’s Gate 3. Each bot represents a unique character — Shadowheart, Karlach, Astarion, Gale, Wyll, and Lae'zel — and participates in voting sessions to help drive group decisions during a custom BG3 campaign run by the Dungeon Master (DM).

🎯 Purpose
The goal is to bring roleplay and personality-driven chaos to the party's choices. These bots simulate the opinions and behavior of their in-game counterparts, voting on Discord polls with unique logic and personality flair.

🤖 Bots Included
Each bot is modeled after a BG3 companion and uses AI to "think" before voting:

🖤 ShadowheartBot – Mysterious, logical, and occasionally sarcastic.

🔥 KarlachBot – Chaotic good energy, driven by emotion.

🧛‍♂️ AstarionBot – Arrogant, stylish, and morally flexible.

🧙 GaleBot – Intellectual and verbose, with an eye toward arcane balance.

🗡️ WyllBot – Heroic and morally grounded, but dramatic.

⚔️ Lae'zelBot – Blunt, aggressive, and honor-bound.

🛠️ Features
Personality-Driven Voting: Each bot makes choices based on character traits and context.

On-Demand Launching: Bots are only activated when needed via a launcher script.

Poll Participation: Bots scan for Discord polls in a specific channel and cast votes accordingly.

ChatGPT Integration: Uses OpenAI’s API to simulate personalities and decisions.

Modular Setup: Bots are run independently, allowing for easy customization and expansion.

🧪 How It Works
The DM posts a poll in Discord.

Bots fetch the latest poll, interpret the options, and "discuss" internally.

Each bot makes a decision based on its logic and sends its vote via the Discord API.

Votes are cast, results are logged (optionally), and drama ensues.

🚀 Usage
Prerequisites
Python 3.8+

OpenAI API key

Discord bot tokens for each character

Installed dependencies: discord.py, openai, python-dotenv, etc.

Running Bots
Each bot is run individually via:

bash
Copy
Edit
python shadowheart_bot.py
Or use the launcher to start all bots simultaneously (in sequence or threads):

bash
Copy
Edit
python bot_launcher.py
Environment Setup
Create a .env file with the following format:

makefile
Copy
Edit
DISCORD_TOKEN_SHADOWHEART=your_token_here
DISCORD_TOKEN_KARLACH=your_token_here
...
OPENAI_API_KEY=your_openai_key
GUILD_ID=your_guild_id
CHANNEL_ID=poll_channel_id
📁 Project Structure
bash
Copy
Edit
bg3-bots/
├── shadowheart_bot.py
├── karlach_bot.py
├── astarion_bot.py
├── gale_bot.py
├── wyll_bot.py
├── laezel_bot.py
├── bot_launcher.py
├── utils/
│   └── personality_logic.py
├── .env
└── README.md
🎮 Customization
Want to add more bots or change personalities?

Clone an existing bot file

Change the name and traits

Update the .env and launcher to include your new bot

You can also tweak the personality prompts in personality_logic.py to tune how each bot interprets poll questions.

🧠 Future Ideas
Log conversation snippets from each bot

Create "party debates" before voting

Integrate dice rolls for chaotic decisions

Add visuals or voice messages to increase immersion

🙌 Credits
Created by [Your Name], inspired by the characters of Baldur’s Gate 3. Bots powered by OpenAI, running in Discord via discord.py.

