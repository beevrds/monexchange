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
class Connection:
    def __init__(self):
        try:
            self.country = json.load(urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/countries'))
        except:
            This_mess = tkMessageBox.showerror('Error!', 'Can\'t connect to API.')
            if This_mess == 'ok':
                main.destroy()
class App:
    def __init__(self, main):
        #Edit GUI Here
        self.values()
        self.textwelcome = Label(main, text = 'monexchange')
        self.fill1 = self.textfill(self.money1)
        self.fill2 = self.textfill(self.money2)
        self.button = Button(main, text = 'OK', command = '#command#')
    def values(self):
        self.money1 = IntVar()
        self.money2 = IntVar()
    def textfill(self, var_money):
        return Entry(main, textvariable = var_money)
main = Tk()
main.title('monexchange')
main.geometry('400x600')
values = StringVar
values2 = StringVar
mainGUI = App(main)
mainGUI.textwelcome.pack()
mainGUI.fill1.pack()
mainGUI.fill2.pack()
mainConnect = Connection()
main.mainloop()
