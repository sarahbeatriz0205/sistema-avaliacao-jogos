import streamlit as st
import time
from views import View
from models.favoritos import Favorito

class ListarJogosUI:
    def main():
        st.title("🎮 Catálogo de jogos")
        st.write("Escreva resenhas e curta seus jogos favoritos!")
        jogos = View.jogos_listar()
        pesquisa = st.text_input("Pesquise seu jogo aqui")
        if st.button("Buscar"):
            resultado = View.pesquisar_jogos(pesquisa)
            if resultado:
                    j = View.jogos_listar_id(resultado)
                    col = st.columns(1)
                    st.success("1 jogo foi encontrado!")
                    if col:
                        st.write(j.get_descricao()) 
                        st.image(j.get_imagem(), width=200)
            else:
                st.error("Nenhum jogo encontrado")
        idCliente = st.session_state["cliente_id"]
        avaliacoes = View.avaliacao_listar()
        cols_por_linha = 4 
        for j in range(0, len(jogos), cols_por_linha): 
            cols = st.columns(cols_por_linha, gap="medium", vertical_alignment="bottom")
            for i, jogo in enumerate(jogos[j:j+cols_por_linha]):
                with cols[i]:
                    st.write(jogo.get_descricao())
                    st.image(jogo.get_imagem())
                    idJogo = str(jogo.get_id())
                    if st.button("Favoritar", key=f"salvar_{jogo.get_id()}_{idCliente}"):
                        obj = Favorito(jogo.get_id(), idCliente)
                        View.favoritar(obj)
                        st.success("Jogo favoritado com sucesso!")
                        time.sleep(1)
                        st.rerun()
                    with st.form(key=f"avaliacao_{jogo.get_id()}_{idCliente}"): 
                        nota = st.slider("Avalie de 0 a 10", min_value=0, max_value=10, key=f"slider_{jogo.get_id()}_{idCliente}")
                        if st.form_submit_button("Salvar"):
                            try:
                                View.avaliacao_inserir(idCliente, jogo.get_id(), nota) 
                                st.success("Nota dada! Agradecemos!") 
                                time.sleep(1)
                                st.rerun()
                            except Exception as erro:
                                st.error(f"{erro}")
                    resenha = st.text_area(f"Escreva sua resenha aqui sobre esse jogo aqui", key=jogo.get_descricao())
                    if st.button("Salvar resenha", key=idJogo):
                        try:
                            View.resenha_inserir(jogo.get_id(), idCliente, resenha)
                            st.success("Resenha salva com sucesso! Acesse 'Minhas resenhas' para vê-las!")
                            time.sleep(1)
                            st.rerun()
                        except Exception as erro:
                            st.error(f"{erro}")