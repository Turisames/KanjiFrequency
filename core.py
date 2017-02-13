

class KanjiCounter():

    def __init__(self):

        # The dict for counting all the kanjis.
        self.__counter = {}

        #Ignores all romaji and kana signs.
        self.__ignore = [	"ABCDEFGHIJKLMNOPQRSŠTUVWXYZŽÅÄÖ"
                            + "ɑbdefgŋhijklmnŋoprsʃtuvyæø"
                            + "!@.,_^¨'*´´``"
                            + "1234567890+-<>"
                            + "あアかカさサたタなナはハまマやヤらラわワ"
                            + "いイきキしシちチにニひヒみミ※りリゐヰ"
	                        + "うウくクすスつツぬヌふフむムゆユるル※"
	                        + "えエけケせセてテねネへヘ	めメ※れレゑヱ"
	                        + "おオこコそソとトのノほホもモよヨろロをヲ"
                            + "んン"
                         ]

    def __is_ignorable__(self, Letter):

        if Letter in self.__ignore:
            return True
        else:
            return False

    def __handle_character__(self, Part):
        if not self.is_ignorable(Part):
            if not in self.__ignore:
                self.__ignore[ Part ] = 1
            else:
                self.__ignore[ Part ] += 1

    def __read_file__(self, fileName):
        try:
            kanjiFile = open(fileName, encoding="utf-8")

            # Go through lines
            for line in kanjiFile:

                # Take away whitespaces.
                line = line.strip()

                # Ignore pointless lines
                if len(line) == 0 or line[0] == "#":
                    continue

                # Go through characters in a line.
                for part in line:

                    pass

            kanjiFile.close()
        except EOFError:
            pass

    def __output_list__(self):
        pass