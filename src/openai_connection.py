import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer la clé API depuis .env
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("La clé API OpenAI n'est pas définie dans le fichier .env.")

# Configurer OpenAI
openai.api_key = api_key

def ask_openai(prompt, model="gpt-4", temperature=0.7, max_tokens=150):
    """
    Fonction pour envoyer une requête à l'API OpenAI avec le nouveau format.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "Tu es un assistant utile."},
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except openai.error.OpenAIError as e:
        print(f"Erreur lors de l'appel à l'API OpenAI : {e}")
        return None
