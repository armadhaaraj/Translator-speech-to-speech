#speech to text
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("SAY SOMETHING")
    audio = r.listen(source)
    print("TIME OVER")

try:
    print("TEXT: "+r.recognize_google(audio));
except:
    pass;

#to translate the text

from textblob import TextBlob
word1 = TextBlob('how are you')
a = word1.translate(from_lang='en', to ='ta')
print (a)

word2 = TextBlob(u'how are you')
b = word2.translate(from_lang='en', to ='hi')
print (b)

word3 = TextBlob(u'how are you')
c=word3.translate(from_lang='en' , to ='ja')
print (c)

word4 = TextBlob(u'how are you')
d=word4.translate(from_lang='en' , to ='ar')
print (d)

word5 = TextBlob(u'how are you')
e = word5.translate(from_lang='en' , to ='zh-CN')
print (e)

#translated speech

va = str(b)
from gtts import gTTS
text =va

speech = gTTS(text,'ta','slow')

#output as tamilhai,mp3

speech.save("tamilhai.mp3")

