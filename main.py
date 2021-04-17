import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class App:
    def __init__(self, root):
        # setting title
        root.title("BEEAP20 ex2and3") #shows the name of the title bar
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

# shows the label name for loading csv file
        
        self.__loadButton = tk.Button(root)
        self.__loadButton["bg"] = "white"
        ft = tkFont.Font(family='Times', size=10)
        self.__loadButton["font"] = ft
        self.__loadButton["fg"] = "#000000"
        self.__loadButton["justify"] = "center"
        self.__loadButton["text"] = "Load csv file"
        self.__loadButton.place(x=70, y=50, width=70, height=25)
        self.__loadButton["command"] = self.__loadButton_command
        self.combo_box = ttk.Combobox(root)
        self.combo_box.place(x=350, y=50, width=80, height=25)
        self.combo_box.bind("<<ComboboxSelected>>", self.__comboBoxCb)
        
  #shows the csv file name      
        self.csv_file_name  = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.csv_file_name["font"] = ft
        self.csv_file_name["fg"] = "#333333"
        self.csv_file_name["justify"] = "center"
        self.csv_file_name["text"] = "csv file name"
        self.csv_file_name.place(x=150, y=50, width=70, height=25)
        
         #shows the selected community      
        self.select_community = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.select_community["font"] = ft
        self.select_community["fg"] = "#333333"
        self.select_community["justify"] = "center"
        self.select_community["text"] = "Select community"
        self.select_community.place(x=250, y=50, width=100, height=25)
        
        # these canvases are broken, fix them
        self.__GLineEdit_392 = tk.Canvas(root)
        self.__GLineEdit_392.place(x=50, y=130, width=230, height=150, bg='green')
       
    
        self.__GLineEdit_517 = tk.Canvas(root)
        self.__GLineEdit_517.place(x=50, y=310, width=230, height=150)
       
    
        self.__GLineEdit_985 = tk.Canvas(root)
        self.__GLineEdit_985.place(x=310, y=130, width=230, height=150)

       
        self.__GLineEdit_700 = tk.Canvas(root)
        self.__GLineEdit_700.place(x=310, y=310, width=230, height=150)
        
       
    def __loadButton_command(self):
       
        filePath = fd.askopenfilename(initialdir='.')
        
        try:
           
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.combo_box['values'] = list(self.__df['COMMUNITY AREA NAME'].unique())
        except:
            # quick and dirty, desired behavior would be to show a notification pop up that says
            # "nope!"
            print('nope')

    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def __comboBoxCb(self, event=None):
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.combo_box.get()]
        print(self.__subdf.head())
        fig1 = Figure(figsize=(230,150), dpi=100)
        ax1 = fig1.add_subplot(111)
        self.__subdf.iloc[:, range(self.__subdf.columns.get_loc('KWH JANUARY 2010'), 12)].mean().plot.bar(ax=ax1)
                                             
        
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    plt.show() 
