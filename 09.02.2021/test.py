from tkinter import *
import math
import random

def delMap():
    x = 0

def drawMap():
    W = float(E6.get()) - float(E5.get())
    H = float(E8.get()) - float(E7.get())
    r = 10

    canvas = Canvas(top, width=int(W+40), height=int(H+40))

    n_points = int(E1.get())
    n_routes = int(E2.get())

    points = []

    while len(points) < n_points:
        X = int(random.randrange(float(E5.get()), float(E6.get())))
        Y = int(random.randrange(float(E7.get()), float(E8.get())))
        point_routes = 0

        points.append([X, Y])

        canvas.create_oval(X - r, Y - r, X + r, Y + r, outline="gray", fill="black")

    routes = []

    used_points = [False] * n_points

    while len(routes) < n_routes:
        rnd_nums = [int(random.randrange(0, n_points - 1)), int(random.randrange(0, n_points - 1))]

        for num in rnd_nums:
            used_points[num] = True

        point_from = points[rnd_nums[0]]
        point_to = points[rnd_nums[1]]
        speed_route = int(random.randrange(float(E3.get()), float(E4.get())))

        all_points_used = True
        for is_used in used_points:
            if is_used == False:
                all_points_used = False

        print(used_points)

        if point_from != point_to and (all_points_used != True and (used_points[rnd_nums[0]] != True and used_points[rnd_nums[1]] != True)):
            route = [[point_from, point_to], speed_route]

            canvas.create_line(point_from[0], point_from[1], point_to[0], point_to[1], arrow=LAST)

            routes.append(route)

    canvas.pack(side = RIGHT)

top = Tk()

f_menu=Frame(top)
f_menu.pack(side = LEFT)

L1= Label(f_menu, text="Points:")
L1.pack()
E1= Entry(f_menu, bd = 5)
E1.insert(0,"10")
E1.pack()

L2= Label(f_menu, text="Paths:")
L2.pack()
E2= Entry(f_menu, bd = 5)
E2.insert(0,"15")
E2.pack()

L3= Label(f_menu, text="Vmin:")
L3.pack()
E3= Entry(f_menu, bd = 5)
E3.insert(0,"5")
E3.pack()

L4= Label(f_menu, text="Vmax:")
L4.pack()
E4= Entry(f_menu, bd = 5)
E4.insert(0,"120")
E4.pack()

L5= Label(f_menu, text="Ymin:")
L5.pack()
E5= Entry(f_menu, bd = 5)
E5.insert(0,"0")
E5.pack()

L6= Label(f_menu, text="Ymax:")
L6.pack()
E6= Entry(f_menu, bd = 5)
E6.insert(0,"600")
E6.pack()

L7= Label(f_menu, text="Xmin:")
L7.pack()
E7= Entry(f_menu, bd = 5)
E7.insert(0,"0")
E7.pack()

L8= Label(f_menu, text="Xmax:")
L8.pack()
E8= Entry(f_menu, bd = 5)
E8.insert(0,"400")
E8.pack()

B1=Button(f_menu, text = "Map Generation", command=drawMap)
B1.pack()

B2=Button(f_menu, text = "Save map")
B2.pack()

B3=Button(f_menu, text = "Delete map", command = delMap)
B3.pack()

top.mainloop()
