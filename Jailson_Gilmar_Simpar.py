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

    def __init__(self, n_balcao):
        self.__n_balcao = n_balcao
        self.__fila = Queue()
        self.__inic_atend = 0
        self.__passt_atend = 0
        self.__numt_bag = 0
        self.__tempt_esp = 0
        self.__bag_utemp = 0
        #self.__bag_utemp = randint(1, int(passageiro.obtem_bag_pass()))

    def muda_inic_atend(self):
        passageiro_em_atendimento = self.obtem_fila().pop()
        self.__inic_atend = passageiro_em_atendimento.obtem_ciclo_in()
        self.incr_passt_atend()
        self.muda_numt_bag(passageiro_em_atendimento.obtem_bag_pass())
        self.muda_tempt_esp(passageiro_em_atendimento)
        self.__bag_utemp = self.obtem_numt_bag() / self.obtem_tempt_esp()

    def __str__(self):
        return "Balcão " + str(self.obtem_numt_bag()) + " tempo " + str(self.obtem_inic_atend()) + " : " + " - "
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

def atende_passageiros(i, balcoes, num_balcoes, ciclos):
    lista_aux = []
    ciclos = int(ciclos)
    if i < int(ciclos/3):
        for balcao in balcoes:
            lista_aux.append(balcao.obtem_fila().size())
        balcoes[lista_aux.index(min(lista_aux))].obtem_fila().enqueue((Passageiro(num_balcoes, tempo_atual() )))
    elif i >= int(ciclos/3) and i < int(2*ciclos/3):
        percetagem = randint(1, 100)
        if percetagem <= 80:
            balcoes[lista_aux.index(min(lista_aux))].obtem_fila().enqueue((Passageiro(num_balcoes, tempo_atual() )))
    else:
        percetagem = randint(1, 100)
        if percetagem <= 60:
            balcoes[lista_aux.index(min(lista_aux))].obtem_fila().enqueue((Passageiro(num_balcoes, tempo_atual() )))
    mostra_balcoes(balcoes)

def mostra_balcoes(balcoes):
    for balcao in balcoes:
        print(balcao)

def simpar_simula(num_pass, num_bag, num_balcoes, ciclos):

    lista_balcao = []
    for i in range(int(num_balcoes)):
        lista_balcao.append(Balcao( i+1 ))

    #Criação de passageiros
    for i in range(1, int(ciclos) + 1):
        print("««« CICLO n.º " + str(i) + " »»»")
        atende_passageiros(i, lista_balcao, num_balcoes, ciclos)
        #lista_passageiros.enqueue(Passageiro(randint(0,num_bag), tempo_atual()))
        #print("Criado passageiro " + str(i+1) + "")
        #time.sleep(randint(1,5))



    #for i in range(len(lista_passageiros)):

    #balcao1.fila.enqueue(lista_passageiros[i])

    #while not balcao1.fila.isEmpty():
    #    balcao1.muda_inic_atend(balcao1.fila.dequeue())

    #print("Tempo total de espera do balcao: "+str(int(balcao1.obtem_temp_esp())))
    #print("Total de bagagens despachadas pelo balcao atual é: "+ str(balcao1.obtem_numt_bag()))

    #print(balcao1.obtem_numt_bag())
    #print(balcao1.numt_bag)

    #print(datetime.date(1989,12,21))
    #print(" .. \n ..")

if __name__ == '__main__' :

    cont = True
    while cont:
        num_pass = input("Número de passageiros:")
        if int(num_pass) > 0:
            cont = False

    cont = True
    while cont:
        num_bag  = input("Número de máximo de bagagens por passageiro:")
        if int(num_bag) > 0:
            cont = False

    cont = True
    while cont:
        num_balcoes = input("Número de balcoes:")
        if int(num_balcoes) > 0:
            cont = False

    cont = True
    while cont:
        ciclos = input("Os ciclos de tempo em que a simulação ocorre:")
        if int(ciclos) > 0:
            cont = False

    simpar_simula(num_pass, num_bag, num_balcoes, ciclos)


