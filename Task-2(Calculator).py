import tkinter as tk

root = tk.Tk()
root.resizable(0, 0)
root.title("Simple Calculator")
root.geometry("312x324")
 
input_value = ""

display_text = tk.StringVar()
 

def click_button_action(item):
    global input_value
    input_value = input_value + str(item)
    display_text.set(input_value)
 
def clear_button_action(): 
    global input_value 
    input_value = "" 
    display_text.set("")

def equal_button_action():
    global input_value
    result = str(eval(input_value))
    display_text.set(result)
    input_value = ""

  
input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
  
input_frame.pack(side = tk.TOP)
  
input_field = tk.Entry(input_frame, font=('times new roman', 18, 'bold'), textvariable = display_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
  
input_field.grid(row=0, column=0)
  
input_field.pack(ipady=10)
  
btns_frame = tk.Frame(root, width=312, height=272.5, bg="black")
  
btns_frame.pack()

clear_btn = tk.Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: clear_button_action()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide_btn = tk.Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "orange", cursor = "hand2", command = lambda: click_button_action("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 

btn_7 = tk.Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
  
btn_8 = tk.Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
  
btn_9 = tk.Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
  
multiply_btn = tk.Button(btns_frame, text = "X", fg = "black", width = 10, height = 3, bd = 0, bg = "orange", cursor = "hand2", command = lambda: click_button_action("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 

btn_4 = tk.Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
  
btn_5 = tk.Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
  
btn_6 = tk.Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
  
minus_btn = tk.Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "orange", cursor = "hand2", command = lambda: click_button_action("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 

btn_1 = tk.Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
  
btn_2 = tk.Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
  
btn_3 = tk.Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
  
plus_btn = tk.Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "orange", cursor = "hand2", command = lambda: click_button_action("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 

btn_0 = tk.Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click_button_action(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
  
point_btn = tk.Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "orange", cursor = "hand2", command = lambda: click_button_action(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
  
equals_btn = tk.Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "green", cursor = "hand2", command = lambda: equal_button_action()).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()
