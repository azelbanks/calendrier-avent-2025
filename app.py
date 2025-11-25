import streamlit as st
from datetime import datetime
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Mon Calendrier de l'Avent",
    page_icon="🎄",
    layout="wide"
)

# --- CSS PERSONNALISÉ POUR LE STYLE FESTIF ---
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        height: 100px;
        background-color: #D42426;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        border: 2px solid #1E5128;
    }
    .stButton>button:hover {
        background-color: #1E5128;
        color: #F0D566;
        border-color: #D42426;
    }
    .day-content {
        padding: 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
        text-align: center;
        border: 2px dashed #1E5128;
    }
</style>
""", unsafe_allow_html=True)

# --- CONTENU DES SURPRISES (À PERSONNALISER) ---
# Vous pouvez mettre du texte, des liens images, ou des liens YouTube
surprises = {
    1: {"type": "text", "content": "🍫 C'est le début ! Prends un chocolat."},
    2: {"type": "text", "content": "🎄 Citation : La meilleure façon de répandre la joie de Noël est de chanter fort pour que tout le monde entende."},
    3: {"type": "image", "content": "https://media.giphy.com/media/3o6fJdYXEWMaCIzyrC/giphy.gif"}, # GIF Exemple
    4: {"type": "text", "content": "🍪 Recette du jour : Fais des sablés !"},
    # ... Remplissez jusqu'au 24 ...
    24: {"type": "text", "content": "🎅 JOYEUX NOËL !"}
}

# Fonction pour remplir les jours manquants avec du contenu par défaut pour l'exemple
for i in range(1, 25):
    if i not in surprises:
        surprises[i] = {"type": "text", "content": f"🎁 Surprise du jour {i} !"}

# --- INITIALISATION DE L'ÉTAT (SESSION STATE) ---
if 'opened_doors' not in st.session_state:
    st.session_state.opened_doors = []

# --- LOGIQUE DE DATE ---
# Pour tester l'application AVANT décembre, décommentez la ligne ci-dessous :
# current_date = datetime(2023, 12, 10) # Simulation au 10 Décembre
current_date = datetime.now() # Date réelle

st.title("🎅 Calendrier de l'Avent 2024 ⛄")
st.write(f"Nous sommes le : **{current_date.strftime('%d/%m/%Y')}**")

# --- GRILLE DU CALENDRIER ---
# On crée une grille de 6 rangées de 4 colonnes (24 jours)
cols = st.columns(4)

for day in range(1, 25):
    # Calcul de l'index de la colonne (0, 1, 2 ou 3)
    col_index = (day - 1) % 4
    
    with cols[col_index]:
        # --- LOGIQUE D'OUVERTURE ---
        
        # Cas 1 : La case est déjà ouverte
        if day in st.session_state.opened_doors:
            st.info(f"Jour {day}")
            content = surprises[day]
            if content["type"] == "text":
                st.markdown(f"<div class='day-content'>{content['content']}</div>", unsafe_allow_html=True)
            elif content["type"] == "image":
                st.image(content["content"])
        
        # Cas 2 : La case est fermée, on affiche le bouton
        else:
            if st.button(f"Jour {day}", key=f"btn_{day}"):
                # Vérification de la date
                # On vérifie si on est en décembre ET si le jour est atteint
                if current_date.month == 12 and current_date.day >= day:
                    st.balloons() # Animation festive
                    st.session_state.opened_doors.append(day)
                    st.rerun() # Recharge la page pour afficher le contenu
                
                # Si on essaie d'ouvrir trop tôt
                elif current_date.month != 12:
                    st.error(f"Patience ! Nous ne sommes pas encore en Décembre.")
                else:
                    st.warning(f"Patience ! Tu ne peux pas encore ouvrir la case du {day}.")

st.markdown("---")
st.caption("Fait avec ❤️ sur Streamlit")