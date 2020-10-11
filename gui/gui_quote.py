import pygame, sys, time
from pygame.color import Color
from threading import Thread
import socket
import ujson
import common

l00 = '*'
l01 = '*'

server_address = common.HOST, common.PORT
data1 = 'iq', None, None, None
data2 = ujson.dumps(data1)
data2 = data2.encode('utf-8')
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Connect the socket to the port where the server is listening
#print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

def send_info_request():
 
    try:
        sock.sendall(data2)
        
        data3 = sock.recv(8192)
        data3 = data3.decode(encoding="utf-8")
  
    finally:
        pass
    return data3


def process_msg(msg):

    msg = msg[1:-1]
    msg = msg.split(',')
    
    p_ask = msg[0]
    p_bid = msg[1]
    
    str0 = 'Ask:    ' + p_ask 
    str1 = 'Bid:     ' + p_bid 

    global l00
    l00 = str0

    global l01
    l01 = str1
        

def worker():
    
    while True:

        msg = send_info_request()
        if(msg is not None): process_msg(msg)
        


t = Thread(target=worker)
t.daemon = True
t.start()

pygame.init()
screen = pygame.display.set_mode([300,150])
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("consolas", 22, True)


pygame.display.set_caption("GUI Quote")



done = False
while not done:
    screen.fill(Color('black'))
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True



    text00 = font1.render(l00, True, Color('white'))
    text01 = font1.render(l01, True, Color('white'))

    
    screen.blit(text00, [40,30])
    screen.blit(text01, [40,60])


    clock.tick(60)
    pygame.display.flip()
    
print('closing socket')
sock.close()  
    
    









