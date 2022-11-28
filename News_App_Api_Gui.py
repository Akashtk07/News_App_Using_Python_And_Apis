import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image


class NewsApp:
    def __init__(self):

        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=ENTER YOUR API KEY FOR API KEY VISIT NEWSAPI.ORG WEBSITE AND MAKE YOUR ACCOUNT').json()

        self.Load_Gui()



        self.load_news_items(0)

    def Load_Gui(self):
        self.root=Tk()
        self.root.title('NEWSAPP')
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.configure(background='white')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def load_news_items(self,index):
        #clear the screen for the next item or news
        self.clear()
        #image
        try:

            img_url=self.data['articles'][index]['urlToImage']
            raw_data=urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo=ImageTk.PhotoImage(im)
            label=Label(self.root,image=photo)
            label.pack()
        except:
            img_url ='https://www.ioshacker.com/wp-content/uploads/2020/12/iPhone-cannot-load-photo-fix.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
            label = Label(self.root, image=photo)
            label.pack()


        heading=Label(self.root,text=self.data['articles'][index]['title'],bg='#aa00ff',fg='pink',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details=Label(self.root,text=self.data['articles'][index]['description'],bg='#aa00ff',fg='pink',wraplength=350,justify='center')
        details.pack(pady=(2,20))
        details.config(font=('verdana',12))

        frame=Frame(self.root,bg='white')
        frame.pack(expand=True,fill=BOTH)

        if index !=0:
            prev=Button(frame,text='Prev',width='16',height='3',command=lambda :self.open_link(index-1))
            prev.pack(side=LEFT)

        Read=Button(frame,text='Read Mode',width='16',height='3',command= lambda :self.open_link(self.data['articles'][index]['url']))
        Read.pack(side=LEFT)

        if index!=len(self.data['articles'])-1:
            Next=Button(frame,text='Next',width='16',height='3',command=lambda:self.load_news_items(index+1))
            Next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)

obj=NewsApp()
