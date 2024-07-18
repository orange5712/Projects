board= [9]*8 
#creates an array of eight 9s

for i in range(len(board)):
    board[i]= ['  ']*8 
#updates the array so each 9 is replaced by an array of eight double spaces
    
def prt_brd(board):
     for i,j in enumerate(board):
         print(8-i,end=": ")
         for k in range(len(j)):
             print(j[k], end=" ") 
         print()
     print('   A  B  C  D  E  F  G  H')
#prints board with array 0 as row '8: ' down to array 7 as row '1: ' with columns from 0 to 7 being listed from A to H


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
#dictionaries noting down the initial placement of all the white and black pieces

def put_pcs(board):
    for i,j in Bpcs.items():
        for m in j:
            board[m[0]][m[1]]=i
    for k,l in Wpcs.items():
        for n in l:
            board[n[0]][n[1]]=k
#puts the pieces on the board in their starting positions
            
put_pcs(board)
prt_brd(board)            


mv_c=0
def movecount(board):
    global mv_c
    mv_c +=1
    if mv_c % 2 ==1:
        print('White to move!')
    else:
        print('Black to move!')
#switches turns between white and black

L_N={
  'A':'0',
  'B':'1',
  'C':'2',
  'D':'3',
  'E':'4',
  'F':'5',
  'G':'6',
  'H':'7'
}
#dictionary that maps chess column notation to array column notation

WK=[7,4]
BK=[0,4]
#original places of the both the Kings

def move(board):
    while(True):
        movecount(board)
        s=input('move peice from:')
        e=input('move piece to:')
        
        w,x=(8-int(s[1])),int(L_N[s[0]])
        y,z=(8-int(e[1])),int(L_N[e[0]])
        
        global WK
        global BK
        
        if WK==[w,x]:
            WK=[y,z]
        
        if BK==[w,x]:
            BK=[y,z]
            
        board[y][z]=board[w][x]
        board[w][x]="  "
        
        if board[BK[0]][BK[1]]=='Bk' and board[WK[0]][WK[1]]=='Wk':
            prt_brd(board)
        elif board[BK[0]][BK[1]]!='Bk':
            print('black has lost')
            return
        else:
            print('white has lost')
            return

#implements a version of chess where each king has to be captured for the other side to win


move(board)
        
