from tkinter import *
from tkinter import messagebox
from Reflection_Back import *

root = Tk()
root.title("Seismic reflection")
root.geometry('600x600')

'''
FUNCTIONS SECTION
'''
errorColor = '#ffaaaa' # '#ff9595'

# Function for disabling Entry after clicking checkbox
def disableEntry(chosen, entry1, entry2):
    if chosen.get():
        entry1.config(state=DISABLED)
        entry2.config(state=NORMAL)
    else:
        entry1.config(state=NORMAL)
        entry2.config(state=DISABLED)


# Function for changing color of all backgrounds due to choosen value in OptionMenu
def bg_chooser1(self):  # Had to do this shitty function instead of changing only 1 variable at a time D:
    if choosed1.get()== 'Fluid':
        frame1.config(bg=fluid_bg)
        layer1.config(bg=fluid_bg)
        c1_Label.config(bg=fluid_bg)
        b1_Label.config(bg=fluid_bg)
        rho1_Label.config(bg=fluid_bg)
        check1.config(bg=fluid_bg)
        calc_b1.config(bg=fluid_bg)
        sigma1_Label.config(bg=fluid_bg)
    else:
        frame1.config(bg=solid_bg)
        layer1.config(bg=solid_bg)
        c1_Label.config(bg=solid_bg)
        b1_Label.config(bg=solid_bg)
        rho1_Label.config(bg=solid_bg)
        check1.config(bg=solid_bg)
        calc_b1.config(bg=solid_bg)
        sigma1_Label.config(bg=solid_bg)
        
def bg_chooser2(self):  
    if choosed2.get()== 'Fluid':
        frame2.config(bg=fluid_bg)
        layer2.config(bg=fluid_bg)
        c2_Label.config(bg=fluid_bg)
        b2_Label.config(bg=fluid_bg)
        rho2_Label.config(bg=fluid_bg)
        check2.config(bg=fluid_bg)
        calc_b2.config(bg=fluid_bg)
        sigma2_Label.config(bg=fluid_bg)
    else:
        frame2.config(bg=solid_bg)
        layer2.config(bg=solid_bg)
        c2_Label.config(bg=solid_bg)
        b2_Label.config(bg=solid_bg)
        rho2_Label.config(bg=solid_bg)
        check2.config(bg=solid_bg)
        calc_b2.config(bg=solid_bg)
        sigma2_Label.config(bg=solid_bg)    

# Function to check if velocities in km/s or m/s (if rho is in kg/m3 or g/sm3), so user can input either way
def checkValue(entry):
    entry.config(bg='white')
    try:
        if 100 < float(entry.get()) < 1000:
            return float(entry.get())
        elif float(entry.get()) % 1000 == float(entry.get()):
            return float(entry.get())*1000
        else:
            return float(entry.get())
    except:
        entry.config(bg=errorColor)
        messagebox.showerror('Error', 'You should enter number here!')

# Need to check sigma with other function, because sigma < 0.7
def checkSigma(entry):
    entry.config(bg='white')
    try:
        return float(entry.get())
    except:
        entry.config(bg=errorColor)
        messagebox.showerror('Error', 'You should enter number here!')

# Function to compute all stuff
def compute():
    Vp1 = checkValue(c1)
    p1 = checkValue(rho1)
    Vp2 = checkValue(c2)
    p2 = checkValue(rho2)
    
    # Checking how to calculate speed
    try:
        if checkVar1.get():
            Vs1 = comp_vs(Vp1, checkSigma(sigma1))
        else:
            Vs1 = checkValue(b1)

        if checkVar2.get():
            Vs2 = comp_vs(Vp2, checkSigma(sigma2))
        else:
            Vs2 = checkValue(b2)

        # Checking wavetype    
        wave.config(bg='white')
        if wave.get() == 'PP':
            waveType = 'PP'
            elem = 'PdPu'
        elif wave.get() == 'PS':
            waveType = 'PS'
            elem = 'PdSu'
        else:
            wave.config(bg=errorColor)
            messagebox.showerror('Error', 'Incorrect input\nEnter "PP" or "PS"')
    
        Rpp = calc_Rpp(Vp1, Vs1, p1, Vp2, Vs2, p2, elem)
    
    except:
        pass

    try:
        computeAndShow(Rpp, waveType, title.get(), xLabel.get(), yLabel.get(), pathToFolder.get())
    except:
        messagebox.showerror('Error', 'Incorrect names\nEnter all names!')

'''
END OF FUNCTIONS SECTION
'''


# Creating types of layer and drops for it
layer_types = ('Fluid', 'Solid')
choosed1, choosed2 = StringVar(), StringVar()
choosed1.set(layer_types[0])
choosed2.set(layer_types[1])


# Creating borderline beetween surface and Layer №1
canva1 = Canvas(root, width=600, height=10)
canva1.create_line(0, 5, 600, 5, width=1, fill='black')
canva1.place(x=0, y=25)

Label(root, text='surface', font=14).place(x=275, y=5, width=50, height=20)

# Variables for setting background
fluid_bg = '#94e7fc'
solid_bg = '#cb9f7c'

bg1 = fluid_bg
bg2 = solid_bg

# Layer №1 display
frame1 = Frame(root, bg=bg1)
frame1.place(x=0, y=31, width=600, height=152)

layer1 = Label(frame1, text='Layer №1', font=24, bg=bg1)
layer1.place(x=20, y=10, width=70, height=20)

drop1 = OptionMenu(frame1, choosed1, *layer_types, command=bg_chooser1)
drop1.place(x=18, y=40, width=70, height=30)


c1_Label = Label(frame1, text='c1 = ', font=12, bg=bg1)
c1_Label.place(x=100, y=30, width=50, height=20)
c1 = Entry(frame1, bg='white', font=10)
c1.place(x=150, y=30, width=60, height=20)


b1_Label = Label(frame1, text='b1 = ', font=12, bg=bg1)
b1_Label.place(x=102, y=60, width=50, height=20)
b1 = Entry(frame1, bg='white', font=10, disabledbackground='#c0c0c0')
b1.place(x=152, y=60, width=60, height=20)

rho1_Label = Label(frame1, text='rho1 = ', font=12, bg=bg1)
rho1_Label.place(x=108, y=90, width=50, height=20)
rho1 = Entry(frame1, bg='white', font=10)
rho1.place(x=160, y=90, width=60, height=20)


# Checkbutton and labels for calculation display layer №1
checkVar1 = IntVar() # creating this variable to get value from checkbutton
check1 = Checkbutton(frame1, bg=bg1, variable=checkVar1, command=lambda: disableEntry(checkVar1, b1, sigma1))
check1.place(x=240, y=59, width=20, height=20)


calc_b1 = Label(frame1, text='calculate b: ', font=12, bg=bg1)
calc_b1.place(x=260, y=58, width=80, height=20)

sigma1_Label = Label(frame1, text='sigma1 = ', font=12, bg=bg1)
sigma1_Label.place(x=340, y=58, width=80, height=20)
sigma1 = Entry(frame1, bg='white', font=10, state=DISABLED, disabledbackground='#c0c0c0')
sigma1.place(x=415, y=58, width=60, height=20)

#disableEntry(checkVar1, b1, sigma1)

# Creating borderline beetween Layer №1 and Layer №2
canva2 = Canvas(root, width=600, height=5)
canva2.create_line(0, 5, 600, 5, width=1, fill='black')
canva2.place(x=0, y=170)


# Layer №2 display
frame2 = Frame(root, bg=bg2)
frame2.place(x=0, y=176, width=600, height=152)

layer2 = Label(frame2, text='Layer №2', font=24, bg=bg2)
layer2.place(x=20, y=10, width=70, height=20)

drop2 = OptionMenu(frame2, choosed2, *layer_types, command=bg_chooser2)
drop2.place(x=18, y=40, width=70, height=30)


c2_Label = Label(frame2, text='c2 = ', font=12, bg=bg2)
c2_Label.place(x=100, y=30, width=50, height=20)
c2 = Entry(frame2, bg='white', font=10)
c2.place(x=150, y=30, width=60, height=20)

b2_Label = Label(frame2, text='b2 = ', font=12, bg=bg2)
b2_Label.place(x=102, y=60, width=50, height=20)
b2 = Entry(frame2, bg='white', font=10, disabledbackground='#c0c0c0')
b2.place(x=152, y=60, width=60, height=20)

rho2_Label = Label(frame2, text='rho2 = ', font=12, bg=bg2)
rho2_Label.place(x=108, y=90, width=50, height=20)
rho2 = Entry(frame2, bg='white', font=10)
rho2.place(x=160, y=90, width=60, height=20)


# Checkbutton and labels for calculation display layer №2
checkVar2 = IntVar() # creating this variable to get value from checkbutton
check2 = Checkbutton(frame2, bg=bg2, variable=checkVar2, command=lambda: disableEntry(checkVar2, b2, sigma2))
check2.place(x=240, y=59, width=20, height=20)

calc_b2 = Label(frame2, text='calculate b: ', font=12, bg=bg2)
calc_b2.place(x=260, y=58, width=80, height=20)

sigma2_Label = Label(frame2, text='sigma2 = ', font=12, bg=bg2)
sigma2_Label.place(x=340, y=58, width=80, height=20)
sigma2 = Entry(frame2, bg='white', font=10, state=DISABLED, disabledbackground='#c0c0c0')
sigma2.place(x=415, y=58, width=60, height=20)


#Label for type of reflected wave
Label(root, text='Enter type of reflected wave', font=12).place(x=0, y=332, width=200, height=20)
wave = Entry(root, bg='white', font=10)
wave.place(x=200, y=333, width=70, height=20)


# Entries for folder's path and picture names
Label(root, text='Picture settings', font="Verdana 15 underline").place(x=0, y=360, width=170, height=30)

Label(root, text='Enter title', font=12).place(x=0, y=400, width=80, height=30)
title = Entry(root, bg='white', font=10)
title.place(x=80, y=406, width=150, height=20)

Label(root, text='xLabel', font=12).place(x=0, y=430, width=80, height=30)
xLabel = Entry(root, bg='white', font=10)
xLabel.place(x=80, y=436, width=150, height=20)

Label(root, text='yLabel', font=12).place(x=0, y=460, width=80, height=30)
yLabel = Entry(root, bg='white', font=10)
yLabel.place(x=80, y=466, width=150, height=20)

Label(root, text='Enter path to folder', font=12).place(x=330, y=400, width=200, height=30)
pathToFolder = Entry(root, bg='white', font=10)
pathToFolder.place(x=293, y=430, width=270, height=20)


#Button to compute result
computeButton = Button(root, text="Compute", font=20, command=compute, activeforeground='blue', activebackground='white', bg='#ff8080', bd=1)
computeButton.place(x=95, y=530, width=400, height=40)


root.resizable(False, False) 
root.mainloop()