import datetime
import pytz
from time import gmtime, strftime

from pythonds.basic import queue

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

class Balcao:

    def __init__(self, n_balcao, fila, inic_atend, passt_atend, numt_bag, tempt_esp, bag_utemp):
        self.__n_balcao = n_balcao
        self.__fila = fila
        self.__inic_atend = inic_atend
        self.__passt_atend = passt_atend
        self.__numt_bag = numt_bag
        self.__tempt_esp = tempt_esp
        self.__bag_utemp = bag_utemp

    def muda_inic_atend(self, inic_atend_pass):
        self.__inic_atend = inic_atend_pass

if __name__ == '__main__' :

    pass1 = Passageiro(4, strftime("%Y-%m-%d_%H:%M:%S", gmtime()))

    print("Teste")
    print(pass1)

