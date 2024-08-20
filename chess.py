board= [9]*8 #creates an array of eight 9s

for i in range(len(board)):
    board[i]= ['  ']*8 #updates the array so each 9 is replaced by an array of eight '  's


def prt_brd(board):#we can do it in lists and then use ennumerate to print it out
     print()
     for i,j in enumerate(board):
         print(8-i,end=": ")
         for k in range(len(j)):
             print(j[k], end=" ") 
         print()
     print('   A  B  C  D  E  F  G  H')
     print()
    

#placing the pieces

Bpcs={
    'Bp':[(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)],
    'Br':[(0,0),(0,7)],
    'Bn':[(0,1),(0,6)],
    'Bb':[(0,2),(0,5)],
    'Bk':[(0,4)],
    'Bq':[(0,3)]    
}

Wpcs={
    'Wp':[(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7)],
    'Wr':[(7,0),(7,7)],
    'Wn':[(7,1),(7,6)],
    'Wb':[(7,2),(7,5)],
    'Wk':[(7,4)],
    'Wq':[(7,3)]    
}

def put_pcs(board):
    for i,j in Bpcs.items():
        for m in j:
            board[m[0]][m[1]]=i
    for k,l in Wpcs.items():
        for n in l:
            board[n[0]][n[1]]=k
            
put_pcs(board)
prt_brd(board)            

#move counter
mc=0

def movecount(board):
    global mc
    mc +=1
    if mc % 2 ==1:
        print('White to move!')
    else:
        print('Black to move!')

#moving
L_N={
  'a':'0',
  'b':'1',
  'c':'2',
  'd':'3',
  'e':'4',
  'f':'5',
  'g':'6',
  'h':'7'
}


WK=[7,4]
BK=[0,4]
enp=[]

def prm(board,y,z):
    validinpt=False
    while validinpt==False:
     promotin=input("Choose promotion (Q/R/B/N): ")
     if len(promotin)==1 and promotin.lower() in ['q','r','b','n']:
         board[y][z]= board[y][z][:1] +promotin
         validinpt=True


def pawnmove(board,w,x,y,z):
    if board[w][x][0]=='W':
        if x==z:
            if y==w-1:
             if board[y][z]=='  ':
                 return True
            elif w==6 and y==4:
                 if board[4][x]!='  ' or board[5][x]!='  ':
                     print('Path is blocked')
                     return False
                 else:
                     if enp:
                         enp.pop()
                     enp.append(x)
                     enp.append(0)
                     return True
            else:
                return False
        elif abs(x-z)==1:
            if y==w-1:
                if board[y][z][0]=='B':
                    return True
                elif w==3 and z==enp[0]:
                     board[3][z]='  '
                     enp.pop()
                     return True
                else:
                    return False
            else:
                return False
        else:
            return False    

    else:
        if x==z:
            if y==w+1:
             if board[y][z]=='  ':
                 return True
            elif w==1 and y==3:
                 if board[2][x]!='  ' or board[3][x]!='  ':
                     print('Path is blocked')
                     return False
                 else:
                     if enp:
                         enp.pop()
                     enp.append(x)
                     enp.append(0)
                     return True
            else:
                return False
        elif abs(x-z)==1:
            if y==w+1:
                if board[y][z][0]=='W':
                    return True
                elif w==4 and z==enp[0]:
                     board[4][z]='  '
                     enp.pop()
                     return True
                else:
                    return False
            else:
                return False
        else:
            return False    
                     

def bishopmove(board, w, x, y, z):
    bishopblocked = False
    for check in range(1, abs(y - w)):
        if y - w > 0:
            if z - x > 0:
                if board[w + check][x + check] != '  ':
                    print('Path is blocked')
                    return False
            else:
                if board[w + check][x - check] != '  ':
                    print('Path is blocked')
                    return False
        else:
            if z - x > 0:
                if board[w - check][x + check] != '  ':
                    print('Path is blocked')
                    return False
            else:
                if board[w - check][x - check] != '  ':
                    print('Path is blocked')
                    return False

    if bishopblocked == False:
        return True
    else:
        return False


def rookmove(board, w, x, y, z):
    rookblocked = False
    if (y - w) > 0:
        for check in range(1, y - w):
            if board[w + check][x] != '  ':
                rookblocked = True
                print('Path is blocked')
    elif (y - w) < 0:
        for check in range(1, abs(y - w)):
            if board[w - check][x] != '  ':
                rookblocked = True
                print('Path is blocked')
    elif (z - x) > 0:
        for check in range(1, z - x):
            if board[w][x + check] != '  ':
                rookblocked = True
                print('Path is blocked')
    elif (z - x) < 0:
        for check in range(1, abs(z - x)):
            if board[w][x - check] != '  ':
                rookblocked = True
                print('Path is blocked')
    if rookblocked == False:
        return True
    else:
        return False


        

def simplekingmove(board,w,x,y,z):
    if abs(w-y)<=1 and abs(x-z)<=1:
        return 0
    elif y==w and abs(x-z)==2:
        if w==7:
            if z==2:
                if castling[0]:
                    if board[7][1]=="  " and board[7][3]=="  ":
                        return 2
                return 1 
            elif z==6:
                if castling[1]:
                    if board[7][5]=="  ":
                        return 3
                return 1
        elif w==0:
            if z==2:
                if castling[2]:
                    if board[0][1]=="  " and board[0][3]=="  ":
                        return 4
                return 1
            elif z==6:
                if castling[3]:
                    if board[0][5]=="  ":
                        return 5
                return 1
    else:
        return 1 
        #king moves without threats

        

def move(board):
    global enp
    enp=[]
    global castling
    castling=[True,True,True,True]
    global WK
    global BK
    global mc
    
    
    while(True):
        movecount(board)
        #switches turns
        
        o=1
        
        validinput=False
        while validinput==False:
            s=input('move peice from:')
            if len(s)==2 and s[0].lower() in L_N and int(s[1]) in range(1,9):
                validinput=True
                #asks for input until valid input is received
            
        w,x=(8-int(s[1])),int(L_N[s[0].lower()])
        #chess notation to array notation
            
        if mc%2==1:
         while board[w][x][0]!= 'W':
             print(f'No white piece present on {s}')
             s=input('move peice from:')
             w,x=(8-int(s[1])),int(L_N[s[0].lower()])
        else:
            while board[w][x][0]!= 'B':
             print(f'No black piece present on {s}')
             s=input('move peice from:')
             w,x=(8-int(s[1])),int(L_N[s[0].lower()])
             #checks if correct piece is chosen
             
        flag=1
        
        
        while flag==1:
         promotion=False       
         e=input('move piece to:')
         y,z=(8-int(e[1])),int(L_N[e[0].lower()])
         if board[w][x][0]==board[y][z][0]:
             print('Self capture not permitted')
         else:
             if board[w][x][1]=='n':
                 if abs(y-w)+abs(z-x)!=3 or abs(y-w)*abs(z-x)!=2:
                     print('Invalid Knight move')
                 else:
                     flag=0
             elif board[w][x][1]=='b':
                 if abs(y-w)!=abs(z-x):
                     print('Invalid Bishop move')
                 else:
                     if bishopmove(board,w,x,y,z):
                         flag=0
             elif board[w][x][1]=='r':
                 if (y-w)*(z-x)!=0:
                     print('Invalid Rook move')
                 else:
                     if rookmove(board,w,x,y,z):
                         flag=0
                         if w==0:
                             if x==0:
                                 castling[2]=False
                                 #black queen side
                             elif x==7:
                                 castling[3]=False
                                 #black king side
                         elif w==7:
                             if x==0:
                                 castling[0]=False
                                 #white queen side
                             elif x==7:
                                 castling[1]=False
                                 #white king side
             elif board[w][x][1]=='q':
                 if abs(y-w)!=abs(z-x) and (y-w)*(z-x)!=0:
                     print('Invalid Queen move')
                 elif abs(y-w)!=abs(z-x):
                     if rookmove(board,w,x,y,z):
                         flag=0
                 else:
                     if bishopmove(board,w,x,y,z):
                         flag=0
             elif board[w][x][1]=='p':
                 if pawnmove(board,w,x,y,z):
                     if y==0 or y==7:
                         flag=0
                         promotion=True
                     else:
                         flag=0
                 else:
                     print('Invalid Pawn move')
             elif board[w][x][1]=='k':
                 o=simplekingmove(board,w,x,y,z)
                 if o!=1:
                    flag=0
                    if o==0:
                        if mc%2==1:
                            castling[0],castling[1]=False,False
                        else:
                            castling[2],castling[3]=False,False     
                    elif o<4:
                        castling[0],castling[1]=False,False
                    else:
                        castling[2],castling[3]=False,False
                 else:
                     print('Invalid king move')                                             
             else:
                 flag=0
        #once we have broken out of this while loop, the move is executed
            
            
            
        if o>1:
         if o==2:
             board[7][3]="Wr"
             board[7][0]="  "
         elif o==3:
             board[7][5]="Wr"
             board[7][7]="  "
         elif o==4:
             board[0][3]="Br"
             board[0][0]="  "
         else:        
             board[0][5]="Br"
             board[0][7]="  "
        
        #checks if castling has been done and makes the necessary changes            
                        

        board[y][z]=board[w][x]
        board[w][x]="  "

 
        if WK==[w,x]:
            WK=[y,z]
        
        if BK==[w,x]:
            BK=[y,z]
        
        if promotion:
            prm(board,y,z)
        #promotes pawn on last rank
        
        if enp!=[]:
            enp.pop()
        #keeps enpassant active for only one turn
        
        if board[BK[0]][BK[1]]=='Bk' and board[WK[0]][WK[1]]=='Wk':
            prt_brd(board)
        elif board[BK[0]][BK[1]]!='Bk':
            prt_brd(board)
            print('Black has lost')
            return
        else:
            prt_brd(board)
            print('White has lost')
            return


move(board)
