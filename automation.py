import sys 
import threading
from tkinter import *
import subprocess
from threading import *
import re
import struct 

import speech_recognition as sr
import pyttsx3 as tts

class AutomationBot:

    def open(self,command):
        command = str(command)
        self.bot_face.config(fg='#A0D8B3')
        
        if 'google chrome' in command and len(command) > 19 :
            terminal_command = 'google-chrome'
            if 'web site' in command:
                argument = ''.join(command.split()[5:])
                final_command = [terminal_command,argument]
                result = subprocess.run(final_command,shell = False , capture_output=False , text=False , executable='/bin/google-chrome')
            elif 'website' in command:
                argument =''.join(command.split()[4:])
                final_command = [terminal_command , argument]
                result = subprocess.run(final_command,shell = False , capture_output=False , text=False , executable='/bin/google-chrome')

        elif 'firefox' in command and len(command) > 13:
            if 'web site' in command: 
                final_command = [command.split()[1],''.join(command.split()[4:])]    
                result = subprocess.run(final_command , shell = False , capture_output= False , text = False, executable='/bin/firefox')
            elif 'website' in command and len(command) > 13 :
                final_command = [command.split()[1],''.join(command.split()[3:])]    
                result = subprocess.run(final_command , shell = False , capture_output= False , text = False, executable='/bin/firefox')
                
        elif 'brave' in command and len(command) > 15:
            terminal_command = 'brave-browser'
            if 'web site' in command:
                argument = command.split()[4]
                final_command = [terminal_command,argument]
                result = subprocess.run(final_command,shell = False , capture_output=False , text=False , executable='/bin/brave-browser')
            elif 'website' in command:
                argument = command.split()[3]
                final_command = [terminal_command , argument]
                result = subprocess.run(final_command,shell = False , capture_output=False , text=False , executable='/bin/brave-browser')


        elif 'file manager' in command:
            terminal_command = 'nautilus'
            
            result = subprocess.run(terminal_command,shell=False,capture_output=False,text=False,executable='/bin/nautilus')
            

        elif "pdf" in command:
            terminal_command = 'xdg-open'
            argument = self.path_e.get()
            if argument is None :
                alert_tk = Tk()
                label = Label(alert_tk , text = 'PLs pass the path to the file !!').grid(row=0 , column=0)

                alert_tk.mainloop()
            else:
                argument = str(argument)
                
                final_command = [terminal_command , argument]
                result  = subprocess.run(final_command , shel = False , text = False , capture_output=False , executable='/bin/xdg-open')


        elif "open" in command :
            command = command.replace('chrome','google-chrome')
            command = command.replace('google','google-chrome')
            command = command.replace('brave','brave-browser')
            
            command.strip()
            terminal_command = command.split()[1]
            result = subprocess.run(terminal_command,shell=False,capture_output=False,text=False,executable='/bin/'+terminal_command)

        elif 'quit' in command or 'exit' in command:
            sys.exit()


        else:
            print("no such command found")

    def themeframe(self):
            self.main_frame.pack_forget()
            self.theme_frame.pack()

    def home(self):
        self.theme_frame.pack_forget()
        self.main_frame.pack()

    def applytheme(self):
        bkg_col = self.bgcol_e.get()
        bkg_col = str(bkg_col)
        fntcol = self.fntcol_e.get()
        fntcol = str(fntcol) 
        rbtidel = self.robotidelcol_e.get()
        rbtidel = str(rbtidel)
        rbtlst = self.robotlistcol_e.get()
        rbtlst = str(rbtlst)
        rbtdw = self.robotdwcol_e.get()
        rbtdw = str(rbtdw) 
        font = self.font_ty_e.get()
        font = str(font) 

        self.data_format = "256s256s256s256s256s256s"
        self.path = "/home/soul/Documents/vscode/python/automation/theme.bin"

        binary_data = struct.pack(self.data_format,bkg_col.encode(),fntcol.encode(),rbtidel.encode(),rbtlst.encode(),rbtdw.encode(),font.encode())

        with open(self.path,'wb') as file:
            file.write(binary_data)
            file.close()

        self.bgcol_e.delete(0,END)
        self.fntcol_e.delete(0,END)
        self.robotidelcol_e.delete(0,END)
        self.robotlistcol_e.delete(0,END)    
        self.robotdwcol_e.delete(0,END)    
        self.font_ty_e.delete(0,END)




    def __init__(self):
        self.index_num = 4
        self.recognizer = sr.Recognizer()
        self.path = "/home/soul/Documents/vscode/python/automation/theme.bin"
        self.data_format = "256s256s256s256s256s256s"

        with open (self.path,'rb') as file :
            theme_data = file.read()

        unpack_data = struct.unpack(self.data_format,theme_data)

        bkg_col = unpack_data[0].decode().strip('\x00')
        fntcol = unpack_data[1].decode().strip('\x00')
        rbtidel = unpack_data[2].decode().strip('\x00')
        rbtlst = unpack_data[3].decode().strip('\x00')
        rbtdw = unpack_data[4].decode().strip('\x00')
        fnt = unpack_data[5].decode().strip('\x00')
        
        
        
        self.root = Tk()
        self.root.geometry('150x150')
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        self.settings_menu = Menu(self.root, tearoff =0)

        self.settings_menu.add_command(label='Theme',command=self.themeframe)
        self.settings_menu.add_command(label='Home' , command = self.home)
        self.menubar.add_cascade(label='Settings' , menu=self.settings_menu)
        
        self.main_frame = Frame(self.root , height=600 , width=800,bg = bkg_col)
        self.bot_face = Label(self.main_frame ,text = '😊', font=('',100),bg = bkg_col,fg=rbtidel)
        self.bot_face.place(x=1, y = 1)


        self.path_e = Entry(self.main_frame , width = 20 , font =(fnt,12) , fg = fntcol,bg =bkg_col)
        self.path_e.place(x = 200 , y = 20)




        self.main_frame.pack()

        self.theme_frame = Frame(self.root , width=800 , height=600,bg = bkg_col)
        theme_label = Label(self.theme_frame , text = 'Theme' , font=(fnt,15),fg=fntcol,bg = bkg_col).place(x=5 , y = 5)
        background_color = Label(self.theme_frame , text = 'Backgorund color :' , font=(fnt,15),fg=fntcol,bg = bkg_col).place(x = 10,y=30)
        font_color = Label(self.theme_frame , text = 'Font color :' , font=(fnt,15),fg=fntcol,bg = bkg_col).place(x = 10,y=60)
        robot_idel = Label(self.theme_frame , text = 'Idel :' , font=(fnt,15),fg=fntcol,bg = bkg_col).place(x = 10 ,y = 90)
        robot_listening = Label(self.theme_frame , text = 'Listening :' , font=(fnt,15),fg=fntcol,bg = bkg_col).place(x = 10 ,y = 120)
        robot_doingwork = Label(self.theme_frame , text = 'Working :' , font=(fnt,15),fg=fntcol,bg = bkg_col).place(x = 10 ,y = 150)
        font_type_lbl = Label(self.theme_frame , text ='Fonat :' , font = (fnt,15),fg = fntcol , bg = bkg_col).place(x=10 , y = 180)
        notice_lbl = Label(self.theme_frame , text = "do put '#' before the hex number of the colour ",font=(fnt,20),fg=fntcol,bg = bkg_col).place(x=5,y = 210)
        self.font_ty_e = Entry(self.theme_frame , width = 20 , font = (fnt,10),bg = bkg_col , fg = fntcol)
        self.bgcol_e = Entry(self.theme_frame,width=20 , font=(fnt,10),bg = bkg_col,fg=fntcol)
        self.fntcol_e = Entry (self.theme_frame , width =20 , font=(fnt,10)  ,bg = bkg_col,fg=fntcol)
        self.robotidelcol_e = Entry (self.theme_frame , width =20 , font=(fnt,10)  ,bg = bkg_col,fg=fntcol)
        self.robotlistcol_e = Entry (self.theme_frame , width =20 , font=(fnt,10)  ,bg = bkg_col,fg=fntcol)
        self.robotdwcol_e = Entry (self.theme_frame , width =20 , font=(fnt,10)  ,bg = bkg_col,fg=fntcol)
        apply_changes = Button(self.theme_frame , text='Apply' , font=(fnt,10), bg = bkg_col,fg = fntcol , activebackground=fntcol,activeforeground=bkg_col,command = self.applytheme)



        apply_changes.place(x=30, y=250)
        self.bgcol_e.place(x = 170 , y =30 )
        self.fntcol_e.place(x=170 , y=60)
        self.robotidelcol_e.place(x=170 , y=90)
        self.robotlistcol_e.place(x=170,y=120)
        self.robotdwcol_e.place(x=170,y=150)
        self.font_ty_e.place(x = 170, y = 180)

        self.bgcol_e.insert(0,bkg_col)
        self.fntcol_e.insert(0,fntcol)
        self.robotidelcol_e.insert(0,rbtidel)
        self.robotlistcol_e.insert(0,rbtlst)
        self.robotdwcol_e.insert(0,rbtdw)
        self.font_ty_e.insert(0,fnt)



        self.theme_frame.pack_forget()

        
        
        def acitivate():
            while True:
                try:
                    with sr.Microphone(device_index=self.index_num) as mic:
                        self.bot_face.config(fg=rbtidel)
                        self.recognizer.adjust_for_ambient_noise(mic)
                        audio = self.recognizer.listen(mic,timeout=3)
                        text = self.recognizer.recognize_google(audio)
                        text = str(text)
                        text = text.lower()
                        if "hello" in text:
                            print('listening')
                            self.bot_face.config(fg=rbtlst)
                            self.recognizer.adjust_for_ambient_noise(mic)
                            command = self.recognizer.listen(mic,timeout=5)
                            command_text =self.recognizer.recognize_google(command)
                            command_text = str(command_text)
                            command_text = command_text.lower()
                            if 'open' in command_text:                                
                                t1 = Thread(target=self.open , args=(command_text,))
                                t1.start()                               
                            elif 'close' in command_text:
                                self.bot_face.config(fg=rbtdw)
                                command_text = command_text.replace('google','chrome')
                                command_text = command_text.replace('google chrome','chrome')
                                command_text = command_text.replace('pdf' , 'evince')
                                print('closing '+ command_text.split()[1])
                                application = command_text.split()[1]
                                terminal_command = ['killall',application]
                                close = subprocess.run(terminal_command,executable='/bin/killall')
                                print('closed '+ command_text.split()[1])
                                self.bot_face.config(fg=rbtidel)
                        else :
                            print('')




                except sr.UnknownValueError:
                    print("Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Speech Recognition service; {0} /n PLS CHECK INTERNET CONNECTION ".format(e))

        activate_thread = Thread(target=acitivate)
        activate_thread.start()
        
        self.root.mainloop()
        
#Apple

        
AutomationBot()
#no comment

