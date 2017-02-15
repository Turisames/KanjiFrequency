

class KanjiCounter():

    def __init__(self):

        # The dict for counting all the kanjis.
        self.__counter = {}

        # A list for containing the results.
        self.__results = []

        #Ignores all romaji and kana signs.
        self.__ignore =	"ABCDEFGHIJKLMNOPQRSŠTUVWXYZŽÅÄÖ" \
                        + "aɑbcdefgŋhijklmnŋoprsʃtuvwyäæø" \
                        + "!@.,_^¨'*´´``\"" \
                        + "1234567890+-<>" \
                        + "あアかがざだばカさサたタなナはハまマやヤらラわワ" \
                        + "いイきキしシちチにニひヒみミ※りリゐヰ" \
                        + "うウくクすスつツぬヌふフむムゆユるル※" \
                        + "えエけケせセてテねネへヘ	めメ※れレゑヱ" \
                        + "おオこコそソとトのノほホもモよヨろロをヲ" \
                        + "んン 、で。ド）（・ィッ()「」　/っ[]プ:" \
                        + "バジパェグポュピブどヴビ%ベ１ペダペャびじォズ" \
                        + "２"
    #

    def __handle_character__(self, Part = ""):
        if Part not in self.__ignore:
            if Part not in self.__counter:
                self.__counter[ Part ] = 1
            else:
                self.__counter[ Part ] += 1

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
                    self.__handle_character__( part )

            kanjiFile.close()

            self.__results = self.__output_list__()

        except EOFError:
            pass

    def __output_list__(self):
        return sorted(self.__counter, key=(lambda hash : self.__counter[ hash ] ), reverse = True )

    def __get_results__(self):
        return self.__results

    def __get_counter__(self):
        return self.__counter

    def __full_process__(self, FileName = ""):
        self.__read_file__( FileName )
        return self.__output_list__()