from pydantic import BaseModel

class QuestionResponse(BaseModel):
    text: str
    visual_analysis: str
    solution: str