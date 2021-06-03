from tkinter import *
root=Tk()
def send():
    send="You = "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Bot = hi")
    elif (e.get() == "hi"):
        txt.insert(END, "\n" + "Bot = hey")
    elif (e.get() == "hey"):
        txt.insert(END, "\n" + "Bot = hello")
    elif (e.get() == "youre age"):
        txt.insert(END, "\n" + "Bot = iam a computer program dude\n serious you are asking me this?")
    elif (e.get() == "name youre team members"):
        txt.insert(END, "\n" + "Bot =shanmuka he is the leader\nnivas the one who execute's the code and visvulize the data\nHarsha the one who make users to see the output")
    elif (e.get() == "you know about current situation?"):
        txt.insert(END, "\n" + "Bot = yes corona in all over the world and now in india too :(")
    elif (e.get() == "do you have updates on current situations"):
        txt.insert(END, "\n" + "Bot = yeh nearly nearly 5lakh+ covid cases were confirmed in india by yesterdays report ")
    elif (e.get() == "on which project youre team worked and currently working"):
        txt.insert(END, "\n" + "Bot = on the current situation of covid they worked on sensitive analzier which help government to take decisions and they used twitter as enitiy")
    elif (e.get() == "show me some neutral words"):
        txt.insert(END, "\n" + "Bot = ok!! there are 34334 words.top neutral words are:  technical,draw,cp delhi...")
    elif (e.get() == "what about youre health"):
        txt.insert(END, "\n" + "Bot = I'm a computer program,so I'm always healthy with my program and\ndon't worry i won't get effected by corona...hahaha!! :) ")
    elif (e.get() == "what about some positive words"):
        txt.insert(END, "\n" + "Bot = ok!! there are 88 positive words.top positive words are: great,love,best..")
    elif (e.get() == "what about some negitive words"):
        txt.insert(END, "\n" + "Bot = yeh sure!! there are 48 negitive words.top negitive words are:dead,killer,shithead..")
    elif (e.get() == "how are you"):
        txt.insert(END, "\n" + "Bot = hmm are you sure u are asking me this question?\nleave about me and what about you")
    elif (e.get() == "bye"):
        txt.insert(END, "\n" + "Bot = BBye take care:) ","It was nice talking to you.Stay home stay safe")
    elif (e.get() == "iam good"):
        txt.insert(END, "\n" + "Bot = ok good ! what you want from me")
    elif (e.get() == "who created you"):
        txt.insert(END, "\n" + "Bot = harsha made me")
    elif (e.get() == "what about the full report"):
        txt.insert(END, "\n" + "Bot = u can find the total word document in the dashboard of smartbridge\nzoho writer..")
    else:
        txt.insert(END,"\n"+"Bot = sorry i didn't get u")
    e.delete(0,END)
txt=Text(root,bg="azure2")
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100,bg="seashell3")
send=Button(root,text="Enter",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("IBM BOT")
main_menu=Menu(root)
main_menu.add_command(label="file")
root.mainloop()