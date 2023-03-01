from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window

root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="dark blue")

# picture
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor-user.png"))

#insert picture
user_label = Label(root,image=scissor_img,bg="dark blue")
comp_label = Label(root,image=scissor_img_comp,bg="dark blue")
comp_label.grid(row=2, column=1)
user_label.grid(row=2, column=5)

#scores
playerScore = Label(root,text=0,font=("Arial",50),bg="dark blue",fg="white")
computerScore = Label(root,text=0,font=("Arial",50),bg="dark blue",fg="white")
computerScore.grid(row=2, column=2)
playerScore.grid(row=2, column=4)

#indicators
user_indicator = Label(root,font=("Arial",20,"bold"),text="  USER  ",bg="dark blue",fg="white")
comp_indicator = Label(root,font=("Arial",20,"bold"),text="COMPUTER",bg="dark blue",fg="white")
vs = Label(root,text="VS",font=("Arial",50,"bold"),bg="dark blue",fg="white")
user_indicator.grid(row=1,column=4)
vs.grid(row=2,column=3)
comp_indicator.grid(row=1,column=2)


#messages
msg= Label(root, font=("Arial",25),bg="dark blue",fg="white")
msg.grid(row=4, column=3)

#update massage
def updateMassage(x):
    msg['text']=x

#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score +=1
    playerScore["text"]=str(score)

#update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score +=1
    computerScore["text"]=str(score)

#check winner
def checkWin(player,computer):
    if player == computer:
        updateMassage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMassage("You lose!")
            updateCompScore()
        else:
            updateMassage("You Win!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMassage("You lose!")
            updateCompScore()
        else:
            updateMassage("You Win!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMassage("You lose!")
            updateCompScore()
        else:
            updateMassage("You Win!")
            updateUserScore()
    else:
        pass
            
   

#update choices
choices = ["rock","paper","scissor"]
def updateChoice(x):
#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)
        

#buttons
rock    = Button(root,width=10,height=2,font=("Arial",20,"bold"),text="  ROCK  ",bg="red",fg="blue",command = lambda:updateChoice("rock"))
paper   = Button(root,width=10,height=2,font=("Arial",20,"bold"),text=" PAPER ",bg="red",fg="red",command = lambda:updateChoice("paper"))
scissor = Button(root,width=10,height=2,font=("Arial",20,"bold"),text="SCISSOR ",bg="red",fg="green",command = lambda:updateChoice("scissor"))
rock.grid(row=3, column=2)
paper.grid(row=3, column=3)
scissor.grid(row=3, column=4)

#border

#top
box1 = Button (width=6,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black")
box2 = Button (width=100,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black")
box3 = Button (width=50,height=6,font=("Arial",5,"bold"),text="        ",bg="dark blue",fg="black")
box4 = Button (width=50,height=6,font=("Arial",5,"bold"),text="        ",bg="dark blue",fg="black")
box5 = Button (width=50,height=6,font=("Arial",5,"bold"),text="        ",bg="dark blue",fg="black")
box6 = Button (width=100,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black")
box7 = Button (width=6,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black")
box1.grid(row=0, column=0)
box2.grid(row=0, column=1)
box3.grid(row=0, column=2)
box4.grid(row=0, column=3)
box5.grid(row=0, column=4)
box6.grid(row=0, column=5)
box7.grid(row=0, column=6)

#bot
bot1= Button (width=6,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=5, column=0)
bot2= Button (width=100,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=5, column=1)
bot3= Button (width=50,height=6,font=("Arial",5,"bold"),text="        ",bg="dark blue",fg="black").grid(row=5, column=2)
bot4= Button (width=50,height=6,font=("Arial",5,"bold"),text="        ",bg="dark blue",fg="black").grid(row=5, column=3)
bot5= Button (width=50,height=6,font=("Arial",5,"bold"),text="        ",bg="dark blue",fg="black").grid(row=5, column=4)
bot6= Button (width=100,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=5, column=5)
bot7= Button (width=6,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=5, column=6)

#left
left1 = Button (width=6,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=1, column=6)
left2 = Button (width=6,height=50,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=2, column=6)
left3 = Button (width=6,height=15,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=3, column=6)
left4 = Button (width=6,height=15,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=4, column=6)
left5 = Button (width=6,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=5, column=6)

#right
right1 = Button (width=6,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=1, column=0)
right2 = Button (width=6,height=50,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=2, column=0)
right3 = Button (width=6,height=15,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=3, column=0)
right4 = Button (width=6,height=15,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=4, column=0)
right5 = Button (width=6,height=6,font=("Arial",5,"bold"),text=" ",bg="dark blue",fg="black").grid(row=5, column=0)

root.mainloop()
