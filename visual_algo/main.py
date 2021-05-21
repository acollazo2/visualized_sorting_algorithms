import random
import tkinter
from tkinter import ttk
from algorithms import *

#Variables
WIDTH = 800
HEIGHT = 500
sort_speed = 0.05
number_of_rectangles = 25
list = []


#Setup
root = tkinter.Tk()
root.title("Visualizing Sorting Algorithms")

UI_frame = tkinter.Frame(root, width=WIDTH, height=HEIGHT)
UI_frame.grid(row=0, column=0)

canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
canvas.grid(row=1, column=0)



#Label
tkinter.Label(UI_frame, text='Algorithm: ').grid(row=0, column=0)


#Generate button
def drawArray(array, colors):
    canvas.delete('all')
    canvas_height = HEIGHT
    canvas_width = WIDTH
    x_width = canvas_width/(len(array)+1)
    spacing = 5
    for i, height in enumerate(array):
        x0 = i * x_width + spacing
        y0 = canvas_height - height

        x1 = (i + 1) * x_width
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1, fill=colors[i])
    root.update_idletasks()
        
def generate():
    global list
    list = []
    for i in range(number_of_rectangles):
        list.append(random.randint(10,400))
    drawArray(list, ['blue' for x in range(len(list))])

tkinter.Button(UI_frame, text='Generate List',command=generate).grid(row=0, column=2)


#Start Button
def start_sorting():
    global list

    if algo_dropdown.get() == 'Bubble Sort':
        bubbleSort(list, drawArray, sort_speed)

tkinter.Button(UI_frame, text='Sort',command=start_sorting).grid(row=0,column=3)


#Dropdown menu
algo_dropdown = ttk.Combobox(UI_frame, values = ['Bubble Sort'])
algo_dropdown.grid(row=0, column=1)
algo_dropdown.current(0)


#Main
root.mainloop()