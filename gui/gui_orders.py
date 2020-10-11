from tkinter import *
from tkinter import ttk
import socket
import sys
import ujson
import common
import random
import time
from threading import Thread

class GuiOrders(Frame):

    def __init__(self, parent):
        
        Frame.__init__(self,parent)
        
        self.server_address = (common.HOST, common.PORT)
        self.trader = 'tr' + str(random.randint(1,51))
        
        self.sock_quote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_quote.connect(self.server_address)
        
        self.var_time = StringVar()
        self.var_price_ask = StringVar()
        self.var_price_bid = StringVar()

        self.label = ttk.Label(self, textvariable=self.var_time)
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        ttk.Label(self, text = "").grid(row = 1, column = 0)
        ttk.Label(self, text = "").grid(row = 1, column = 1)
        
        self.label_price_2 = ttk.Label(self, text = "Bid - Mkt Sell  ").grid(row = 2, column = 0)
        self.label_price_1 = ttk.Label(self, text = "  Ask - Mkt Buy").grid(row = 2, column = 1)
                
        ttk.Label(self, text = "").grid(row = 3, column = 0)
        ttk.Label(self, text = "").grid(row = 3, column = 1)
        
        ttk.Label(self, textvariable=self.var_price_bid).grid(row = 4, column = 0)
        ttk.Label(self, textvariable=self.var_price_ask).grid(row = 4, column = 1)
                
        ttk.Label(self, text = "").grid(row = 5, column = 0)
        ttk.Label(self, text = "").grid(row = 5, column = 1)
        
        ttk.Button(self, text = "Market Sell", command = self.send_market_order_sell).grid(row = 6, column = 0)
        ttk.Button(self, text = "Market Buy", command = self.send_market_order_buy).grid(row = 6, column = 1)
                        
        ttk.Label(self, text = "").grid(row = 7, column = 0)
        ttk.Label(self, text = "").grid(row = 7, column = 1)
                   
        ttk.Button(self, text = "Limit  Buy", command = self.send_limit_order_buy).grid(row = 8, column = 0)
        ttk.Button(self, text = "Limit  Sell", command = self.send_limit_order_sell).grid(row = 8, column = 1)
        
        self.after(1000,self._update)
        
        self.thread = Thread(target=self.worker)
        self.thread.daemon = True
        self.thread.start()
        
    def _update(self):
        self.var_time.set(time.asctime())  
        self.after(1000, self._update)

    def send_limit_order_buy(self):
        order_type = 'lb'
        order_price = random.uniform(1.09, 1.17)
        order_volume = random.randint(1,17)
        order_price = round(order_price, 2)
        trader = 'tr' + str(random.randint(1,51))
        
        order = [order_type, order_price, order_volume, trader]
        data = ujson.dumps(order)
        data = data.encode('utf-8')
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.server_address)
            self.sock.sendall(data)
            
            data3 = self.sock.recv(4096)
            data4 = ujson.loads(data3)
            data4 = str(data4)
            print(data4)
            
        finally:
            print('closing connection')
            self.sock.close()
        
    
    def send_limit_order_sell(self):
        order_type = 'ls'
        order_price = random.uniform(1.2, 1.3)
        order_price = round(order_price, 2)
        order_volume = random.randint(1,19)
        trader = 'tr' + str(random.randint(1,55))
                
        order = [order_type, order_price, order_volume, self.trader]
        data = ujson.dumps(order)
        data = data.encode('utf-8')
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.server_address)
            self.sock.sendall(data)
            
            data3 = self.sock.recv(4096)
            data4 = ujson.loads(data3)
            #data4 = str(data4)
            print(data4)
            
        finally:
            print('closing connection')
            self.sock.close()
            
                        
    def send_market_order_buy(self):

        order_type = 'mb'
        order_price = 0
        order_volume = random.randint(1,17)
        
        order = [order_type, order_price, order_volume, self.trader]
        data = ujson.dumps(order)
        data = data.encode('utf-8')
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.server_address)
            self.sock.sendall(data)
            
            data3 = self.sock.recv(4096)
            data4 = ujson.loads(data3)
            data4 = str(data4)
            print(data3)
            
        finally:
            print('closing connection')
            self.sock.close()
        
    
    def send_market_order_sell(self):

        order_type = 'ms'
        order_price = 0
        order_volume = random.randint(1,15)
        
        order = [order_type, order_price, order_volume, self.trader]
        data = ujson.dumps(order)
        data = data.encode('utf-8')
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.server_address)
            self.sock.sendall(data)
            
            data3 = self.sock.recv(4096)
            data4 = ujson.loads(data3)
            data4 = str(data4)
            print(data4)
            
        finally:
            print('closing connection')
            self.sock.close()
            
    def send_quote_request(self):
        
        data1 = 'iq', None, None, None
        data2 = ujson.dumps(data1)
        data2 = data2.encode('utf-8')

        try:
            self.sock_quote.sendall(data2)
            
            data_quote = self.sock_quote.recv(8192)
            data_quote = data_quote.decode(encoding="utf-8")
            data_quote = data_quote[1:-1]
            data_quote = data_quote.split(',')
        
            p_ask = data_quote[0]
            p_bid = data_quote[1]
            
            self.var_price_ask.set(p_ask)  
            self.var_price_bid.set(p_bid)
  
        finally:
            pass
     
    def worker(self):
    
        while True:
            msg = self.send_quote_request()
     
            
def main():            
    
    root = Tk()
    app = GuiOrders(root).pack(fill = "both", expand = True)
    root.mainloop()
    
    
if __name__ == "__main__": main()
