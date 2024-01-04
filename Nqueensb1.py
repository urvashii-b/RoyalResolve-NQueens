from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import nqueens as nq
root=Tk()
root.title("Nqueens")
root.geometry("800x600")
img=ImageTk.PhotoImage(Image.open('queen.jpg'))
img2=ImageTk.PhotoImage(Image.open('queenwhite.jpg'))
img3=ImageTk.PhotoImage(Image.open('queenred.jpg'))
def changeOnHover(button, number, chover, cleave,n):
    global L
    a,b=tuple(map(int,number.split()))
    number=[]
    for k in range(1,n+1):#1,2,3,4
        number.append((k,b))
        number.append((a,k))
    number=list(set(number))
    i=0
    while a-i>0 and b-i>0:
        number.append((a-i,b-i))
        i+=1
    i=0
    while a+i<n+1 and b+i<n+1:
        number.append((a+i,b+i))
        i+=1
    i=0
    while a-i>0 and b+i<n+1:
        number.append((a-i,b+i))
        i+=1
    i=0
    while a+i<n+1 and b-i>0:
        number.append((a+i,b-i))
        i+=1
    def change(z):
        for x in number:
            i,j,button=x[0],x[1],d[str(x[0])+str(x[1])]
            if L[i-1][j-1]==1 and not((i==a) and (j==b)):
                button.config(height=50,width=52,image=img3,bg='red')
            elif L[i-1][j-1]==0 and (i==a) and (j==b):
                if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
                    button.config(height=50,width=52,image=img,bg="white")
                else:
                    button.config(height=50,width=52,image=img2,bg='black')
            else:
                button.configure(bg=chover)
    def change2(z):
        for x in number:
            i,j,button=x[0],x[1],d[str(x[0])+str(x[1])]
            if L[i-1][j-1]==1 and not((i==a) and (j==b)):
                if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
                    button.config(height=50,width=52,image=img,bg="white")
                else:
                    button.config(height=50,width=52,image=img2,bg='black')
            elif L[i-1][j-1]==0 and (i==a) and (j==b):
                if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
                    button.config(height=3,width=7,image="",bg="white")
                else:
                    button.config(height=3,width=7,image="",bg='black')
            else:
                if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
                    button.config(height=3,width=7,bg='white')
                else:
                    button.config(height=3,width=7,bg='black')
    button.bind("<Enter>", func=change)
    button.bind("<Leave>", func=change2)
def changeOnClick(button, number, color):
    global L
    def change(a=0):
        i,j=tuple(map(int,number.split()))
        if L[i-1][j-1]==1:
            if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
                button.config(text=number,height=3,width=7,fg='black',bg='white',image='')
            else:
                button.config(text=number,height=3,width=7,fg='white',bg='black',image='')
            L[i-1][j-1]=0
        else:
            if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
                button.config(height=50,width=52,image=img)
            else:
                button.config(height=50,width=52,image=img2)
            L[i-1][j-1]=1
    button.bind("<ButtonPress>",func=change)
def createGame():
    global frame1,e1,n,frame2,L,frame3
    try:
        global frame2
        frame2.destory()
    except:
        pass
    n=e1.get()
    frame1.destroy()
    frame1=Frame(root)
    frame1.pack()
    try:
        def check():
            global frame1,frame2,frame3
            frame2.destroy()
            frame1.destroy()
            frame3=Frame(root)
            frame3.pack()
            if L==board:
                text='''Congratulations you have won!!\n≧◠ᴥ◠≦'''
                Label(frame3,text=text,font = ("Helvetica",24)).grid(rowspan=4,columnspan=3)
                Button(frame3, text="Main Menu",command=start,font = ("Helvetica",18)).grid(row=6,column=0)
                Button(frame3, text="Exit",command=root.destroy,font = ("Helvetica",18)).grid(row=6,column=1)
            else:
                text='''Sorry you have lost\n( ˘︹˘ )'''
                Label(frame3,text=text,font = ("Helvetica",24)).grid(rowspan=4,columnspan=3)
                Button(frame3, text="Main Menu",command=start,font = ("Helvetica",18)).grid(row=6,column=0)
                Button(frame3, text="Exit",command=root.destroy,font = ("Helvetica",18)).grid(row=6,column=1)     
        def see_sol():
            res=messagebox.askquestion('See solution', 'Your progress will be lost.\nAre you sure you wish to continue?')
            if res == 'yes' :
                showSolution()
            else :
                messagebox.showinfo('Return', 'Returning to the game!')
        def back():
            res=messagebox.askquestion('Go back to main menu', 'Your progress will be lost.\nAre you sure you wish to go back?')
            if res == 'yes' :
                start()
            else :
                messagebox.showinfo('Return', 'Returning to the game!')
        def sub():
            res=messagebox.askquestion('Submit', 'Are you sure you wish to submit?')
            if res == 'yes' :
                check()
            else :
                messagebox.showinfo('Return', 'Returning to the game!')
        global L,board,d
        N=int(n)
        L=[[0 for j in range(N)] for i in range(N)]                
        board=nq.solveNQ(N)
        if N>9:
            Label(frame1,text="Sorry you cannot play for this dimension",font = ("Helvetica",11)).pack()
            Button(frame1,text="Re-enter value",font = ("Helvetica",11),command=start).pack()
        elif board==False:
            Label(frame1,text="Solution does not exist for this board",font = ("Helvetica",11)).pack()
            Button(frame1,text="Re-enter value",font = ("Helvetica",11),command=start).pack()
        else:
            d={}
            for i in range(1,N+1):
                for j in range(1,N+1):
                    if (i%2==0 and j%2==0) or (j%2==1 and i%2==1):
                        d[str(i)+str(j)]=Button(frame1,height=3,width=7,bg='black',fg='white')
                        d[str(i)+str(j)].grid(row=i,column=j)
                        changeOnHover(d[str(i)+str(j)],str(i)+" "+str(j),"#00b9fb", "black",N)
                        changeOnClick(d[str(i)+str(j)],str(i)+" "+str(j),"black")
                    else:
                        d[str(i)+str(j)]=Button(frame1,height=3,width=7,bg='white',fg='black')
                        d[str(i)+str(j)].grid(row=i,column=j)
                        changeOnHover(d[str(i)+str(j)],str(i)+" "+str(j),"#00b9fb", "white",N)
                        changeOnClick(d[str(i)+str(j)],str(i)+" "+str(j),"white")
            frame2=Frame(root)
            frame2.pack()
            Label(frame1,text="Game:",font = ("Helvetica",11)).grid(row=0,columnspan=j)
            Button(frame2,text="Click to go back",command=back,font = ("Helvetica",11)).grid(row=1,column=0)
            Button(frame2,text="Click to Submit",command=sub,font = ("Helvetica",11)).grid(row=1,column=1)
            Button(frame2,text="Click to see solution",command=see_sol,font = ("Helvetica",11)).grid(row=2,columnspan=2)
    except:
        Label(frame1,text="Wrong input given",font = ("Helvetica",11)).pack()
        Button(frame1,text="Re-enter value",font = ("Helvetica",11),command=start).pack()
def entry_page():
    global frame
    frame=Frame(root)
    frame.pack()
    Label(frame,text='''Hello!!
Welcome to NQuees!
Clicking on the start button will take you to the main page.
You have two options
1. See the solution of a certain board
2. Try to find the solution on your own!
We hope you enjoy!''',font = ("Helvetica",11),justify= CENTER).pack()
    Button(frame,text="Start",font = ("Helvetica",11),command=start).pack()
    Button(frame,text="Quit",font = ("Helvetica",11),command=root.destroy).pack()
def start():
    global frame1,e1,frame
    try:
        frame.destroy()
        frame1.destroy()
        global frame2,frame3
        frame2.destroy()
        frame3.destroy()
    except:
        pass
    frame1=Frame(root)
    frame1.pack()
    Label(frame1,text="Hello to Nqueens",font = ("Helvetica",11)).grid(row=0,columnspan=2)
    Label(frame1,text="Enter board size:",font = ("Helvetica",11)).grid(row=1,column=0)
    e1=Entry(frame1)
    e1.grid(row=1,column=1)
    Button(frame1,text="Click to play",command=createGame,font = ("Helvetica",11)).grid(row=2,columnspan=2)
    Button(frame1,text="Click to see solution",command=showSolution,font = ("Helvetica",11)).grid(row=3,columnspan=2)
def showSolution():
    global frame1
    try:
        global n,frame2
        frame2.destroy()
    except:
        n=e1.get()
    frame1.destroy()
    frame1=Frame(root)
    frame1.pack()
    try:
        N=int(n)
        board=nq.solveNQ(N)
        if N>10:
            Label(frame1,text="Sorry you cannot see solution for this dimension",font = ("Helvetica",11)).pack()
            Button(frame1,text="Re-enter value",font = ("Helvetica",11),command=start).pack()
        elif board==False:
            Label(frame1,text="Solution does not exist",font = ("Helvetica",11)).pack()
            Button(frame1,text="Re-enter value:",font = ("Helvetica",11),command=start).pack()
        else:
            for i in range(1,N+1):
                for j in range(N):
                    if board[i-1][j]==1:
                        if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
                            Label(frame1,height=50,width=52,image=img2,bg='black').grid(row=i,column=j)
                        else:
                            Label(frame1,height=50,width=52,image=img).grid(row=i,column=j)
                    else:
                        if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
                            Label(frame1,height=3,width=7,bg='black').grid(row=i,column=j)
                        else:
                            Label(frame1,height=3,width=7,bg='white').grid(row=i,column=j)
            Label(frame1,text="Solution",font = ("Helvetica",11)).grid(row=0,columnspan=j+1)
            Button(frame1,text="Click to go back to main menu",font = ("Helvetica",11),command=start).grid(row=i+1,columnspan=j+1)
            Button(frame1,text="Click to exit",font = ("Helvetica",11),command=root.destroy).grid(row=i+2,columnspan=j+1)
    except:
        Label(frame1,text="Wrong input given",font = ("Helvetica",11)).pack()
        Button(frame1,text="Re-enter value:",font = ("Helvetica",11),command=start).pack()
entry_page()
root.mainloop()
###########################################################################################################################
'''Things to improve:
1. Make it pretty looking...?
2. Show hints.
3. Works for all possible solutions.'''
###########################################################################################################################
