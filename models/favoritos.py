import json

class Favorito:
    def __init__(self, idJogo, idCliente):
        self.set_idJogo(idJogo)
        self.set_idCliente(idCliente)
    
    def set_idJogo(self, idJogo):
        self.__idJogo = idJogo
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    
    def get_idJogo(self):
        return self.__idJogo
    def get_idCliente(self):
        return self.__idCliente
    
    def __str__(self):
        return f"{self.__idJogo} - {self.__idCliente}"
    @staticmethod
    def to_json(obj):
        return {"idJogo" : obj.get_idJogo(), "idCliente" : obj.get_idCliente()}
    
    @staticmethod
    def from_json(dic):
        return Favorito(dic["idJogo"], dic["idCliente"]) 

class FavoritoDAO:
    objetos = []     
    @classmethod              
    def favoritar(cls, obj : Favorito):
        cls.abrir()
        aux = cls.favoritos_produto(obj.get_idJogo(), obj.get_idCliente())
        if aux == None:
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def favoritos_produto(cls, idJogo, idCliente):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_idJogo() == idJogo and obj.get_idCliente() == idCliente: return obj
        return None
    @classmethod 
    def favoritos(cls, idCliente):
        cls.abrir()
        favoritados = []
        for obj in cls.objetos:
            if obj.get_idCliente() == idCliente: favoritados.append(obj)
        return favoritados
    @classmethod
    def desfavoritar(cls, obj):
        aux = cls.favoritos_produto(obj.get_idJogo(), obj.get_idCliente())
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
    def excluir_lote_idJogo(cls, idJogo):
        cls.abrir()
        for objeto in cls.objetos:
            if objeto.get_idJogo() == idJogo:
                cls.excluir(objeto)
    @classmethod
    def excluir(cls, obj):
        aux = cls.favoritos_Jogo(obj.get_idJogo(), obj.get_idCliente())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("favorito.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default=Favorito.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("favorito.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Favorito.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            