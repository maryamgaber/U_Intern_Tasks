from tkinter import *
from tkinter import messagebox
class init:
    def __init__(self,parent):
        self.win = parent
        self.win.title("calculaor")
        self.calculator_value = StringVar()
        self.expression = ''
        self.cal_frame = Frame(self.win,highlightthickness=5,bg='#BCED91')
        self.cal_frame.pack(padx=15,pady=15)
        self.screen = Entry(self.cal_frame,text='Start Calculating',fg='white',width=19,font=('Arial',20,'bold'),bg="#458B00",textvariable = self.calculator_value)
        self.screen.grid(row=0,column=0,columnspan=4,pady=10,ipady=5)

        Button(self.cal_frame,text='7',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('7')).grid(row=1,column=0)
        Button(self.cal_frame,text='8',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('8')).grid(row=1,column=1)
        Button(self.cal_frame,text='9',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('9')).grid(row=1,column=2)
        Button(self.cal_frame,text='C',bg="#458B00",font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('c')).grid(row=1,column=3)
            
        Button(self.cal_frame,text='4',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('4')).grid(row=2,column=0)
        Button(self.cal_frame,text='5',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('5')).grid(row=2,column=1)
        Button(self.cal_frame,text='6',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('6')).grid(row=2,column=2)
        Button(self.cal_frame,text='+',bg="#FFC300 ",font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('+')).grid(row=2,column=3)

        Button(self.cal_frame,text='1',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('1')).grid(row=3,column=0)
        Button(self.cal_frame,text='2',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('2')).grid(row=3,column=1)
        Button(self.cal_frame,text='3',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('3')).grid(row=3,column=2)
        Button(self.cal_frame,text='-',bg="#FFC300 ",font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('-')).grid(row=3,column=3)

        Button(self.cal_frame,text='0',font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('0')).grid(row=4,column=0)
        Button(self.cal_frame,text='.',bg="#FFC300 ",font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen(',')).grid(row=4,column=1)
        Button(self.cal_frame,text='/',bg="#FFC300 ",font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('/')).grid(row=4,column=2)
        Button(self.cal_frame,text='x',bg="#FFC300 ",font=('Arial',20,'bold'),width=4,relief='groove',command = lambda : self.fill_screen('*')).grid(row=4,column=3)

        Button(self.cal_frame,text="=",bg="#458B00",font=('Arial',20,'bold'),width=8,relief='groove',command=self.calculator_equal).grid(row=6,column=0,columnspan = 2)
        Button(self.cal_frame,text="(",bg="#FFC300 ",font=('Arial',20,'bold'),width=4,relief='groove',command=self.calculator_equal).grid(row=6,column=2)
        Button(self.cal_frame,text=")",bg="#FFC300 ",font=('Arial',20,'bold'),width=4,relief='groove',command=self.calculator_equal).grid(row=6,column=3)


        # self.win.mainloop()
    def fill_screen(self,sym):
        # print(sym)
        if sym == ".":
        # print(self.calculator_value.get())
            self.expression = self.expression[:-1]
        elif sym =='c':
            self.expression=''
        else:
            self.expression = self.expression+sym
        
        self.screen.delete(0,END)
        self.screen.insert(END,self.expression)
        
    def calculator_equal(self):
        value = self.calculator_value.get()
        try:
            ans = eval(value)
            self.screen.delete(0,END)
            self.screen.insert(END,ans)
        except:
            messagebox.showerror("Wrong Input!","Your Input was given worng")
            self.expression = ''
            self.screen.delete(0,END)
    def discard(self):
        super().distroy()
if __name__ == "__main__":
    init(Tk())
