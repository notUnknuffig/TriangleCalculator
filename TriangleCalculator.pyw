import sys                  #imports
import math
import tkinter as tk


def draw_pythagoras(a, b, c, angle):
    global t_canvas, canvas_height, canvas_width
    
    #Normalize
    if a > b and a > c:
        max = a
        cath_1 =b
        cath_2 =c
    elif b > a and b > c:
        max = b
        cath_1 = a
        cath_2 = c
    elif c > a and c > b:
        max = c
        cath_1 = a
        cath_2 = b

    min = 0

    lengths = []
    for length in [cath_1, cath_2, max]:
        length = (length - min)/(max - min)
        lengths.append(length)

    size = 0.8

    can_relativ_width = canvas_width * 0.5 - 0.5 * canvas_width * lengths[0] * size
    can_relativ_height = canvas_height * 0.5 + 0.5 * canvas_height * lengths[1] * size

    t_canvas.delete("all")

    t_canvas.create_line(can_relativ_width,
                         can_relativ_height,
                         can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         fill= "green")
    
    t_canvas.create_text(can_relativ_width + 0.5 * canvas_width * lengths[0] * size,
                         can_relativ_height,
                         text= round(cath_1 ,2), font=('Arial', 11))
    
    t_canvas.create_line(can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height - canvas_height * lengths[1] * size,
                         fill="green")
    
    t_canvas.create_text(can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height - 0.5 * canvas_height * lengths[1] * size,
                         text= round(cath_2,2), font=('Arial', 11))
    
    t_canvas.create_line(can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height - canvas_height * lengths[1] * size,
                         can_relativ_width,
                         can_relativ_height,
                         fill="red")
    
    t_canvas.create_text(can_relativ_width + 0.5 * canvas_width * lengths[0] * size,
                         can_relativ_height -  0.5 * canvas_height * lengths[1] * size,
                         text= round(max,2), font=('Arial', 11))
    
    t_canvas.pack(pady=10,padx=10)


def draw_cosins(a, b, c, angle):
    global t_canvas, canvas_height, canvas_width
    
    #Normalize
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c
    else:
        max = a

    min = 0

    lengths = []
    for length in [a, b, c]:
        length = (length - min)/(max - min)
        lengths.append(length)

    size = 0.8

    if angle > 90:
        can_relativ_width = canvas_width * 0.5 - 0.5 * canvas_width * lengths[0] * size - 0.5 * canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size
        can_relativ_height = canvas_height * 0.5 + 0.5 * canvas_height * lengths[1] * size
    else:
        can_relativ_width = canvas_width * 0.5 - 0.5 * canvas_width * lengths[0] * size
        can_relativ_height = canvas_height * 0.5 + 0.5 * canvas_height * lengths[1] * size

    t_canvas.delete("all")

    t_canvas.create_line(can_relativ_width,
                         can_relativ_height,
                         can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         fill = "green")
    
    t_canvas.create_text(can_relativ_width + 0.5 * canvas_width * lengths[0] * size,
                         can_relativ_height,
                         text= round(a ,2), font=('Arial', 11))
    
    t_canvas.create_arc(can_relativ_width + canvas_width * lengths[0] * size-30,
                         can_relativ_height-30,
                         can_relativ_width + canvas_width * lengths[0] * size+30,
                         can_relativ_height+30,
                        start=180,
                        extent=-angle,
                        outline = "green")
    
    t_canvas.create_text(can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         text= f"{round(angle ,2)}°", font=('Arial', 9))
    
    t_canvas.create_line(can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         fill = "green")
    
    t_canvas.create_text(can_relativ_width + canvas_width * lengths[0] * size + 0.5 * canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - 0.5 * canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         text= round(b ,2), font=('Arial', 11))
    
    t_canvas.create_line(can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         can_relativ_width,
                         can_relativ_height,
                         fill = "red")
    
    t_canvas.create_text(can_relativ_width + 0.5 * canvas_width * lengths[0] * size + 0.5 * canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - 0.5 * canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         text= round(c ,2), font=('Arial', 11))
    
    t_canvas.pack(pady=10,padx=10)


def draw_3s(a, b, c, A, B, C):
    global t_canvas, canvas_height, canvas_width
    
    sorted_lengths = [a]

    for length in [b,c]:
        if length <= sorted_lengths[0]:
            sorted_lengths.append(length)
        else:
            sorted_lengths.insert(0, length)

    max = sorted_lengths[0]

    sorted_angles = [A]

    for angle in [B,C]:
        if angle <= sorted_angles[0]:
            sorted_angles.append(angle)
        else:
            sorted_angles.insert(0, angle)

    angle = sorted_angles[2]

    min = 0

    lengths = []
    for length in sorted_lengths:
        length = (length - min)/(max - min)
        lengths.append(length)

    size = 0.8

    if angle > 90:
        can_relativ_width = canvas_width * 0.5 - 0.5 * canvas_width * lengths[0] * size - 0.5 * canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size
        can_relativ_height = canvas_height * 0.5 + 0.5 * canvas_height * lengths[1] * size
    else:
        can_relativ_width = canvas_width * 0.5 - 0.5 * canvas_width * lengths[0] * size
        can_relativ_height = canvas_height * 0.5 + 0.5 * canvas_height * lengths[1] * size

    t_canvas.delete("all")

    t_canvas.create_line(can_relativ_width,
                         can_relativ_height,
                         can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         fill = "green")
    
    t_canvas.create_text(can_relativ_width + 0.5 * canvas_width * lengths[0] * size,
                         can_relativ_height,
                         text= round(sorted_lengths[0] ,2), font=('Arial', 9))
    
    t_canvas.create_arc(can_relativ_width + canvas_width * lengths[0] * size - 30,
                         can_relativ_height + 30,
                         can_relativ_width + canvas_width * lengths[0] * size + 30,
                         can_relativ_height - 30,
                        start=180,
                        extent=-sorted_angles[2],
                        outline = "red")
    
    t_canvas.create_text(can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         text= f"{round(sorted_angles[2] ,2)}°", font=('Arial', 11))
    
    t_canvas.create_line(can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         fill = "green")
    
    t_canvas.create_text(can_relativ_width + canvas_width * lengths[0] * size + 0.5 * canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - 0.5 * canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         text= round(sorted_lengths[1] ,2), font=('Arial', 9))
    
    t_canvas.create_arc(can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size + 30,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size - 30,
                         can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size - 30,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size + 30,
                        start=-angle,
                        extent=-sorted_angles[0],
                        outline = "red")
    
    t_canvas.create_text(can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         text= f"{round(sorted_angles[0] ,2)}°", font=('Arial', 11))
    
    t_canvas.create_line(can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         can_relativ_width,
                         can_relativ_height,
                         fill = "green")
    
    t_canvas.create_text(can_relativ_width + 0.5 * canvas_width * lengths[0] * size + 0.5 * canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - 0.5 * canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         text= round(sorted_lengths[2] ,2), font=('Arial', 9))
    
    t_canvas.create_arc(can_relativ_width + 30,
                         can_relativ_height + 30,
                         can_relativ_width - 30,
                         can_relativ_height - 30,
                        start=0,
                        extent=sorted_angles[1],
                        outline = "red")
    
    t_canvas.create_text(can_relativ_width,
                         can_relativ_height,
                         text= f"{round(sorted_angles[1] ,2)}°", font=('Arial', 11))
    
    t_canvas.pack(pady=10,padx=10)


def clear():
    global t_canvas
    t_canvas.delete("all")
    t_canvas.pack_forget()

def calc():
    global result_text
    global current, calcCath
    global textbox_1, textbox_2, textbox_3, cathCheck, t_canvas
    current_equation = current.get()

    value_1 = 0
    value_2 = 0
    value_3 = 0
    values = []
    strings = []
    unite = {"mm":1000, "cm":100, "dm":100, "m":1, "km":0.001}

    try:
        strings = [textbox_1.get().split(), textbox_2.get().split(), textbox_3.get().split()]
        values = []
        for string in strings:
            if len(string) >= 1:
                value = float(string[0])
            else:
                value = 0
            if len(string) >= 2:
                if string[1][-1] == "²":
                    value = math.sqrt(value)
                #if string[1][:-1] in unite:
                    #value = value * unite[string[1][:-1]]
                
            values.append(value)
    except:
        pass

    if current_equation == "Pythagoras":
        if calcCath.get() == False:
            value_1 = math.pow(values[0], 2)
            value_2 = math.pow(values[1], 2)
            result = value_1 + value_2
            result = round(math.sqrt(result),2)
        else:
            if values[0] > values[1]:
                value_1 = math.pow(values[0], 2)
                value_2 = math.pow(values[1], 2)
                result = value_1 - value_2
                result = round(math.sqrt(result),2)
            else:
                value_1 = math.pow(values[0], 2)
                value_2 = math.pow(values[1], 2)
                result = value_2 - value_1
                result = round(math.sqrt(result),2)

        result_text.config(text=f"The searched for side c is {str(result)} long.")
        result_text.pack()
        draw_pythagoras(values[0], values[1], result, 90)
    elif current_equation == "Law of Cosin":
        value_1 = values[0]
        value_2 = values[1]
        value_3 = values[2]

        result = round(math.sqrt(value_1**2 + value_2**2 - 2 * value_1 * value_2 * math.cos(value_3 * (math.pi / 180))), 2)

        result_text.config(text=f"The searched for side c is {str(result)} long.")
        result_text.pack()

        draw_cosins(values[0], values[1], result, values[2])
    elif current_equation == "Three Sides":
        result_array = [0, 0, 0]

        value_1 = values[0]
        value_2 = values[1]
        value_3 = values[2]

        try:
            result_array[0] = round(math.degrees(math.acos((value_2**2 + value_3**2 - value_1**2) / (2 * value_2 * value_3))),2)

            result_array[1] = round(math.degrees(math.acos((value_1**2 + value_3**2 - value_2**2) / (2 * value_1 * value_3))),2)

            result_array[2] = round(180 - result_array[0] - result_array[1] ,2)

            result_text.config(text=f"The searched angles are A = {str(result_array[0])}°, B = {str(result_array[1])}°, C = {str(result_array[2])}°.")
            result_text.pack()

            draw_3s(values[0], values[1], values[2], result_array[0], result_array[1], result_array[2])
        except:
            clear()
            result_text.config(text=f"Math error: Sides of Triangle don't connect.")
            result_text.pack()



def dropdownChange(*args):
    global current
    global input_text_1, input_text_2, input_text_3, textbox_1, textbox_2, textbox_3, t_canvas
    print(current.get())

    textbox_1.config(text="")
    textbox_2.config(text="")
    textbox_3.config(text="")

    if current.get() == "Pythagoras":
        input_text_1.config(text="Length of Side a:")
        input_text_1.grid(row=0, column= 0)
        textbox_1.grid(row=0, column= 1)

        input_text_2.config(text="Length of Side b:")
        input_text_2.grid(row=1, column= 0)
        textbox_2.grid(row=1, column= 1)

        cathCheck.grid(row=2, column= 1)

        input_text_3.grid_forget()
        textbox_3.grid_forget()

    elif current.get() == "Three Sides":
        input_text_1.config(text="Length of Side a:")
        input_text_1.grid(row=0, column= 0)
        textbox_1.grid(row=0, column= 1)


        input_text_2.config(text="Length of Side b:")
        input_text_2.grid(row=1, column= 0)
        textbox_2.grid(row=1, column= 1)

        input_text_3.config(text="Length of Side c:")
        input_text_3.grid(row=2, column= 0)
        textbox_3.delete(0, tk.END)
        textbox_3.grid(row=2, column= 1)

        cathCheck.grid_forget()

    elif current.get() == "Law of Cosin":
        input_text_1.config(text="Length of Side a:")
        input_text_1.grid(row=0, column= 0)
        textbox_1.grid(row=0, column= 1)

        input_text_2.config(text="Length of Side b:")
        input_text_2.grid(row=1, column= 0)
        textbox_2.grid(row=1, column= 1)

        input_text_3.config(text="Angle between side a and b:")
        input_text_3.grid(row=2, column= 0)
        textbox_3.delete(0, tk.END)
        textbox_3.grid(row=2, column= 1)

        cathCheck.grid_forget()
        
 
equations = ["Pythagoras", "Law of Cosin", "Three Sides"]

window= tk.Tk()      #Setup root
window.minsize(width=500, height=300)
window.title('Triangle Calculator')
try:
    window.iconbitmap(r"C:\Users\User\Desktop\textures\math.ico")
except:
    print("Triangle Calc: Error_01 No Icon Found")
window.resizable(width=True, height=True)

label = tk.Label(window, text="Simple Calculator for Triangles.", font=('Arial', 14))
label.pack(padx=20, pady=20)

current = tk.StringVar()
current.set("Choose Equation...")
current.trace("w", dropdownChange)

dropdown = tk.OptionMenu(window, current, *equations)
dropdown.pack()

input_frame = tk.Frame(window)
input_frame.pack(pady=10, padx=10)
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

textbox_1 = tk.Entry(input_frame, font=('Arial',12))

textbox_2 = tk.Entry(input_frame, font=('Arial',12))

textbox_3 = tk.Entry(input_frame, font=('Arial',12))

input_text_1 = tk.Label(input_frame, text="Length of side a:", font=('Arial', 11))

input_text_2 = tk.Label(input_frame, text="Length of side b:", font=('Arial', 11))

input_text_3 = tk.Label(input_frame, text="Length of side c:", font=('Arial', 11))

calcCath = tk.IntVar()
cathCheck = tk.Checkbutton(input_frame, text='Calculate Cathetus',variable=calcCath, onvalue=1, offvalue=0)

button = tk.Button(window, text="Calculate", font=('Arial',12), command=calc)
button.pack(padx=10, pady=10)

result_text = tk.Label(window, text="", font=('Arial', 11))

t_canvas = tk.Canvas(window, width=300, height=300, bg="white")

canvas_width = 300
canvas_height = 300


window.mainloop()         #Culprit
        
