import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title= "select a file to compress or decompress")
    return filename

def compression(i, o):
    compress(i, o)

def decompression(i, o):
    decompress(i, o)

window = tk.Tk()
window.title("Compression engine")
window.geometry("600x400")



compress_button = tk.Button(window, text="Compress", command=lambda: compression(open_file(), 'compessotput1.txt'))
decompress_button = tk.Button(window, text="Decompress", command=lambda: decompression(open_file(), "decompressoutput.txt"))


compress_button.grid(row=2, column=0)
decompress_button.grid(row=2, column=1)

window.mainloop()