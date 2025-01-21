from app.domain.services.image_processor import extract_text_from_image, caption_image
from app.core.llm_client import solve_with_gpt

async def solve_question(image_bytes: bytes) -> dict:
    """
    Resolve a questão combinando OCR e CLIP.
    """
    # Extrai texto da imagem
    text = await extract_text_from_image(image_bytes)
    print(text)
    analysis = await caption_image(image_bytes)
    print(analysis)
    # Formata os dados para o LLM
    combined_input = f"Texto da questão: {text}\nAnálise visual: {analysis}"

    # Resolve com GPT
    solution = solve_with_gpt(combined_input)

    return {"text": text, "visual_analysis": clip_analysis, "solution": solution}
