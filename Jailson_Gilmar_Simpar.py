import datetime
import pytz
from time import gmtime, strftime
from pythonds.basic import Queue
import time

def tempo_atual():
    return time.time()
    #return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def unix_para_datetime(tempo_unix):
    return datetime.datetime.fromtimestamp(int(tempo_unix)).strftime("%Y-%m-%d %H:%M:%S")

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

    def __init__(self, n_balcao, tempt_esp, bag_utemp):
        self.__n_balcao = n_balcao
        self.__fila = Queue()
        self.__inic_atend = 0
        self.__passt_atend = 0
        self.__numt_bag = 0
        self.__tempt_esp = tempt_esp
        self.__bag_utemp = bag_utemp

    def muda_inic_atend(self, passageiro):
        self.__inic_atend = passageiro.ciclo_in()
        self.incr_passt_atend()
        self.muda_numt_bag(passageiro.obtem_bag_pass())

        print(tempo_atual())
        print(passageiro.ciclo_in())
        print(tempo_atual() - passageiro.ciclo_in())


    def incr_passt_atend(self):
        self.__passt_atend += 1

    def muda_numt_bag(self, bag_passageiro):
        self.__numt_bag += bag_passageiro



if __name__ == '__main__' :

    balcao1 = Balcao("1", "10", "20")

    pass1 = Passageiro(4, tempo_atual())
    time.sleep(2)
    pass2 = Passageiro(2, tempo_atual())

    fila = Queue()

    print(int(time.time()))

    fila.enqueue(pass1)
    fila.enqueue(pass2)

    print(fila)
    balcao1.muda_inic_atend(fila.dequeue())
    print(fila)
    balcao1.muda_inic_atend(fila.dequeue())

    print(fila)

    print(pass1)

