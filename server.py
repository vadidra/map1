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
            message_type = data2[0]
            order_price = data2[1]
            order_volume = data2[2]
            trader = data2[3]
            '''
            print(message_type)
            print(order_price)
            print(order_volume)
            print(trader)
            '''     
                 
                 
            if(message_type=='iq'):
                #print('info quote request')
                quote1 = order_book.get_quote()
                data3 = ujson.dumps(quote1)

                
            if(message_type=='ip'):
                list1 = order_book.get_pool()
                data3 = ujson.dumps(list1)
                
            
            if(message_type=='id'):
                #print('info dom request')
                dom1 = order_book.get_dom()
                data3 = ujson.dumps(dom1)


            if(message_type=='ls'):
                #print('limit sell order')
                order_id = order_book.add_order('ls', order_price, order_volume, trader)
                data3 = ujson.dumps(order_id)

                
            if(message_type=='lb'):
                #print('limit buy order')
                order_id = order_book.add_order('lb', order_price, order_volume, trader)
                data3 = ujson.dumps(order_id)

            
            if(message_type=='mb'):
                print('market buy order')
                order_id = order_book.process_market_buy('mb', 0, order_volume, trader)
                data3 = ujson.dumps(order_id)
                
            if(message_type=='ms'):
                print('market sell order')
                order_id = order_book.process_market_sell('ms', 0, order_volume, trader)
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
