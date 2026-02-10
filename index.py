import streamlit as st
from views import View
from templates.criar_conta import CriarContaUI
from templates.login import LoginUI
from templates.listar_jogos import ListarJogosUI
from templates.manter_categorias_adm import ManterCategoriaUI
from templates.manter_cliente_adm import ManterClienteUI
from templates.manter_jogos_adm import ManterJogosUI
from templates.listar_resenha import ListarResenhaUI
from templates.listar_favoritos import ManterFavoritoUI
from templates.listar_avaliacoes import ListarAvaliacaoUI


class IndexUI:
        def menu_visitante():
                op = st.selectbox("Entre no sistema ou crie sua conta", ["Entrar no sistema", 
                                                                        "Criar Conta"])
                if op == "Entrar no sistema": LoginUI.main()
                if op == "Criar Conta": CriarContaUI.main()
        def menu_cliente():
                op = st.sidebar.selectbox("Menu", ["Catálogo de jogos",
                                        "Meus favoritos",
                                        "Acompanhar resenhas",
                                        "Acompanhar avaliações"])
                if op == "Catálogo de jogos": ListarJogosUI.main()
                if op == "Acompanhar resenhas": ListarResenhaUI.main()
                if op == "Meus favoritos": ManterFavoritoUI.main()
                if op == "Acompanhar avaliações": ListarAvaliacaoUI.main()
        def menu_admin():
                # st.sidebar.selectbox: caixa de seleção
                op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", 
                                        "Cadastro de Clientes", 
                                        "Cadastro de Jogos"])
                
                # ao clicar, direciono o usuário para a página correspode àquela opção
                if op == "Cadastro de Categorias": ManterCategoriaUI.main()
                if op == "Cadastro de Clientes": ManterClienteUI.main()
                if op == "Cadastro de Jogos": ManterJogosUI.main()

        
        def sidebar():
                if "cliente_id" not in st.session_state: IndexUI.menu_visitante()
                else:
                        st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
                        admin = st.session_state["cliente_email"] == "admin@"
                        if admin: IndexUI.menu_admin()
                        else: IndexUI.menu_cliente()
                        IndexUI.sair_do_sistema() 

        def sair_do_sistema():
                if st.sidebar.button("Sair"):
                        del st.session_state["cliente_id"]
                        del st.session_state["cliente_nome"]
                        st.rerun()
        def main():
                View.cliente_criar_admin("admin@", "admin")
                IndexUI.sidebar() 


IndexUI.main()