#A GROUP 12 PRODUCTION
#Hannu Korhonen
#Petteri Piipponen
#Vladimir Gavrilov

import mysql.connector
import tkinter as tk
import math

#Dining hall puzzle
def dining_hall_puzzle():

    global highlighted_doll
    highlighted_doll = ""

    def solve_puzzle():
        for index in range(len(doll_array)):
            doll_object = doll_array[index]
            doll_x1 = canvas.coords(doll_object)[0]
            doll_y1 = canvas.coords(doll_object)[1]
            if (index == 0):
                #Bob Doll should be in chair 0
                chair_object = chair_array[0]
            elif (index == 1):
                #Karen Doll should be in chair 3
                chair_object = chair_array[3]
            elif (index == 2):
                #Martha Doll should be in chair 5
                chair_object = chair_array[5]
            elif (index == 3):
                #Susan Doll should be in chair 2
                chair_object = chair_array[2]
            elif (index == 4):
                #Tom Doll should be in chair 4
                chair_object = chair_array[4]
            else:
                #Timmy Doll should be in chair 1
                chair_object = chair_array[1]
            chair_x1 = canvas.coords(chair_object)[0]
            chair_y1 = canvas.coords(chair_object)[1]
            if ((doll_x1 == chair_x1) and (doll_y1 == chair_y1)):
                #Doll position correct, proceed to check next doll position
                #print(index,"doll is correct")
                pass
            else:
                #print(index,"doll is incorrect")
                return
        #Solution correct
        update_sql("UPDATE Item SET Available = True WHERE Item_ID = 8")
        print("I heard a metallic noise from under the table.")
        return
            
    def onClickDoll(event):
        global highlighted_doll
        object_found = False
        #Check which doll has been clicked
        object_list = canvas.find_overlapping(event.x, event.y, event.x, event.y)
        for obj in object_list:
            obj_tags = canvas.itemcget(obj, 'tags')
            if ('doll' in obj_tags):
                object_found = True
                doll_object = obj
                break
        if object_found == False: return
        this_doll = canvas.itemcget(doll_object, 'tags').split()[0]
        this_doll = this_doll.replace('doll_', '')
        #Check if a doll has been highlighted
        if (highlighted_doll != ""):
            if (highlighted_doll == this_doll):
                #If it is this doll, remove highlight
                canvas.itemconfigure(doll_object, outline='black', width=1)
                highlighted_doll = ""
            else:
                #Else highlight this doll
                canvas.itemconfigure(doll_object, outline='yellow', width=6)
                #Remove highlight from previous doll
                doll_object = doll_array[int(highlighted_doll)]
                canvas.itemconfigure(doll_object, outline='black', width=1)
                highlighted_doll = this_doll
        else:
            #Else highlight this doll
            canvas.itemconfigure(doll_object, outline='yellow', width=6)
            highlighted_doll = this_doll
        return

    def onClickBox(event):
        global highlighted_doll
        object_found = False
        #Check which chair has been clicked
        object_list = canvas.find_overlapping(event.x, event.y, event.x, event.y)
        for obj in object_list:
            obj_tags = canvas.itemcget(obj, 'tags')
            if (('chair' in obj_tags) or ('box' in obj_tags)):
                object_found = True
                chair_object = obj
                break
        if object_found == False: return
        #chair_object = canvas.find_closest(event.x, event.y)
        this_chair = canvas.itemcget(chair_object, 'tags').split()[0]
        this_chair = this_chair.replace('chair_', '')
        #If a doll has been highlighted
        if (highlighted_doll != ""):
            #Set a doll's position to this chair
            doll_object = doll_array[int(highlighted_doll)]
            label = doll_label[int(highlighted_doll)]
            #Doll position
            doll_x1 = canvas.coords(doll_object)[0]
            doll_y1 = canvas.coords(doll_object)[1]
            #Chair position
            chair_x1 = canvas.coords(chair_object)[0]
            chair_y1 = canvas.coords(chair_object)[1]
            #Move position
            move_direction_x = chair_x1 - doll_x1
            move_direction_y = chair_y1 - doll_y1
            canvas.move(doll_object, move_direction_x, move_direction_y)
            #Also move the corresponding label
            canvas.move(label, move_direction_x, move_direction_y)
            #Remove doll highlight
            canvas.itemconfigure(doll_object, outline='black', width=1)
            highlighted_doll = ""
        solve_puzzle()
        pass
    #Window variables
    window_width = 600
    window_height = 250
    window_start_x = 10
    window_start_y = 10
    window_end_x = window_width - window_start_x
    window_end_y = window_width - window_start_y

    doll_side = 40
    doll_array = []
    doll_label = []
    
    root = tk.Tk()
    canvas = tk.Canvas(root, width=window_width, height=window_height)
    canvas.grid()
    #Draw inventory boxes
    inventory_array = []
    inventory_array.append(canvas.create_rectangle(doll_side*0, 180, doll_side*1, 180+doll_side, fill="white", outline = 'black', tags=("0", "box")))
    inventory_array.append(canvas.create_rectangle(doll_side*1, 180, doll_side*2, 180+doll_side, fill="white", outline = 'black', tags=("1", "box")))
    inventory_array.append(canvas.create_rectangle(doll_side*2, 180, doll_side*3, 180+doll_side, fill="white", outline = 'black', tags=("2", "box")))
    inventory_array.append(canvas.create_rectangle(doll_side*3, 180, doll_side*4, 180+doll_side, fill="white", outline = 'black', tags=("3", "box")))
    inventory_array.append(canvas.create_rectangle(doll_side*4, 180, doll_side*5, 180+doll_side, fill="white", outline = 'black', tags=("4", "box")))
    inventory_array.append(canvas.create_rectangle(doll_side*5, 180, doll_side*6, 180+doll_side, fill="white", outline = 'black', tags=("5", "box")))
    #Draw dolls
    doll_array.append(canvas.create_rectangle(doll_side*0, 180, doll_side*1, 180+doll_side, fill="grey", outline = 'black', tags=("0", "doll")))
    doll_array.append(canvas.create_rectangle(doll_side*1, 180, doll_side*2, 180+doll_side, fill="grey", outline = 'black', tags=("1", "doll")))
    doll_array.append(canvas.create_rectangle(doll_side*2, 180, doll_side*3, 180+doll_side, fill="grey", outline = 'black', tags=("2", "doll")))
    doll_array.append(canvas.create_rectangle(doll_side*3, 180, doll_side*4, 180+doll_side, fill="grey", outline = 'black', tags=("3", "doll")))
    doll_array.append(canvas.create_rectangle(doll_side*4, 180, doll_side*5, 180+doll_side, fill="grey", outline = 'black', tags=("4", "doll")))
    doll_array.append(canvas.create_rectangle(doll_side*5, 180, doll_side*6, 180+doll_side, fill="grey", outline = 'black', tags=("5", "doll")))
    #Draw the table
    box = canvas.create_rectangle(window_start_x+60, window_start_y+55, window_start_x+190, window_start_y+105, fill="red", outline = 'black')
    #Draw chairs
    chair_array = []
    chair_array.append(canvas.create_rectangle(window_start_x+0, window_start_y+60, window_start_x+40, window_start_y+100, fill="red", outline = 'black', tags=("0", "chair")))
    chair_array.append(canvas.create_rectangle(window_start_x+60, window_start_y+0, window_start_x+100, window_start_y+40, fill="red", outline = 'black', tags=("1", "chair")))
    chair_array.append(canvas.create_rectangle(window_start_x+150, window_start_y+0, window_start_x+190, window_start_y+40, fill="red", outline = 'black', tags=("2", "chair")))
    chair_array.append(canvas.create_rectangle(window_start_x+210, window_start_y+60, window_start_x+250, window_start_y+100, fill="red", outline = 'black', tags=("3", "chair")))
    chair_array.append(canvas.create_rectangle(window_start_x+150, window_start_y+120, window_start_x+190, window_start_y+160, fill="red", outline = 'black', tags=("4", "chair")))
    chair_array.append(canvas.create_rectangle(window_start_x+60, window_start_y+120, window_start_x+100, window_start_y+160, fill="red", outline = 'black', tags=("5", "chair")))

    #Bind mouse click to chairs
    for chair in chair_array:
        canvas.tag_bind(chair, '<Button-1>', onClickBox)
    #Bind mouse click to inventory boxes
    for box in inventory_array:
        canvas.tag_bind(box, '<Button-1>', onClickBox)
    #Bind mouse click to dolls
    for doll in doll_array:
        canvas.tag_bind(doll, '<Button-1>', onClickDoll)
        canvas.tag_raise(doll) #Raise dolls above other objects
    #for label in doll_label:
        #canvas.tag_bind(label, '<Button-1>', onClickDoll)
        #label.tag_raise(label)

    #Labels
    doll_label.append(canvas.create_text((doll_side*0, 192), text="Bob", font=("Arial", 10), state='disabled', fill="white", anchor='w'))
    doll_label.append(canvas.create_text((doll_side*1, 192), text="Karen", font=("Arial", 10), state='disabled', fill="white", anchor='w'))
    doll_label.append(canvas.create_text((doll_side*2, 192), text="Martha", font=("Arial", 10), state='disabled', fill="white", anchor='w'))
    doll_label.append(canvas.create_text((doll_side*3, 192), text="Susan", font=("Arial", 10), state='disabled', fill="white", anchor='w'))
    doll_label.append(canvas.create_text((doll_side*4, 192), text="Tom", font=("Arial", 10), state='disabled', fill="white", anchor='w'))
    doll_label.append(canvas.create_text((doll_side*5, 192), text="Timmy", font=("Arial", 10), state='disabled', fill="white", anchor='w'))

    #Write puzzle instructions
    instruction_text = "1)Bob sits closest to the kitchen\n2)Karen refuses to sit next to her sister\n3)Tom sits next to her mother\n4)Susan sits next to Timmy\n5)Martha sits on the south side of the table\n6)Timmy likes to talk about cars"
    mylabel = canvas.create_text((450, 100), text=instruction_text, font=("Arial", 12), state="disabled")
    #mylabel.text.configure(state="disabled")
    
    canvas.pack()
    root.wm_title("Dining hall puzzle") #Window title
    root.call('wm', 'attributes', '.', '-topmost', '1') #Window always on top
    root.mainloop()

#Dartboard puzzle
def dartboard_puzzle():
   root = tk.Tk()
   #Dartboard variables
   circle_r = 160 #Radius
   circle_x0 = 30 #Starting X
   circle_y0 = 30 #Starting Y
   circle_x1 = circle_x0 + circle_r * 2 #Ending X
   circle_y1 = circle_y0 + circle_r * 2 #Ending Y
   #Dart variables
   dart_array = []
   global dart_number
   global dart_circle_array
   global dart_text_array
   dart_number = 1
   dart_circle_array = []
   dart_text_array = []
   #Puzzle variable
   global dart_value_array
   global solution_value_array
   dart_value_array = []
   solution_value_array = [9, 18, 25, 18, 26, 24]
   canvas = tk.Canvas(root, width=circle_x1+100, height=circle_y1+30, borderwidth=0, highlightthickness=0, bg="white")
   canvas.grid()
   #Attempt to solve the puzzle
   def solve_puzzle():
      global dart_value_array
      global solution_value_array
      solved = True
      for index in range(len(solution_value_array)):
         if (dart_value_array[index] != solution_value_array[index]):
            solved = False
      #Clear value array
      dart_value_array = []
      #Check if puzzle has already been solved
      if (solved == True):
         cur = select_sql("SELECT Available FROM Item WHERE Item_Id = 4")
         for row in cur.fetchall():
            if (row[0] == False):
               #Open safe and end the game
               update_sql("UPDATE Item SET Available = True WHERE Item_Id = 4")
               myprint("The dartboard slides open revealing an open safe. Inside the safe is I see a doll.")
      return
   #Remove dart circle and text objects from canvas
   def collect_darts():
      global dart_number
      global dart_circle_array
      global dart_text_array
      for dart_index in range(len(dart_circle_array)):
         #Delete object
         canvas.delete(dart_circle_array[-dart_index]) #Deletes the rectangle
         canvas.delete(dart_text_array[-dart_index]) #Deletes the text
      #Clear array
      dart_circle_array = []
      dart_text_array = []
      dart_number = 1
      return
   def _create_circle(self, x, y, r, **kwargs):
       return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
   tk.Canvas.create_circle = _create_circle
   def _create_circle_arc(self, x, y, r, **kwargs):
       if "start" in kwargs and "end" in kwargs:
           kwargs["extent"] = kwargs["end"] - kwargs["start"]
           del kwargs["end"]
       return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
   #Mouse click event
   def button(event):
      global dart_number
      global dart_value_array
      if (dart_number > 6):
         #Remove darts
         collect_darts()
      #Draw circle
      c = canvas.create_circle(event.x, event.y, 8, fill="yellow", outline="yellow")
      dart_circle_array.append(c)
      #Write dart number
      t = canvas.create_text(event.x, event.y, font="Arial", text=dart_number)    
      dart_text_array.append(t)
      dart_value = calculate_dart_points(event.x, event.y)
      print("You got ",dart_value,"points")
      #Add dart value to array
      dart_value_array.append(dart_value)
      dart_number = dart_number + 1
      #Try to solve puzzle if this was the sixth dart
      if (dart_number > 6):
         solved = solve_puzzle()
      return
    
   def calculate_dart_points(dart_x, dart_y):
       #Calculate dart distance from bullseye
       deltaX = circle_x0 + circle_r - dart_x;
       deltaY = circle_y0 + circle_r - dart_y;
       distance = ((deltaX)**2+(deltaY)**2)**(1/2)
       #Distance > circle radius
       if (distance>circle_r):
           points = 0 #Out of bounds
       elif (distance>=0 and distance <17): 
           points = 50 #Distance 0-17: 50 points
       elif (distance>=17 and distance<28):
           points = 25 #Distance 17-28: 25 points
       else:
           #Distance 28-94: 1x
           if (distance>=28 and distance<94):
               multiplier = 1
           #Distance 94-106: 3x
           elif (distance>=94 and distance<106):
               multiplier = 3
           #Distance 106-148: 1x
           elif (distance>=106 and distance<148):
               multiplier = 1
           #Distance 148-160: 2x
           elif (distance>=148 and distance<=160):
               multiplier = 2
           #Calculate dart radian value from the dartboard circle area
           rad = math.atan2(deltaY, deltaX)
           #Convert radian to degrees
           deg = round(math.degrees(rad),2)
           #Check which value for calculated degree
           if ((deg<=-171 and deg>=-180) or (deg<=180 and deg>=171)):
               value = 6
           elif (deg<171 and deg>=153):
               value = 13
           elif (deg<153 and deg>=135):
               value = 4
           elif (deg<135 and deg>=117):
               value = 18
           elif (deg<117 and deg>=99):
               value = 1
           elif (deg<99 and deg>=81):
               value = 20
           elif (deg<81 and deg>=63):
               value = 5
           elif (deg<63 and deg>=45):
               value = 12
           elif (deg<45 and deg>=27):
               value = 9
           elif (deg<27 and deg>=9):
               value = 14
           elif ((deg<9 and deg>=0) or (deg<=0 and deg>-9)):
               value = 11
           elif (deg<=-9 and deg>-27):
               value = 8
           elif (deg<=-27 and deg>-45):
               value = 16
           elif (deg<=-45 and deg>-63):
               value = 7
           elif (deg<=-63 and deg>-81):
               value = 19
           elif (deg<=-81 and deg>-99):
               value = 3
           elif (deg<=-99 and deg>-117):
               value = 17
           elif (deg<=-117 and deg>-135):
               value = 2
           elif (deg<=-135 and deg>-153):
               value = 15
           elif (deg<=-153 and deg>-171):
               value = 10
           else:
               value = 0
           points = multiplier * value
       return points
   tk.Canvas.create_circle_arc = _create_circle_arc
   #create_arc(x0, y0, x1, y1, option, ...)
   #(x0, y0) = upper left
   #(x1, x1) = bottom right
   #18 = 90/5 = one fifth of 90 degrees
   #9 = half of 18 = starting degree
   #start = starting degree
   #extent = width in degrees
   for index_sector in range(20):
       if (index_sector%2 == 0):
           multiplier_color = "red"
           single_color = "black"
       else:
           multiplier_color = "green"
           single_color = "white"
       #Double area
       canvas.create_arc(circle_x0, circle_y0, circle_x1, circle_y1, start=9 + index_sector * 18, 
           extent=18, outline="black", fill=multiplier_color, width=2)
       #Single area
       canvas.create_arc(circle_x0+12, circle_y0+12, circle_x1-12, circle_y1-12, start=9 + index_sector * 18, 
           extent=18, outline="black", fill=single_color, width=2)
       #Triple area
       canvas.create_arc(circle_x0+54, circle_y0+54, circle_x1-54, circle_y1-54, start=9 + index_sector * 18, 
           extent=18, outline="black", fill=multiplier_color, width=2)
       #Single area
       canvas.create_arc(circle_x0+66, circle_y0+66, circle_x1-66, circle_y1-66, start=9 + index_sector * 18, 
           extent=18, outline="black", fill=single_color, width=2)
   #Outer Bull
   canvas.create_circle(circle_x0 + circle_r, circle_y0 + circle_r, circle_r-132, fill="green", outline="black", width=1)
   #Bulls Eye
   canvas.create_circle(circle_x0 + circle_r, circle_y0 + circle_r, circle_r-143, fill="red", outline="black", width=1)
   #Sector values
   canvas.create_text(191, 18, font="Arial", text="20")
   canvas.create_text(136, 28, font="Arial", text="5")
   canvas.create_text(92, 48, font="Arial", text="12")
   canvas.create_text(53, 86, font="Arial", text="9")
   canvas.create_text(27, 136, font="Arial", text="14")
   canvas.create_text(19, 188, font="Arial", text="11")
   canvas.create_text(27, 239, font="Arial", text="8")
   canvas.create_text(48, 285, font="Arial", text="16")
   canvas.create_text(86, 326, font="Arial", text="7")
   canvas.create_text(133, 351, font="Arial", text="19")
   canvas.create_text(189, 361, font="Arial", text="3")
   canvas.create_text(245, 352, font="Arial", text="17")
   canvas.create_text(295, 328, font="Arial", text="2")
   canvas.create_text(329, 289, font="Arial", text="15")
   canvas.create_text(354, 245, font="Arial", text="10")
   canvas.create_text(360, 188, font="Arial", text="6")
   canvas.create_text(352, 133, font="Arial", text="13")
   canvas.create_text(322, 87, font="Arial", text="4")
   canvas.create_text(289, 46, font="Arial", text="18")
   canvas.create_text(246, 26, font="Arial", text="1")
   canvas.bind('<Button>',button) #Bind left click action
   root.wm_title("Dartboard puzzle") #Window title
   root.call('wm', 'attributes', '.', '-topmost', '1') #Window always on top
   root.mainloop()

def sudoku_puzzle():
   def solve_puzzle():
      index = 0
      for text_object in tex_field_array:
         #Find text field value
         value = canvas.itemcget(text_object, 'text')
         #Stop solving if even a single square is empty
         if (value == ' '):
            return
         else:
            #Stop solving if even a single square value is wrong
            if (int(value) != sudoku_solution[index]):
               #print(value,"!=",sudoku_solution[index])
               return
            else:
               index = index + 1
      #No wrong numbers found
      cur = select_sql("SELECT Available FROM Item WHERE Item_ID = 5")
      for row in cur.fetchall():
         if (row[0] == False):
            myprint("You hear a click coming from the toybox. There is a doll inside.")
            update_sql("UPDATE ITEM Set Available = True WHERE Item_ID = 5")
            return
   def onObjectClick(event):                  
      text_object = event.widget.find_closest(event.x, event.y) #Set the clicked object to variable
      #Item type
      item_type = canvas.type(text_object)
      if (item_type == 'text'):
         #Check square value
         value = canvas.itemcget(text_object, 'text')
         if (value == ' '):
            value = 0
         #Increase value by 1
         value = int(value)
         if (value == 9):
            value = 1
         else:
            value = value + 1
         #Set new value
         canvas.itemconfigure(text_object, text=value)
         solve_puzzle()
      return
   def onObjectClick3(event):
      text_object = event.widget.find_closest(event.x, event.y) #Set the clicked object to variable
      #Item type
      item_type = canvas.type(text_object)
      if (item_type == 'text'):
         canvas.itemconfigure(text_object, text=" ")
      solve_puzzle()
      return
   sudoku_solution = [8,4,6,9,3,7,1,5,2,3,1,9,6,2,5,8,4,7,7,5,2,1,8,4,9,6,3,2,8,5,7,1,3,6,9,4,4,6,3,8,5,9,2,7,1,9,7,1,2,4,6,3,8,5,1,2,7,5,9,8,4,3,6,6,3,8,4,7,1,5,2,9,5,9,4,3,6,2,7,1,8]
   sudoku_show_square = [1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1]
   #sudoku_show_square = [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]
   tex_field_array = []
   index_square = 0
   square_side = 50
   square_x_start = 5
   square_y_start = 5
   square_x1 = square_x_start
   square_x2 = square_x1 + square_side
   square_y1 = square_y_start
   square_y2 = square_y1 + square_side
   root = tk.Tk()
   canvas = tk.Canvas(root, width=9*square_side + 10, height=9*square_side + 10)
   canvas.grid()
   #Draw sudoku
   for i_height in range(9):
      #Aseta x arvot alkuun
      square_x1 = square_x_start
      square_x2 = square_x1 + square_side
      for i_width in range(9):
         #Piirrä laatikko
         box_tag = str(index_square)
         box = canvas.create_rectangle(square_x1, square_y1, square_x2, square_y2, fill="white", outline = 'black', tags=box_tag)
         #Kirjoita ruutuun arvo
         label_x = (square_x1+square_x2)/2
         label_y = (square_y1+square_y2)/2
         if (sudoku_show_square[index_square] == 1):
            mylabel = canvas.create_text((label_x, label_y), text=sudoku_solution[index_square], fill="black", font=("Arial", 26))
         else:
            mylabel = canvas.create_text((label_x, label_y), text=" ", fill="black", font=("Arial", 26))
         #Kasvata x arvoja
         square_x1 = square_x1 + square_side
         square_x2 = square_x2 + square_side
         #Kerää lista editoitavista tekstikentistä
         tex_field_array.append(mylabel)
         if (sudoku_show_square[index_square] == 0):
            canvas.itemconfig(mylabel, fill="red") # change color
         #Kasvata array arvoa
         index_square = index_square + 1
      #Kasvata y arvoja
      square_y1 = square_y1 + square_side
      square_y2 = square_y2 + square_side
   #Piirrä paksut laatikot 3x3 sektoreiden ympärille
   #Aseta x arvot alkuun
   square_x1 = square_x_start
   square_x2 = square_x1 + square_side * 3
   square_y1 = square_y_start
   square_y2 = square_y1 + square_side * 3
   for i_height in range(3):
      square_x1 = square_x_start
      square_x2 = square_x_start + square_side * 3
      for i_width in range(3):
         box = canvas.create_rectangle(square_x1, square_y1, square_x2, square_y2, outline = 'black', width=4)
         square_x1 = square_x1 + square_side * 3
         square_x2 = square_x1 + square_side * 3
      square_y1 = square_y1 + square_side * 3
      square_y2 = square_y2 + square_side * 3
   #Aseta klikattaville tekstikentille onObjectClick eventti
   for text_field in tex_field_array:
      canvas.tag_bind(text_field, '<ButtonPress-1>', onObjectClick)
      canvas.tag_bind(text_field, '<ButtonPress-3>', onObjectClick3)
   canvas.pack()
   root.wm_title("Sudoku puzzle") #Window title
   root.call('wm', 'attributes', '.', '-topmost', '1') #Window always on top
   root.mainloop()

def open_map(player_location):
   root = tk.Tk()
   canvas = tk.Canvas(root, width=230, height=200, borderwidth=0, highlightthickness=0, bg="white")
   canvas.grid()
   map_start_x = 10
   map_start_y = 10
   def draw_room(location_id, location_name, coordinates):
      coordinate_array = coordinates.split(',')
      #Move x,y values away from 0,0 position
      room_x1 = int(coordinate_array[0]) + map_start_x
      room_y1 = int(coordinate_array[1]) + map_start_y
      room_x2 = int(coordinate_array[2]) + map_start_x
      room_y2 = int(coordinate_array[3]) + map_start_y
      #Room center coordinates
      room_center_x = room_x1+(room_x2 - room_x1)/2
      room_center_y = room_y1+(room_y2 - room_y1)/2
      #Draw a red dot if the player is in the room
      if (player_location <= 2 and location_id <= 2) or (player_location > 2 and player_location <= 14  and location_id > 2 and location_id <= 14) or (player_location > 14 and location_id >14):
         #Draw second floor
         canvas.create_rectangle(room_x1, room_y1, room_x2, room_y2, fill="white", outline = 'black')
         location_name = location_name.replace(' ', '\n')
         #location_name = "East" + '\n' + "hallway"
         text = canvas.create_text(room_center_x, room_center_y, font=("Arial", 5), text=location_name)
      else:
         #Dont draw the room
         pass
      if (location_id == player_location):
         #Player position is in the middle of the room
         circle = canvas.create_oval(room_center_x-10, room_center_y-10, room_center_x+10, room_center_y+10, fill="red")
      ##Else write room name
      #else:
      #    text = canvas.create_text(room_center_x, room_center_y, font=("Arial", 5), text=location_name)
   #Check from database which rooms have been visited
   cur = db.cursor()
   sql = "SELECT Room_ID, Name, Map_Coordinates FROM Room WHERE Visited = True"
   cur.execute(sql)
   for row in cur.fetchall():
      if (player_location <= 2 and row[0] <= 2):
         draw_roow = True
         Window_Title = "Basement map"
      elif (player_location > 2 and player_location <= 14  and row[0] > 2 and row[0] <= 14):
         draw_roow = True
         Window_Title = "Floor 1 map"
      elif (player_location > 14 and row[0] >14):
         draw_roow = True
         Window_Title = "Floor 2 map"
      else:
         draw_roow = False
      if (draw_roow == True):
         draw_room(row[0], row[1], row[2])
   root.wm_title(Window_Title) #Window title
   root.call('wm', 'attributes', '.', '-topmost', '1') #Window always on top
   root.mainloop()
   return

def electric_lock(solution):
   #Ask the player to input a four digit code
   player_input = input("Please enter a four digit code: ")
   if (player_input == solution):
      return True
   else:
      return False
   
def move(source_location, target_direction):
   #Check Access route for target direction
   cur = db.cursor()
   sql = "SELECT Access_Target_ID, Locked, Description FROM Access WHERE Access_Source_ID = " + str(source_location) + " AND Direction = '" + str(target_direction) + "'"
   #print(sql)
   cur.execute(sql)
   if (cur.rowcount>=1):
      for row in cur.fetchall():
         #Check if access is locked
         if (row[1] == True):
            #Show why it is locked
            print(row[2])
         else:
            #Access route found
            target_location = row[0]
            #Update player location
            update_sql("UPDATE Room SET Visited = True Where Room_ID = " + str(target_location))
            global player_location
            player_location = target_location
            #Print a long line to divide texts ------
            print("-"*80)
            look_all(player_location)
   else:
      #No access point found
      print("I can't move that way!")

def take_object(source_location, target):
   #Look for all available objects in current room
   cur = db.cursor()
   sql = "SELECT Item_ID, Name FROM Item WHERE Room_ID = " + str(source_location) + " AND Available = True AND Takeable = True"
   if (target != "all"):
      sql = sql + " AND Name = '" + target + "'"
   #print(sql)
   cur.execute(sql)
   if (cur.rowcount>=1):
      for row in cur.fetchall():
         #Update item taken = True
         update_sql("UPDATE Item SET Carried = True, Available = False, Room_ID = NULL WHERE Item_ID = " + str(row[0]))
         print("I took the " + str(row[1]))
   else:
      print("I can't take that.")
   return

def drop_object(source_location, target):
   #Check if you are holding said object
   cur = db.cursor()
   sql = "SELECT Item_ID FROM Item WHERE Carried = True"
   if (target != "all"):
      sql = sql + " AND Name = '" + target + "'"
   #print(sql)
   cur.execute(sql)
   if (cur.rowcount>=1):
      for row in cur.fetchall():
         update_sql("UPDATE Item SET Carried = False, Available = True, Room_ID = " + str(source_location) + " WHERE Item_ID = " + str(row[0]))
         print("I dropped the " + target)
   else:
      if (len(target) > 0):
         print("I´m not holding any " + target)
   return
   
def look_all(player_location):
   #Room description
   look_room(player_location)
   look_items(player_location)
   return

def look_room(player_location):
   cur = db.cursor()
   #Room description
   sql = "SELECT Room_Description FROM Room WHERE Room_ID = " + str(player_location)
   cur.execute(sql)
   for row in cur.fetchall():
      myprint(row[0])
   return
   
def look_items(player_location):
   cur = db.cursor()
   #Show item names in the room
   sql = "SELECT Name FROM Item WHERE Room_ID = " + str(player_location) + " AND Carried = False AND Available = True"
   cur.execute(sql)
   if cur.rowcount >= 1:
      print("In the room I see:")
      for row in cur.fetchall():
         print(row[0])
   else:
      #print("I don't see anything of interest.")
      pass
   return

def look_at_item(player_location, target):
   cur = db.cursor()
   #Item is carried OR Item is in the room
   sql = "SELECT Description FROM Item WHERE Name = '" + target + "' AND (Room_ID = " + str(player_location) + " OR Carried = True)"
   #print(sql)
   cur.execute(sql)
   if cur.rowcount>=1:
      for row in cur.fetchall():
         myprint(row[0])
   else:
      print("I don't see any " + target)
   return

def check_inventory():
   cur = db.cursor()
   sql = "SELECT Name FROM Item WHERE Carried = True"
   cur.execute(sql)
   if cur.rowcount>=1:
      print("I´m holding:")
      for row in cur.fetchall():
         print(row[0])
   else:
      print("I´m not holding anything!")

def myprint(string):
   row_length = 60
   string_list = string.split()
   used_length = 0
   for word in string_list:
      if used_length + len(word) <= row_length:
         if used_length > 0:
            print(" ", end='')
            used_length = used_length + 1
         print(word, end='')
      else:
         print("")
         used_length = 0
         print(word, end='')
      used_length = used_length + len(word)
   print("")

def select_sql(sql):
   #print(sql)
   cur = db.cursor()
   cur.execute(sql)
   return cur
   
def update_sql(sql):
   #print(sql)
   cur = db.cursor()
   cur.execute(sql)
   return

def help():
    #Print list of commands
    print("")
    print("List of commands I know:")
    print("N,E,S,W for moving around")
    print("NE,NW,SE,SW for diagonal moving")
    print("Stairs require going UP and DOWN")
    print("TAKE, DROP, INVENTORY for item management")
    print("Sometimes I can USE items")
    print("I should also LOOK UNDER and INSIDE objects too")
    print("If I ever get stuck I should look at the MAP")
    print("")

def specific_command(action, target, preposition, player_location):
   command_found = True
   #Each room has its own specific commands
   
   #??? Room
   if (player_location == 1):
      if (action == 'look' and (preposition == 'under') and ((target == 'desk') or (target == 'table'))):
         #Check if bin code has been found yet
         cur = select_sql("SELECT Available FROM Item WHERE Item_ID = 30")
         if (cur.rowcount >= 1):
            for row in cur.fetchall():
               if (row[0] == False):
                  update_sql("UPDATE Item SET Available = True WHERE Item_ID = 30 or Item_ID = 25")
                  look_at_item(1,"trash bin")
                  update_sql("UPDATE Item SET Description = 'A trash bin, with some rubbish inside.' WHERE Item_ID = 25")            
         else:
            look_at_item(1, "trash bin")
      elif ((action == 'use' and target == "keypad")):
         cur = select_sql("SELECT locked FROM Access WHERE Access_Source_ID ='" + str(player_location) + "' AND Direction = 'e'")
         for row in cur.fetchall():
            if (row[0] == False):
               print('The door is already open')
            else:
               if(electric_lock("5081")):
                  print("Lock opened")
                  update_sql("UPDATE Access SET Locked = False WHERE Access_Source_ID = 1 AND Direction = 'e'")
               else:
                  print("Incorrect code")
      else:
         command_found = False

   #Boiler room
   elif (player_location == 2):
      if (action == 'use' and (target == 'boiler' or target == 'block of ice')):
         #Check if you are holding the block of ice
         cur = select_sql("SELECT Carried FROM Item WHERE Item_ID = 56")
         if (cur.rowcount >= 1):
            for row in cur.fetchall():
               if (row[0] == True):
                  #Melt the ice block
                  update_sql("UPDATE Item SET Available = False, Carried = False WHERE Item_ID = 56") #Ice block
                  update_sql("UPDATE Item SET Available = True, Carried = True WHERE Item_ID = 2") #Martha doll
                  print("The ice block melts and reveals a doll")
      #No specific command found
      else:
         command_found = False
   
   #Lobby
   elif (player_location == 3):
      if (action == 'look' and (preposition == 'inside' or preposition == 'in' or preposition == '') and target == 'closet'):
         #Check if Jacket has been found yet
         cur = select_sql("SELECT Available FROM Item Where Item_ID = 59")
         if (cur.rowcount >= 1):
            for row in cur.fetchall():
               if (row[0] == False):
                  update_sql("UPDATE Item SET Available = True WHERE Item_ID = 59")
                  look_at_item(3,'Jacket')
      elif (action == 'look' and (preposition == 'inside' or preposition == 'in') and (target == 'jacket' or (target == 'pocket' or target == 'pockets'))):
         #Check if car key has been found yet
         cur = select_sql("SELECT Available FROM Item WHERE Item_ID = 9") #Car key
         if (cur.rowcount >= 1):
            for row in cur.fetchall():
               if (row[0] == False):
                  update_sql("UPDATE Item SET Available = True WHERE Item_ID = 9") #Car key
                  print("There is a car key inside the jacket's pocket.")
      elif (action == 'use' and target == 'front door key'):
         cur = select_sql('SELECT Carried FROM Item WHERE Item_ID = 8') #Front door key
         if (cur.rowcount >= 1):
            for row in cur.fetchall():
               if (row[0] == True):
                  update_sql('UPDATE Item SET Carried = False WHERE Item_ID = 8') #Front door key no longer carried
                  update_sql('UPDATE Item SET Available = False WHERE Item_ID = 8') #Front door key no longer accessible
                  update_sql('UPDATE Access SET Locked = False WHERE Access_Source_ID = 3 and Access_Target_ID = 14')#Opens door to Front yard
                  print('The front door is open!')
      #No specific command found
      else:
         command_found = False
   
   #West hallway
   elif (player_location == 4):
      if (action == 'look' and target == 'painting'):
         #Look at the painting
         look_at_item(player_location, target)
         #Update hints table
         #
         #Do something
      #No specific command found
      else:
         command_found = False
   
   #Dining hall
   elif (player_location == 5):
      if (action == 'look' and target == 'table'):
         cur = select_sql("SELECT * FROM Item WHERE Carried = TRUE AND Item_ID IN(1,2,3,4,5,6)")
         if (cur.rowcount == 6):
             dining_hall_puzzle()
         else:
             look_at_item(player_location, target)
      #No specific command found
      else:
         command_found = False
   
   #Livingroom
   elif (player_location == 6):
      if (action == 'look' and target == 'toybox'):
         myprint("The toybox seems to be locked with a novelty lock. I need to solve a sudoku to unlock it.")
         sudoku_puzzle()
      else:
         command_found = False

   #Kitchen
   elif (player_location == 7):
      if ((action == 'open' and target == 'freezer') or (action == 'look' and (preposition == 'in' or preposition == 'inside') and preposition == 'freezer')):
         #Check if the block of ice has been found yet
         cur = select_sql("SELECT Available FROM Item WHERE Item_ID = 56")
         if (cur.rowcount >= 1):
            for row in cur.fetchall():
               if (row[0] == False):
                  update_sql("UPDATE Item SET Available = True WHERE Item_ID = 56")
                  print("I see an unnatural block of ice inside the freezer.")
      #No specific command found
      else:
         command_found = False
   
   #Garage
   elif (player_location == 11):
      if (action == 'use' and (target == "car keys" or target == "car key")):
         cur = select_sql("SELECT Carried FROM Item WHERE Item_ID = 9")
         if (cur.rowcount >= 1):
            for row in cur.fetchall():
               if (row[0] == True):
                  update_sql("UPDATE ITEM Set Available = False WHERE Item_ID = 9")
                  update_sql("UPDATE ITEM Set Carried = False WHERE Item_ID = 9")
                  update_sql("UPDATE ITEM Set Available = True WHERE Item_ID = 1")
                  update_sql("UPDATE ITEM set description = 'It is a car, the doors are open' WHERE Item_ID = 36")
                  print("The car doors open")
         else:
            command_found = False
      else:
         command_found = False
   
   #Recreation room
   elif (player_location == 12):
      if (action == 'look' and target == "dartboard"):
         dartboard_puzzle()
      elif (action == 'break' and (target == 'door' or target == 'bathroom door' or target == 'south door')):
          cur = select_sql("SELECT Locked FROM Access WHERE Access_Source_ID = 12 AND Access_Target_ID = 13")
          if (cur.rowcount >= 1):
            for row in cur.fetchall():
               if(row[0]==False):
                  print("The door is already open")
               else:
                  update_sql('UPDATE Access set Locked = False WHERE Access_Source_ID = 12 AND Access_Target_ID = 13')
                  print("I smash into the door with hulk-like powers and the door opens")
      else:
         command_found = False
   
   #Bedroom
   elif (player_location == 16):
      if (action == 'look' and (target == 'table')):
         #Check if bookmark has been found yet
         cur = select_sql("SELECT Available FROM Item WHERE Item_ID = 57")
         if (cur.rowcount >= 1):
            for row in cur.fetchall():
               if (row[0] == False):
                  update_sql("UPDATE Item SET Available = True WHERE Item_ID = 57")
                  look_at_item(16, "table")
                  look_at_item(7, "bookmark")
      elif (action == 'listen' and target ==''):
         print("You hear static coming from behind the cupboard.")
      elif ((action == 'look') and (preposition == 'under') and (target == 'carpet')):
         print("There are countless unused items from the database sweeped under the carpet. I will pretend like I saw nothing.")
      else:
         command_found = False

   #Library
   elif (player_location == 18):
      if (action == 'look' and 'bookshelf' in target):
         print("There are a lot of books. I wonder what book I should take.")
         player_shelf = target.replace('bookshelf', '').strip()
         #Ask the player the row
         player_row = input("Which row of books (1-3): ")
         #Ask the player the column
         player_column = input("Which book to choose (1-20): ")
         if (player_shelf.lower() == "c" and player_row == "2" and player_column == "17" ):
            #Check if book has been found yet
            cur = select_sql("SELECT Available FROM Item WHERE Item_ID = 58")
            if (cur.rowcount >= 1):
               for row in cur.fetchall():
                  if (row[0] == False):
                     update_sql("UPDATE Item SET Available = True WHERE Item_ID = 58")
                     update_sql('UPDATE Access SET Locked = False WHERE Access_Source_ID = 16 and Access_Target_ID = 17')
                     update_sql("UPDATE Room SET Room_Description = 'You are in a bedroom. There is grand twin bed and a cupboard on the south wall. You hear faint static noise coming from somewhere. There is a door to the east and a new doorway to the south.' WHERE Room_ID = 16")
                     take_object(18, "book")
                     print("I heard a click followed by some slight rumbling sounds. It seems that taking the book launched some mechanism.")
      elif (action == 'take' and target == "book"):
         #Ask the player the shelf
         player_shelf = input("Which shelf to choose (A-G): ")
         #Ask the player the row
         player_row = input("Which row of books (1-3): ")
         #Ask the player the column
         player_column = input("Which book to choose (1-20): ")
         if (player_shelf.lower() == "c" and player_row == "2" and player_column == "17" ):
            #Check if book has been found yet
            cur = select_sql("SELECT Available FROM Item WHERE Item_ID = 58")
            if (cur.rowcount >= 1):
               for row in cur.fetchall():
                  if (row[0] == False):
                     update_sql("UPDATE Item SET Available = True WHERE Item_ID = 58")
                     update_sql('UPDATE Access SET Locked = False WHERE Access_Source_ID = 16 and Access_Target_ID = 17')
                     update_sql("UPDATE Room SET Room_Description = 'You are in a bedroom. There is grand twin bed and a cupboard on the south wall. You hear faint static noise coming from somewhere. There is a door to the east and a new doorway to the south.' WHERE Room_ID = 16")
                     take_object(18, "book")
                     print("I heard a click followed by some slight rumbling sounds. It seems that taking the book launched some mechanism.")
         else:
            print("Nothing of interesting")
      else:
         command_found = False
   
   #Greenhouse
   elif (player_location == 19):
      if (action == 'move' and (target == 'bench')):
         #Check if bench has been moved yet
         cur = select_sql("SELECT Takeable FROM Item WHERE Item_ID = 55")
         for row in cur.fetchall():
            if (row[0] == False):
               update_sql("UPDATE Item SET Takeable = True, Description = 'The pot seems cracked, it could break any second now.' WHERE Item_ID = 55")
               print("Now I can reach the pot")
            else:
               print('I already moved it')
      elif (action == 'break' and (target == 'pot')):
         #Check if pot has been broken yet
         cur = select_sql("SELECT Available FROM Item WHERE Item_ID = 3")
         for row in cur.fetchall():
            if (row[0] == False):
               update_sql("UPDATE Item SET Available = True WHERE Item_ID = 3")
               update_sql("UPDATE Item SET Takeable = False WHERE Item_ID = 55")
               update_sql("UPDATE Item SET Carried = False WHERE Item_ID = 55")
               print("There was a doll inside it")
            else:
               print('I already broke it')
      else:
         command_found = False
   else:
      #No specific command found
      command_found = False
   return command_found
      
#Open DB connection
db = mysql.connector.connect(
    host = "localhost",
    user = "dbuser12",
    passwd = "dbpass",
    db = "escape_text_adventure",
    buffered = True)

# Clear console
print("\n"*1000)

#Start text
print("Whoah.... Where the hell am I? Damn my head hurts... What is this place? ")
print("I'm in some kind basement... There's a desk with an old pc on top...")
print("")

#Initialize variables
player_location = 1

#Main loop
while True:
   user_command_list = input("Command: ") #Take user input
   user_command_list = user_command_list.replace("'","")#Replace quotation marks
   user_command_list = user_command_list.replace('"',"")#Replace quotation marks
   user_command_list = user_command_list.split() #Split it up in a list
   command_word_count = len(user_command_list) #Count the number of words
   #Clear command variables
   action = ""
   target = ""
   preposition = ""
   #Set commands to variables
   for index in range(len(user_command_list)):
      #The first word is the action
      if (index == 0):
         action = user_command_list[index].lower()
      #The second word might be preposition
      elif (user_command_list[index].lower() in["at","inside","under","behind","in"]):
         if (len(preposition)!=0):preposition = preposition + " "
         preposition = preposition + str(user_command_list[index].lower())
      #The rest of the words are the target
      else:
         if (user_command_list[index].lower() not in["a","an","the"]): #Skip a, an, the
            if (len(target)!=0):target = target + " "
            target = target + user_command_list[index].lower()
   #print("action:",action)
   #print("preposition:",preposition)
   #print("target:",target)
   #Check if the command is for a specific purpose
   if (specific_command(action, target, preposition, player_location)):
      pass
   #inventory
   elif (action == "i" or action == "inventory"):
      check_inventory()
      pass
   #map
   elif (action == "map" or (action == "look" and target == "map")):
      open_map(player_location)
   #look
   elif (action == "look"):
      if (target == ""):
         #Look at everything
         look_all(player_location)
      else:
         look_at_item(player_location, target)
   #move
   elif (action in ["u","d","n","e","s","w","ne","nw","se","sw","up","down","north","east","south","west"]):
      #Change north to n, east to e, etc...
      if (action == "north"): action = "n"
      elif (action == "east"): action = "e"
      elif (action == "south"): action = "s"
      elif (action == "west"): action = "w"
      elif (action == "up"): action = "u"
      elif (action == "down"): action = "d"
      #Change diagonal direction North East = ne, etc...
      if (target == "north"): target = "n"
      elif (target == "east"): target = "e"
      elif (target == "south"): target = "s"
      elif (target == "west"): target = "w"
      elif (target == "up"): target = "u"
      elif (target == "down"): target = "d"
      #the rest of the commands are propably the direction/room
      move(player_location, action + target)
      #Check if player location = Front yard
      if (player_location == 14):
          #GAME OVER
          db.rollback()
          break
   #take
   elif (action == "take"):
      take_object(player_location, target)
      pass
   #drop
   elif (action == "drop"):
      drop_object(player_location, target)
      pass
   #quit
   elif (action == "quit"):
      descision = input("Are you sure? ")
      if (descision == "yes"):
         db.rollback()
         print("Game over. Thank you for playing!")
         break
      elif (descision == "no"):
         myprint("You quit the game... Just kidding, you'd better not quit!")
   #help
   elif (action == 'help'):
       help()
   #error
   else:
      print("I don't know how to " + action + " " + target)
      pass
