'''
Program: monexchange
Author: Mathurin (094) and Thatchakon (053)
Version: Alpha 2.0
Date modified: 22/11/2014 10.41 AM
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
        #Try to connect The API 
        try:
            self.country = json.load(urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/countries'))
            self.mess = 'Pass'
        except:
            self.mess = tkMessageBox.showerror('Error!', 'Can\'t connect to API.')
    def thisrate(self, val1, val2):
        return json.load(urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/convert?q=%s_%s&compact=y' % (val1, val2)))
class App:
    def __init__(self, main):
        #Edit GUI Here
        #Label
        self.text = self.textlabel(main, 'TO ', '#A9742B')
        #Fillbox
        self.fill1 = self.textfill(value.money1)
        self.fill1.config(width=40)
        #Dropdown
        self.select1 = self.select(value.curr1, country)
        self.select1.config(width=20)
        self.select2 = self.select(value.curr2, country)
        self.select2.config(width=20)
        #Button
        self.button = Button(main, text = 'EXCHANGE !', command = self.calculate)
        self.button.config(height = 2, width = 10)
    def textfill(self, var_money):
        #Create Text Fill <Entry>
        return Entry(main, textvariable = var_money, bg = '#fcb062')
    def select(self, inputvalues, list_country):
        #Create Dropdown Menu
        return apply(OptionMenu, (main, inputvalues) + tuple(list_country))
    def textlabel(self, main, your_text, color = '#A9742B'):
        #Create Label
        return Label(main, text = your_text, bg = color)
    def calculate(self):
        #Calculate money exchange
        money1 = value.money1.get()
        current1 = value.curr1.get()
        current2 = value.curr2.get()
        rate = mainConnect.thisrate(short[current1], short[current2])
        present = float(money1)*rate['%s_%s' % (short[current1], short[current2])]['val']
        self.text1 = self.textlabel(main, present)
        self.text1.place(x = 150, y = 350)
class Allvalues:
    '''
    Set All Values
    '''
    def __init__(self):
        #All of Values in Program
        self.money1 = StringVar()
        self.curr1 = StringVar()
        self.curr2 = StringVar()
def guipack():
    #Build and Display Widgets in mainGUI
    mainGUI.fill1.place(x = 80, y = 200)
    mainGUI.select1.place(x = 10, y = 250)
    mainGUI.text.place(x = 190, y = 255)
    mainGUI.select2.place(x = 225, y = 250)
    mainGUI.button.place(x = 160, y = 300)
def addcountry():
    #Create and return List of Country
    country = list()
    short_form = dict()
    for i in mainConnect.country['results'].keys():
        if mainConnect.country['results'][i]['currencyName'] not in country:
            country.append(mainConnect.country['results'][i]['currencyName'])
            short_form[mainConnect.country['results'][i]['currencyName']] = mainConnect.country['results'][i]['currencyId']
    return (country, short_form)
main = Tk()
main.title('monexchange')
main.geometry('400x600')
main.configure(background = '#A9742B')
value = Allvalues()
mainConnect = Connection()
canvas = Canvas(main, bd = 0, bg='#A9742B', width=400, height=160, highlightthickness=0, relief='ridge')
canvas.pack()
logo = PhotoImage(file = "logoo2.gif")
canvas.create_image(200, 80, image=logo)
if mainConnect.mess != 'ok':
    value.curr1.set('Change Country')
    value.curr2.set('Change Country')
    country, short = addcountry()
    mainGUI = App(main)
    guipack()
    main.mainloop()
else:
    main.destroy()
