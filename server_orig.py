import asyncore
import socket
import common
import ujson
import time
from order_book import OrderBook


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        if data:
            
            data2 = ujson.loads(data)
            #print(data2)
            #print(data2[0])
            message_id = data2[0]
            order_type = data2[1]
            order_price = data2[2]
            order_volume = data2[3]
            trader = data2[4]
            '''
            print(message_id)     
            print(order_type)
            print(order_price)
            print(order_volume)
            print(trader)
            '''     
                 
                 
            if(data2[0]==1):
                #print('info quote request')
                quote1 = order_book.get_quote()
                data3 = ujson.dumps(quote1)

                
            if(data2[0]==2):
                #print('info dom2 request')
                #list1 = order_book.get_dom()
                list1 = order_book.get_pool()
                #print(list1)
                data3 = ujson.dumps(list1)
                #print(data3)
            
            if(data2[0]==11):
                print('limit sell order')
                ls_order = [order_type, order_price, order_volume, trader]
                order_id = order_book.add_order(ls_order)
                data3 = ujson.dumps(order_id)
                
            if(data2[0]==12):
                print('market sell order')
                ms_order = [order_type, order_price, order_volume, trader]
                order_id = order_book.add_order_ms(ms_order)
                data3 = ujson.dumps(order_id)
                
            if(data2[0]==13):
                print('limit buy order')
                order_id = order_book.add_order(self, order_type, order_price, order_volume, trader)
                data3 = ujson.dumps(order_id)
                
            if(data2[0]==14):
                print('market buy order')
                order_id = int(time.time())
                mb_order = [order_type, order_price, order_volume, trader]
                order_id = order_book.match_order_mb(mb_order)
                #order_id = order_book.add_order_mb(mb_order)
                data3 = ujson.dumps(order_id)
                            
            data3 = data3.encode('utf-8')
            self.send(data3)

class EchoServer(asyncore.dispatcher):

    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((common.HOST, common.PORT))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print('Incoming connection from %s' % repr(addr))
            handler = EchoHandler(sock)

order_book = OrderBook()
order_book.init_populate()

server = EchoServer()
asyncore.loop()
