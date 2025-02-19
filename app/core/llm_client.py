from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


# Configuração da API Key

def solve_with_gpt(input_data: str) -> str:
    #print(inp)
    """
    Usa o modelo GPT-4 para interpretar e resolver o problema.
    """

    prompt = f"""
    Você é um professor altamente experiente e especialista em resolver questões de Matemática, Física, Química e Biologia. Sua missão é não apenas resolver a questão, mas *explicá-la de forma didática, passo a passo, como se estivesse ensinando um aluno que não tem um bom conhecimento prévio*.

    Por favor, siga este formato ao responder:

    1 - *Enunciado*: Reescreva a questão recebida para garantir que foi interpretada corretamente.

    2 - *Conceitos Fundamentais*: Antes de resolver, explique os conceitos teóricos necessários para entender a questão.

    3 - *Passo a Passo da Solução*: Resolva o problema de maneira organizada, detalhando cada etapa do raciocínio.

    4 - *Resposta Final*: Destaque a resposta final e explique seu significado.

    5 - *Aplicação Prática (Opcional)*: Se possível, forneça um exemplo do mundo real onde esse conceito pode ser aplicado.

    ⚠️ *Regras Importantes*:
    - Use uma linguagem simples e acessível.
    - Evite pular etapas, explique *como e por que* cada passo é feito.
    - Se houver diferentes maneiras de resolver, mencione as alternativas.

    Agora, resolva a seguinte questão e siga essas diretrizes: 

    {input_data}
    """

    try:
        response = client.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt}
            #{"role": "user", "content": input_data}
        ],
        max_tokens=1500,
        temperature=0.9)
        print(response.choices[0].message.content.strip())
        return response.choices[0].message.content.strip()
    except Exception as e:  # Captura erros genéricos
        raise ValueError(f"Erro ao acessar o OpenAI API: {str(e)}")
