import streamlit as st
from transformers import pipeline
from googletrans import Translator
import json
import os

from bd import *

# Carregar o pipeline de geração de texto do GPT-2
generator = pipeline('text-generation', model='gpt2')

# Inicializar o tradutor
translator = Translator()

# Define o ícone da aplicação
st.set_page_config(page_title="SpeakFlow", page_icon="speakflow.ico")

# Função para gerar a frase
def generate_sentence(subject, verb, topics):
    prompt = f"{subject} {verb} {' '.join(topics)}"
    result = generator(prompt, max_length=30, num_return_sequences=1)
    generated_text = result[0]['generated_text']
    
    # Parar no primeiro ponto
    if '.' in generated_text:
        generated_text = generated_text.split('.')[0] + '.'
    return generated_text

# Função para traduzir a frase
def translate_text(text, dest_language='pt'):
    translation = translator.translate(text, dest=dest_language)
    return translation.text

# Função para salvar as frases em um arquivo JSON
def save_sentences_to_json(sentences, filename="sentences.json"):
    with open(filename, 'w') as f:
        json.dump(sentences, f)

# Função para carregar as frases de um arquivo JSON
def load_sentences_from_json(filename="sentences.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

# Função para deletar uma frase
def delete_sentence(index):
    if 0 <= index < len(st.session_state.sentences):
        del st.session_state.sentences[index]
        save_sentences_to_json(st.session_state.sentences)

# Função para compartilhar uma frase
def share_sentence(sentence):
    # Aqui você pode implementar a lógica para compartilhar, por exemplo, copiar para a área de transferência, enviar para uma rede social, etc.
    st.write(f"Shared: {sentence}")

# Inicializar a sessão de armazenamento de frases
if 'sentences' not in st.session_state:
    st.session_state.sentences = load_sentences_from_json()

# Elementos da página
st.header("English Sentence Generator")

# Layout de colunas
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    subject = st.selectbox("Subject", list_sujeitos, index=0)

with col2:
    verb = st.selectbox("Verb", list_verbos, index=0)

with col3:
    food = st.selectbox("Food", list_alimentos)

with col4:
    drink = st.selectbox("Drink", list_bebidas)

with col5:
    place = st.selectbox("Place", list_paises)

with col6:
    beach = st.selectbox("Beach", list_lugares)

# Coletar os temas selecionados
selected_topics = []
if food != "None":
    selected_topics.append(food)
if drink != "None":
    selected_topics.append(drink)
if place != "None":
    selected_topics.append(place)
if beach != "None":
    selected_topics.append(beach)

# Botão para gerar a frase, fora da linha dos selectbox
if st.button("Generate Sentence"):
    if selected_topics:
        sentence = generate_sentence(subject, verb, selected_topics)
        translated_sentence = translate_text(sentence, dest_language='pt')
        
        # Adicionar a frase gerada à lista na sessão
        st.session_state.sentences.append({
            'sentence': sentence,
            'translation': translated_sentence
        })

        # Salvar a lista de frases em um arquivo JSON
        save_sentences_to_json(st.session_state.sentences)

        # Mostrar a frase gerada e a tradução em um contêiner
        with st.expander("Generated Sentence and Translation"):
            st.write(f"Sentence: {sentence}")
            st.write(f"Tradução: {translated_sentence}")
    else:
        st.write("Please select at least one topic to generate a sentence.")

# Mostrar todas as frases geradas na sessão com opções de deletar ou compartilhar
st.sidebar.header("Sentence History")
st.sidebar.markdown("""
    <style>
    .sentence-history {
        background-color: #D2B48C;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
                    
    .button-setence {
        background-color: #F4A460;
        border: 1px solid #F4A460;
        border-radius: 5px;
        margin-top: 15px;     
        margin-left: 10px;   
        color: #000000;   
    }
                    
    .title-setence {
        font-weight: bold;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

for i, entry in enumerate(st.session_state.sentences):
    st.sidebar.markdown(f"""
        <div class="sentence-history">
            <b class="title-setence">Sentence {i + 1}:</b> {entry['sentence']}<br>
            <b class="title-setence">Tradução {i + 1}:</b> {entry['translation']}<br>
            <button class="button-setence" onclick="window.location.href='/?delete={i}'">delete</button>
            <button class="button-setence" onclick="window.location.href='/?share={i}'">share</button>
        </div>
    """, unsafe_allow_html=True)

# Verificar se o usuário clicou em deletar ou compartilhar
params = st.query_params

if 'delete' in params:
    delete_sentence(int(params['delete'][0]))
    st.query_params  # Limpa os parâmetros da URL

if 'share' in params:
    share_sentence(st.session_state.sentences[int(params['share'][0])]['sentence'])
    st.query_params  # Limpa os parâmetros da URL
