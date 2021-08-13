import requests
import os
import time
import shutil
import subprocess
from git import Repo

print("""
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     

################################################# LOST.#0404 ###########################################################
""")

print("[LOST] Checking for updates...")

# Clones Lost-UB repository
Repo.clone_from("https://github.com/L-o-s-t/Lost-UB", "repo/").index.remove(['.github'],
                                                                            True, r=True)

# Checks if data/bot.ico exists, if not it will create it
if not os.path.exists("data") and not os.path.exists("data/bot.ico"):
    print("[LOST] data folder not found, creating new one...")
    os.replace("repo/data", "data")
elif os.path.exists("data") and not os.path.exists("data/bot.ico"):
    print("[LOST] bot.ico not found, creating new one...")
    os.replace("repo/data/bot.ico", "data/bot.ico")

# Checks if README.md exists, if not it will create it
if not os.path.exists("README.md"):
    print("[LOST] Readme.md not found, creating new one...")
    os.replace("repo/README.md", "README.md")

# Checks if commands.md exists, if not then it will create it.
if not os.path.exists("commands.md"):
    print("[LOST] Commands.md not found, creating new one...")
    os.replace("repo/commands.md", "commands.md")

# Checks if bot.py exists, if not it will create it
if not os.path.exists("bot.py"):
    print("[LOST] Bot.py not found, creating new one")
    os.replace("repo/bot.py", "bot.py")
elif os.path.exists("bot.py"):
    with open("repo/bot.py", "r") as new:
        newbot = new.read()
    with open("bot.py", "r") as old:
        oldbot = old.read()
    if newbot != oldbot:
        print("[LOST] Update found, please do not close the window until it is done updating...")
        os.remove("bot.py")
        os.replace("repo/bot.py", "bot.py")
    elif newbot == oldbot:
        print("[LOST] No updates found...")

# Checks if bot.exe exists, if not it will create it
if not os.path.exists("bot.exe"):

    # Starts creating bot executable file
    print("[LOST] Bot executable not found, creating new one...")
    process = subprocess.Popen("pyinstaller --icon data\\bot.ico --onefile bot.py",
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)
    process.wait()

    # Cleans up unncessary files from the creation of the bot executable file
    os.remove("bot.spec")
    shutil.rmtree("build")
    shutil.rmtree("__pycache__")
    os.replace("dist/bot.exe", "bot.exe")
    shutil.rmtree("dist")
    print("[LOST] Successfully created bot executable")

# If bot.exe does exist, and bot.py isn't up to date
elif os.path.exists("bot.exe"):

    # updates bot executable file
    os.remove("bot.exe")
    process = subprocess.Popen("pyinstaller --icon data\\bot.ico --onefile bot.py",
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)
    process.wait()

    # Cleans up unncessary files from the creation of the bot executable file
    os.remove("bot.spec")
    shutil.rmtree("build")
    shutil.rmtree("__pycache__")
    os.replace("dist/bot.exe", "bot.exe")
    shutil.rmtree("dist")
    print("[LOST] Successfully updated bot executable")

process = subprocess.run("echo y | rmdir /s repo",
                         shell=True,
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.STDOUT)

input("[LOST] You may now close this window.")
