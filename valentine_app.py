import streamlit as st
import streamlit.components.v1 as components
import random

# Configuração da página
st.set_page_config(page_title="Para o meu Dengo", page_icon="💖")

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
</style>
""", unsafe_allow_html=True)

# Mecanismo de estado para rastrear o progresso
if 'app_state' not in st.session_state:
    st.session_state['app_state'] = {
        'asked': True,
        'started': False,
        'finished': False,
        'error_count': 0
    }

# --- TELA 1: O PEDIDO ---
if st.session_state['app_state']['asked'] and not st.session_state['app_state']['started']:
    st.markdown('<p class="big-font">Você quer sair com o dengo para comemorar o dia dos namorados?</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2]) # Deixando a coluna 2 maior pro botão ter espaço pra fugir
    
    with col1:
        st.write("") # Espaçamento
        st.write("")
        if st.button("Sim, eu amo ele", type="primary"):
            st.session_state['app_state']['asked'] = False
            st.session_state['app_state']['started'] = True
            st.rerun()
            
    with col2:
        # Botão Fujão usando HTML e JavaScript puro
        btn_html = """
        <div style="position: relative; width: 100%; height: 300px;">
            <button id="btn-no" style="
                position: absolute; 
                top: 20px; 
                left: 20px; 
                padding: 10px 20px; 
                border: 1px solid #ff4b4b; 
                border-radius: 8px; 
                background-color: #ffe0e0; 
                color: #ff4b4b;
                font-family: 'Open Sans', sans-serif;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: 0.1s; /* Movimento suave */
            ">não, odeio ele</button>
        </div>
        <script>
            const btn = document.getElementById('btn-no');
            btn.addEventListener('mouseover', function() {
                // Sorteia novas posições quando o mouse passa por cima
                const newTop = Math.random() * 250; 
                const newLeft = Math.random() * 300; 
                btn.style.top = newTop + 'px';
                btn.style.left = newLeft + 'px';
            });
        </script>
        """
        components.html(btn_html, height=350)

# --- TELA 2: O QUIZ ---
if st.session_state['app_state']['started'] and not st.session_state['app_state']['finished']:
    st.markdown('<p class="big-font">Ok, dengo! Mas antes você precisa provar que me conhece!</p>', unsafe_allow_html=True)
    st.balloons() # Confete de boas-vindas
    
    q1_ans = st.text_input("Qual o nome completo do amor da sua vida?", placeholder="Nome completo aqui").strip().lower()
    q2_ans = st.text_input("Qual dia e mês (no formato DD/MM) que a gente começou a namorar?", placeholder="e.g., 01/01").strip()
    q3_ans = st.text_input("Quanto que amô ama ela?", placeholder="Pense grande...").strip().lower()
    q4_ans = st.text_input("Onde a gente geralmente faz nossos dates?", placeholder="Aonde você quer ir?").strip().lower()
    
    if st.button("Enviar Respostas"):
        correct_a1 = "matheus haug"
        correct_a2 = "07/06"
        correct_a3 = "infinito"
        correct_a4 = "madeiro"
        
        is_q1_correct = q1_ans == correct_a1
        is_q2_correct = q2_ans == correct_a2
        is_q3_correct = q3_ans == correct_a3 or "muito" in q3_ans or "pra caramba" in q3_ans 
        is_q4_correct = q4_ans == correct_a4
        
        if is_q1_correct and is_q2_correct and is_q3_correct and is_q4_correct:
            st.session_state['app_state']['started'] = False
            st.session_state['app_state']['finished'] = True
            st.balloons() 
            st.rerun()
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
            st.snow()

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