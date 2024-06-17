



from tkinter import *
from tkintermapview import TkinterMapView
import os

root = Tk()
root.geometry("850x450")
root.title("Rody[صيدليات المناوبة]")
root.configure(background="white")

# Global map variable
map = TkinterMapView(root, width=500, height=400, corner_radius=0)
map.place(x=500, y=45)

# =====Defs=======

def markazi():
    global map
    map.set_tile_server("http://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=22)
    map.set_position(33.513612346705095, 36.317851971401105)
    map.set_zoom(15)
    marker = map.set_marker(33.513612346705095, 36.317851971401105)
    marker.set_text("Rody[صيدلية مركزية]")

def cu():
    global map
    country = En.get()
    map.set_tile_server("http://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=22)
    map.set_address(country, marker=True)

# ======== TITLE =======

title = Label(root, 
              text="مشروع صيدليات المناوبة", 
              fg="white",
              bg="black",
              font=('tajwal', 18)
)
title.pack(fill='x')  

#======= logo =======

logo_path = os.path.join(os.path.dirname(__file__), "images", "doctor.png")
print('logo path', logo_path)
logo = PhotoImage(file=logo_path)
lab_log = Label(root, image=logo, bd=0, bg="white")
lab_log.place(x=30, y=40)

#======Label + Entry + Button=======

l = Label(root, text="country:", font=("tajwal 13"), fg="black", bg="white")
l.place(x=30, y=420)

En = Entry(root, font=("tajwal", 14), width=10, bd=2, relief=GROOVE)
En.place(x=120, y=420)

b1 = Button(root, text="Get Country",
            bg='black', fg="white", bd=1,
            relief=SOLID,
            width=10, cursor="hand2", command=cu
            )
b1.place(x=260, y=420)

#==========Pharmacy Buttons==========

b = Button(
    root, text="صيدلية مركزية",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13, command=markazi
    )
b.place(x=10, y=600)

b1 = Button(
    root, text="صيدلية مزرعة",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13
    )
b1.place(x=150, y=490)

b2 = Button(
    root, text="صيدلية الطحان",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13
    )
b2.place(x=290, y=490)

b3 = Button(
    root, text=" صيدلية جماصيني",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13
    )
b3.place(x=10, y=550)

b4 = Button(
    root, text="صيدلية  شاكر ماهر شاكر ",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13
    )
b4.place(x=150, y=490)

b5 = Button(
    root, text=" صيدلية مرعي",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13
    )
b5.place(x=290, y=550)

b6 = Button(
    root, text="صيدلية ايمن مرزة",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13
    )
b6.place(x=290, y=600)

b7 = Button(
    root, text="صيدلية ملقي",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13
    )
b7.place(x=150, y=550)

b8 = Button(
    root, text=" صيدلية شمندر",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13
    )
b8.place(x=10, y=490)

b9 = Button(
    root, text="صيدلية مجتهد",
    cursor="hand2",
    bg="White",
    fg="black",
    bd=1,
    relief=SOLID,
    font=("tajwal 12"),
    width=13
    )
b9.place(x=150, y=600)

#=======maps=======

map = TkinterMapView(root, width=500, height=400, corner_radius=0)
map.place(x=500, y=45)

root.mainloop()
x