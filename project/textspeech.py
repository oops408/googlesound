from gtts import gTTS 

import os 

f = open("output.txt", "r")
text_file = f.read()

language = 'en'

tts = gTTS(text=text_file, lang=language, slow=False) 

# Support for multiple accents/languages to come: tld='com.country'

tts.save("file.mp3") 

os.system("afplay file.mp3") 