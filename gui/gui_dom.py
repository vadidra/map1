import pygame, sys, time
from pygame.color import Color
from threading import Thread
import socket
import ujson
import common

l00 = '*'
l01 = '*'
l02 = '*'
l03 = '*'
l04 = '*'
l05 = '*'
l06 = '*'
l07 = '*'
l08 = '*'
l09 = '*'
l10 = '*'
l11 = '*'
l12 = '*'
l13 = '*'
l14 = '*'
l15 = '*'
l16 = '*'
l17 = '*'
l18 = '*'
l19 = '*'

#lr = []

server_address = common.HOST, common.PORT
data1 = 'id', None, None, None
data2 = ujson.dumps(data1)
data2 = data2.encode('utf-8')
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Connect the socket to the port where the server is listening
sock.connect(server_address)

def send_info_request():
 
    try:
        sock.sendall(data2)
        
        data3 = sock.recv(8192)
        data3 = data3.decode(encoding="utf-8")
        data4 = data3[2:-2]
        data6 = data4.split('],[')
        ld = []
        
        for d6 in data6:
            d1 = {}
            d7 = d6.split(',')
            #print(d7)
            
            d1['type'] = d7[0][1:-1]
            d1['price'] = float(d7[1])
            d1['volume'] = int(d7[2])
            
            ld.append(d1)
           
    finally:
        pass
    return ld

def get_key2(item):
        return item[3]

def process_msg(msg):

    lr = []

    for m1 in msg:
           
        l2 = []
        if(m1['type']=='lb'):
            l2.append('lb')
            l2.append(m1['volume'])
            l2.append(m1['price'])
            l2.append('')
        else:
         
            if(m1['type']=='ls'):
                l2.append('ls')
                l2.append('    ')
                l2.append(m1['price'])
                l2.append(m1['volume'])
            
        lr.append(l2)
        #lr = sorted(lr, key = get_key2, reverse = True)
        
        for i, lri in enumerate(lr):
            str1 = str(lri[0]) + '       ' + str(lri[1]).rjust(2) + '        ' + "{:.2f}".format(lri[2]) + '       '  + str(lri[3]).rjust(2)
            
            if(i==0):
                global l00
                l00 = str1
                continue
            
            if(i==1):
                global l01
                l01 = str1
                continue

            if(i==2):
                global l02
                l02 = str1
                continue
            
            if(i==3):
                global l03
                l03 = str1
                continue
                    
            if(i==4):
                global l04
                l04 = str1
                continue
                
            if(i==5):
                global l05
                l05 = str1
                continue
                        
            if(i==6):
                global l06
                l06 = str1
                continue
            
            if(i==7):
                global l07
                l07 = str1
                continue
                
            if(i==8):
                global l08
                l08 = str1
                continue
                
            if(i==9):
                global l09
                l09 = str1
                continue
                
            if(i==10):
                global l10
                l10 = str1
                continue
                
            if(i==11):
                global l11
                l11 = str1
                continue
            
            if(i==12):
                global l12
                l12 = str1
                continue
            
            if(i==13):
                global l13
                l13 = str1
                continue
            
            if(i==14):
                global l14
                l14 = str1
                continue
            
            if(i==15):
                global l15
                l15 = str1
                continue
            
            if(i==16):
                global l16
                l16 = str1
                continue
            
            if(i==17):
                global l17
                l17 = str1
                continue
            
            if(i==18):
                global l18
                l18 = str1
                continue
            
            if(i==19):
                global l19
                l19 = str1
                continue
        

        
        

def worker():
    
    while True:

        msg = send_info_request()
        if(msg is not None): process_msg(msg)
        


t = Thread(target=worker)
t.daemon = True
t.start()

pygame.init()
screen = pygame.display.set_mode([500,650])
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("consolas", 22, True)


pygame.display.set_caption("GUI DOM Test")



done = False
while not done:
    screen.fill(Color('black'))
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True



    text00 = font1.render(l00, True, Color('white'))
    text01 = font1.render(l01, True, Color('white'))
    text02 = font1.render(l02, True, Color('white'))
    text03 = font1.render(l03, True, Color('white'))
    text04 = font1.render(l04, True, Color('white'))
    text05 = font1.render(l05, True, Color('white'))
    text06 = font1.render(l06, True, Color('white'))
    text07 = font1.render(l07, True, Color('white'))
    text08 = font1.render(l08, True, Color('white'))
    text09 = font1.render(l09, True, Color('white'))
    text10 = font1.render(l10, True, Color('white'))
    text11 = font1.render(l11, True, Color('white'))
    text12 = font1.render(l12, True, Color('white'))
    text13 = font1.render(l13, True, Color('white'))
    text14 = font1.render(l14, True, Color('white'))
    text15 = font1.render(l15, True, Color('white'))
    text16 = font1.render(l16, True, Color('white'))
    text17 = font1.render(l17, True, Color('white'))
    text18 = font1.render(l18, True, Color('white'))
    text19 = font1.render(l19, True, Color('white'))
    
    screen.blit(text00, [40,30])
    screen.blit(text01, [40,60])
    screen.blit(text02, [40,90])
    screen.blit(text03, [40,120])
    screen.blit(text04, [40,150])
    screen.blit(text05, [40,180])
    screen.blit(text06, [40,210])
    screen.blit(text07, [40,240])
    screen.blit(text08, [40,270])
    screen.blit(text09, [40,300])
    screen.blit(text10, [40,330])
    screen.blit(text11, [40,360])
    screen.blit(text12, [40,390])
    screen.blit(text13, [40,420])
    screen.blit(text14, [40,450])
    screen.blit(text15, [40,480])
    screen.blit(text16, [40,510])
    screen.blit(text17, [40,540])
    screen.blit(text18, [40,570])
    screen.blit(text19, [40,600])

    clock.tick(60)
    pygame.display.flip()
    
print('closing socket')
sock.close()  
    
    









