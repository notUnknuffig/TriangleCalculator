import math
import os
import tkinter as tk
import customtkinter as ctk


def draw_pythagoras(a: float, b: float, c: float):
    global t_canvas, canvas_height, canvas_width
    
    cath_1: float
    cath_2: float

    #Normalize
    if a > b and a > c:
        max_side = a
        cath_1 = b
        cath_2 = c
    elif b > a and b > c:
        max_side = b
        cath_1 = a
        cath_2 = c
    elif c > a and c > b:
        max_side = c
        cath_1 = a
        cath_2 = b

    min_side: float = 0

    lengths = []
    for length in [cath_1, cath_2, max_side]:
        length = (length - min_side)/(max_side - min_side)
        lengths.append(length)

    size: float = 0.8

    can_relativ_width: float = canvas_width * 0.5 - 0.5 * canvas_width * lengths[0] * size
    can_relativ_height: float = canvas_height * 0.5 + 0.5 * canvas_height * lengths[1] * size

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
                         text= round(max_side,2), font=('Arial', 11))
    
    t_canvas.pack(pady=10,padx=10)

def draw_cosins(a: float, b: float, c: float, angle: float):
    global t_canvas, canvas_height, canvas_width
    
    #Normalize
    if a > b and a > c:
        max_side = a
    elif b > a and b > c:
        max_side = b
    elif c > a and c > b:
        max_side = c
    else:
        max_side = a

    min_side: float = 0

    lengths = []
    for length in [a, b, c]:
        length = (length - min_side)/(max_side - min_side)
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

def draw_3s(a: float, b: float, c: float, alpha: float, beta: float, gamma: float):
    global t_canvas, canvas_height, canvas_width
    
    sorted_lengths = [a]

    for length in [b,c]:
        if length <= sorted_lengths[0]:
            sorted_lengths.append(length)
        else:
            sorted_lengths.insert(0, length)

    max_side = sorted_lengths[0]

    sorted_angles = [alpha]

    for angle in [beta,gamma]:
        if angle <= sorted_angles[0]:
            sorted_angles.append(angle)
        else:
            sorted_angles.insert(0, angle)

    angle = sorted_angles[2]

    min_side = 0

    lengths = []
    for length in sorted_lengths:
        length = (length - min_side)/(max_side - min_side)
        lengths.append(length)

    size = 0.8

    can_relativ_width: float
    can_relativ_height: float

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

def draw_AllSides(a: float, b: float, c: float, alpha: float, beta: float, gamma: float):
    global t_canvas, canvas_height, canvas_width
    
    angles = [beta,gamma,alpha]
    angle = alpha

    max_side: float = 0
    min_side: float = 0

    if a > b and a > c:
        max_side = a
    elif b > a and b > c:
        max_side = b
    elif c > a and c > b:
        max_side = c
    else:
        max_side = a


    unit_lengths = [c,a,b]
    lengths = []
    for length in [c, a, b]:
        length = (length - min_side)/(max_side - min_side)
        lengths.append(length)

    size = 0.8

    can_relativ_width = canvas_width * 0.5 - 0.5 * canvas_width * lengths[0] * size
    can_relativ_height = canvas_height * 0.5 + 0.5 * canvas_height * lengths[1] * math.sin(angles[0]) * size

    t_canvas.delete("all")

    t_canvas.create_line(can_relativ_width,
                         can_relativ_height,
                         can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         fill = "green")
    
    t_canvas.create_text(can_relativ_width + 0.5 * canvas_width * lengths[0] * size,
                         can_relativ_height,
                         text= round(unit_lengths[0] ,2), font=('Arial', 9))
    
    t_canvas.create_arc(can_relativ_width + canvas_width * lengths[0] * size - 30,
                         can_relativ_height + 30,
                         can_relativ_width + canvas_width * lengths[0] * size + 30,
                         can_relativ_height - 30,
                        start=180,
                        extent=-angles[2],
                        outline = "red")
    
    t_canvas.create_text(can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         text= f"{round(angles[2] ,2)}°", font=('Arial', 11))
    
    t_canvas.create_line(can_relativ_width + canvas_width * lengths[0] * size,
                         can_relativ_height,
                         can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         fill = "green")
    
    t_canvas.create_text(can_relativ_width + canvas_width * lengths[0] * size + 0.5 * canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - 0.5 * canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         text= round(unit_lengths[1] ,2), font=('Arial', 9))
    
    t_canvas.create_arc(can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size + 30,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size - 30,
                         can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size - 30,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size + 30,
                        start=-angle,
                        extent=-angles[0],
                        outline = "red")
    
    t_canvas.create_text(can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         text= f"{round(angles[0] ,2)}°", font=('Arial', 11))
    
    t_canvas.create_line(can_relativ_width + canvas_width * lengths[0] * size + canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         can_relativ_width,
                         can_relativ_height,
                         fill = "green")
    
    t_canvas.create_text(can_relativ_width + 0.5 * canvas_width * lengths[0] * size + 0.5 * canvas_width * lengths[1] * math.sin((angle - 90) * (math.pi/180)) * size,
                         can_relativ_height - 0.5 * canvas_height * lengths[1] * math.cos((angle - 90) * (math.pi/180)) * size,
                         text= round(unit_lengths[2] ,2), font=('Arial', 9))
    
    t_canvas.create_arc(can_relativ_width + 30,
                         can_relativ_height + 30,
                         can_relativ_width - 30,
                         can_relativ_height - 30,
                        start=0,
                        extent=angles[1],
                        outline = "red")
    
    t_canvas.create_text(can_relativ_width,
                         can_relativ_height,
                         text= f"{round(angles[1] ,2)}°", font=('Arial', 11))
    
    t_canvas.pack(pady=10,padx=10)

def clear():
    global t_canvas, result_text
    result_text.forget()
    t_canvas.delete("all")
    t_canvas.pack_forget()

def calc():
    global result_text
    global current, calcCath, trig_func
    global textbox_1, textbox_2, textbox_3, cathCheck, trig_func, t_canvas
    current_equation = current.get()

    value_1 = 0
    value_2 = 0
    value_3 = 0
    values = []
    strings = []
    unit = {"mm":1000, "cm":100, "dm":100, "m":1, "km":0.001}

    try:
        strings = [textbox_1.get(), textbox_2.get(), textbox_3.get()]
        values = []
        for string in strings:
            if string[-1] == "²":
                value = float(string[:-1])
                value = math.sqrt(value)
            elif string[-2:] in unit:
                value = value * unit[string[-2:]]
                value = float(string[:-2])
            else:
                  value = float(string)
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

        result_text.configure(text=f"The searched for side c is {str(result)} long.")
        result_text.pack()
        draw_pythagoras(values[0], values[1], result)
    elif current_equation == "Law of Cosin":
        value_1 = values[0]
        value_2 = values[1]
        value_3 = values[2]

        result = round(math.sqrt(value_1**2 + value_2**2 - 2 * value_1 * value_2 * math.cos(value_3 * (math.pi / 180))), 2)

        result_text.configure(text=f"The searched for side c is {str(result)} long.")
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

            result_text.configure(text=f"The searched angles are A = {str(result_array[0])}°, B = {str(result_array[1])}°, C = {str(result_array[2])}°.")
            result_text.pack()

            draw_3s(values[0], values[1], values[2], result_array[0], result_array[1], result_array[2])
        except:
            clear()
            result_text.configure(text=f"Math error: Sides of Triangle don't connect.")
            result_text.pack()
    elif current_equation == "Right Triangle":
        value_1 = values[0]
        value_2 = values[1]
        side_type = trig_func_var.get()

        if side_type == "Adjacent":
            adjacent = value_1
            opposite = value_1 * math.tan(value_2 * (math.pi / 180))
            hypothenuse = value_1 / math.cos(value_2 * (math.pi / 180))

        elif side_type == "Opposite":
            adjacent = value_1 / math.tan(value_2 * (math.pi / 180))
            opposite = value_1
            hypothenuse = value_1 / math.sin(value_2 * (math.pi / 180))

        elif side_type == "Hypothenuse":
            adjacent = value_1 * math.cos(value_2 * (math.pi / 180))
            opposite = value_1 * math.sin(value_2 * (math.pi / 180))
            hypothenuse = value_1
        
        area = adjacent * opposite * 0.5

        alpha = value_2
        beta = 90.0
        gamma = 90 - alpha

        result_text.configure(text=f"""
The searched sides are: 
Adjacent: {round(adjacent, 3)}, Opposite: {round(opposite, 3)}, Hypothenuse: {round(hypothenuse, 3)}.

The searched angles are: 
Alpha: {round(alpha, 3)}, Beta: {round(beta, 3)}, Gamma: {round(gamma, 3)}.

The Circumference is {round(adjacent + opposite + hypothenuse, 3)}.
The Area is {round(area, 3)}
        """)
        result_text.pack()

        draw_AllSides(adjacent, opposite, hypothenuse, alpha, beta, gamma)

def dropdownChange(current):
    global input_text_1, input_text_2, input_text_3, textbox_1, textbox_2, textbox_3, t_canvas

    textbox_1.delete(0, -1)
    textbox_2.delete(0, -1)
    textbox_3.delete(0, -1)

    if current == "Pythagoras":
        input_text_1.configure(text="Length of side a:")
        input_text_1.grid(row=0, column= 0)
        textbox_1.grid(row=0, column= 1)

        input_text_2.configure(text="Length of side b:")
        input_text_2.grid(row=1, column= 0)
        textbox_2.grid(row=1, column= 1)

        cathCheck.grid(row=2, column= 1)

        input_text_3.grid_forget()
        textbox_3.grid_forget()

        trig_func.grid_forget()

    elif current == "Three Sides":
        input_text_1.configure(text="Length of side a:")
        input_text_1.grid(row=0, column= 0)
        textbox_1.grid(row=0, column= 1)


        input_text_2.configure(text="Length of side b:")
        input_text_2.grid(row=1, column= 0)
        textbox_2.grid(row=1, column= 1)

        input_text_3.configure(text="Length of side c:")
        input_text_3.grid(row=2, column= 0)
        textbox_3.delete(0, tk.END)
        textbox_3.grid(row=2, column= 1)

        cathCheck.grid_forget()
        trig_func.grid_forget()

    elif current == "Law of Cosin":
        input_text_1.configure(text="Length of side a:")
        input_text_1.grid(row=0, column= 0)
        textbox_1.grid(row=0, column= 1)

        input_text_2.configure(text="Length of side b:")
        input_text_2.grid(row=1, column= 0)
        textbox_2.grid(row=1, column= 1)

        input_text_3.configure(text="Angle between side a and b:")
        input_text_3.grid(row=2, column= 0)
        textbox_3.delete(0, tk.END)
        textbox_3.grid(row=2, column= 1)

        cathCheck.grid_forget()
        trig_func.grid_forget()
    
    elif current == "Right Triangle":
        input_text_1.configure(text="Length of side a:")
        input_text_1.grid(row=0, column= 0)
        textbox_1.grid(row=0, column= 1)

        input_text_2.configure(text="Angel between side two sides:")
        input_text_2.grid(row=1, column= 0)
        textbox_2.grid(row=1, column= 1)

        input_text_3.configure(text="Type of Side relativ to the angle:")
        input_text_3.grid(row=2, column= 0)
        textbox_3.grid_forget()

        trig_func.grid(row=2, column= 1)
        cathCheck.grid_forget()
    
    call_update()
      #Culprit

def call_update(*args):
    global current
    global textbox_1, textbox_2, textbox_3, trig_func_var
    match current.get():
        case "Pythagoras":
            if textbox_1.get() != "" and textbox_2.get():
                calc()
            else:
                clear()
        case "Right Triangle":
            if textbox_1.get() != "" and textbox_2.get() and trig_func_var.get() != "Side Name":
                calc()
            else:
                clear()
        case "Three Sides":
            if textbox_1.get() != "" and textbox_2.get() and textbox_3.get():
                calc()
            else:
                clear()
        case "Law of Cosin":
            if textbox_1.get() != "" and textbox_2.get() and textbox_3.get():
                calc()
            else:
                clear()

if __name__ == "__main__":
    equations = ["Pythagoras", "Right Triangle", "Law of Cosin", "Three Sides"]
    array_trig_func = ["Adjacent","Opposite","Hypothenuse"]

    bg_color: tuple = "#f0f0f0", "#0f0f0f"
    text_color: tuple = "#000000", "#ffffff"
    fg_hover_color: tuple = "#fff0fa", "#b51b8c"
    fg_color: tuple = "#fffaff", "#b50b8f"
    ac_color: tuple = "#ffade9", "#eb0caf"

    ctk.set_appearance_mode("light")

    window = ctk.CTk()    #Setup root
    window.minsize(width=500, height=300)
    window.title('Triangle Calculator')
    try:
        os.getcwd()
        window.iconbitmap(r"TrigIcon.ico")
    except:
        print("Triangle Calc: Error_01 No Icon Found")
    window.resizable(width=True, height=True)

    #label = tk.Label(window, text="Simple Calculator for Triangles.", font=('Arial', 14))
    #label.pack(padx=20, pady=20)

    current = ctk.StringVar()
    current.set("Calculation..")

    dropdown = ctk.CTkOptionMenu(master=window, 
                                command=dropdownChange,
                                variable=current,
                                values=equations
                                )
    dropdown.pack(padx=10, pady=10)

    input_frame = ctk.CTkFrame(window)
    input_frame.pack(pady=10, padx=10)
    input_frame.columnconfigure(0, weight=1)
    input_frame.columnconfigure(1, weight=1)

    #textvar_1 = tk.StringVar()
    #textvar_1.trace_add("write", lambda name, index, mode, var:textvar_1: call_update(var))
    textbox_1 = ctk.CTkEntry(master=input_frame, font=('Arial',12), corner_radius=5)
    textbox_1.bind("<KeyRelease>", call_update)

    #textvar_2 = tk.StringVar()
    #textvar_2.trace_add("write", call_update)
    textbox_2 = ctk.CTkEntry(master=input_frame, font=('Arial',12), corner_radius=5)
    textbox_2.bind("<KeyRelease>", call_update)

    #textvar_3 = tk.StringVar()
    #textvar_3.trace_add("write", call_update)
    textbox_3 = ctk.CTkEntry(master=input_frame, font=('Arial',12), corner_radius=5)
    textbox_3.bind("<KeyRelease>", call_update)

    input_text_1 = ctk.CTkLabel(input_frame, text="Length of side a:", font=('Arial', 11))

    input_text_2 = ctk.CTkLabel(input_frame, text="Length of side b:", font=('Arial', 11))

    input_text_3 = ctk.CTkLabel(input_frame, text="Length of side c:", font=('Arial', 11))

    calcCath = ctk.IntVar()
    calcCath.trace_add("write", call_update)
    cathCheck = ctk.CTkCheckBox(master=input_frame, text='Calculate Cathetus',variable=calcCath, onvalue=1, offvalue=0)

    trig_func_var = ctk.StringVar()
    trig_func_var.trace_add("write", call_update)
    trig_func_var.set("Side Name")
    trig_func = ctk.CTkOptionMenu(master=input_frame, values=array_trig_func)

    #button = ctk.CTkButton(window, text="Calculate", font=('Arial',12), command=calc)
    #button.pack(padx=10, p74ady=10)

    result_text = tk.Label(window, text="", font=('Arial', 11))

    t_canvas = ctk.CTkCanvas(window, width=300, height=300, bg="white")

    canvas_width = 300
    canvas_height = 300

    window.mainloop()