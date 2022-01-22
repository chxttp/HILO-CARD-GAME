from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import random as rand
import time

class Hi_Lo_Game(Frame):
    def __init__(self, master = None):
        self.uniCode = {
            1: ('/U0001F0B1', '1 Hearts'), 2: ('/U0001F0B2', '2 Hearts'), 3: ('/U0001F0B3', '3 Hearts'), 4: ('/U0001F0B4', '4 Hearts'), 5: ('/U0001F0B5', '5 Hearts'), 6: ('/U0001F0B6', '6 Hearts'), 7: ('/U0001F0B7', '7 Hearts'), 8: ('/U0001F0B8', '8 Hearts'), 9: ('/U0001F0B9', '9 Hearts'), 10: ('/U0001F0BA', '10 Hearts'), 11: ('/U0001F0BB', 'J Hearts'), 12: ('/U0001F0BD', 'Q Hearts'), 13: ('/U0001F0BE', 'K Hearts'),
            14: ('/U0001F0C1', '1 Diamonds'), 15: ('/U0001F0C2', '2 Diamonds'), 16: ('/U0001F0C3', '3 Diamonds'), 17: ('/U0001F0C4', '4 Diamonds'), 18: ('/U0001F0C5', '5 Diamonds'), 19: ('/U0001F0C6', '6 Diamonds'), 20: ('/U0001F0C7', '7 Diamonds'), 21: ('/U0001F0C8', '8 Diamonds'), 22: ('/U0001F0C9', '9 Diamonds'), 23: ('/U0001F0CA', '10 Diamonds'), 24: ('/U0001F0CB', 'J Diamonds'), 25: ('/U0001F0CD', 'Q Diamonds'), 26: ('/U0001F0CE', 'K Diamonds'),
            27: ('/U0001F0D1', '1 Clubs'), 28: ('/U0001F0D2', '2 Clubs'), 29: ('/U0001F0D3', '3 Clubs'), 30: ('/U0001F0D4', '4 Clubs'), 31: ('/U0001F0D5', '5 Clubs'), 32: ('/U0001F0D6', '6 Clubs'), 33: ('/U0001F0D7', '7 Clubs'), 34: ('/U0001F0D8', '8 Clubs'), 35: ('/U0001F0D9', '9 Clubs'), 36: ('/U0001F0DA', '10 Clubs'), 37: ('/U0001F0DB', 'J Clubs'), 38: ('/U0001F0DD', 'Q Clubs'), 39: ('/U0001F0DE', 'K Clubs'),
            40: ('/U0001F0A1', '1 Spades'), 41: ('/U0001F0A2', '2 Spades'), 42: ('/U0001F0A3', '3 Spades'), 43: ('/U0001F0A4', '4 Spades'), 44: ('/U0001F0A5', '5 Spades'), 45: ('/U0001F0A6', '6 Spades'), 46: ('/U0001F0A7', '7 Spades'), 47: ('/U0001F0A8', '8 Spades'), 48: ('/U0001F0A9', '9 Spades'), 49: ('/U0001F0AA', '10 Spades'), 50: ('/U0001F0AB', 'J Spades'), 51: ('/U0001F0AD', 'Q Spades'), 52: ('/U0001F0AE', 'K Spades')
        }
        self.record = dict()
        self.PATH = os.path.dirname(__file__) + '/images' 
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand = 1) ##เว้น 1
        load = Image.open(r'%s' %(self.PATH + '/Table.jpg'))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        load1 = Image.open(r'%s' %(self.PATH + '/Coin10b.png'))
        render1 = ImageTk.PhotoImage(load1)
        btn1 = Button(self, image = render1, borderwidth = 0, activebackground = '#2D375A', bg = '#2D375A', command = self.clickCoin10)##border width 0 ไม่มีขอบ
        btn1.image = render1
        btn1.place(x = 50, y = 560)
    
        load2 = Image.open(r'%s' %(self.PATH + '/Coin20b.png'))
        render2 = ImageTk.PhotoImage(load2)
        btn2 = Button(self, image=render2, borderwidth = 0, activebackground = '#2D375A', bg = '#2D375A', command = self.clickCoin20)
        btn2.image = render2
        btn2.place(x = 150, y = 560)
        
        load3 = Image.open(r'%s' %(self.PATH + '/Coin50b.png'))
        render3 = ImageTk.PhotoImage(load3)
        btn3 = Button(self, image=render3, borderwidth = 0, activebackground = '#2D375A', bg = '#2D375A', command = self.clickCoin50)
        btn3.image = render3
        btn3.place(x = 250, y = 560)
        
        load4 = Image.open(r'%s' %(self.PATH + '/Coin100b.png'))
        render4 = ImageTk.PhotoImage(load4)
        btn4 = Button(self, image=render4, borderwidth = 0, activebackground = '#2D375A', bg = '#2D375A', command = self.clickCoin100)
        btn4.image = render4
        btn4.place(x = 350, y = 560)

        l1 = Label(self, text = 'BET', fg = 'white', bg = '#00815A', font = (None, 18))
        l1.place(x = 455, y = 400)

        self.str1 = StringVar()
        self.str1.set('0')
        entry1 = Entry(self, textvariable = self.str1, justify = CENTER, font = (None, 18))
        entry1.place(x = 435, y = 435, width = 100, height = 40)

        btnHigh = Button(self, text = 'HIGH', bg = '#CCA727', command = self.clickHigh)
        btnHigh.place(x = 300, y = 400, width = 100, height = 40)

        btnLow = Button(self, text = 'LOW', bg = '#CCA727', command = self.clickLow)
        btnLow.place(x = 570, y = 400, width = 100, height = 40)

        btnClear = Button(self, text = 'CLEAR', fg = 'white', bg = '#007F6D', command = self.clickClear)
        btnClear.place(x = 550, y = 585, width = 100, height = 40)

        btnDouble = Button(self, text = 'DOUBLE', fg = 'white', bg = '#007F6D', command = self.clickDouble)
        btnDouble.place(x = 700, y = 585, width = 100, height = 40)

        btnReport = Button(self, text = 'REPORT', fg = 'white', bg = '#2D375A', command = self.clickReport)
        btnReport.place(x = 850, y = 585, width = 100, height = 40)

        load5 = Image.open(r'%s' %(self.PATH + '/BackCard.png'))
        render5 = ImageTk.PhotoImage(load5)
        self.labelBot = Label(self, image=render5)
        self.labelBot.image = render5
        self.labelBot.place(x = 380, y = 210)

        self.labelPlayer = Label(self, image=render5)
        self.labelPlayer.image = render5 
        self.labelPlayer.place(x = 490, y = 210)

        load6 = Image.open(r'%s' %(self.PATH + '/coin.png'))
        render6 = ImageTk.PhotoImage(load6)
        labelMoney = Label(self, image=render6)
        labelMoney.image = render6
        labelMoney.place(x = 5, y = 5)

        self.labelMoney1 = Label(self, text = '1000', fg = 'black', bg = '#F4CE3F', font = (None, 20))
        self.labelMoney1.place(x = 50, y = 8)
        
        self.labelTime = Label(self, text = '', fg = 'red', bg = '#2D375A', font = ('Helvetica', 18))
        self.labelTime.place(x = 850, y = 20)
        self.updateClock()

        self.gameStart()

    def clickCoin10(self):
        money = int(self.labelMoney1.cget('text'))
        bet = int(self.str1.get()) + 10
        if money >= bet:
            self.str1.set(bet)
        else:
            messagebox.showerror('ERROR', 'Not enough money')
    def clickCoin20(self):
        money = int(self.labelMoney1.cget('text'))
        bet = int(self.str1.get()) + 20
        if money >= bet:
            self.str1.set(bet)
        else:
            messagebox.showerror('ERROR', 'Not enough money')
    def clickCoin50(self):
        money = int(self.labelMoney1.cget('text'))
        bet = int(self.str1.get()) + 50
        if money >= bet:
            self.str1.set(bet)
        else:
            messagebox.showerror('ERROR', 'Not enough money')
    def clickCoin100(self):
        money = int(self.labelMoney1.cget('text'))
        bet = int(self.str1.get()) + 100
        if money >= bet:
            self.str1.set(bet)
        else:
            messagebox.showerror('ERROR', 'Not enough money')
    def clickHigh(self):
        if self.str1.get().isnumeric():
            if int(self.str1.get()) == 0:
                messagebox.showerror('Input Bet', 'Input Bet')
            elif int(self.labelMoney1.cget('text')) > 9999:
                messagebox.showerror('Balance Over', 'Balance > 9,999')
            elif int(self.str1.get()) > int(self.labelMoney1.cget('text')):
                messagebox.showerror('Over Balance', 'Bet is more than Balance')
            else:
                self.numberPlay = rand.randint(1, 52)
                self.player = self.numberPlay % 13
                if self.player > 9 or self.player == 0:
                    self.player = 10
                card = '/Card' + str(self.numberPlay) + '.png'
                loadPlayer = Image.open(r'%s' %(self.PATH + card))
                renderPlayer = ImageTk.PhotoImage(loadPlayer)
                self.labelPlayer.configure(image = renderPlayer)
                self.labelPlayer.image = renderPlayer
                if self.bot == self.player:
                    messagebox.showinfo('', 'DRAW')
                    self.addReport('HIGH', '0')
                elif self.bot > self.player:
                    money = int(self.labelMoney1.cget('text')) - int(self.str1.get())
                    self.labelMoney1.configure(text = money)
                    messagebox.showinfo('', 'LOST')
                    self.addReport('HIGH', '-' + self.str1.get())
                else:
                    money = int(self.labelMoney1.cget('text')) + int(self.str1.get())
                    self.labelMoney1.configure(text = money)
                    messagebox.showinfo('', 'WIN')
                    self.addReport('HIGH', '+' + self.str1.get())
                self.gameStart()
        else:
            messagebox.showerror('Not Numeric', 'Please input only Positive Integer')
    def clickLow(self):
        if self.str1.get().isnumeric():
            if int(self.str1.get()) == 0:
                messagebox.showerror('Input Bet', 'Input Bet')
            elif int(self.labelMoney1.cget('text')) > 9999:
                messagebox.showerror('Balance Over', 'Balance > 9,999')
            elif int(self.str1.get()) > int(self.labelMoney1.cget('text')):
                messagebox.showerror('Over Balance', 'Bet is more than Balance')
            else:
                self.numberPlay = rand.randint(1, 52)
                self.player = self.numberPlay % 13
                if self.player > 9 or self.player == 0:
                    self.player = 10
                card = '/Card' + str(self.numberPlay) + '.png'
                loadPlayer = Image.open(r'%s' %(self.PATH + card))
                renderPlayer = ImageTk.PhotoImage(loadPlayer)
                self.labelPlayer.configure(image = renderPlayer)
                self.labelPlayer.image = renderPlayer
                if self.bot == self.player:
                    messagebox.showinfo('', 'DRAW')
                    self.addReport('LOW', '0')
                elif self.bot > self.player:
                    money = int(self.labelMoney1.cget('text')) + int(self.str1.get())
                    self.labelMoney1.configure(text = money)
                    messagebox.showinfo('', 'WIN')
                    self.addReport('LOW', '+' + self.str1.get())
                else:
                    money = int(self.labelMoney1.cget('text')) - int(self.str1.get())
                    self.labelMoney1.configure(text = money)
                    messagebox.showinfo('', 'LOST')
                    self.addReport('LOW', '-' + self.str1.get())
                self.gameStart()
        else:
            messagebox.showerror('Not Numeric', 'Please input only positive integer')
    def clickClear(self):
        self.str1.set('0')
        self.labelMoney1.configure(text = '1000')
        self.record = dict()
    def clickDouble(self):
        money = int(self.labelMoney1.cget('text'))
        bet = int(self.str1.get()) * 2
        if money >= bet:
            self.str1.set(bet)
        else:
            messagebox.showerror('ERROR', 'Not enough money')
    def addReport(self, result, bet):
        now = time.strftime("%H:%M:%S")
        self.record[now] = [self.uniCode[self.numberBot], self.uniCode[self.numberPlay], result, bet]
    def clickReport(self):
        if len(self.record) > 0:
            txt = ''
            for x in self.record:
                txt2 = "{0} BOT {1}, USER {2} Select: {3}, Result: {4}".format(x, self.record[x][0], self.record[x][1], self.record[x][2] , self.record[x][3])
                txt += txt2 + '\n'
            messagebox.showinfo(' ', txt)
        else:
            messagebox.showwarning('No Record', 'No Record')
    def gameStart(self):
        card = '/BackCard.png'
        loadPlayer = Image.open(r'%s' %(self.PATH + card))
        renderPlayer = ImageTk.PhotoImage(loadPlayer)
        self.labelPlayer.configure(image = renderPlayer)
        self.labelPlayer.image = renderPlayer
        self.numberBot = rand.randint(1, 52)
        self.bot = self.numberBot % 13
        if self.bot > 9 or self.bot == 0:
            self.bot = 10
        card = '/Card' + str(self.numberBot) + '.png'
        loadBot = Image.open(r'%s' %(self.PATH + card))
        renderBot = ImageTk.PhotoImage(loadBot)
        self.labelBot.configure(image = renderBot)
        self.labelBot.image = renderBot
    def updateClock(self):
        now = time.strftime("%H:%M:%S")
        self.labelTime.configure(text = now)
        self.after(1000, self.updateClock)
root = Tk()
app = Hi_Lo_Game(root)
root.wm_title("HI LO CARD GAME")
root.geometry("966x646")
root.mainloop() 