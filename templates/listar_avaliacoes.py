import streamlit as st
import pandas as pd
import time
from views import View

class ListarAvaliacaoUI:
    def main():
        st.title("Veja as avaliações da galera")
        tab1, tab2, tab3 = st.tabs(["Listar", "Atualizar", "Excluir"])
        with tab1: ListarAvaliacaoUI.listar_avaliacoes()
        with tab2: ListarAvaliacaoUI.atualizar_avaliacoes()
        with tab3: ListarAvaliacaoUI.excluir_avaliacoes()

    def listar_avaliacoes():
        avaliacoes = View.avaliacao_listar()
        if avaliacoes == None: 
            st.write("Nenhuma avaliação feita até o momento")
        else:
            list_dic = []
            for a in avaliacoes: list_dic.append(a.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "idCliente", "idJogo", "avaliacao"])
    
    def atualizar_avaliacoes():
        idCliente = st.session_state["cliente_id"]
        avaliacoes = View.avaliacao_listar_cliente(idCliente)
        if len(avaliacoes) == 0: st.write("Nenhuma avaliação feita até o momento")
        else:
            st.selectbox("Atualizar avaliação", avaliacoes)
            for percorre_avaliacoes in avaliacoes:
                r = st.text_input(f"Avaliação {percorre_avaliacoes["id"]} do jogo {percorre_avaliacoes["idJogo"]}", percorre_avaliacoes["avaliacao"])
                if st.button("Atualizar", key=f"{percorre_avaliacoes["id"]}"):
                    try:
                        View.avaliacao_atualizar(idCliente, percorre_avaliacoes["idJogo"], percorre_avaliacoes["avaliacao"])
                        st.success("Avaliação atualizada com sucesso!")
                        time.sleep(1)
                        st.rerun()
                    except Exception as erro:
                        st.error(f"{erro}")
    def excluir_avaliacoes():
        idCliente = st.session_state["cliente_id"]
        avaliacoes = View.avaliacao_listar_cliente(idCliente) or []
        if len(avaliacoes) == 0: st.write("Nenhuma resenha salva até o momento")
        else:
            op = st.selectbox("Excluir avaliação", avaliacoes)
            if op:
                if st.button("Excluir"):
                    View.resenha_excluir(op["id"], op["idCliente"], op["idJogo"], op["resenha"])
                    st.success("Avaliação excluída com sucesso!")
                    time.sleep(2)
                    st.rerun()