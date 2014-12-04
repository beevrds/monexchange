'''
Program: monexchange
Author: Mathurin (094) and Thatchakon (053)
Version: 1.0
Date modified: 04/12/2014 09.16 AM
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
    def __init__(self):
        #Try to connect The API 
        try:
            self.country = json.load(urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/countries'))
            self.mess = 'Pass'
        except:
            self.mess = Msgbox.showerror('Error!', 'Can\'t connect to API.')
    def thisrate(self, val1, val2):
        return json.load(urllib2.urlopen('http://www.freecurrencyconverterapi.com/api/v2/convert?q=%s_%s&compact=y' % (val1, val2)))
class App:
    def __init__(self, main):
        #Edit GUI Here
        #Label
        self.text = self.textlabel(main, 'TO ', '#A9742B')
        self.texta = self.textlabel(main, 'App Created & Developed : 11/11/2014 - 04/12/14', '#A9742B')
        #Fillbox
        self.fill1 = self.textfill(value.money1)
        self.fill1.config(width=22, font = ('', 14))
        self.fill2 = self.textfill(value.present)
        self.fill2.config(width=16, state='readonly', readonlybackground='#fcb062', font = ('', 20))
        #Dropdown
        self.select1 = self.select(value.curr1, country)
        self.select1.config(width=20, highlightbackground = '#A9742B')
        self.select2 = self.select(value.curr2, country)
        self.select2.config(width=20, highlightbackground = '#A9742B')
        #Button
        self.button = Button(main, text = 'EXCHANGE !', command = self.calculate)
        self.button.config(height = 2, width = 10)
        #MenuBar
        self.menuBar = Menu(main)
        self.aboutMenu = Menu(self.menuBar, tearoff=0)
        self.aboutMenu.add_command(label="About", command=self.about_window)
        self.menuBar.add_cascade(label="About", menu=self.aboutMenu)
        main.config(menu=self.menuBar)
    def textfill(self, var):
        #Create Text Fill <Entry>
        return Entry(main, textvariable = var, bg = '#fcb062')
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
        try:
            if current1 == 'Change Country' or current2 == 'Change Country':
                Msgbox.showerror('Error!', 'Please Select Country')
            else:
                rate = mainConnect.thisrate(short[current1], short[current2])
                if len(rate) == 0:
                    Msgbox.showerror('Error!', 'Can\'t connect to rate API \n Please try again later!')
                else:
                    present = float(money1)*rate['%s_%s' % (short[current1], short[current2])]['val']
                    value.present.set('%.4f' % present)
        except:
            Msgbox.showerror('Error!', 'Please Insert Integer (ex. 100)\n Or Float (ex. 120.75) Only -w-')
    def about_window(self):
        def thatOk():
          about.destroy()
        about = Toplevel(main, bg='#A9742B')
        about.geometry('200x140')
        about.title("About")
        about_message = "monexchange by Thatchakon and Mathurin \n for PSIT Project \n Faculty of \n Information technology \n KMITL"
        msg = Message(about, text=about_message, justify=CENTER, bg='#A9742B', font = ('', 10))
        msg.pack()
        button = Button(about, text="Ok", command=thatOk)
        button.pack()
class Allvalues:
    '''
    Set All Values
    '''
    def __init__(self):
        #All of Values in Program
        self.money1 = StringVar()
        self.curr1 = StringVar()
        self.curr2 = StringVar()
        self.present = StringVar()
def guipack():
    #Build and Display Widgets in mainGUI
    mainGUI.fill1.place(x = 80, y = 200)
    mainGUI.select1.place(x = 10, y = 250)
    mainGUI.text.place(x = 190, y = 255)
    mainGUI.select2.place(x = 225, y = 250)
    mainGUI.button.place(x = 160, y = 300)
    mainGUI.fill2.place(x = 80, y = 350)
    mainGUI.texta.place(x = 70, y = 430)
def addcountry():
    #Create and return List of Country
    country = list()
    short_form = dict()
    for i in mainConnect.country['results'].keys():
        if mainConnect.country['results'][i]['currencyName'] not in country:
            country.append(mainConnect.country['results'][i]['currencyName'])
            short_form[mainConnect.country['results'][i]['currencyName']] = mainConnect.country['results'][i]['currencyId']
    return (country, short_form)
if __name__ == "__main__":
    main = Tk()
    main.title('monexchange')
    main.geometry('400x450')
    main.resizable(width=FALSE, height=FALSE)
    main.configure(background = '#A9742B')
    value = Allvalues()
    mainConnect = Connection()
    canvas = Canvas(main, bd = 0, bg='#A9742B', width=400, height=160, highlightthickness=0, relief='ridge')
    canvas.pack()
    logo = PhotoImage(file = "logoo2.gif")
    canvas.create_image(200, 80, image=logo)
    if mainConnect.mess != 'ok':
        value.money1.set('0')
        value.present.set('0.0000')
        value.curr1.set('Change Country')
        value.curr2.set('Change Country')
        country, short = addcountry()
        mainGUI = App(main)
        guipack()
        main.mainloop()
    else:
        main.destroy()
