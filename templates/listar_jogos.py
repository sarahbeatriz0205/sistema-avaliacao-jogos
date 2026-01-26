import streamlit as st
import time
from views import View
from models.favoritos import Favorito

class ListarJogosUI:
    def main():
        st.title("🎮 Catálogo de jogos")
        st.selectbox("Busque seu jogo pela sua categoria preferida!", View.categoria_listar())
        jogos = View.jogos_listar()
        idCliente = st.session_state["cliente_id"]
        cols_por_linha = 4 
        for j in range(0, len(jogos), cols_por_linha): 
            cols = st.columns(cols_por_linha, gap="medium", vertical_alignment="bottom")
            for i, jogo in enumerate(jogos[j:j+cols_por_linha]):
                with cols[i]:
                    st.write(jogo.get_descricao())
                    st.image(jogo.get_imagem(), width="content")
                    idJogo = str(jogo.get_id())
                    if st.button("Favoritar", key=f"salvar_{jogo.get_id()}_{idCliente}"):
                        obj = Favorito(jogo.get_id(), idCliente)
                        View.favoritar(obj)
                        st.success("Jogo favoritado com sucesso!")
                        time.sleep(2)
                        st.rerun()
                    resenha = st.text_area(f"Escreva sua resenha aqui sobre esse jogo aqui", key=jogo.get_descricao())
                    if st.button("Salvar resenha", key=idJogo):
                        try:
                            View.resenha_inserir(jogo.get_id(), idCliente, resenha)
                            st.success("Resenha salva com sucesso! Acesse 'Minhas resenhas' para vê-las!")
                            time.sleep(1)
                            st.rerun()
                        except Exception as erro:
                            st.error(f"{erro}")