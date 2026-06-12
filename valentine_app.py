import streamlit as st
import random
import time

# Configuração da página
st.set_page_name("Para o meu Dengo")
st.set_page_icon("💖")

# Adicionando um pouco de estilo romântico
st.markdown("""
<style>
    .big-font {
        font-size:30px !important;
        font-family: 'Open Sans', sans-serif;
        color: #ff4b4b;
        font-weight: bold;
    }
    .quiz-question {
        font-size:20px !important;
        color: #4b4b4b;
    }
    .vales {
        font-size:24px !important;
        color: #ff4b4b;
        font-weight: bold;
        text-align: center;
        background-color: #ffe0e0;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #ff4b4b;
    }
    /* Estilo para o botão "Não" pulando */
    #no_button {
        position: absolute;
        width: 150px;
        height: 50px;
    }
</style>
""", unsafe_allow_html=True)

# Mecanismo de estado para rastrear o progresso e a posição do botão
if 'app_state' not in st.session_state:
    st.session_state['app_state'] = {
        'asked': True,
        'started': False,
        'finished': False,
        'no_button_pos': {'top': '60%', 'left': '60%'},
        'error_count': 0
    }

def move_no_button():
    # Gera novas posições aleatórias
    new_top = f"{random.randint(10, 80)}%"
    new_left = f"{random.randint(10, 80)}%"
    st.session_state['app_state']['no_button_pos'] = {'top': new_top, 'left': new_left}
    st.experimental_rerun()

# --- TELA 1: O PEDIDO ---
if st.session_state['app_state']['asked'] and not st.session_state['app_state']['started']:
    st.markdown('<p class="big-font">Você quer sair com o dengo para comemorar o dia dos namorados?</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Sim, eu amo ele"):
            st.session_state['app_state']['asked'] = False
            st.session_state['app_state']['started'] = True
            st.experimental_rerun()
            
    with col2:
        # Posição do botão "Não" do estado
        pos = st.session_state['app_state']['no_button_pos']
        # Usando CSS inline para mover o botão
        no_button_html = f"""
        <div style="position: absolute; top: {pos['top']}; left: {pos['left']}; width: 150px; height: 50px;">
            <button id="no_button" style="width: 100%; height: 100%; color: #4b4b4b; border: 1px solid #4b4b4b; border-radius: 4px; background-color: #ffcccc;">não, odeio ele</button>
        </div>
        """
        st.markdown(no_button_html, unsafe_allow_html=True)
        # O botão "Não" é apenas visual, o JavaScript no navegador não move ele nativamente no Streamlit
        # Vamos fazer o Streamlit re-renderizar em um clique normal.
        if st.button("não, odeio ele"):
            move_no_button()

# --- TELA 2: O QUIZ ---
if st.session_state['app_state']['started'] and not st.session_state['app_state']['finished']:
    st.markdown('<p class="big-font">Ok, dengo! Mas antes você precisa provar que me conhece!</p>', unsafe_allow_html=True)
    st.balloons() # Confete de boas-vindas
    
    q1_ans = st.text_input("Qual o nome completo do amor da sua vida?", placeholder="Nome completo aqui").strip().lower()
    q2_ans = st.text_input("Qual dia e mês (no formato DD/MM) que a gente começou a namorar?", placeholder="e.g., 01/01").strip()
    q3_ans = st.text_input("Quanto que o amô ama você?", placeholder="Pense grande...").strip().lower()
    q4_ans = st.text_input("Onde a gente geralmente faz nossos dates?", placeholder="Aonde você quer ir?").strip().lower()
    
    if st.button("Enviar Respostas"):
        # Respostas Corretas (normalizadas)
        correct_a1 = "matheus haug"
        correct_a2 = "07/06"
        correct_a3 = "infinito"
        correct_a4 = "madeiro"
        
        # Lógica de verificação
        is_q1_correct = q1_ans == correct_a1
        is_q2_correct = q2_ans == correct_a2
        is_q3_correct = q3_ans == correct_a3 or "muito" in q3_ans or "pra caramba" in q3_ans # Toque de flexibilidade
        is_q4_correct = q4_ans == correct_a4
        
        if is_q1_correct and is_q2_correct and is_q3_correct and is_q4_correct:
            st.session_state['app_state']['started'] = False
            st.session_state['app_state']['finished'] = True
            st.balloons() # Confete de vitória
            st.experimental_rerun()
        else:
            st.session_state['app_state']['error_count'] += 1
            error_messages = [
                "Humm, tente de novo, dengo! Algo não está certo.",
                "Poxa, amô, acho que você errou uma.",
                "Vamos lá, você consegue! Pense bem.",
                "Certeza? Tente ler com mais carinho.",
                "Você me conhece, dengo! Eu acredito."
            ]
            error_msg = random.choice(error_messages)
            st.error(error_msg)
            st.snow() # Neve para dar um gelinho no erro

# --- TELA 3: A TELA FINAL COM FOTOS ---
if st.session_state['app_state']['finished']:
    st.markdown('<p class="big-font">PARABÉNS, MEU AMOR!</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="vales">
        Você acertou tudo! 🎉
        <br>
        Está liberado um vale madeiro e um vale dengo! Use com sabedoria. 😉
    </div>
    """, unsafe_allow_html=True)
    st.balloons()
    
    # Galeria de fotos
    st.markdown('<p class="quiz-question" style="text-align: center; margin-top: 30px;">Alguns dos nossos momentos...</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    try:
        with col1:
            st.image("image_0.png", use_column_width=True)
            st.image("image_1.png", use_column_width=True)
        with col2:
            st.image("image_2.png", use_column_width=True)
            st.image("image_3.png", use_column_width=True)
    except FileNotFoundError:
        st.warning("As imagens 'image_0.png', 'image_1.png', 'image_2.png', e 'image_3.png' não foram encontradas. Salve-as na mesma pasta do código para vê-las aqui!")

    st.markdown('<p class="quiz-question" style="text-align: center; margin-top: 20px;">Te amo infinito! 💖<br>Com carinho, Matheus</p>', unsafe_allow_html=True)