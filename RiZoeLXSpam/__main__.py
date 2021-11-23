#RiZoeLXSpam By @TheRiZoeL

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from RiZoeLXSpam.utils import load_plugins
import logging
from telethon import events
from . import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "RiZoeLXSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("RiZoeL Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @RiZoeLX")

if __name__ == "__main__":
    Riz.run_until_disconnected()
    
if __name__ == "__main__":
    Riz2.run_until_disconnected()

if __name__ == "__main__":
    Riz3.run_until_disconnected()
    
if __name__ == "__main__":
    Riz4.run_until_disconnected()

if __name__ == "__main__":
    Riz5.run_until_disconnected()
    
if __name__ == "__main__":
    Riz6.run_until_disconnected()
    
if __name__ == "__main__":
    Riz7.run_until_disconnected()

if __name__ == "__main__":
    Riz8.run_until_disconnected()
    
if __name__ == "__main__":
    Riz9.run_until_disconnected()

if __name__ == "__main__":
    Riz10.run_until_disconnected()    
