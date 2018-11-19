from gpiozero import Button
from time import sleep
import simpleaudio as sa

button = Button(2, pull_up = true)
audio = sa.WaveObject.from_wave_file()
playAudio = audio.play()
while true:
    if button.is_released:
        playAudio.wait_done()
    pass
