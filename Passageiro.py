import datetime
import pytz
from time import gmtime, strftime

class Passageiro:

    name = ""

    def __init__(self, bag_pass, ciclo_in):
        self.__bag_pass = bag_pass
        self.__ciclo_in = ciclo_in

    def __str__(self):
        return "[b:"+str(self.__bag_pass)+" t:"+str(self.__ciclo_in)+"]"

    def obtem_bag_pass(self):
        return self.__bag_pass

    def ciclo_in(self):
        return self.__ciclo_in



if __name__ == '__main__' :

    pass1 = Passageiro(4, strftime("%Y-%m-%d_%H:%M:%S", gmtime()))

    print(pass1)

