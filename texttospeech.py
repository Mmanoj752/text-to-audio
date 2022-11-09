from gtts import gTTS
ex=open('sample.txt')
text=ex.read()
language='en'
obj=gTTS(text=text,lang=language,slow=True)
obj.save('sample.mp3')
