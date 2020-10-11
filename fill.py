import time 
class Fill(object):


    def __init__(self, price, volume, order_id_b, order_id_s):
                
        self.id = int(time.time())
        self.price = price
        self.volume = volume
        self.order_id_b = order_id_b
        self.order_id_s = order_id_s


