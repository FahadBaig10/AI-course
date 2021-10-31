
# coding: utf-8

# In[30]:


import numpy as np

def checkwinner(currentboard, s, symbol):

    #for horizontal checking
    counter=0                               #counter for my agent
    counter1=0                                #counter for other agent
    for i in range(0,s):
        counter=0
        counter1=0
        for j in range(0,s):
            if currentboard[i][j] == symbol:
                counter+=1
                counter1+=1
        if(counter==s):
            return 1
        elif(counter==-1):
            return -1
    #for vertical checking
    counter=0
    counter1=0
    for j in range(0,s):
        counter=0
        counter1=0
        for i in range(0,s):
            if currentboard[i][j]==symbol:
                counter+=1
                counter1+=1
        if(counter==s):
            return 1
        elif(counter1==s):
            return -1
    #for diagonal checking
    counter=0
    counter1=0
    for i in range(0,s):
        if(curretboard[i][i]==symbol):
            counter+=1
            counter1+=1
    if counter==s:
        return 1
    elif counter1==s:
        return -1
    #for second diagnal checking
    counter=0
    for i in range(s-1,0,-1):
        if(currentboard[i][i]==symbol):
            counter+=1
            counter1+=1
    if counter==s:
        return 1
    elif counter1==s:
        return -1
    
    #for checking tie 
    
    # for i in range(0,s):
    #    for j in range(0,s):
            
    #       return False
        
    #game is continue right now   
    return 0
#function of agent that is providing 
def Agent(Currentboard, n, symbol):   
    ismaximizing = True
    sizee=n
    if symbol=='X':                             #checking symbol
        my_agent='X'
        other_agent='O'
        for i in range(0,Currentboard):
            if Currentboard !='X'or Currentboard!='O':
                minimax(Currentboard, ismaximizing,sizee,my_agent,other_agent)
    elif symbol=='O':                          #checking symbol
        my_agent='O'                     
        other_agent='X'
        for i in range(0,Currentboard):
            if Currentboard !='X'or Currentboard!='O':
                minimax(Currentboard, ismaximizing,sizee,my_agent,other_agent)
        
            
    
    
#minimax function that is used to find the best possible move
def minimax(board, ismaximizing, sizee, my_agent,other_agent):
    
            
    result=0        
    result= checkwinner(board, sizee,symbol,my_agent,other_agent)
    if result !=False :
        return result
    n=sizee
    if(ismaximizing):             #this is for maximizing function
        bestestscore=-infinity
        for i in range(0,n):
            for j in range(0,n):
                if board[i][j]=='':
                    board[i][j]= my_agent
                    score= minimax(board,False, sizee+1,my_agent,other_agent)
                    board[i][j]=''
                    bestestscore= max(score,bestestscore)
        return bestestscore
    
    else:                         #this is for minimizing function 
        bestestscore = infinity
        for i in range(0,n):
            for j in range(0,n):
                if board[i][j]=='':
                    board[i][j]= other_agent
                    score= minimax(board,True, sizee+1,my_agent,other_agent)
                    board[i][j]=''
                    bestestscore= min(score,bestestscore)
        return bestestscore
 

