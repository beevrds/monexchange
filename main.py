'''
Program: monexchange
Author: Mathurin (094) and Thatchakon (053)
Version: Alpha 1.0
Date modified: 15/11/2014 11.41 AM
Detail: Currency Exchanging Program by input number of money and
        select input's currency and another one currency which
        you want to exchange.
API : http://www.freecurrencyconverterapi.com/api
'''
import json
import urllib2
from Tkinter import *
import tkMessageBox
class connection:
    def __init__(self):
        try:
            self.country = json.load(urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/countries'))
        except:
            This_mess = tkMessageBox.showerror('Error!', 'Can\'t connect to API.')
            if This_mess == 'ok':
                main.destroy()
class app:
    def __init__(self, main):
        #Edit GUI Here
        self.textwelcome = Label(main, text = 'monexchange')
        
main = Tk()
main.title('monexchange')
main.geometry('400x400')
mainGUI = app(main)
mainGUI.textwelcome.pack()
mainConnect = connection()
main.mainloop()
