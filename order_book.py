import time
from fill import Fill
from order import Order

class OrderBook(object):



    def __init__(self):
        self.pool = []
        self.price_ask = 0
        self.price_bid = 0

        
    def add_order(self, order_type, order_price, order_volume, trader):
        new_order = Order(order_type, order_price, order_volume, trader )
        self.pool.append(new_order)
        if(new_order is not None): order_id = new_order.id
        else: order_id = -1
        return order_id

    def process_market_buy(self, order_type, order_price, order_volume, trader):
        mb_order = Order('mb', 0, order_volume, trader )
                
        done = False
        fill=1
        
        while( done is not True):
            
            o1 = self.get_ls_order_with_min_price()
            #print('ls price : ' + str(o1.price))
            #print('ls volume : ' + str(o1.volume))
            #print('mb volume : ' + str(order_volume))
      
            
            if(mb_order.volume <= o1.volume):
                # Full fill
                o1.volume -= mb_order.volume 
                done = True
            else:
                fill+=1
                fill_vol = o1.volume
                mb_order.volume -= fill_vol
                o1.volume = 0
                o1.status = 'filled'
                self.pool.remove(o1)
                continue
                
            print('--- mb order completed')
            
        self.get_ask_bid()  
        return mb_order.id 
    
    def process_market_sell(self, order_type, order_price, order_volume, trader):
        ms_order = Order('ms', 0, order_volume, trader )
                
        done = False
        fill=1
        
        while( done is not True):
            
            o1 = self.get_lb_order_with_max_price()
            #print('ls price : ' + str(o1.price))
            #print('ls volume : ' + str(o1.volume))
            #print('mb volume : ' + str(order_volume))
      
            
            if(ms_order.volume <= o1.volume):
                # Full fill
                o1.volume -= ms_order.volume 
                done = True
            else:
                fill+=1
                fill_vol = o1.volume
                ms_order.volume -= fill_vol
                o1.volume = 0
                o1.status = 'filled'
                self.pool.remove(o1)
                continue
                
            print('--- ms order completed')
            
        self.get_ask_bid()    
        return ms_order.id 

        
    def get_lb_order_with_max_price(self):
        
        b1 = -1
        lb_order = None
        
        for o1 in self.pool:
            
            if(o1.type =='lb'):
                
                if(o1.price > b1):
                    b1 = o1.price
                    lb_order = o1
        
        return lb_order
    
    def get_ls_order_with_min_price(self):
        
        a1 = 100000000.00
        ls_order = None
        for o1 in self.pool:
            if(o1.type =='ls'):
                if(o1.price < a1):
                    a1 = o1.price
                    ls_order = o1
        
        return ls_order
    
    def get_ask_bid(self):
        
        o_b = self.get_lb_order_with_max_price()
        self.price_bid = o_b.price
        
        o_a = self.get_ls_order_with_min_price()
        self.price_ask = o_a.price
    
    def get_ask_bid_(self):
        
        b1 = -1
        for o1 in self.pool:
            
            if(o1.type =='lb'):
                
                if(o1.price > b1):
                    b1 = o1.price
        
        self.price_bid = b1

        a1 = 1000000
        for o1 in self.pool:
            
            if(o1.type =='ls'):
                
                if(o1.price < a1):
                    a1 = o1.price
        
        self.price_ask = a1
        

        
    def get_quote(self):
        return (self.price_ask, self.price_bid)
    
    def init_populate(self):
        
        self.pool.append(Order('lb', 1.11, 12, 'tr5' ))
        self.pool.append(Order('lb', 1.10,  8, 'tr2' ))
        self.pool.append(Order('lb', 1.13,  6, 'tr6' ))
        self.pool.append(Order('lb', 1.11,  1, 'tr21'))
        self.pool.append(Order('lb', 1.11, 12, 'tr5' ))
        self.pool.append(Order('lb', 1.12, 14, 'tr31'))
        self.pool.append(Order('lb', 1.17, 22, 'tr`5'))
        self.pool.append(Order('lb', 1.14, 16, 'tr25'))
        
        self.pool.append(Order('ls', 1.25,  5, 'tr1' ))
        self.pool.append(Order('ls', 1.25,  8, 'tr2' ))
        self.pool.append(Order('ls', 1.27,  6, 'tr6' ))
        self.pool.append(Order('ls', 1.23,  1, 'tr21'))
        self.pool.append(Order('ls', 1.24, 12, 'tr5' ))
        self.pool.append(Order('ls', 1.19, 13, 'tr31'))
        self.pool.append(Order('ls', 1.21,  2, 'tr`5'))
        self.pool.append(Order('ls', 1.20, 10, 'tr25'))
   
    
        self.get_ask_bid()
    
   
    def get_pool(self):
        return self.pool
    
    def get_dom(self):
    
        dom = []
        d1 = {}
        
        for o1 in self.pool:

            if(o1.price in d1):
                v1 = d1[o1.price]
                v1[2] += o1.volume
            else:
                l1 = []
                l1.append(o1.type)
                l1.append(o1.price)
                l1.append(o1.volume)
                d1[o1.price] = l1
                
        for i,v in d1.items():
            dom.append(v) 
                
        
        dom = sorted(dom, key = self.get_key, reverse = True)
        
        return dom
    
    def get_key(self,item):
        return item[1]    
        
        
