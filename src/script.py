import openai

# Remplace par ta clé API
openai.api_key = "****"

try:
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",  # Modèle spécifique
        messages=[
            {"role": "system", "content": "Tu es GPT-4. Réponds uniquement comme GPT-4."},
            {"role": "user", "content": "Quel modèle es-tu ?"}
        ],
        max_tokens=50
    )
    print("Modèle utilisé :", response["model"])
    print("Réponse de l'API :")
    print(response.choices[0].message.content.strip())
except Exception as e:
    print(f"Erreur lors de l'appel à l'API : {e}")