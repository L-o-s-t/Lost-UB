import os
import shutil
import subprocess
try:
    from git import Repo
except ModuleNotFoundError:
    process = subprocess.Popen("py -m pip install GitPython",
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)
    process.wait()
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
    with open("repo/bot.py", "r", encoding="utf8") as new:
        newbot = new.read()
    with open("bot.py", "r", encoding="utf8") as old:
        oldbot = old.read()
    if newbot != oldbot:
        print("[LOST] Update found, please do not close the window until it is done updating...")
        os.remove("bot.py")
        os.replace("repo/bot.py", "bot.py")
    elif newbot == oldbot:
        print("[LOST] No updates found...")

if os.path.exists("commands"):
    shutil.rmtree("commands")
shutil.move("repo/commands", "commands")

process = subprocess.run("echo y | rmdir /s repo",
                         shell=True,
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.STDOUT)

input("[LOST] You may now close this window.")
