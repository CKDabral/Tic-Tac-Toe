
#tic tac toe
def prnt(b):
    print(b['top l']+'|'+b['top m']+'|'+b['top r'])
    print('-+-+-')
    print(b['mid l']+'|'+b['mid m']+'|'+b['mid r'])
    print('-+-+-')
    print(b['low l']+'|'+b['low m']+'|'+b['low r'])

def work(b):
    count=0
    s=''
    while(1):
        print('enter the position you want to enter x')
        loc=input('press for any location')
        if loc in s:
            prnt(b)
            continue
        else:
            s+=loc
        if count%2==0:
            b[loc]='x'
            f=check(b,loc,'x')
        else:
            b[loc]='0'
            f=check(b,loc,'0')
        prnt(b)
        if count>=8 or f==1:
            break
        count+=1

def check(b,loc,p):
    f=0
    ch=loc[4]
    pre=loc[:4]
    if b['top {}'.format(ch)]==p and b['low {}'.format(ch)]==p and b['mid {}'.format(ch)]==p:
        f=1
    elif b['{}l'.format(pre)]==p and b['{}m'.format(pre)]==p and b['{}r'.format(pre)]==p:
        f=1
    elif b['top l']==p and b['mid m']==p and b['low r']==p:
        f=1
    elif b['top r']==p and b['mid m']==p and b['low l']==p:
        f=1
    if f==1:
        print('{} player Won'.format(p))
    return f
            
board={'top l':' ','top m':' ','top r':' ',
       'mid l':' ','mid m':' ','mid r':' ',
       'low l':' ','low m':' ','low r':' '}
prnt(board)
work(board)
