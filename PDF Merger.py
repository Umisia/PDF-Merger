import tkinter, os
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger

window = tkinter.Tk()
window.title("PDF Merger")
files_path_list = []

def merge():    
    option_selected = var_int.get()    
    result_file_name = var_string.get() 
    
    if not result_file_name:
        tkinter.messagebox.showinfo("Failed", "Input file name")
    else:
        pdfs = ['1.pdf', '2.pdf']if option_selected == 1 else files_path_list
        try:              
            merger = PdfFileMerger()         
            for pdf in pdfs:
                merger.append(pdf)         
            merger.write(result_file_name+".pdf")
            merger.close()
            tkinter.messagebox.showinfo("Success", "Files merged.")
            if option_selected == 1:
                rename(result_file_name) 
        except:
            tkinter.messagebox.showinfo("Failed", "Something went wrong.")
        else:
            
            reset()
            

def rename(file_name):
    os.rename("1.pdf", file_name+"-1.pdf")
    os.rename("2.pdf", file_name+"-2.pdf")
    
def select_files():
    midFrame.pack()
    filename = askopenfilename(initialdir="./", filetypes=[('pdf file', '*.pdf')], title = "Choose a file.") 
    if filename:
        files_path_list.append(filename)
        label_added.grid(column=0, row=1, columnspan=3)
    if files_path_list:
        label_added.config(text=("\n".join(files_path_list)))  
        add_more = tkinter.Button(midFrame, text="Add another", command = select_files)
        add_more.grid(column=1, row=0)
        
def reset():
    entry.delete(0, 'end')
    midFrame.pack_forget()
    label_added.config(text=(""))
    radio_1.select()
    del files_path_list[:]

    
var_string = tkinter.StringVar()
var_int = tkinter.IntVar()
topFrame = tkinter.Frame(window)
topFrame.pack()

radio_1 = tkinter.Radiobutton(topFrame, text="Default", variable=var_int, value=1, command = reset)
radio_1.grid(column=0, row=0)
radio_1.select()
radio_2 = tkinter.Radiobutton(topFrame, text="Chose files", variable=var_int, value=2, command = select_files)
radio_2.grid(column=1, row=0)

midFrame = tkinter.Frame(window)
label_added = tkinter.Label(midFrame) 


bottomFrame = tkinter.Frame(window)
bottomFrame.pack(side="bottom")
label_1 = tkinter.Label(bottomFrame, text="New file name")
label_1.grid(column=0, row=1)

entry = tkinter.Entry(bottomFrame, textvariable = var_string)
entry.grid(column=1, row=1)

mergebutton = tkinter.Button(bottomFrame, text ="Merge", command = merge)
mergebutton.grid(column=0, row=2,columnspan=2)


window.mainloop()

