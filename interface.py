import tkinter.filedialog as filedialog
import tkinter as tk


global filepath

main_window = tk.Tk()

def input():
    input_path = tk.filedialog.askopenfilename()
    filepath = input_path
    startparse()
    input_entry.delete(1, tk.END)  
    input_entry.insert(0, input_path) 
    input_entry.insert(0, input_path) 
    print(input_path)


def output():
    path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  
    input_entry.insert(0, path)  


top_frame = tk.Frame(main_window)
bottom_frame = tk.Frame(main_window)
line = tk.Frame(main_window, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)


def startparse():
  print(filepath)



begin_button = tk.Button(bottom_frame, text='Begin filepath', command =startparse)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)



begin_button.pack(pady=20, fill=tk.X)

#begins listening for events
main_window.mainloop()
