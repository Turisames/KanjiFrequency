import tkinter as tk
import tkinter.filedialog as filedialog
import core
from enum import Enum

class FrequenceMode(Enum):
    REAL_NUMBERS = 1
    RELATIVE_NUMBER = 2

class mainWindow:
    def __init__(self):
        # Start the Window
        self.__root = tk.Tk()

        # Core
        # Give this widget an instance of the KanjiCounter class.
        self.__core = core.KanjiCounter()

        # Name and icon.
        self.__root.title( "Kanji Frequency" )
        #self.__root.iconbitmap("")

        # The button for taking a file.
        self.__takeFileButton = tk.Button( self.__root, text="Choose a text file full of Japanese texts." , \
                                           command=self.__takeFile__ , padx=10, pady=10 )
        self.__takeFileButton.pack()
        # </filebutton>

        # The radiobuttons.
        self.__frequencyMode = FrequenceMode.REAL_NUMBERS
        self.__RealRadioBtn = tk.Radiobutton( self.__root, text="Real Numbers", \
                             variable=self.__frequencyMode, value=FrequenceMode.REAL_NUMBERS)
        self.__RealRadioBtn.pack()
        self.__RelativeRadioBtn =tk.Radiobutton( self.__root, text="Relative Frequency", \
                                 variable=self.__frequencyMode, value=FrequenceMode.RELATIVE_NUMBER)
        self.__RelativeRadioBtn.pack()
        self.__RealRadioBtn.select()
        # </radiobuttons>

        # The widget for showing the results.
        self.__textWidget = tk.Text( self.__root, \
                                     padx=4, pady=4, width=30, state=tk.NORMAL )
        self.__textWidget.pack( side=tk.LEFT )
        #</text>

        # Get the GUI going.
        self.__root.mainloop()

    def __takeFile__(self):
        kanjiFilePath = filedialog.askopenfilename( filetypes=[ ("text files", ".txt") ] )

        # If there was some trouble getting the file, cancel.
        if not kanjiFilePath or kanjiFilePath == "":
            return

        # Interaction with the core.
        results = self.__core.__full_process__( kanjiFilePath )
        map = self.__core.__get_counter__()
        total = self.__core.__get_total__()

        #  Text: Printing the results.
        if self.__textWidget.index(0.0) != "":
            self.__clear__()


        number = 0
        sentence = ""
        self.__textWidget.config( state=tk.NORMAL)
        for line in results:
            if self.__frequencyMode == FrequenceMode.REAL_NUMBERS:
                number = map[ line ]
            elif self.__frequencyMode == FrequenceMode.RELATIVE_NUMBERS:
                number = map[ line ] / total
            word = line + ":" + str( number )
            sentence += word + "\n"
            self.__textWidget.insert( tk.CURRENT, \
                                      line + ":" + str( map [ line ] ) + "\n" )
        self.__textWidget.config( state=tk.DISABLED )
        # </Text>

    def __clear__(self):
        self.__textWidget.config( state=tk.NORMAL )
        self.__textWidget.delete( 0.0, tk.END )
        self.__textWidget.config(state=tk.DISABLED )

# End of definition.
mainWindow()