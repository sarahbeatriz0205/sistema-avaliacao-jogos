import json
from models.classe_dao import DAO

class Resenha:
    def __init__(self, id, idCliente, idJogo, resenha):
        self.set_id(id)
        self.set_idCliente(idCliente)
        self.set_idJogo(idJogo)
        self.set_resenha(resenha)
    
    def set_id(self, id):
        self.__id = id
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    def set_idJogo(self, idJogo):
        self.__idJogo = idJogo
    def set_resenha(self, resenha):
        self.__resenha = resenha
    

    def get_id(self):
        return self.__id
    def get_idCliente(self):
        return self.__idCliente
    def get_idJogo(self):
        return self.__idJogo
    def get_resenha(self):
        return self.__resenha
    
    def __str__(self):
        return f"Id da resenha: {self.__id} - Seu id (cliente): {self.__idCliente} - Id do jogo avaliado: {self.__idJogo} - Sua resenha: {self.__resenha}"
    
    def to_json(self):
        return {"id" : self.__id, "idCliente": self.__idCliente,"idJogo" : self.__idJogo ,"resenha" : self.__resenha}
    @staticmethod
    def from_json(dic):
        return Resenha(dic["id"], dic["idCliente"], dic["idJogo"], dic["resenha"]) 

class ResenhaDAO(DAO):
    objetos = []
    @classmethod
    def excluir_lote_idCliente(cls, idCliente):
        cls.abrir()
        for objeto in cls.objetos:
            if objeto.get_idCliente() == idCliente:
                cls.excluir(objeto)
    @classmethod
    def listar_resenha_cliente(cls, idCliente):
        cls.abrir()
        resenhas = []
        for objeto in cls.objetos:
            if objeto.get_idCliente() == idCliente:
                resenhas.append(objeto)
        return resenhas 
    @classmethod
    def salvar(cls):
        with open("resenhas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default =Resenha.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("resenhas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Resenha.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            