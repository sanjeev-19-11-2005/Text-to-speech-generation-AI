from gtts import gTTS
from IPython.display import Audio

text = "அகர முதல எழுத்தெல்லாம் ஆதி பகவன் முதற்றே உலகு"

tts = gTTS(text,lang='ta')

tts.save("welcome_message.mp3")
Audio("welcome_message.mp3",autoplay=True)