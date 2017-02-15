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
        # </radiobuttons>

        # The widget for showing the results.
        self.__textWidget = tk.Text( self.__root, \
                                     padx=4, pady=4, width=30 )
        self.__textWidget.pack()
        #</text>

        # Get the GUI going.
        self.__root.mainloop()

    def __takeFile__(self):
        kanjiFilePath = filedialog.askopenfilename( filetypes=[ ("text files", ".txt") ] )

        # If there was some trouble getting the file, cancel
        if not kanjiFilePath or kanjiFilePath == "":
            return

        # Interaction with the core.
        results = self.__core.__full_process__( kanjiFilePath )
        map = self.__core.__get_counter__()

        #  Text: Printing the results.
        for line in results:
            self.__textWidget.insert( tk.CURRENT, \
                                      line + ":" + str( map [ line ] ) + "\n" )
        # </Text>
# End of definition.
mainWindow()