import tkinter as tk
import tkinter.filedialog as filedialog
import core

class mainWindow:
    def __init__(self):
        # Start the Window
        self.__root = tk.Tk()

        # Give this widget an instance of the KanjiCounter class.
        self.__core = core.KanjiCounter()

        self.__root.title( "Kanji Frequency" )
        #self.__root.iconbitmap("")

        self.__takeFileButton = tk.Button( self.__root, text="Choose a text file full of Japanese texts." , \
                                            command=self.__takeFile__ , padx=10, pady=10 )
        self.__takeFileButton.pack()

        # Get the GUI going.
        self.__root.mainloop()

    def __takeFile__(self):
        kanjiFilePath = filedialog.askopenfilename( filetypes=[ ("text files", ".txt") ] )

        # If there was some trouble getting the file, cancel
        if not kanjiFilePath or kanjiFilePath == "":
                return




mainWindow()