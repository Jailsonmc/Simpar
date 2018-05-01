
class Contacto:

    def __init__(self, nome, email, telefone, aniversario):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.aniversario = aniversario

class Aluno(Contacto):

    def __init__(self, n_aluno, curso, ano, turma, notas, nome,  email, telefone, aniversario):
        super(). __init__(nome, email, telefone, aniversario)
        self.n_aluno = n_aluno
        self.curso = curso
        self.ano = ano
        self.turma = turma
        self.notas = notas


class Professor(Contacto):

    def __init__(self, n_professor, nome,  email, telefone, aniversario):
        super(). __init__(nome, email, telefone, aniversario)
        self.nome = n_professor
