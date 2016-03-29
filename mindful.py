# -*- coding: utf-8 -*-

"""
Mindful Bell Module
Plays a bell sound every 5 minutes to remind you to stay mindful

Configuration parameters:
    - cache_timeout : how often we refresh this module in seconds

@author zenbinary zenbinary@gmail.com
"""

# import your useful libs here
#from subprocess import call
#from syslog import syslog, LOG_INFO
#import pyglet
from pygame import mixer
#from time import sleep
import time

mixer.init()

class Py3status:
   # available configuration parameters
    cache_timeout = 1
    bell_sound = "/home/zen/core/i3mods/spotify/bell5.mp3"

    def __init__(self):
        self.status = 'stop' 
        mixer.music.load(self.bell_sound)

    def on_click(self, i3s_output_list, i3s_config, event):
        if event['button'] == 1:
            if self.status == 'stop':
                self.status = 'start'
                self.__play_sound(self.bell_sound) 
            elif self.status == 'start':
                self.status = 'stop'
                self.__stop_sound()  

    def mindful(self, i3s_output_list, i3s_config):
        response = {
            'color': '#FF0000',
            'cached_until': time.time() + self.cache_timeout,
            'full_text': ' ☯ '
        }
        if self.status == 'start':
            response['color'] = '#00A5FF' #33EAFF
            response['full_text'] = ' ☯ '
        elif self.status == 'stop':
            response['color'] = '#cb4b16'
            response['full_text'] = ' ☯ '
        return response
    
    def play_bell():
        mixer.music.play()

    def __play_sound(self, sound_fname):
        mixer.music.play(-1)
        #repeats mp3 indefinitely. 
    def __stop_sound(self):
        mixer.music.stop()
    
if __name__ == "__main__":
    from time import sleep
    x = Py3status()
    config = {
        'color_bad': '#FF0000',
        'color_degraded': '#FFFF00',
        'color_good': '#00FF00'
    }
    while True:
        print(x.mindful([], config))
        sleep(1)
