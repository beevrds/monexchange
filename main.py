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
from PIL import ImageTk, Image
class Connection:
    def __init__(self):
        try:
            self.country = json.load(urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/countries'))
            self.mess = 'Pass'
        except:
            self.mess = tkMessageBox.showerror('Error!', 'Can\'t connect to API.')
class App:
    def __init__(self, main):
        #Edit GUI Here
        self.text = Label(main, text = 'to', bg = '#A9742B')
        self.fill1 = self.textfill(value.money1)
        self.fill2 = self.textfill(value.money2)
        self.select1 = self.select(value.current1, country)
        self.select1.config(width=20)
        self.select2 = self.select(value.current2, country)
        self.select2.config(width=20)
        self.button = Button(main, text = 'OK', command = 'Test')
    def textfill(self, var_money):
        return Entry(main, textvariable = var_money, bg = '#fcb062')
    def select(self, inputvalues, list_country):
        return apply(OptionMenu, (main, inputvalues) + tuple(list_country))
    def printt(self):
        '''Test Button'''
        print current.money1.get()
class Allva:
    '''
    Set All Values
    '''
    def __init__(self):
        self.money1 = IntVar()
        self.money2 = IntVar()
        self.current1 = StringVar()
        self.current2 = StringVar()
def guipack():
    '''
    Build and Display Widgets in mainGUI
    '''
    mainGUI.fill1.place(x = 130, y = 200)
    mainGUI.select1.place(x = 10, y = 250)
    mainGUI.text.place(x = 190, y = 255)
    mainGUI.select2.place(x = 225, y = 250)
##    mainGUI.button.pack()
def addcountry():
    country = list()
    for i in mainConnect.country['results'].keys():
        country.append(mainConnect.country['results'][i]['currencyName'])
    return country
main = Tk()
main.title('monexchange')
main.geometry('400x600')
main.configure(background = '#A9742B')
value = Allva()
mainConnect = Connection()
canvas = Canvas(main, bd = 0, bg='#A9742B', width=400, height=160, highlightthickness=0, relief='ridge')
canvas.pack()
local_logo = Image.open("logoo2.gif")
logo = ImageTk.PhotoImage(local_logo)
canvas.create_image(200, 80, image=logo)
##panel = Label(main, image = logo)
##panel.photo = local_logo
##panel.pack()
if mainConnect.mess != 'ok':
    value.current1.set('Change Country')
    value.current2.set('Change Country')
    country = addcountry()
    mainGUI = App(main)
    guipack()
    main.mainloop()
else:
    main.destroy()
