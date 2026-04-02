import streamlit as st

# Configuração da página para um título bonitinho
st.set_page_config(page_title="Momento Fofo", page_icon="❤️")

# --- CSS PARA O FUNDO DE CORAÇÕES E ESTILO ---
st.markdown("""
    <style>
    .stApp {
        background-color: #ffb6c1;
        background-image: url("https://www.transparenttextures.com/patterns/hearts.png");
    }
    
    h1, h2, h3, p, label {
        color: #d63384 !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }

    .stTextInput > div > div > input {
        border-color: #ff69b4;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DO APP ---

st.title("Um recadinho especial... ❤️")

# 1. Pergunta o nome dela
nome_dela = st.text_input("Oi, quem é você?", placeholder="Digite seu nome aqui...")

if nome_dela:
    st.subheader(f"Oi, {nome_dela}! ✨")
    
    # 2. Pergunta o seu nome
    meu_nome = st.text_input("E qual o meu nome?", placeholder="Quem sou eu para você?")
    
    if meu_nome:
        if meu_nome.lower() == "dengo":
            st.write(f"Isso mesmo! Eu sou o seu **{meu_nome}**! 🥰")
            
            # 3. Pergunta o que ela está fazendo
            o_que_faz = st.text_input(f"O que você está fazendo agora, {nome_dela}?")
            
            if o_que_faz:
                st.write(f"Olha só: a **{nome_dela}** está **{o_que_faz}**! Que amor.")
                
                # 4. Pergunta o que você está fazendo
                o_que_eu_faco = st.text_input("E eu, o que estou fazendo?")
                
                if o_que_eu_faco:
                    # Resposta final romântica
                    st.divider()
                    st.balloons() # Efeito de balões para comemorar
                    st.header("Resumo do nosso momento:")
                    st.write(f"Você é a **{nome_dela}** e está **{o_que_faz}**.")
                    st.write(f"E eu sou o seu **{meu_nome}** e estou **{o_que_eu_faco}**.")
                    
                    st.markdown("### ❤️ Amo falar com você! ❤️")