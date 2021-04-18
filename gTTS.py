import gTTS
from gtts import gTTS
import os
tts = gTTS(text='namstey, India', lang='hi', slow=True)

tts.save("namstey.mp3")

os.system("mpg321 namstey.mp3")
