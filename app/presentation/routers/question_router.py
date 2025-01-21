from fastapi import APIRouter, UploadFile, HTTPException
from app.domain.services.solve_question_service import solve_question
from app.presentation.schemas.question_schemas import QuestionResponse

router = APIRouter()

@router.post("/solve", response_model=QuestionResponse)
async def solve_question_endpoint(image: UploadFile):
    """
    Endpoint para resolver questões enviadas pelo aluno.
    """
    try:
        image_bytes = await image.read()
        result = await solve_question(image_bytes)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a questão: {str(e)}")
