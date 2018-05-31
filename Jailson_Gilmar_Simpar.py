import pytz
from time import gmtime, strftime
import datetime
import time
from pythonds.basic import Queue
from random import  randint

class Passageiro:

    name = ""
    """ bag_pass : número de bagagens do passageiro """
    """ ciclo_in : instante em que foi colocado na fila (número do ciclo da simulação) """
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

    def __init__(self, n_balcao, num_bag):
        self.__n_balcao = n_balcao
        self.__fila = Queue()
        self.__inic_atend = 0
        self.__passt_atend = 0
        self.__numt_bag = 0
        self.__tempt_esp = 0
        self.__bag_utemp = randint(1 ,int(num_bag))

    def muda_inic_atend2(self):
        passageiro_em_atendimento = self.obtem_fila().enqueue(self)
        self.__inic_atend += passageiro_em_atendimento.obtem_ciclo_in()

    def muda_inic_atend(self,passageiro_em_atendimento):
        self.__inic_atend += passageiro_em_atendimento.obtem_ciclo_in()

    def __str__(self):
        if not self.obtem_fila().isEmpty():
            lista_aux = self.obtem_fila()
            return "Balcão " + str(self.obtem_n_balcao()) + " tempo " + str(self.obtem_inic_atend()) + " : " + " - " + lista_aux.size()*str(lista_aux.dequeue()) + " - "
        else:
            return "Balcão " + str(self.obtem_n_balcao()) + " tempo " + str(self.obtem_inic_atend()) + " : " + " - "

    def incr_passt_atend(self):
        self.__passt_atend += 1

    def muda_numt_bag(self, bag_passageiro):
        self.__numt_bag += bag_passageiro

    def muda_tempt_esp(self, passageiro):
        self.__tempt_esp += passageiro.obtem_ciclo_in()

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

def atende_passageiros(i, balcoes):
    global num_pass, num_bag, num_balcoes, ciclos, n_p_atend, fila_de_espera
    # for balcao in balcoes:
    #     if balcao.obtem_fila().size() > 0:
    #         if balcao.obtem_fila().dequeue().obtem_bag_pass()
    lista_aux = []
    for balcao in balcoes:
        lista_aux.append(balcao.obtem_fila().size())
    #for i in range(n_p_atend):
    if fila_de_espera > 0:
        index_balcao_menor_fila = lista_aux.index(min(lista_aux))

        #despacha passageiro
        if not balcoes[index_balcao_menor_fila].obtem_fila().isEmpty():
            passageiro_em_atendimento = balcoes[index_balcao_menor_fila].obtem_fila().dequeue()
            balcoes[index_balcao_menor_fila].muda_inic_atend(passageiro_em_atendimento)
            balcoes[index_balcao_menor_fila].incr_passt_atend()
            balcoes[index_balcao_menor_fila].muda_numt_bag(passageiro_em_atendimento.obtem_bag_pass())
            balcoes[index_balcao_menor_fila].muda_tempt_esp(passageiro_em_atendimento)
            if balcoes[index_balcao_menor_fila].obtem_temp_esp() > 0:
                balcoes[index_balcao_menor_fila].__bag_utemp = balcoes[index_balcao_menor_fila].obtem_numt_bag() / balcoes[index_balcao_menor_fila].obtem_temp_esp()

        #recebe passageiro
        if i < ciclos/3 :
            balcoes[index_balcao_menor_fila].obtem_fila().enqueue((Passageiro(randint(1,num_bag), i )))
            fila_de_espera -= 1
        elif i >= ciclos/3 and i < 2*ciclos/3:
            percetagem = randint(1, 100)
            if percetagem <= 80:
                balcoes[index_balcao_menor_fila].obtem_fila().enqueue((Passageiro(randint(1,num_bag), i )))
                fila_de_espera -= 1
        else:
            percetagem = randint(1, 100)
            if percetagem <= 60:
                balcoes[index_balcao_menor_fila].obtem_fila().enqueue((Passageiro(randint(1,num_bag), i )))
                fila_de_espera -= 1

        mostra_balcoes(balcoes)
    #for i in range(len(balcoes)):
    #    balcoes[i].muda_inic_atend()

def mostra_balcoes(balcoes):
    for balcao in balcoes:
        print(balcao)

def apresenta_resultados(balcoes):
    for balcao in balcoes:
        if balcao.obtem_passt_atend() > 0:
            print("Balcão " + str(balcao.obtem_n_balcao()) + " despachou " + str(balcao.obtem_bag_utemp()) + " bagagens por ciclo:")
            media_bag_pass = balcao.obtem_numt_bag()/balcao.obtem_bag_utemp()
            print(str(balcao.obtem_passt_atend()) + " passageiros atendidos com média de bagagens / passageiro = " + str(media_bag_pass))
            print("Tempo médio de espera = " + str(balcao.obtem_passt_atend()))

def existem_balcoes_com_fila(balcoes):
    for balcao in balcoes:
        if balcao.obtem_fila().size() > 0:
            return True
    return False

def simpar_simula():
    global num_pass, num_bag, num_balcoes, ciclos, n_p_atend, fila_de_espera
    # Cria os balcões
    balcoes = []
    for i in range(num_balcoes):
        balcoes.append(Balcao( i+1 , num_bag ))

    for i in range(n_p_atend):
        for balcao in balcoes:
            if fila_de_espera > 0:
                balcao.obtem_fila().enqueue((Passageiro(randint(1,num_bag), 1 )))
                fila_de_espera -= 1

    #while num_pass > 0:
    #Criação de passageiros
    for i in range(1, int(ciclos) + 1):# Atende os passageiros nos balcões
        print("««« CICLO n.º " + str(i) + " »»»")
        for j in range(n_p_atend):
            atende_passageiros(i, balcoes)
    #apresenta_resultados(balcoes)
    print("Fechou a chegada de novos passageiros")
    ciclos += 1

    #print("Há "+str(fila_de_espera) + " passageiros restantes na fila de espera.")
    #mostra_balcoes(balcoes)
    while fila_de_espera > 0:
        print("««« CICLO n.º " + str(ciclos) + " »»»")
        ciclos += 1
        for i in range(n_p_atend):
            for balcao in balcoes:
                if fila_de_espera > 0:
                    balcao.obtem_fila().enqueue((Passageiro(randint(1,num_bag), 1 )))
                    fila_de_espera -= 1
        apresenta_resultados(balcoes)


    print("Há "+str(fila_de_espera) + " passageiros restantes na fila de espera.")
    #mostra_balcoes(balcoes)
    #while existem_balcoes_com_fila(balcoes):
    #    print("««« CICLO n.º " + str(i) + " »»»")
    #    atende_passageiros(i, balcoes, ciclos, num_bag)
    #apresenta_resultados(balcoes)
    #num_pass -= 1
    #apresenta_resultados(balcoes)

if __name__ == '__main__' :

    # Principais variáveis do SIMPAR
    num_pass = 100 # O número de passageiros com bagagem previsto para este voo
    num_bag = 3 # O número máximo de bagagens permitido por passageiro
    num_balcoes = 4 # O número de balcões abertos para atendimento e despacho de bagagem
    ciclos = 20 # Os ciclos de tempo em que a simulação decorre

    fila_de_espera = num_pass
    n_p_atend = 3

    if 4 == 5:
        cont = True
        while cont:
            try:
                num_pass = int(input("Digite o número de passageiros com bagagem previsto para este voo:"))
                if num_pass > 0:
                    cont = False
                else:
                    print("Valor precisa ser maior que zero.")
            except:
                print("Valor inválido.")

        fila_de_espera = num_pass
        cont = True
        while cont:
            try:
                num_bag  = int(input("Digite o número máximo de bagagens permitido por passageiro:"))
                if num_bag > 0:
                    cont = False
                else:
                    print("Valor precisa ser maior que zero.")
            except:
                print("Valor inválido.")

        cont = True
        while cont:
            try:
                num_balcoes = int(input("Digite o número de balcões abertos para atendimento e despacho de bagagem:"))
                if num_balcoes > 0:
                    cont = False
                else:
                    print("Valor precisa ser maior que zero.")
            except:
                print("Valor inválido.")

        cont = True
        while cont:
            try:
                ciclos = int(input("Digite os ciclos de tempo em que a simulação decorre:"))
                if ciclos > 0:
                    cont = False
                else:
                    print("Valor precisa ser maior que zero.")
            except:
                print("Valor inválido.")

        cont = True
        while cont:
            try:
                n_p_atend = int(input("Digite o total de passageiros atendidos por ciclos:"))
                if ciclos > 0:
                    cont = False
                else:
                    print("Valor precisa ser maior que zero.")
            except:
                print("Valor inválido.")

    simpar_simula()


