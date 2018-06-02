import pytz
from time import gmtime, strftime
import datetime
import time
from pythonds.basic import Queue
from random import randint
#from pkg.string import names
import names

class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print("O passageiro " + str(self.key) + " de ordem " + str(self.payload) + ".")
        if self.rightChild:
            self.rightChild.inorder()

    def posorder(self):
        if self.leftChild:
            self.leftChild.posorder()
        if self.rightChild:
            self.rightChild.posorder()
        print(self.key)

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)

class Passageiro:

    #name = ""
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

    def obtem_nome(self):
            return self.__nome

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
    #print(lista_aux)

    #for i in range(n_p_atend):
    if fila_de_espera > 0:
        index_balcao_menor_fila = lista_aux.index(min(lista_aux))

        # percorre os balcoes para serem atendidos
        for j in range(len(balcoes)):
            #despacha passageiro
            if not balcoes[j].obtem_fila().isEmpty():
                passageiro_em_atendimento = balcoes[j].obtem_fila().dequeue()
                balcoes[j].muda_inic_atend(passageiro_em_atendimento)
                balcoes[j].incr_passt_atend()
                balcoes[j].muda_numt_bag(passageiro_em_atendimento.obtem_bag_pass())
                balcoes[j].muda_tempt_esp(passageiro_em_atendimento)
                if balcoes[j].obtem_temp_esp() > 0:
                    balcoes[j].__bag_utemp = balcoes[j].obtem_numt_bag() / balcoes[j].obtem_temp_esp()

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

        #mostra_balcoes(balcoes)
    #for i in range(len(balcoes)):
    #    balcoes[i].muda_inic_atend()

def mostra_balcoes(balcoes):
    for balcao in balcoes:
        print(balcao)

def apresenta_resultados(balcoes):
    ficheiro = open('SimpOutpu.txt', 'a')

    for balcao in balcoes:
        if balcao.obtem_passt_atend() > 0:

            print("Balcão " + str(balcao.obtem_n_balcao()) + " despachou " + str(balcao.obtem_bag_utemp()) + " bagagens por ciclo:")
            ficheiro.write(str("Balcão " + str(balcao.obtem_n_balcao()) + " despachou " + str(balcao.obtem_bag_utemp()) + " bagagens por ciclo:\n"))

            media_bag_pass = balcao.obtem_numt_bag()/balcao.obtem_bag_utemp()
            print(str(balcao.obtem_passt_atend()) + " passageiros atendidos com média de bagagens / passageiro = " + str(media_bag_pass))
            ficheiro.write(str(balcao.obtem_passt_atend()) + " passageiros atendidos com média de bagagens / passageiro = " + str(media_bag_pass))

            print("Tempo médio de espera = " + str(balcao.obtem_passt_atend()))
            ficheiro.write(str("Tempo médio de espera = " + str(balcao.obtem_passt_atend())))

    ficheiro.close()

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

    #TODO: Debbugar essa parte
    #for i in range(n_p_atend):
    fila_de_espera_aux = fila_de_espera
    while fila_de_espera > (int(fila_de_espera_aux/2) + 1):
        for balcao in balcoes:
            if fila_de_espera > int(fila_de_espera_aux/2) + 1:
                balcao.obtem_fila().enqueue((Passageiro(randint(1, num_bag), 1)))
                fila_de_espera -= 1

    #while num_pass > 0:
    #Criação de passageiros
    for i in range(1, int(ciclos) + 1):# Atende os passageiros nos balcões
        print("««« CICLO n.º " + str(i) + " »»»")
        for j in range(n_p_atend):
            atende_passageiros(i, balcoes)
        mostra_balcoes(balcoes)
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

def infra():
    global num_pass, lista_passageiros
    #names.get_full_name()
    #names.get_full_name(gender='male')
    #names.get_first_name()
    #names.get_first_name(gender='female')
    #names.get_last_name()

    i = 1
    while True:
        name = names.get_first_name()
        if lista_passageiros.get(name) == None:
            lista_passageiros.put(name, i)
            i += 1
        if i == num_pass + 1:
            break

    lista_passageiros.root.inorder()
    #print(lista_passageiros.size)

ficheiro1 = open('gil.txt', 'a')




if __name__ == '__main__' :

    # Principais variáveis do SIMPAR
    num_pass = 100 # O número de passageiros com bagagem previsto para este voo
    num_bag = 3 # O número máximo de bagagens permitido por passageiro
    num_balcoes = 4 # O número de balcões abertos para atendimento e despacho de bagagem
    ciclos = 10 # Os ciclos de tempo em que a simulação decorre

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
    lista_passageiros = BinarySearchTree()
    infra()

    while True:
        nome = input("Insira um nome para verificar se ele existe na árvore.")
        nome_passagerio = lista_passageiros.get(nome)
        if nome_passagerio != None :
            print("Passageiro " + nome + " existe na árvore.")
        else:
            print("Passageiro " + nome + " não existe na árvore.")
        valor = input("Deseja fazer outra procura? ( 's' para sim e 'n' para não)")
        if valor == 'n':
            break



