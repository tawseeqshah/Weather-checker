from tkinter import *
from tkinter.font import BOLD, Font
from requests_html import HTMLSession
screen=Tk()

screen.geometry("600x400")
screen.title("Tawseeq's Weather Info")
screen.config(bg="#b7eb34")
screen.resizable(False,False)

def input():
    pass
   
    


def getinfo():
    ulr=urltext.get()
    s = HTMLSession()
    query = ulr
    url = f'https://www.google.com/search?q=weather+{query}'

    r = s.get(url, headers={"User-Agent"  : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 "})

    temp=(r.html.find('span#wob_tm',first=True).text)
    unit=(r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
    des=(r.html.find('div.VQF4g',first=True).find('span#wob_dc',first=True).text)
    labe=Label(screen,text=(f'The temperature in {query} is {temp}{unit} and it is {des} there.'),fg='blue',font=("Ariel",15,"italic"))
    labe.place(x=5,y=340)




#Labels.......................................................
intro_label=Label(screen,text="Tawseeq's Weather Checker",width=30,font=("Chiller",35,"bold"),relief="ridge",bd=4,fg='red')
intro_label.place(x=30,y=50)

intro_label=Label(screen,text="Enter Place name (like Srinagar,Jammu)",width=40,font=("Ariel",10,"italic bold"),bd=4,fg='Black')
intro_label.place(x=120,y=140)


#Entry.............................................................
urltext=StringVar()
urlentry=Entry(screen,textvariable=urltext,font=("Ariel",25,'italic bold'),width=15)
urlentry.place(x=150,y=180)

#Buttons.............................................................

ClickButton = Button(screen,text="Check Weather",font=('Ariel',10,'italic bold'),bg='green',fg='red',activebackground='blue',width=23,bd=8,command=getinfo)
ClickButton.place(x=180,y=250)

#Printing...........................................................

# printing=Label(screen,text=f'The temperature in {query} is {temp}{unit} and it is {des} there.'))










screen.mainloop()