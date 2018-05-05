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

    def obtem_ciclo_in(self):
        return self.__ciclo_in

class Balcao:

    def __init__(self, n_balcao, passageiro):
        self.__n_balcao = n_balcao
        self.__fila = Queue()
        self.__inic_atend = 0
        self.__passt_atend = 0
        self.__numt_bag = 0
        self.__tempt_esp = 0
        self.__bag_utemp = int(passageiro.obtem_bag_pass())
        #self.__bag_utemp = randint(1, int(passageiro.obtem_bag_pass()))

    def muda_inic_atend(self, passageiro):
        self.__inic_atend = passageiro.obtem_ciclo_in()
        self.incr_passt_atend()
        self.muda_numt_bag(passageiro.obtem_bag_pass())
        self.muda_tempt_esp(passageiro)
        self.__bag_utemp = self.obtem_tempt_esp() / self.obtem_numt_bag()

    def __str__(self):
        return "Balcão " + self.obtem_numt_bag() + " tempo " + self.obtem_inic_atend() + " : " + " - "
        #print("Tempo Atual: " + str(int(tempo_atual())))
        #print("Ciclo in passageiro: " + str(int(passageiro.ciclo_in())))
        #print("Tempo atual - tempo do passageiro: " + str(int(tempo_atual() - passageiro.ciclo_in())))

    def incr_passt_atend(self):
        self.__passt_atend += 1

    def muda_numt_bag(self, bag_passageiro):
        self.__numt_bag += bag_passageiro

    def muda_tempt_esp(self, passageiro):
        self.__tempt_esp += (tempo_atual() - passageiro.obtem_ciclo_in())

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

    for i in range(4):
        print("kk")

    lista_passageiros = Queue()
    lista_balcao = []
    n_balcao = input("Quantos balcões:")

    #Criação de passageiros
    for i in range(10):
        lista_passageiros.enqueue(Passageiro(randint(0,5), tempo_atual()))
        print("Criado passageiro " + str(i+1) + "")
        #time.sleep(randint(1,5))

    #print(lista_passageiros)

    #print(lista_passageiros.size())
    #Os primeiros passageiros a ir para o balcão
    for i in range(int(n_balcao)):
        lista_balcao.append(Balcao( (i+1) , lista_passageiros.dequeue() ))
    #print(lista_passageiros.size())

    for i in range(len(lista_passageiros)):

        #balcao1.fila.enqueue(lista_passageiros[i])

    #while not balcao1.fila.isEmpty():
    #    balcao1.muda_inic_atend(balcao1.fila.dequeue())

    print("Tempo total de espera do balcao: "+str(int(balcao1.obtem_temp_esp())))
    print("Total de bagagens despachadas pelo balcao atual é: "+ str(balcao1.obtem_numt_bag()))

    #print(balcao1.obtem_numt_bag())
    #print(balcao1.numt_bag)

    #print(datetime.date(1989,12,21))
    #print(" .. \n ..")
