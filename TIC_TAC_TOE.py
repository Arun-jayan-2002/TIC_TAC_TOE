import random

print('\n \t \b---- TIC TAC TOE ---\n')
print('\t\bWelcome to the game !!!\n')
print('\t\b1.Start \n\t\b2.Exit')

a=[" "for i in range(9)]
b=[]
c=[j for j in range(9)]
d={'user':'x','cmp':'O'}
e=[]
e1=[]
op=[1,2]
l=['X','x','O','o']
l1=['X','x']
l2=['O','o']

def gm():
    print("\n")
    print("\t     |     |")
    print(f'\t {a[0]}   |  {a[1]}  | {a[2]}')
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f'\t {a[3]}   |  {a[4]}  | {a[5]}')
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f'\t {a[6]}   |  {a[7]}  | {a[8]}')

def win(a1):
    a1=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in a1:
        if all(y in e for y in i):
            return True
        elif all(y in e1 for y in i):
            return True


def play():
    try:
        option=int(input('\n\t\bChoose your option (1 or 2):-'))
        while option not in op:
            print('\n\t\bPlease enter correct option !!!')
            option=int(input('\n\t\bChoose your option (1 or 2):-'))
            
        if option==1:
            
            option1=input("\n\t\bChoose (X or O) :-")
            while option1 not in l:
                print("\n\t\bplease choose a valid option")
                option1=input("\n\t\bChoose (X or O) :-")

            if option1 in l1:
                d={'user':'X','cmp':'O'}
                
            elif option1 in l2:
                d={'user':'O','cmp':'X'}  
            gm()   
            while True:
                option2=int(input("\n\t\bEnter the index number (0-8) :-  "))
                if option2 <=8:
                    if option2 not in b:
                        b.append(option2)
                        e.append(option2)
                        a[option2]=d['user']
                        c.remove(option2)
                        userresult=win(e)
                           
                        if len(b)!=9:
                            j=random.choice(c)
                            a[j]=d['cmp']
                            b.append(j)
                            e1.append(j)
                            c.remove(j)
                            cmpresult=win(e1)
                            
                            gm()
                    
                    else:
                        b.sort()
                        print(f'\n\t\bAlready filled please select other  index position  {b}')
                        
                    if userresult:
                        print('\n\t\bUser win')
                        
                        break  
                    elif cmpresult:
                        print('\n\t\bComputer win')
                        
                        break     
                    elif len(b) == 9:
                        print("\n\t\bIt's a draw!")
                        
                        break
                else:
                    print('\n\t\bInvalid syntax!!!')

        elif option==2:
            exit()       
                
    except ValueError:
        print('\bplease enter digits ')
play()
