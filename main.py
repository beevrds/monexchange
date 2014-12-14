'''
Program: monexchange
Author: Mathurin (094) and Thatchakon (053)
Version: 1.0
Date modified: 13/12/2014 21.35 PM
Detail: Currency Exchanging Program by input number of money and
        select input's currency and another one currency which
        you want to exchange.
API : http://www.freecurrencyconverterapi.com/api
'''
import json
import urllib2
from Tkinter import *
import tkMessageBox as Msgbox
class Connection:
    #Connect the API
    def __init__(self):
        '''Try to connect The API '''
        try:
            self.country = json.load(urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/countries'))
            self.mess = 'Pass'
        except:
            self.mess = Msgbox.showerror('Error!', 'Can\'t connect to API.')
    def thisrate(self, val1, val2):
        '''Return Rate of money'''
        return json.load(urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/convert?q=%s_%s&compact=y' % (val1, val2)))
class App:
    #Main GUI
    def __init__(self, main):
        '''GUI Editing Function'''
        #Label
        self.text = self.textlabel(main, 'TO ', '#A9742B')
        self.texta = self.textlabel(main, 'App Created & Developed : 11/11/2014 - 04/12/14', '#A9742B')
        #Fillbox
        self.fill1 = self.textfill(value.money1)
        self.fill1.config(width=22, font = ('', 14))
        self.fill1.bind('<Return>', self.call_calculate)
        self.fill2 = self.textfill(value.present)
        self.fill2.config(width=16, state='readonly', readonlybackground='#fcb062', font = ('', 20))
        #Dropdown
        self.select1 = self.select(value.curr1, start.country)
        self.select1.config(width=20, highlightbackground = '#A9742B')
        self.select2 = self.select(value.curr2, start.country)
        self.select2.config(width=20, highlightbackground = '#A9742B')
        #Button
        self.button = Button(main, text = 'EXCHANGE !', command = self.calculate)
        self.button.config(height = 2, width = 10)
        #MenuBar
        self.menuBar = Menu(main)
        self.aboutMenu = Menu(self.menuBar, tearoff=0)
        self.aboutMenu.add_command(label="About", command=self.about_window)
        self.menuBar.add_cascade(label="About", menu=self.aboutMenu)
        self.exitMenu = Menu(self.menuBar, tearoff=0)
        self.exitMenu.add_command(label="Exit", command=main.quit)
        self.menuBar.add_cascade(label="Exit", menu=self.exitMenu)
        main.config(menu=self.menuBar)
    def textfill(self, var):
        '''Create Text Fill <Entry>'''
        return Entry(start.main, textvariable = var, bg = '#fcb062')
    def select(self, inputvalues, list_country):
        '''Create Dropdown Menu'''
        return apply(OptionMenu, (start.main, inputvalues) + tuple(list_country))
    def textlabel(self, main, your_text, color = '#A9742B'):
        '''Create Label'''
        return Label(start.main, text = your_text, bg = color)
    def calculate(self):
        '''Calculate money exchange'''
        money1 = value.money1.get()
        current1 = value.curr1.get()
        current2 = value.curr2.get()
        try:
            if current1 == 'Change Country' or current2 == 'Change Country':
                Msgbox.showerror('Error!', 'Please Select Country')
            else:
                rate = mainConnect.thisrate(start.short[current1], start.short[current2])
                if len(rate) == 0:
                    Msgbox.showerror('Error!', 'Can\'t connect to rate API \n Please try again later!')
                else:
                    present = float(money1)*rate['%s_%s' % (start.short[current1], start.short[current2])]['val']
                    value.present.set('%.4f' % present)
        except:
            Msgbox.showerror('Error!', 'Please Insert Integer (ex. 100)\n Or Float (ex. 120.75) Only -w-')
    def call_calculate(self, event):
        '''Calcultor calling function'''
        self.calculate()
    def about_window(self):
        '''About Menu Window'''
        def thatOk():
            '''Closing About Window if click OK'''
            about.destroy()
        about = Toplevel(start.main, bg='#FFFFFF')
        about.geometry('250x150')
        about.resizable(width=FALSE, height=FALSE)
        about.title("About")
        about_message = "monexchange by Thatchakon and Mathurin \n for PSIT Project \n Faculty of \n Information technology \n KMITL"
        msg = Message(about, text=about_message, justify=CENTER, bg='#FFFFFF', font = ('', 10))
        msg.pack()
        button = Button(about, text="Ok", command=thatOk)
        button.pack()
    def guipack(self):
        '''Build and Display Widgets in main'''
        self.fill1.place(x = 80, y = 200)
        self.select1.place(x = 10, y = 250)
        self.text.place(x = 190, y = 255)
        self.select2.place(x = 225, y = 250)
        self.button.place(x = 160, y = 300)
        self.fill2.place(x = 80, y = 350)
        self.texta.place(x = 70, y = 430)
class Allvalues:
    #Set All Values
    def __init__(self):
        '''All of Values in Program'''
        self.money1 = StringVar()
        self.curr1 = StringVar()
        self.curr2 = StringVar()
        self.present = StringVar()
    def addcountry(self):
        '''Create and return List of Country'''
        country = list()
        short_form = dict()
        for i in mainConnect.country['results'].keys():
            if mainConnect.country['results'][i]['currencyName'] not in country:
                country.append(mainConnect.country['results'][i]['currencyName'])
                short_form[mainConnect.country['results'][i]['currencyName']] = mainConnect.country['results'][i]['currencyId']
        return (country, short_form)
class Start():
    #Start App
    def __init__(self):
        '''All About App's Structure'''
        self.main = Tk()
        self.main.title('monexchange')
        self.main.geometry('400x450')
        self.main.resizable(width=FALSE, height=FALSE)
        self.main.configure(background = '#A9742B')
        self.main.wm_iconbitmap('logoo_ico.ico')
    def run(self):
        '''App GUI Setting'''
        canvas = Canvas(self.main, bd = 0, bg='#A9742B', width=400, height=160, highlightthickness=0, relief='ridge')
        canvas.pack()
        logo = PhotoImage(file = "logoo2.gif")
        canvas.create_image(200, 80, image=logo)
        if mainConnect.mess != 'ok':
            value.money1.set('0')
            value.present.set('0.0000')
            value.curr1.set('Change Country')
            value.curr2.set('Change Country')
            self.country, self.short = value.addcountry()
            mainGUI = App(self.main)
            mainGUI.guipack()
            self.main.mainloop()
        else:
            self.main.destroy()
start = Start()
mainConnect = Connection()
value = Allvalues()
start.run()
