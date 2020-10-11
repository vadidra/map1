import time

class Order(object):


    def __init__(self, type, price, volume, trader):
                
        self.type = type
        self.price = price
        self.volume = volume
        self.trader = trader
        self.id = int(time.time())
        self.status ='new'

    def to_string(self):
        return self._type + ' ' + str(self._price) + ' ' + str(self._volume) + ' ' + self._trader  + ' ' + str(self._id)