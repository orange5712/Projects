#board
#peices
#turns
#move pieces 

board= [9]*8 #creates an array of eight 9s

for i in range(len(board)):
    board[i]= ['  ']*8 #updates the array so each 9 is replaced by an array of eight _s


# for row in board:#for every element array in board
#     for col in row:#for every element in each element array of board 
#         print(col,end = ' ')#print the _ followed by a space
#     print("")#after you finish one column (one array) print a line space
    
def prt_brd(board):#we can do it in lists and then use ennumerate to print it out
     for i,j in enumerate(board):
         print(8-i,end=": ")
         for k in range(len(j)):
             print(j[k], end=" ") 
         print()
     print('   A  B  C  D  E  F  G  H')
    

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
  'A':'0',
  'B':'1',
  'C':'2',
  'D':'3',
  'E':'4',
  'F':'5',
  'G':'6',
  'H':'7'
}

def move(board):
    while(True):
        movecount(board)
        s=input('move peice from:')
        e=input('move piece to:')
        w,x=(8-int(s[1])),int(L_N[s[0]])
        y,z=(8-int(e[1])),int(L_N[e[0]])
        board[y][z]=board[w][x]
        board[w][x]="  "
        prt_brd(board)
        
move(board)
        