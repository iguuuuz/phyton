class Aluno:
    def __init__(self, nome, nota1=0.0, nota2=0.0):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nota1(self, nota1):
        if 0.0 <= nota1 <= 10.0:  
            self.__nota1 = nota1
        else:
            raise ValueError("A nota 1 deve estar entre 0 e 10")

    def get_nota1(self):
        return self.__nota1

    def set_nota2(self, nota2):
        if 0.0 <= nota2 <= 10.0:  
            self.__nota2 = nota2
        else:
            raise ValueError("A nota 2 deve estar entre 0 e 10")

    def get_nota2(self):
        return self.__nota2

    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2