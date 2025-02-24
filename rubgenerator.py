
import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Laad GPT-2 model en tokenizer van Hugging Face
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Kruiden en vleesopties
kruiden = {
    "Anijszaad": "kruidig",
    "Basilicum": "kruidig",
    "Bieslook": "kruidig",
    "Bonenkruid": "kruidig",
    "Citroenmelisse": "fris",
    "Citroengras": "fris",
    "Citroenrasp": "fris",
    "Citroentijm": "fris",
    "Kaneel": "kruidig",
    "Kardemom": "kruidig",
    "Karwijzaad": "kruidig",
    "Kervel": "kruidig",
    "Korianderzaad": "kruidig",
    "Komijn": "kruidig",
    "Kurkuma": "kruidig",
    "Dille": "fris",
    "Dragon": "kruidig",
    "Fenegriek": "kruidig",
    "Foelie": "kruidig",
    "Gemberpoeder": "kruidig",
    "Goudsbloem": "fris",
    "Himalayazout": "kruidig",
    "Honingpoeder": "fris",
    "Kerrieblad": "kruidig",
    "Knoflookpoeder": "kruidig",
    "Lavas (maggiplant)": "kruidig",
    "Laurierblad": "kruidig",
    "Munt": "fris",
    "Nootmuskaat": "kruidig",
    "Oregano": "kruidig",
    "Paprikapoeder (zoet, gerookt, pikant)": "rokerig",
    "Peper (wit, zwart, groen, roze)": "pittig",
    "Peterselie": "fris",
    "Rozemarijn": "kruidig",
    "Safraan": "kruidig",
    "Salie": "kruidig",
    "Selderijblad": "fris",
    "Sereh (citroengras)": "fris",
    "Steranijs": "kruidig",
    "Tijm": "kruidig",
    "Ui-poeder": "kruidig",
    "Vanillepoeder": "zoet",
    "Venkelzaad": "kruidig",
    "Witte Mosterdzaad": "kruidig",
    "BBQ Rub": "rokerig",
    "Cajun Mix": "pittig",
    "Jerk Seasoning": "pittig",
    "Blackened Seasoning": "pittig",
    "Tex-Mex Rub": "pittig",
    "Chinese Vijfkruidenpoeder": "kruidig",
    "Garam Masala": "kruidig",
    "Tandoori Masala": "kruidig",
    "Ras el Hanout": "kruidig",
    "Herbes de Provence": "kruidig",
    "Italiaanse Kruidenmix": "kruidig",
    "Za’atar": "kruidig",
    "Baharat": "kruidig",
    "Bouquet Garni": "kruidig",
    "Beenhamspek Kruidenmix": "kruidig",
    "Franse Kruidenmix": "kruidig",
    "Bruine Suiker Rub": "zoet",
    "Kaneel-Suiker Mix": "zoet",
    "Chai Masala": "kruidig"
}

vleesopties = ["Kip", "Rund", "Varken", "Wild", "Vis"]
smaakprofielen = ["Pittig", "Kruidig", "Rokerig", "Fris"]

# Functie om een recept te genereren met GPT-2
def generate_recipe(kruiden, vlees):
    # Maak een prompt voor GPT-2
    prompt = f"Maak een recept voor een kruidenrub voor {vlees} met de volgende kruiden: {', '.join(kruiden)}. Geef de hoeveelheden in theelepels."

    # Tokenize de prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Genereer een antwoord van GPT-2
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return generated_text

# Streamlit app
st.title("Kruidenrub Generator")

# Kruidenkeuze
selected_kruiden = st.multiselect("Selecteer minimaal twee kruiden", list(kruiden.keys()))

# Vleeskeuze
selected_vlees = st.selectbox("Kies het type vlees", vleesopties)

# Smaakprofiel
smaakprofiel = st.radio("Kies een smaakprofiel", smaakprofielen)

# Genereer rub
if len(selected_kruiden) >= 2:
    rub = generate_recipe(selected_kruiden, selected_vlees)
    st.write(f"Recept voor je rub met {', '.join(selected_kruiden)} voor {selected_vlees}:

{rub}")
else:
    st.error("Selecteer minimaal twee kruiden!")
