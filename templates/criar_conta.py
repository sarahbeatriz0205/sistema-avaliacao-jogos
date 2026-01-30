import streamlit as st
import time
from views import View

class CriarContaUI:
    def main():
        st.header("Criar Conta")

        nome = st.text_input("Nome completo")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Criar Conta"):
            try:
                View.cliente_inserir(nome, email, senha)
                st.success("Conta criada com sucesso!", icon="✅")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(f"{erro}")