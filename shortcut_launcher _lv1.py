shortcut_launcher=tkinter.Tk()

shortcut_launcher.title("Shortcut launcher")
shortcut_launcher.geometry("800x200+100+100")
shortcut_launcher.resizable(False, False)
#window setting

imgNote = tkinter.PhotoImage(file="Notes.png")
imgcalc = tkinter.PhotoImage(file="calc.png")
imgFinder = tkinter.PhotoImage(file="finder.png")
imgGoogle = tkinter.PhotoImage(file="google.png")


def notepad():
    # notepad = "Notes.app"
    # notepad
    os.system("open /Applications/Notes.app")
    
def calc():
    os.system('open /Applications/Calculator.app')

def finder():
    os.system('open .')
#mac os -> use "finder" instead of "c:"
    
def google():
    google = "http://google.com"
    webbrowser.open(google)


btn1 = tkinter.Button(shortcut_launcher,overrelief="groove", width=60
, height=60, command=notepad, image= imgNote)
btn2 = tkinter.Button(shortcut_launcher, overrelief="groove", width=60
, height=60,command=calc,image= imgcalc)
btn3 = tkinter.Button(shortcut_launcher, overrelief="groove",width=60
, height=60,command = finder, image= imgFinder)
btn4 = tkinter.Button(shortcut_launcher, text='버튼4', overrelief="groove", width=7, height=4)

btn5 = tkinter.Button(shortcut_launcher, overrelief="groove",width=60
, height=60,command=google, image = imgGoogle)
btn6 = tkinter.Button(shortcut_launcher, text='버튼6', overrelief="groove", width=7, height=4)
btn7 = tkinter.Button(shortcut_launcher, text='버튼7', overrelief="groove", width=7, height=4)
btn8 = tkinter.Button(shortcut_launcher, text='버튼8', overrelief="groove", width=7, height=4)
#button setting


btn1.place(x = 50, y = 20)
btn2.place(x = 150, y = 20)
btn3.place(x = 250, y = 20)
btn4.place(x = 350, y = 20)

btn5.place(x = 50, y = 110)
btn6.place(x = 150, y = 110)
btn7.place(x = 250, y = 110)
btn8.place(x = 350, y = 110)
#button place


shortcut_launcher.mainloop()

