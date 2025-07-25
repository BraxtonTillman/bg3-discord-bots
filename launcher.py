import subprocess
import os
import signal
import time

# List of bot directories and bot script names
bots = [
    "shadowheart-bot/bot.py",
    "karlach-bot/bot.py",
    "astarion-bot/bot.py",
    "gale-bot/bot.py",
    "wyll-bot/bot.py",
    "laezel-bot/bot.py"
]

# Store processes here
processes = []

try:
    # Launch each bot in its own subprocess
    for bot_script in bots:
        print(f"🚀 Launching {bot_script}...")
        proc = subprocess.Popen(
            ["python", bot_script],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        processes.append(proc)

    print("\n✅ All bots are running. Press Ctrl+C to stop them.\n")

    # Keep the script alive while bots are running
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Shutting down all bots...")
    for proc in processes:
        proc.send_signal(signal.SIGINT)  # Gracefully terminate
    for proc in processes:
        proc.wait()
    print("✅ All bots have been shut down.")
