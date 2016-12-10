

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

    def is_ignorable(self, Letter):

        if Letter in self.__ignore:
            return True
        else:
            return False

    def read_file(self, fileName):
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

    def