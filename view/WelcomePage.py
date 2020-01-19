from tkinter import *
from control.CourseData import *

# Set up
screen_width = 600
screen_height = 600
main_screen_background = "light blue"

# initializing entry boxes
global box1
global box2
global box3
global box4
global box5


def main_screen():
    # function called when button clicked
    def enter():
        course_list = [box1.get().lower(), box2.get().lower(), box3.get().lower(), box4.get().lower(), box5.get().lower()]
        get_data(course_list)

    # On click events
    def on_click(event):
        box1.configure(state=NORMAL)
        box1.delete(0, END)
        box1.unbind('<Button-1>', on_click_id)

    def on_click2(event):
        box2.configure(state=NORMAL)
        box2.delete(0, END)
        box2.unbind('<Button-1>', on_click_id2)

    def on_click3(event):
        box3.configure(state=NORMAL)
        box3.delete(0, END)
        box3.unbind('<Button-1>', on_click_id3)

    def on_click4(event):
        box4.configure(state=NORMAL)
        box4.delete(0, END)
        box4.unbind('<Button-1>', on_click_id4)

    def on_click5(event):
        box5.configure(state=NORMAL)
        box5.delete(0, END)
        box5.unbind('<Button-1>', on_click_id5)

    screen = Tk()
    screen.configure(background=main_screen_background)
    screen.geometry(str(screen_width) + "x" + str(screen_height))  # Setting the size of the main screen
    screen.title("Perfect Schedule Make")  # Title of the screen

    # Setting the labels
    Label(text="", bg="blue", width=str(screen_width), height="2", font=("Calibri, 13")).pack()
    Label(width=str(screen_width), height="1", bg=main_screen_background).pack()

    Label(text="WELCOME", width=str(screen_width), font=("Calibri, 20"), bg=main_screen_background).pack()
    Label(width=str(screen_width), height="1", bg=main_screen_background).pack()

    Label(text="ENTER YOUR COURSES (EG: CS135):", width=str(screen_width), font=("Calibri, 15"),
          bg=main_screen_background).pack()
    Label(width=str(screen_width), height="1", bg=main_screen_background).pack()

    # Setting the input fields
    box1 = Entry(width="30", bg="white", selectborderwidth="0.25", font=("Calibri, 20"))
    box1.insert(0, "First Choice")
    box1.configure(state=DISABLED)
    on_click_id = box1.bind('<Button-1>', on_click)
    box1.pack()
    Label(width=str(screen_width), bg=main_screen_background).pack()

    box2 = Entry(width="30", bg="white", selectborderwidth="0.25", font=("Calibri, 20"))
    box2.insert(0, "Second Choice")
    box2.configure(state=DISABLED)
    on_click_id2 = box2.bind('<Button-1>', on_click2)
    box2.pack()
    Label(width=str(screen_width), bg=main_screen_background).pack()

    box3 = Entry(width="30", bg="white", selectborderwidth="0.25", font=("Calibri, 20"))
    box3.insert(0, "Third Choice")
    box3.configure(state=DISABLED)
    on_click_id3 = box3.bind('<Button-1>', on_click3)
    box3.pack()
    Label(width=str(screen_width), bg=main_screen_background).pack()

    box4 = Entry(width="30", bg="white", selectborderwidth="0.25", font=("Calibri, 20"))
    box4.insert(0, "Fourth Choice")
    box4.configure(state=DISABLED)
    on_click_id4 = box4.bind('<Button-1>', on_click4)
    box4.pack()
    Label(width=str(screen_width), bg=main_screen_background).pack()

    box5 = Entry(width="30", bg="white", selectborderwidth="0.25", font=("Calibri, 20"))
    box5.insert(0, "Fifth Choice")
    box5.configure(state=DISABLED)
    on_click_id5 = box5.bind('<Button-1>', on_click5)
    box5.pack()
    Label(width=str(screen_width), bg=main_screen_background).pack()

    # Setting up the enter button
    button = Button(text="Enter", height="2", width="15", command=lambda: enter())
    button.pack()

    screen.mainloop()

main_screen()
