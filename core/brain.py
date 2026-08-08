from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Olá, eu sou o PETER"
)

texto = interaction.output_text
