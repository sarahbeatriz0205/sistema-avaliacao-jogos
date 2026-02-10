import json
from models.classe_dao import DAO

class Avaliacoes:
    def __init__(self, id, idCliente, idJogo, avaliacao):
        self.set_id(id)
        self.set_idCliente(idCliente)
        self.set_idJogo(idJogo)
        self.set_avaliacao(avaliacao)

    def set_id(self, id):
        self.__id =id
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    def set_idJogo(self, idJogo):
        self.__idJogo = idJogo
    def set_avaliacao(self, avaliacao):
        self.__avaliacao = avaliacao
    
    def get_id(self):
        return self.__id
    def get_idCliente(self):
        return self.__idCliente
    def get_idJogo(self):
        return self.__idJogo
    def get_avaliacao(self):
        return self.__avaliacao
    
    def __str__(self):
        return f"Id da avaliação: {self.__id} - Id do cliente: {self.__idCliente} - Id do jogo avaliado: {self.__idJogo} - Nota dada: {self.__resenha}"
    
    def to_json(self):
        return {"id": self.__id, "idCliente": self.__idCliente,"idJogo" : self.__idJogo ,"avaliacao" : self.__avaliacao}
    @staticmethod
    def from_json(dic):
        return Avaliacoes(dic["id"], dic["idCliente"], dic["idJogo"], dic["avaliacao"])
    

class AvaliacoesDAO(DAO):
    objetos = []

    @classmethod
    def excluir_lote_idCliente(cls, idCliente):
        cls.abrir()
        for objeto in cls.objetos:
            if objeto.get_idCliente() == idCliente:
                cls.excluir(objeto)
    @classmethod
    def salvar(cls):
        with open("avaliacoes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default =Avaliacoes.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("avaliacoes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Avaliacoes.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass     