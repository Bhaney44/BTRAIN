#Copyright Brian Haney 2021

# Widgets
from tkinter import *
from tkinter.messagebox import *
import csv

master = Tk()
label0 = Label(master, text = 'BTC', relief = 'groove', width = 25)
label1 = Label(master, text = 'BCH', relief = 'groove', width = 25)
label2 = Label(master, text = 'XTZ', relief = 'groove', width = 25)
label3 = Label(master, text = 'ETH', relief = 'groove', width = 25)
label4 = Label(master, text = 'CVC', relief = 'groove', width = 25)
label5 = Label(master, text = 'Close Price Today', relief = 'groove', width = 25)
label6 = Label(master, text = 'Close Price Tomorrow', relief = 'groove', width = 25)

#Input
entry0 = Entry(master, relief = 'groove', width = 12)
entry1 = Entry(master, relief = 'groove', width = 12)
entry2 = Entry(master, relief = 'groove', width = 12)
entry3 = Entry(master, relief = 'groove', width = 12)
entry4 = Entry(master, relief = 'groove', width = 12)

#Output
blank0 = Entry(master, relief = 'groove', width = 12)
blank1 = Entry(master, relief = 'groove', width = 12)
blank2 = Entry(master, relief = 'groove', width = 12)
blank3 = Entry(master, relief = 'groove', width = 12)
blank4 = Entry(master, relief = 'groove', width = 12)

#Close
def close_value():

    def btc_close():
        btc_0 = float(entry0.get())
        btc_1 = btc_0 * 1.07
        blank0.insert(0, btc_1)
        #return btc_1
    btc_close()

    def bch_close():
        bch_0 = float(entry1.get())
        bch_1 = bch_0 * 1.07
        blank1.insert(0, bch_1)
        #return bch_1
    bch_close()
    
    def xtz_close():
        xtz_0 = float(entry2.get())
        xtz_1 = xtz_0 * 1.09
        blank2.insert(0, xtz_1)
        #return xtz_1
    xtz_close()

    def eth_close():
        eth_0 = float(entry3.get())
        eth_1 = eth_0 * 1.07
        blank3.insert(0, eth_1)
        #return eth_1
    eth_close()
        
    def cvc_close():
        cvc_0 = float(entry4.get())
        cvc_1 = cvc_0 * 1.096
        blank4.insert(0, cvc_1)
        #return cvc_1
    cvc_close()
    
def clear():
    entry0.delete(0,END)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

    
button1 = Button(master, text = 'Close Value', relief = 'groove', width = 20, command = close_value)
button2 = Button(master, text = 'Clear', relief = 'groove', width = 20, command = clear)

#Geometry
label0.grid( row = 2, column = 1, padx = 10 )
label1.grid( row = 3, column = 1, padx = 10 )
label2.grid( row = 4, column = 1, padx = 10 )
label3.grid( row = 5, column = 1, padx = 10 )
label4.grid( row = 6, column = 1, padx = 10 )
label5.grid( row = 1, column = 2, padx = 10 )
label6.grid( row = 1, column = 3, padx = 10 )

entry0.grid( row = 2, column = 2, padx = 10 )
entry1.grid( row = 3, column = 2, padx = 10 )
entry2.grid( row = 4, column = 2, padx = 10 )
entry3.grid( row = 5, column = 2, padx = 10 )
entry4.grid( row = 6, column = 2, padx = 10 )

blank0.grid( row = 2, column = 3, padx = 10 )
blank1.grid( row = 3, column = 3, padx = 10 )
blank2.grid( row = 4, column = 3, padx = 10 )
blank3.grid( row = 5, column = 3, padx = 10 )
blank4.grid( row = 6, column = 3, padx = 10 )

button1.grid( row = 7, column = 2, columnspan = 2)
button2.grid( row = 8, column = 2, columnspan = 2)

#Static Properties
master.title('AI Cryptocurrency Valuation')
