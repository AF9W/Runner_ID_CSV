
from Tkinter import *
import ttk
from time import  strftime, localtime

def store_time(*args): # Store time runner # arrived
    try:
        if number.get() == '':
            status.set('No number')
            return

        else:
            runner.set(number.get())
            number.set('')

        if runner_list.has_key(int(runner.get())):
            status.set('DUPE')
            time.set(runner_list[int(runner.get())])

        else:
            time.set(strftime("%H:%M", localtime()))
            runner_list[int(runner.get())] = time.get()
            listb.set(int(runner.get()),runner.get()+' '+time.get())
            status.set('')

    except ValueError:
        pass

def DNS_time(*args): # Enter DNS for runner #
    try:
        if number.get() == '':
            status.set('No number')
            return

        else:
            runner.set(number.get())
            time.set('DNS')
            number.set('')

        if runner_list.has_key(int(runner.get())):
            status.set('DUPE')

        else:
            runner_list[int(runner.get())] = time.get()
            listb.insert(END, runner.get() + ' ' + time.get())
            status.set('')

    except ValueError:
        pass

def delete_time(*args): # Delete runner entry
    try:
        if number.get() == '':
            status.set('No number')
            return

        else:
            runner.set(number.get())
            time.set(strftime("%H:%M", localtime()))
            number.set('')

        if runner_list.has_key(int(runner.get())):
            runner_list.pop(int(runner.get()))
            status.set('Deleted')
        else:
            status.set('Not Found')

    except ValueError:
        pass

def print_nums(*args):
    print runner_list
    for i in range(tot_runners):
        print i+1,runner_list.get(i+1,"none")

tot_runners = 15

root = Tk()
root.title("Runner Timing Entry")

# Create main window frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Create list frame
list = StringVar()
listb = Listbox(mainframe)
listb.grid(column=0,columnspan=4,row=5,rowspan=10,sticky=(N, W, E, S))
for i in range(tot_runners):
    listb.insert(END, i+1)

# Create Main Menu
menubar = Menu(root)
menubar.add_command(label='Print',command=print_nums)
menubar.add_command(label='Quit',command=root.quit)
root.config(menu=menubar)

# Create data structures
runner_list = {}
runner = StringVar()
number = StringVar()
time = StringVar()
status = StringVar()

# Create entry box
number_entry = ttk.Entry(mainframe, width=7, textvariable=number)
number_entry.grid(column=2, row=1, sticky=(W, E))

# Display static text
ttk.Label(mainframe, text="Runner Number").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Runner").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Time in").grid(column=1, row=3, sticky=E)

# Display buttons
ttk.Button(mainframe, text="Time", command=store_time).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="DNS", command=DNS_time).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="Delete", command=delete_time).grid(column=3, row=3, sticky=W)

# Display variables
ttk.Label(mainframe, textvariable=runner).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=time).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=status).grid(column=2, columnspan = 2, sticky=(W, E), row=4)

# add padding to each child of the main window
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

number_entry.focus() # put cursor into entry box
root.bind('<Return>', store_time) # execute store_time function when Enter key is pressed

root.mainloop()