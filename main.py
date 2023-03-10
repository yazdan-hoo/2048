import random
import keyboard
import time

arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def get_arr():
    return arr

def scerrn ():
    for _ in arr :
        for i in _ :
            print (i,end = " ")
        print()
    print("--------------")

def add_2 ():
    empty_cells = []
    for i in range(0,4):
        for j in range(0,4):
            if arr[i][j] == 0 :
                empty_cells.append((i,j))                
    cell_to_add = random.choice(empty_cells)
    arr[cell_to_add[0]][cell_to_add[1]] = 2
    



def move_up (s):
    print ("move up {0}".format(x))

def can_move_left():
    
    for row in range(0,4):
        for cell in range(1,4):
            if arr[row][cell] != 0:
                   if arr[row][cell] == arr[row][cell - 1]:
                       return True
                   if arr[row][cell - 1] == 0:
                       return True
    return False       
             
    


def move_down ():
    board_changed = False
    for column in range(0,4):
        last_nonzero_cell_index = None
        for row in range(3,-1,-1):
           if arr[row][column] != 0:
                 if last_nonzero_cell_index == None:
                    last_nonzero_cell_index = (row,column)
                 elif arr[row][column] == arr[last_nonzero_cell_index[0]][last_nonzero_cell_index[1]]:
                     arr[row][column] = arr[row][column] *2
                     arr[last_nonzero_cell_index[0]][last_nonzero_cell_index[1]] = 0
                     last_nonzero_cell_index = None       
                     board_changed = True
                 else:
                     last_nonzero_cell_index = (row,column)
    for column in range(0,4):
        for _ in range(0,3):
            for row in range(2,-1,-1):
                if arr[row][column] != 0 and arr[row + 1][column] == 0:
                    arr[row + 1][column] = arr[row][column]
                    arr[row][column] = 0
                    board_changed = True
    
    return board_changed


def move_right ():
    print ("move right") 
def move_left ():
    for row in range(4):
        current_cell_value = None
        current_cell_index = None
        for cell in range(4):
            selected_cell = (row,cell)
            if arr[row][cell] == 0:
                continue
            if current_cell_value == None:
                current_cell_value = arr[row][cell]
                current_cell_index = (row,cell)
            elif arr[row][cell] == current_cell_value:
               arr[current_cell_index[0]][current_cell_index[1]] = current_cell_value * 2 
               arr[row][cell] = 0
               current_cell_value = None
               current_cell_index = None             
            else:
                current_cell_value = arr[row][cell]
                current_cell_index = (row,cell)
                
    for row in range(4):
        for _ in range(0,4):
            for cell in range(1,4):
                if arr[row][cell] != 0:
                    if arr[row][cell - 1] == 0:
                        arr[row][cell - 1] = arr[row][cell]           
                        arr[row][cell] = 0

                


            
            




def register_moves():

    keyboard.on_press_key("w",lambda a : move_up())
    
    def down(x):
    
        if move_down():
            add_2()
            scerrn()


    keyboard.on_press_key("s",down)
    keyboard.on_press_key("d",lambda a : move_right())
    def left(x):
        if can_move_left():
            move_left()
            add_2() 
            scerrn()

    
    keyboard.on_press_key("a",left)

def run ():
    
    add_2()
    scerrn()
    register_moves()
    time_elaps = 0

    while True :
        time.sleep(1)
        time_elaps += 1

if __name__ == "__main__":
    run()
    