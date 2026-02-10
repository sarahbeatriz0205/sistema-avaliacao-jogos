from models.cliente import Cliente, ClienteDAO
from models.categorias import Categoria, CategoriaDAO
from models.jogos import Jogos, JogosDAO
from models.favoritos import Favorito, FavoritoDAO
from models.resenha import Resenha, ResenhaDAO
from models.avaliacoes import Avaliacoes, AvaliacoesDAO

class View:
    @staticmethod
    def cliente_criar_admin(email="admin@", senha="admin"):
        id = None
        nome = "Administrador"
        for obj in ClienteDAO.listar():
            if obj.get_email() == "admin@" and obj.get_senha() == "admin": return
        ClienteDAO.inserir(Cliente(id, nome, email, senha)) 
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
        if nome == "" or email == "" or senha == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        if "0" in nome or "1" in nome or "2" in nome or "3" in nome or "4" in nome or "5" in nome or "6" in nome or "7" in nome or "8" in nome or "9" in nome:
            raise ValueError("Erro! O nome não pode conter números.")
        if "@" not in email:
            raise ValueError("Erro! O email fornecido é inválido.")
        c = Cliente(id, nome, email, telefone, senha)
        ClienteDAO.atualizar(c)
        
    def cliente_excluir(id, nome, email, telefone, senha):
        c = Cliente(id, nome, email, telefone, senha)
        ResenhaDAO.excluir_lote_idCliente(id)
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

    def jogos_inserir(id, descricao, idCategoria, imagem):
        id = 0
        if descricao == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        c = Jogos(id, descricao, idCategoria, imagem)
        JogosDAO.inserir(c)
    def jogos_listar():
        return JogosDAO.listar()
    def jogos_listar_id(id):
        return JogosDAO.listar_id(id)
    def jogos_atualizar(id, descricao, idCategoria, imagem):
        if descricao == "":
            raise ValueError("Erro! O preenchimento de todos os campos é obrigatório.")
        c = Jogos(id, descricao, idCategoria, imagem)
        JogosDAO.atualizar(c)
    def jogos_excluir(id, descricao, idCategoria, imagem):
        c = Jogos(id, descricao, idCategoria, imagem)
        JogosDAO.excluir(c)
        FavoritoDAO.excluir_lote_idJogo(id)
    def listar_jogos(descricao):
        for obj in JogosDAO.listar():
            if obj.get_descricao() == descricao:
                return obj
        return f"Jogo não encontrado!"
    
    #def inserir_jogados(idJogo, idCliente):
       # j = Jogados(idJogo, idCliente)
        #JogadosDAO.marcar_jogado(j)
    #def jogados_cliente(idCliente):
     #   return JogadosDAO.jogados_cliente(idCliente)
    #def excluir_jogado(idJogo, idCliente):
     #   j = Jogados(idJogo, idCliente)
      #  JogadosDAO.excluir_jogado(j)

    def favoritar(obj):
        f = JogosDAO.listar_id(obj.get_idJogo())
        if f != None:
            FavoritoDAO.favoritar(obj)
    def desfavoritar(obj):
        f = JogosDAO.listar_id(obj.get_idJogo())
        if f != None:
            FavoritoDAO.desfavoritar(obj)
    def produtos_favoritos(idCliente):
        fav = []
        favoritos = FavoritoDAO.favoritos(idCliente)
        for f in favoritos:
            produto = JogosDAO.listar_id(f.get_idJogo())
            fav.append({
            "idJogo": produto.get_id(),
            "Jogo": produto.get_descricao(),
        })
        if len(fav) == 0:
            return None 
        return fav
    def lista_favoritados(idCliente):
        fav = []
        favoritos = FavoritoDAO.favoritos(idCliente)
        for f in favoritos:
            produto = JogosDAO.listar_id(f.get_id())
            fav.append([produto.get_id(), produto.get_descricao()])
        return fav
    def resenha_inserir(idJogo, idCliente, resenha):
        id = 0
        c = Resenha(id, idCliente, idJogo, resenha)
        ResenhaDAO.inserir(c)
    
    def resenha_listar():
        return ResenhaDAO.listar()
    
    def resenha_listar_id(id):
        return ResenhaDAO.listar_id(id)
    
    def resenha_listar_cliente(idCliente):
        res = []
        resenhas = ResenhaDAO.listar_resenha_cliente(idCliente)
        for r in resenhas:
            opiniao_cliente = ResenhaDAO.listar_id(r.get_id())
            res.append({
            "id": opiniao_cliente.get_id(),
            "idJogo": opiniao_cliente.get_idJogo(),
            "idCliente" : opiniao_cliente.get_idCliente(),
            "resenha" : opiniao_cliente.get_resenha()
        })
        if len(res) == 0:
            return []
        return res

    def resenha_atualizar(id, idCliente, idJogo, resenha):
        c = Resenha(id, idCliente, idJogo, resenha)
        ResenhaDAO.atualizar(c)
        
    def resenha_excluir(id, idCliente, idJogo, resenha):
        c = Resenha(id, idCliente, idJogo, resenha)
        ResenhaDAO.excluir_lote_idCliente(id)
        ResenhaDAO.excluir(c)
    
    def pesquisar_jogos(descricao):
        jogos = JogosDAO.listar()
        for obj in jogos:
            if obj.get_descricao() == descricao: 
                return obj.get_id()
        return None
        
    def avaliacao_inserir(idCliente, idJogo, avaliacao):
        id = 0
        c = Avaliacoes(id, idCliente, idJogo, avaliacao)
        AvaliacoesDAO.inserir(c)
    
    def avaliacao_listar():
        return AvaliacoesDAO.listar()

    def avaliacao_atualizar(idCliente, idJogo, avaliacao):
        id = 0
        c = Avaliacoes(id, idCliente, idJogo, avaliacao)
        AvaliacoesDAO.atualizar(c)
        
    def avaliacao_excluir(idCliente, idJogo, avaliacao):
        id = 0
        c = Avaliacoes(id, idCliente, idJogo, avaliacao)
        AvaliacoesDAO.excluir_lote_idCliente(idCliente)
        AvaliacoesDAO.excluir(c)
    
    def avaliacao_listar_cliente(idCliente):
        av = []
        avaliacoes = ResenhaDAO.listar_resenha_cliente(idCliente)
        for a in avaliacoes:
            av_cliente = AvaliacoesDAO.listar_id(a.get_id())
            av.append({
            "id": av_cliente.get_id(),
            "idCliente" : av_cliente.get_idCliente(),
            "idJogo": av_cliente.get_idJogo(),
            "avaliacao" : av_cliente.get_avaliacao()
        })
        if len(av) == 0:
            return []
        return av
