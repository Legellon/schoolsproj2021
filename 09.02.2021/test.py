from tkinter import *
import math
import random

def delMap():
    x = 0

def drawMap():
    W = float(E6.get()) - float(E5.get())
    H = float(E8.get()) - float(E7.get())

    canvas = Canvas(top, width=int(W+40), height=int(H+40))

    n_points = int(E1.get()) if int(E1.get()) > 2 else 3
    n_routes = int(E2.get()) if int(E2.get()) > n_points - 1 else n_points - 1

    if n_routes > n_points and n_routes > n_points * (n_points - 1):
        n_routes = n_points * (n_points - 1)

    points = []

    while len(points) < n_points:
        X = int(random.randrange(float(E5.get()), float(E6.get())))
        Y = int(random.randrange(float(E7.get()), float(E8.get())))

        point = {'X': X, 'Y': Y}
        points.append(point)

        r = 5
        canvas.create_oval(X - r, Y - r, X + r, Y + r, outline="gray", fill="black")

    routes = []

    used_points = [False] * len(points)


    while len(routes) < n_routes:
        p_route_from_to = [None, None]
        speed_newRoute = int(random.randrange(float(E3.get()), float(E4.get())))

        print(len(routes))
        print(used_points)

        if used_points.count(True) != len(points):

            if used_points.count(False) == 1:
                p_route_from_to[0] = points[random.randrange(0, len(points)-1)]

            for newPointIndex in range(p_route_from_to.index(None), 2):
                p_route_from_to[newPointIndex] = points[used_points.index(False)]
                used_points[used_points.index(False)] = True
        else:
            p_route_from_to[0] = points[random.randrange(0, len(points)-1)]
            p_route_from_to[1] = points[random.randrange(0, len(points)-1)]

        newRoute = [[p_route_from_to[0], p_route_from_to[1]], speed_newRoute]

        check_copy_routes = False
        if p_route_from_to[0] == p_route_from_to[1]:
            continue
        elif len(routes) > 0:
            for route in routes:
                if route[0] == newRoute[0]:
                    print(route)
                    print(newRoute)
                    check_copy_routes = True
                    break
        if check_copy_routes:
            continue

        routes.append(newRoute)

        canvas.create_line(newRoute[0][0]['X'], newRoute[0][0]['Y'], newRoute[0][1]['X'], newRoute[0][1]['Y'], arrow=LAST)

    print(len(points))
    print(len(routes))
    for i in range(len(routes)):
        route = routes[i]
        for j in range(len(routes)):
            if i == j:
                continue
            else:
                if(route[0] == routes[j][0]):
                    print(1)

    canvas.pack(side = RIGHT)

top = Tk()

f_menu=Frame(top)
f_menu.pack(side = LEFT)

L1= Label(f_menu, text="Points:")
L1.pack()
E1= Entry(f_menu, bd = 5)
E1.insert(0,"10")
E1.pack()

L2= Label(f_menu, text="routes:")
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

f_menu

top.mainloop()
