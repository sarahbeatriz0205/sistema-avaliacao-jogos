from models.cliente import Cliente, ClienteDAO
from models.categorias import Categoria, CategoriaDAO
from models.jogos import Jogos, JogosDAO
from models.favoritos import Favorito, FavoritoDAO
from models.jogados import Jogados, JogadosDAO
from models.classe_dao import DAO

class View:
    @staticmethod
    def cliente_criar_admin(email="admin@", senha="admin"):
        id = None
        nome = "Administrador"
        telefone = 84999999999
        for obj in ClienteDAO.listar():
            if obj.get_email() == "admin@" and obj.get_senha() == "admin": return
        ClienteDAO.inserir(Cliente(id, nome, email, telefone, senha)) # se o if não for verdadeiro, ele passa para a próxima linha e cria um novo admin
    @staticmethod
    def cliente_autenticar(email, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email and obj.get_senha() == senha: 
                return { "id" : obj.get_id(), "nome" : obj.get_nome(), "email": obj.get_email(), "senha" : obj.get_senha()}
        return None
    @staticmethod
    def get_cliente_id(email, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email and obj.get_senha() == senha: 
                return obj.get_id()
        return None
    def cliente_inserir(nome, email, senha):
        id = 0
        if nome == "" or email == "" or senha == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        if "0" in nome or "1" in nome or "2" in nome or "3" in nome or "4" in nome or "5" in nome or "6" in nome or "7" in nome or "8" in nome or "9" in nome:
            raise ValueError("Erro! O nome fornecido não pode conter números.")
        if "@" not in email:
            raise ValueError("Erro! O email fornecido é inválido.")
        c = Cliente(id, nome, email, senha)
        ClienteDAO.inserir(c)
      
    def cliente_listar():
        return ClienteDAO.listar()
    
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_atualizar(id, nome, email, telefone, senha):
        if nome == "" or email == "" or telefone == "" or senha == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        if "0" in nome or "1" in nome or "2" in nome or "3" in nome or "4" in nome or "5" in nome or "6" in nome or "7" in nome or "8" in nome or "9" in nome:
            raise ValueError("Erro! O nome não pode conter números.")
        if "@" not in email:
            raise ValueError("Erro! O email fornecido é inválido.")
        ddds_brasil = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 64, 63, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 87, 82, 83, 84, 85, 88,86, 89, 91, 93, 94, 92, 97, 95, 96, 98, 99]
        if len(telefone) == 0 or int(telefone[:2]) not in ddds_brasil:
            raise ValueError("Erro! O número de telefone fornecido é inválido.")
        c = Cliente(id, nome, email, telefone, senha)
        ClienteDAO.atualizar(c)
        
    def cliente_excluir(id, nome, email, telefone, senha):
        c = Cliente(id, nome, email, telefone, senha)
        JogadosDAO.excluir_lote_idCliente(id)
        FavoritoDAO.excluir_lote_idCliente(id)
        ClienteDAO.excluir(c)

    def categoria_inserir(descricao):
        id = 0
        if descricao == "":
            raise ValueError("Erro! O preenchimento desse campo é obrigatório.")
        if "0" in descricao or "1" in descricao or "2" in descricao or "3" in descricao or "4" in descricao or "5" in descricao or "6" in descricao or "7" in descricao or "8" in descricao or "9" in descricao:
            raise ValueError("Erro! A descrição não pode conter números.")
        CategoriaDAO.inserir(Categoria(id, descricao))
    def categoria_listar():
        return CategoriaDAO.listar()
    def categoria_listar_id(id):
        return CategoriaDAO.listar_id(id)
    def categoria_atualizar(id, descricao):
        if descricao == "":
            raise ValueError("Erro! O preenchimento desse campo é obrigatório.")
        if descricao.isnumeric():
            raise ValueError("Erro! A descrição não pode ser numérica.")
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)
    def categoria_excluir(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.excluir(c)

    def jogos_inserir(id, descricao, idCategoria, idJogados):
        id = 0
        if descricao == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        c = Jogos(id, descricao, idCategoria, idJogados)
        JogosDAO.inserir(c)
    def jogos_listar():
        return JogosDAO.listar()
    def jogos_listar_id(id):
        return JogosDAO.listar_id(id)
    def jogos_atualizar(id, descricao, idCategoria, idJogados):
        if descricao == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        c = Jogos(id, descricao, idCategoria, idJogados)
        JogosDAO.atualizar(c)
    def jogos_excluir(id, descricao, idCategoria, idJogados):
        c = Jogos(id, descricao, idCategoria, idJogados)
        JogosDAO.excluir(c)
        FavoritoDAO.excluir_lote_idJogo(id)
    def listar_jogos(descricao):
        for obj in JogosDAO.listar():
            if obj.get_descricao() == descricao:
                return obj
        return f"Jogo não encontrado!"
    
    def inserir_jogados(idJogo, idCliente):
        j = Jogados(idJogo, idCliente)
        JogadosDAO.marcar_jogado(j)
    def jogados_cliente(idCliente):
        return JogadosDAO.jogados_cliente(idCliente)
    def excluir_jogado(idJogo, idCliente):
        j = Jogados(idJogo, idCliente)
        JogadosDAO.excluir_jogado(j)