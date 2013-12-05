import random

def show_line(dist):
    print(" -------------",file=dist)
def show_head(dist):
    print("   a   b   c",file=dist)
    show_line(dist)

def show_board(board_list,dist=None):
    show_head(dist)
    for i in range(3):
        print("%d| %s | %s | %s |" % \
              (i+1,board_list[i][0],board_list[i][1],board_list[i][2]),file=dist)
        show_line(dist)
   
 
def init_board():
    board_list=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    return board_list

    
def check_win(board_list):
    a=board_list
    for i in range(3):
        if a[i][0]==a[i][1] and a[i][1]==a[i][2]:
            if a[i][0] != ' ':
                return a[i][0]
        if a[0][i]==a[1][i] and a[1][i]==a[2][i]:
            if a[0][i] != ' ':
                return a[0][i]        
    if a[0][0]==a[1][1] and a[1][1]==a[2][2]:
        if a[0][0] != ' ':
            return a[0][0]
    if a[0][2]==a[1][1] and a[1][1]==a[2][0]:
        if a[0][2] != ' ':
            return a[0][2]
    return False

def check_move(new_move):
    if len(new_move)!=2:
        return False
    s="abc"
    n="123"
    new_move=new_move.lower()
    if (new_move[0] not in s) or (new_move[1] not in n):
        return False

def put_chess(board_list,m,side='O'):
    row=int(m[1])-1
    col=ord(m[0].lower())-ord('a')
    if board_list[row][col]!=' ':    #mean the place is not empty
        return False
    else:
        board_list[row][col]=side
        return True
        

def get_move(board_list):
    flag=True
    while(flag):     
        m=input("Enter your move:")
        if check_move(m)==False:
            print("Invalid coordinates.")
        else:
            if put_chess(board_list,m):
                flag=False
            else:
                print("This position is already taken. ")
            
def put_com_move(board_list):
    while True: 
        row=random.choice("abc")
        col=random.choice("123")
        if put_chess(board_list,row+col,'X'):
            print("My move is: %s" % row+col)
            break

def show_res(res,dist=None):
    if res==False:
        print("Game over! No winner.",file=dist)
    elif res=='O':
        print("Game over! You win.",file=dist)
    elif res=='X':
        print("Game over! I win.",file=dist)    


def writeFinal(board_list,filename,res):
    try:
        f=open(filename,"w")
    except:
        print("file %s open error!" % filename)
        return
    show_board(board_list,f)
    show_res(res,f)
    f.close()
    
if __name__=='__main__':
    board_list=init_board()
    get_move(board_list)
    show_board(board_list)
    turn=0
    while True:
        put_com_move(board_list)
        show_board(board_list)
        if check_win(board_list) != False:
            break
        get_move(board_list)
        show_board(board_list)
        if check_win(board_list) != False:
            break        
        turn+=1
        if turn == 4:
            break
    res=check_win(board_list)
    show_res(res)
    writeFinal(board_list,"final.txt",res)   
    