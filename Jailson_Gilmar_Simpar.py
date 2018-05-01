import pytz
from time import gmtime, strftime
import datetime
from pythonds.basic import Queue
import time
from random import  randint

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

    def __init__(self, n_balcao):
        self.__n_balcao = n_balcao
        self.__fila = Queue()
        self.__inic_atend = 0
        self.__passt_atend = 0
        self.__numt_bag = 0
        self.__tempt_esp = 0
        self.__bag_utemp = 0

    def muda_inic_atend(self, passageiro):
        self.__inic_atend = passageiro.ciclo_in()
        self.incr_passt_atend()
        self.muda_numt_bag(passageiro.obtem_bag_pass())
        self.__tempt_esp += (tempo_atual() - passageiro.ciclo_in())
        self.__bag_utemp = self.__numt_bag

        #print("Tempo Atual: " + str(int(tempo_atual())))
        #print("Ciclo in passageiro: " + str(int(passageiro.ciclo_in())))
        #print("Tempo atual - tempo do passageiro: " + str(int(tempo_atual() - passageiro.ciclo_in())))

    def incr_passt_atend(self):
        self.__passt_atend += 1

    def muda_numt_bag(self, bag_passageiro):
        self.__numt_bag += bag_passageiro

    def obtem_n_balcao(self):
        return self.__n_balcao

    def obtem_fila(self):
        return self.__fila

    def obtem_inic_atend(self):
        return self.__inic_atend

    def obtem_passt_atend(self):
        return self.__passt_atend

    def obtem_numt_bag(self):
        return self.__numt_bag

    def obtem_temp_esp(self):
        return self.__tempt_esp

    def obtem_bag_utemp(self):
        return self.__bag_utemp

if __name__ == '__main__' :

    balcao1 = Balcao("1")
    lista_passageiros = []

    for i in range(10):
        lista_passageiros.append(Passageiro(randint(0,5), tempo_atual()))
        print("Criado passageiro " + str(i+1) + "")
        time.sleep(randint(2,9))

    fila = Queue()

    for i in range(len(lista_passageiros)):
        fila.enqueue(lista_passageiros[i])

    while not fila.isEmpty():
        balcao1.muda_inic_atend(fila.dequeue())

    print("Tempo total de espera do balcao: "+str(int(balcao1.obtem_temp_esp())))
    print("Total de bagagens despachadas pelo balcao atual é: "+ str(balcao1.obtem_numt_bag()))

