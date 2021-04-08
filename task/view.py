from tkinter import *
from restart import restarting
from update_param import setFirstWorkingDay, setFirstHour, setLastHour,setMeasuringDuration,setInterval,updateStatus
from program import run

# in this func I made the user interface just run this page
def GUI():
    window = Tk()
    window.geometry('1200x500')
    window.title("awesome scheduler")

    lbl = Label(window, text="Hi Eric! welcome to my scheduler\n here I will give you  The schedule that will be as tight as possible ", font=("Arial Bold", 20),fg="grey")
    lbl.grid(column=10, row=0)
    lbl = Label(window, text="First of all press Restart", font=("Arial Bold", 10),fg="blue")
    lbl.grid(column=10, row=2)
    btn = Button(window, text="Restart",bg="blue", fg="white",command=restarting)
    btn.grid(column=10, row=3)

    lbl = Label(window, text="Okay, now please let me know, what day of the week you want to start working(in number, for Sunday press 1)?", font=("Arial Bold", 10),fg="green")
    lbl.grid(column=10, row=4)
    spin = Spinbox(window, from_=1, to=5, width=5)
    spin.grid(column=11,row=4)
    lbl = Label(window, text="Now enter the hours you want to work each day:   ", font=("Arial Bold", 10),fg="green")
    lbl.grid(column=10, row=5)
    lbl = Label(window, text="start at: ", font=("Arial Bold", 10),fg="green")
    lbl.grid(column=11, row=5)
    spin1 = Spinbox(window, from_=00, to=24, width=4)
    spin1.grid(column=12,row=5)
    spin2 = Spinbox(window, from_=0, to=59, width=4)
    spin2.grid(column=13,row=5)
    lbl = Label(window, text="finish at: ", font=("Arial Bold", 10),fg="green")
    lbl.grid(column=11, row=6)
    spin3 = Spinbox(window, from_=0, to=24, width=4)
    spin3.grid(column=12,row=6)
    spin4 = Spinbox(window, from_=0, to=59, width=4)
    spin4.grid(column=13,row=6)
    lbl = Label(window, text="what is the duration of one measuring?   ", font=("Arial Bold", 10),fg="green")
    lbl.grid(column=10, row=7)
    spin5 = Spinbox(window, from_=0.0, to=20.0, width=4)
    spin5.grid(column=11,row=7)
    lbl = Label(window, text="what is the interval between measurements?", font=("Arial Bold", 10),fg="green")
    lbl.grid(column=10, row=8)
    spin6 = Spinbox(window, from_=0.000000001, to=9.9999999, width=4)
    spin6.grid(column=11,row=8)
    def durationClicked():
        setFirstWorkingDay(spin.get())
        setFirstHour(spin1.get(),spin2.get())
        setLastHour(spin3.get(),spin4.get())
        setMeasuringDuration(spin5.get())
        setInterval(spin6.get())
    ok = Button(window, text="ok",bg="green", fg="white",command=durationClicked)
    ok.grid(column=10, row=9)

    lbl = Label(window, text="want to make any canges from tommorow? no problem. just let me know what is your status:", font=("Arial Bold", 10),fg="purple")
    lbl.grid(column=10, row=10)

    lbl = Label(window, text="enter the number of the person that you want to update:", font=("Arial Bold", 10),fg="purple")
    lbl.grid(column=10, row=11)
    spin7 = Spinbox(window, from_=1, to=100, width=4)
    spin7.grid(column=11,row=11)
    lbl = Label(window, text="Enter the number of measuring left for this person:", font=("Arial Bold", 10),fg="purple")
    lbl.grid(column=10, row=12)
    spin8 = Spinbox(window, from_=0, to=10000, width=4)
    spin8.grid(column=11,row=12)
    def commitClicked():
        updateStatus(spin7.get(),spin8.get())
    btn = Button(window, text="Commit",bg="purple", fg="white",command=commitClicked)
    btn.grid(column=11, row=13)

    lbl = Label(window, text="ready? press Start!", font=("Arial Bold", 20),fg="pink")
    lbl.grid(column=10, row=15)
    btn = Button(window, text="Start",bg="pink", fg="white",command=run)
    btn.grid(column=10, row=16)

    window.mainloop()

GUI()

