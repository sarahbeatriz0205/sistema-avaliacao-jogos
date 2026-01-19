import json
from models.classe_dao import DAO

class Jogados:
    def __init__(self, idJogo, idCliente):
        self.set_id(idJogo)
        self.set_idCliente(idCliente)
    
    def set_id(self, idJogo):
        self.__id = idJogo
    
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente

    def get_id(self):
        return self.__id
    def get_idCliente(self):
        return self.__idCliente

class JogadosDAO:
c
    @classmethod 
    def jogados_cliente(cls, idCliente):
        cls.abrir()
        jogados_cliente = []
        for obj in cls.objetos:
            if obj.get_idCliente() == idCliente: jogados_cliente.append(obj)
        return jogados_cliente
    @classmethod
    def jogados_cliente_jogo(cls, idJogo, idCliente):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_idJogo() == idJogo and obj.get_idCliente() == idCliente: return obj
        return None
    @classmethod
    def excluir_jogado(cls, obj):
        aux = cls.jogados_cliente_jogo(obj.get_id(), obj.get_idCliente())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def excluir_lote_idCliente(cls, idCliente):
        cls.abrir()
        for objeto in cls.objetos:
            if objeto.get_idCliente() == idCliente:
                cls.excluir(objeto)
    @classmethod
    def excluir_lote_id(cls, id):
        cls.abrir()
        for objeto in cls.objetos:
            if objeto.get_id() == id:
                cls.excluir(objeto)
    @classmethod
    def excluir(cls, obj):
        aux = cls.Jogados(obj.get_id(), obj.get_idCliente())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("jogados.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default=Jogados.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("jogados.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Jogados.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            
