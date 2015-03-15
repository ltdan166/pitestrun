'''
Created on 11 Mar 2015

@author: Dang Quang
'''
##WS for Rapsberry PI
import cherrypy
import test

class HelloCherry:
    
    def index(self):
        #Ask for the parameters
        return '''
            <form action="blink" method="GET">
            Number of times to blink : 
            <input type="text" name="tme"/>
            Length of each blink : 
            <input type="text" name="length"/>
            <input type="submit"/>
            </form>'''
    index.exposed = True
    
    def blink(self, tme=None, length=None):
        #if both params are correct
        if int(tme) and float(length):
            test.Blink (int(tme), float (length))
        else:
            print ("The parameters are incorrects")
    blink.exposed = True

import os.path
tutconf = os.path.join('/home/pi/Desktop/', 'tutorial.conf')

if __name__ == '__main__':
    cherrypy.quickstart(HelloCherry(), config=tutconf)
else:
    cherrypy.tree.mount(HelloCherry(), config=tutconf)
    
