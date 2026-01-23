import json
from models.classe_dao import DAO

class Jogos:
    def __init__(self, idJogo, descricao, idCategoria):
        self.set_id(idJogo)
        self.set_descricao(descricao)
        self.set_idCategoria(idCategoria)
    
    def set_id(self, id):
        self.__id = id

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_idCategoria(self, idCategoria):
        self.__idCategoria = idCategoria

    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_idCategoria(self):
        return self.__idCategoria
    
    def to_json(self):
        return {"id" : self.__id, "descricao" : self.__descricao, "idCategoria" : self.__idCategoria} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Jogos(dic["id"], dic["descricao"], dic["idCategoria"])
    
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - Categoria {self.__idCategoria}"


class JogosDAO(DAO):
    objetos = []
    @classmethod
    def excluir_lote_idJogo(cls, idJogo):
        cls.abrir()
        for objeto in cls.venda_item:
            if objeto.get_id() == idJogo:
                cls.excluir(objeto)
    def pesquisa_jogos(cls, descricao):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_descricao() == descricao: return obj
        return None
    @classmethod
    def salvar(cls):
        with open("jogos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Jogos.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("jogos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Jogos.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass