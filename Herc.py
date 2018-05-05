class Contacto:

    def __init__(self, nome, email, telefone, aniversario):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.aniversario = aniversario

class Aluno(Contacto):

    def __init__(self, n_aluno, curso, ano, turma, notas, nome, email, telefone, aniversario):
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

if __name__ == '__main__':

    notas = [ 3, 5, 12, 1, 19 ,2]

    print(min(notas))
    print(notas.index(min(notas)))

    aluno = Aluno("12312", "Automação Industrial", "2012", "D", notas, "Jailson", "jailsonmc@gmail.com", "123 432 432", "1964-12-12")

    print(aluno.nome)