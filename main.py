class aluno :
    def __init__(self,nome, nota1, nota2):
      
        self.__Nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2
    
    def set_nome(self, novo_nome):
        self.__Nome = novo_nome

    def get_nome(self):
        return self.__Nome
       
    def set_nota1(self, nova_nota1):
        self.__nota1 = nova_nota1

    def get_nota1(self):
        return self.__nota1

    def set_nota2(self, nova_nota2):
        self.__nota2 = nova_nota2

    def get_nota2(self):
        return self.__nota2
   
   
    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 
    def exibir_informacoes(self):
        media = self.calcular_media()
        print(f"Nome: {self.__Nome}, média: {ou media:.2f} "o)

aluno1 = aluno("igor", 8 , 9)
aluno1.exibir_informacoes()

aluno1.set_nome("lucas")
aluno1.set_nota1(10)
aluno1.set_nota2(7)
aluno1.exibir_informacoes()

aluno1.set_nome("juliana")
aluno1.set_nota1(8)
aluno1.set_nota2(3)
aluno1.exibir_informacoes()
