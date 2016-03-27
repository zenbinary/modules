# -*- coding: utf-8 -*-
"""
Adds procrastination sites to the hosts file/refreshes DNS

@author zenbinary   zenbinary@gmail.com
"""

# import your useful libs here
import time
import os

class Py3status:
    
    # available configuration parameters
    cache_timeout = 10

    def __init__(self):
        """
        This is the class constructor which will be executed once.
        """
        self.status = 'stop'

    def on_click(self, i3s_output_list, i3s_config, event):
        
        if event['button'] == 1:
            if self.status == 'stop':
                self.status = 'start'
                self.block_sites()
            elif self.status == 'start':
                self.status = 'stop'
                self.unblock_sites()

    def hosts(self, i3s_output_list, i3s_config):
       
        response = {
            'color': '#FF0000',
            'cached_until': time.time() + self.cache_timeout,
            'full_text': ' X '
        }
        
        if self.status == 'start':
            response['color'] = '#00A5FF'
            response['full_text'] = ' X '
        elif self.status == 'stop':
            response['color'] = '#cb4b16'
            response['full_text'] = ' X '
        
        return response
    
    def block_sites(self):
        os.popen('pkexec /home/zen/core/i3mods/block_sites')

    def unblock_sites(self):
        os.popen('pkexec /home/zen/core/i3mods/unblock_sites')

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    This SHOULD work before contributing your module please.
    """
    from time import sleep
    x = Py3status()
    config = {
        'color_bad': '#FF0000',
        'color_degraded': '#FFFF00',
        'color_good': '#00FF00'
    }
    while True:
        print(x.hosts([], config))
        sleep(1)
