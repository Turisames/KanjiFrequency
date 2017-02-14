import tkinter as tk
import tkinter.filedialog as filedialog

class mainWindow:
    def __init__(self):
        # Start the Window
        self.__root = tk.Tk()

        self.__root.title( "Kanji Frequency" )
        #self.__root.iconbitmap("")

        self.__takeFileButton = tk.Button( self.__root, text="Choose a text file full of Japanese texts.", command=self.__takeFile__  )
        self.__takeFileButton.pack()

        # Get the GUI going.
        self.__root.mainloop()

    def __takeFile__(self):
        kanjiFile = filedialog.askopenfilename( filetypes=[ ("text files", ".txt") ] )

        # If there was some trouble getting the file, cancel
        if not kanjiFile or kanjiFile == "":
                return


mainWindow()