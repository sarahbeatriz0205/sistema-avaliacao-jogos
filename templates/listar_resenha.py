import streamlit as st
import pandas as pd
import time
from views import View

class ListarResenhaUI:
    def main():
        st.title("O que a galera está achando dos jogos?")
        tab1, tab2, tab3 = st.tabs(["Listar", "Atualizar", "Excluir"])
        with tab1: ListarResenhaUI.listar_resenha()
        with tab2: ListarResenhaUI.atualizar_resenha()
        with tab3: ListarResenhaUI.excluir_resenha()

    def listar_resenha():
        resenhas = View.resenha_listar()
        if resenhas == None: 
            st.write("Nenhuma resenha salva até o momento")
        else:
            list_dic = []
            for r in resenhas: list_dic.append(r.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "idCliente", "idJogo", "resenha"])
    
    def atualizar_resenha():
        idCliente = st.session_state["cliente_id"]
        resenhas = View.resenha_listar_cliente(idCliente)
        if len(resenhas) == 0: st.write("Nenhuma resenha salva até o momento")
        else:
            st.selectbox("Atualizar resenha", resenhas)
            for percorre_resenhas in resenhas:
                r = st.text_input(f"Resenha {percorre_resenhas["id"]}", percorre_resenhas["resenha"])
                if st.button("Atualizar", key=f"{percorre_resenhas["id"]}"):
                    try:
                        View.resenha_atualizar(percorre_resenhas["id"], idCliente, percorre_resenhas["idJogo"], r)
                        st.success("Possível resenha atualizada e averiguada com sucesso!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as erro:
                        st.error(f"{erro}")
    def excluir_resenha():
        idCliente = st.session_state["cliente_id"]
        resenhas = View.resenha_listar_cliente(idCliente) or []
        if len(resenhas) == 0: st.write("Nenhuma resenha salva até o momento")
        else:
            op = st.selectbox("Excluir resenhas", resenhas)
            if op:
                if st.button("Excluir"):
                    View.resenha_excluir(op["id"], op["idCliente"], op["idJogo"], op["resenha"])
                    st.success("Resenha excluída com sucesso!")
                    time.sleep(2)
                    st.rerun()