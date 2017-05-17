import struct
import sys

sys.setrecursionlimit(0x2000)

d_pkt = b''
c_index, d_index1, d_index2 = 0,0,0
#dl = c_pkt[c_index]


def _2b0615():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    
    return d_pkt
    
def _2b064b():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    
    return d_pkt

def _2b0647():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    
    return d_pkt
def _2b065d():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    
    return d_pkt
    
def _2b0627():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx

    return d_pkt
def delete():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    del c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx




def _2B0291():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    c_index, d_index1, d_index2 = 0,0,0
    try: c_pkt
    except NameError: return b''
    #print('_2B0291')
    dl = c_pkt[c_index]
    if not dl > 0x11:
        return _2b02e0()
    esi = dl
    esi -= 0x11
    #c_index+=1
    if esi < 4:
        return _2b0406()
    edx = 0x2000 - len(d_pkt)
    if edx < esi:
        return _eb064b()
    edx = len(c_pkt) - c_index
    edi = esi +1
    if edx < edi:
        return _2b0615()
    return _2b02d0()

def _2b02d0():
    #print('_2b02d0')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    while esi > 0:
        dl = c_pkt[c_index]
        d_pkt+=bytes([dl])
        d_index1+=1
        c_index+=1
        esi-=1
    #print('_2b02d0', d_pkt[-100:], '001');input('sair 001?')
    return _2b039b()

def _2b02e0():
    #print('_2b02e0')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    #print(c_index, d_index1, dl,);exit()
    if c_index >= len(c_pkt):
        return _2b0627()
    esi = c_pkt[c_index]
    #print(esi, 'paulo', c_pkt[c_index:c_index+5]);input('sair?')
    c_index +=1
    #print(esi);exit()
    if esi >= 0x10:
        return _2b044b()
    if not esi == 0:
        #print('indo p/ _2b0331()')
        return _2b0331()
    if len(c_pkt)-c_index < 1:
        return _2b0615()
    if not c_pkt[c_index] == 0:
        return _2b0329()
    return _2b0310()

def _2b0310():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    c_index+=1
    edx = len(c_pkt)-c_index
    esi+=0xff
    if edx < 1:
        return _2b0615()
    return _2b0329()
    


def _2b0329():
    #print('_2b0329')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    edx = c_pkt[c_index]
    #print(edx);input('sair')
    esi = esi+edx +0xf
    #print(edx, esi, hex(edx), hex(esi))
    c_index +=1
    return _2b0331()




def _2b0331():
    #print('_2b0331')
    global c_pkt, edi, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    edx = 0x2000 - d_index1
    
    #
    edi = esi + 3
    if edx < edi:
        return _2b064b()
        
    edx = len(c_pkt) - c_index
    edi = esi +4
    #print(edx, 'paulo');input('sair')
    if edx < edi:
        return _2b0615()
    edx = c_pkt[c_index:c_index+4]
    #print(edx);exit()
    d_pkt+=edx
    d_index1+=4
    c_index+=4
    esi -=1
    #print(d_pkt, esi, edi,edx, 'paulo');input('sair')
    #_2b0331 print(d_pkt);input('sair')
    if esi == 0:
        return _2b039b()
    if esi < 4:
        return _2b0390()
    while esi >= 4:
        edx = c_pkt[c_index:c_index+4]
        d_pkt+=edx
        esi-=4
        c_index+=4
        d_index1+=4
    if not esi > 0:
        return _2b039b()
    ################## 2b0380
    while esi > 0:
        dl = c_pkt[c_index]
        d_pkt+=bytes([dl])
        c_index+=1
        d_index1+=1
        esi -=1
    ############  2B039B
    return _2b039b()

def _2b039b():
    #print('_2b039b')
    global c_pkt,xxx, edi, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    esi = c_pkt[c_index]
    #print(d_pkt, hex(esi), edi, );input('sair?')
    c_index+=1
    #print('last:',c_index,edi,esi,d_index1, edx)
    if esi >= 0x10:
        #print('ops')
        return _2b044b()
    edx = c_pkt[c_index]
    edx += edx
    edx += edx
    edi = d_index1 - edx
    esi = esi >> 2
    edi -= esi
    edi -= 0x801
    c_index+=1
    if edi < 0:
        
        return _2b065d()
    if edi >= d_index1:
        return _2b065d()
    edx = 0x2000 - len(d_pkt)
    if edx < 3:
        return _2b064b()
    edx = d_pkt[edi]
    d_pkt+=bytes([edx])
    edx = d_pkt[edi+1]
    edi+=1
    d_index1 +=1
    d_pkt+=bytes([edx])
    edx = d_pkt[edi+1]
    d_index1+=1
    d_pkt+=bytes([edx])
    d_index1+=1
    #print(d_pkt[-100:], '002');input('sair 002?')
    return _2b03f5()


def _2b0390():
    #print('_2b0390')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    while esi > 0:
        dl = c_pkt[c_index]
        d_pkt+=bytes([dl])
        c_index+=1
        d_index1+=1
        esi-=1
    #print(d_pkt[-100:], '003');input('sair 003?')
    return _2b039b()


def _2b044b():
    #print('_2b044b')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    #print('vai p/ 2b044b')
    if esi < 0x40:
        return _2b04b0()
    edx = esi
    edx = edx >> 2
    edx = edx & 7
    edi = d_index1
    edi-= edx 
    edx = c_pkt[c_index]
    edx +=edx
    edx +=edx
    edx +=edx
    edi = edi - edx
    esi = esi >> 5
    edi -=1
    c_index+=1
    esi-=1

    
    if edi < 0:
        return _2b065d()
    if edi>=d_index1:
        return _2b065d()
        
    edx = 0x2000 - len(d_pkt)
    #print(hex(edx));input('--')
    ebx = esi+2
    if edx < ebx:
        return _2b0647()
        
    edx = d_pkt[edi]
    d_pkt+=bytes([edx])
    #print(d_pkt);exit()
    edx  = d_pkt[edi+1]
    edi+=1
    d_index1+=1
    d_pkt+=bytes([edx])
    #print(d_pkt);exit()
    edi+=1
    d_index1+=1
    while esi > 0:
        dl = d_pkt[edi]
        d_pkt+=bytes([dl])
        edi+=1
        d_index1+=1
        esi-=1
    
    #print(d_pkt[-100:], '004');input('sair 004?')
    return _2b03f5()



def _2b03f5():
    #print('_2b03f5')
    
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    ebx = 0
    
    esi = c_pkt[c_index-2]
    #print(esi);exit()
    esi = esi & 3
    if esi == 0:
        return _2b02e0()
    return _2b0406()

     
def _2b04b0():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx

    if esi < 0x20:
        return _2b0504()
    esi = esi & 0x1f
    if not esi == 0:
        return _2b04f1()
    edx = (len(c_pkt))-c_index
    if edx < 1:
        return _2b0615()
    if not c_pkt[c_index] == 0:
        return _2b04e9()
    while c_pkt[c_index] == 0:
        c_index +=1
        edx = len(c_pkt) - c_index
        esi+=0xff
        if edx < 1:
            return _2b0615()
    return _2b04e9()
        

def _2b04f1():
    #print('_2b04f1')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    #print('_2b04f1()')
    dx = c_pkt[c_index:c_index+2] # TESTADO
    dx, = struct.unpack('H',dx)
    edx = dx
    edx = edx >> 2
    #_ = d_pkt[d_index1-1:d_index1+3]
    #edi, = struct.unpack('I',_+b'\x00'*(4-len(_)))
    edi = d_index1 - 1
    edi-=edx
    c_index += 2
    return _2b056d()
    


    

    
def _2b0504():
    #print('_2b0504')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    edi = d_index1
    if esi < 0x10:
        return _2b05e0()
    edx = esi
    edx = edx & 8
    edx >> 0xb
    edi -= edx
    esi =esi & 7
    if not esi == 0:
        return _2b0551()
    #

def _2b0551():
    #print('_2b0551')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    c_index-=1
    dx = c_pkt[c_index:c_index+2]#TESTADO
    #if isinstance(dx, int):
    #    dx = bytes([dx])+b'\x00'
    dx, =  struct.unpack('H',dx)
    edx = dx
    
    edx = edx >> 2
    
    edi -= edx
    c_index +=2
    if edi == d_index1:
        return _2b0627()
    edi -=0x4000
    return _2b056d()
    
    
    
    



def _2b04e9():
    #print('_2b04e9')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    #print('vai p/ 2b04e9')
    edx = c_pkt[c_index]
    esi = esi+edx+0x1f
    c_index+=1
    return _2b04f1()
##    dx = c_pkt[c_index:c_index+2] ####TESTADO 000000000000011
##    dx, = struct.unpack('H',dx)
##    edx = dx
##    edx = edx >> 2
##    edi, = struct.unpack('I',c_pkt[c_index-1:c_index+3])
##    #edi = d_index1 - edx -1
##    edi -= edx
##    c_index+=2
    ####
    ###### JMP 2b056d
    #####
##    return _2b056d()

def _2b056d():
    
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    #print('_2b056d()')
    if edi < 0:
        return _2b065d()
    if edi >= d_index1:
        return _2b065d()
    edx =0x2000-d_index1
    ebx = esi+2
    if edx < ebx:
        return _2b0647()
    if esi < 6:
        return _2b048e()
    edx = d_index1 - edi
    if edx < 4:
        return _2b048e()
    edx = d_pkt[edi:edi+4]
    d_pkt+=edx
    d_index1 += 4
    edi +=4
    esi -=2
    while esi >= 4:
        edx = d_pkt[edi:edi+4]
        d_pkt+=edx
        esi-=4
        d_index1+=4
        edi+=4
    if esi <= 0:
        #print(d_pkt[-100:], '002');input('sair 005?')
        return _2b03f5()
    
    while esi > 0:
        dl = d_pkt[edi]
        d_pkt+=bytes([dl])
        d_index1+=1
        edi+=1
        esi-=1
    #print(d_pkt[-100:], '002');input('sair 005?')
    return _2b03f5()
    
    
    


    
def _2b048e():
    #print('_2b048e')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    
    edx = d_pkt[edi]
    d_pkt+=bytes([edx])
    edx = d_pkt[edi+1]
    edi+=1
    d_index1+=1
    d_pkt+=bytes([edx])
    d_index1+=1
    edi+=1
    while esi > 0:
        dl = d_pkt[edi]
        d_pkt+=bytes([dl])
        d_index1+=1
        edi+=1
        esi-=1
    #print(d_pkt[-100:], '006');input('sair 006?')
    return _2b03f5()



def _2b0406():
    #print('_2b0406')
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    edx = 0x2000 - d_index1
    if edx < esi:
        return _2b0627()
    edx = len(c_pkt)-c_index#############
    edi = esi+1
    if edx < edi:
        return _2b0627()
    dl = c_pkt[c_index]
    d_pkt+=bytes([dl])
    d_index1+=1
    c_index+=1
    if not esi > 1:
        return _2b043f()
    
    dl = c_pkt[c_index]
    d_pkt+=bytes([dl])
    d_index1+=1
    c_index+=1
    if not esi > 2:
        return _2b043f()
    
    dl = c_pkt[c_index]
    d_pkt+=bytes([dl])
    d_index1+=1
    c_index+=1
    return _2b043f()

def _2b043f():
    global c_pkt, c_index, d_pkt, d_index1,d_index2, dl,esi,edi,edx,ebx,dx
    #print('_2b043f')
    esi = c_pkt[c_index]
    c_index +=1
    if c_index >= len(d_pkt):
        return _2b0627()
    return _2b044b()

def decrypt(packet):
    global c_pkt, d_pkt
    if not packet.startswith(b'\x00\x01'):
        return packet
    packet = packet[2:]
    c_pkt = packet
    d_pkt = b''
    return b'\x00\x00'+_2B0291()
