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

        '''
        # A temporary label for checking things.
        self.__tmpTextVariable = tk.StringVar()
        self.__tmpTextVariable.set("Default text.")
        self.__tempLabel = tk.Label(self.__root, textvariable=self.__tmpTextVariable )
        self.__tempLabel.pack()'''

        self.__textWidget = tk.Text( self.__root, \
                                     padx=4, pady=4, width=30 )
        self.__textWidget.pack()

        # Get the GUI going.
        self.__root.mainloop()

    def __takeFile__(self):
        kanjiFilePath = filedialog.askopenfilename( filetypes=[ ("text files", ".txt") ] )

        #self.__tmpTextVariable.set( kanjiFilePath )

        # If there was some trouble getting the file, cancel
        if not kanjiFilePath or kanjiFilePath == "":
            return

        results = self.__core.__full_process__( kanjiFilePath )
        map = self.__core.__get_counter__()

        for line in results:

            self.__textWidget.insert( tk.CURRENT, \
                                      line + ":" + str( map [ line ] ) + "\n" )

mainWindow()