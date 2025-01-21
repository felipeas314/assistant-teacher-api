from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


# Configuração da API Key

def solve_with_gpt(input_data: str) -> str:
    """
    Usa o modelo GPT-4 para interpretar e resolver o problema.
    """
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um professor especialista em resolver questões de Física, Matemática, Química e Biologia."},
            {"role": "user", "content": input_data}
        ],
        max_tokens=500,
        temperature=0.7)
        return response.choices[0].message.content.strip()
    except Exception as e:  # Captura erros genéricos
        raise ValueError(f"Erro ao acessar o OpenAI API: {str(e)}")
