import requests
import os
import time
import shutil
import subprocess
from git import Repo
import stat

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


def on_rm_error(path):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


lostUB_new = requests.get("https://raw.githubusercontent.com/L-o-s-t/Lost-UB/main/bot.py")
with open("bot_new.py", "w", encoding="utf-8") as new:
    new.write(lostUB_new.text)
if os.path.exists("bot.py"):
    with open("bot.py", "r", encoding="utf-8") as old:
        lostUBold_old = old.read()

    print("[LOST-UPDATER] Checking for updates...")
    time.sleep(3)
    if lostUB_new.text != lostUBold_old:
        if os.path.exists("bot.exe"):
            os.remove("bot.exe")
        print("[LOST-UPDATER] Update found, do not close until done...")
        process = subprocess.Popen("pyinstaller --icon data\\bot.ico --onefile bot_new.py",
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.STDOUT)
        process.wait()
        print("[LOST-UPDATER] Update finished. Cleaning up...")
        shutil.rmtree("build")
        shutil.rmtree("__pycache__")
        os.remove("bot_new.spec")
        os.remove("bot.py")
        os.rename("bot_new.py", "bot.py")
        os.replace("dist/bot_new.exe", "bot_new.exe")
        os.rename("bot_new.exe", "bot.exe")
        shutil.rmtree("dist")
        input("[LOST-UPDATER] You may now close this window")
    elif not os.path.exists("bot.exe"):
        os.remove("bot_new.py")
        print("[LOST-UPDATER] Executable not found, creating executable... Do not close until done.")
        process = subprocess.Popen("pyinstaller --icon data\\bot.ico --onefile bot.py",
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.STDOUT)
        process.wait()
        print("[LOST-UPDATER] Executable created, cleaning up...")
        shutil.rmtree("build")
        shutil.rmtree("__pycache__")
        os.remove("bot.spec")
        os.replace("dist/bot.exe", "bot.exe")
        shutil.rmtree("dist")
        input("[LOST-UPDATER] You may now close this window.")
    else:
        os.remove("bot_new.py")
        input("[LOST-UPDATER] You are already up to date!")

else:
    print("[LOST-UPDATER] Installing Lost-UB...")
    os.remove("bot_new.py")
    Repo.clone_from("https://github.com/L-o-s-t/Lost-UB", "repo/").index.remove(['.github'],
                                                                                True, r=True)
    os.replace("repo/bot.exe", "bot.exe")
    os.replace("repo/bot.py", "bot.py")
    os.remove("repo/updater.exe")
    shutil.copytree("repo/data", "data")
    shutil.rmtree("repo/data")
    os.replace("repo/commands.md", "commands.md")
    os.replace("repo/README.md", "README.md")
    process = subprocess.run("echo y | rmdir /s repo",
                             shell=True,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.STDOUT)
    input("[LOST-UPDATER] Lost-UB was successfully installed. You may now close this window.")
