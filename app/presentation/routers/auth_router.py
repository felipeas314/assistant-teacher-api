from fastapi import APIRouter, Depends, HTTPException, status
from app.core.database import get_database
from app.presentation.schemas.auth_schemas import RegisterRequest, RegisterResponse, LoginResponse, LoginRequest
from app.infrastructure.repositories_impl.user_repository_impl import UserRepositoryMongo
from app.domain.services.user_service import UserService

router = APIRouter()

@router.post("/register", response_model=RegisterResponse)
async def register_user(
    payload: RegisterRequest,
    database=Depends(get_database),
):
    user_repo = UserRepositoryMongo(database)
    user_service = UserService(user_repo)

    try:
        created_user = await user_service.register_user(payload.email, payload.password)
        return RegisterResponse(id=created_user.id, email=created_user.email)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

@router.post("/login", response_model=LoginResponse)
async def login_user(
    payload: LoginRequest,
    database=Depends(get_database),  # Injeta o banco de dados
):
    # Instancia o repositório e o serviço
    user_repo = UserRepositoryMongo(database)
    user_service = UserService(user_repo)

    # Autentica o usuário
    token = await user_service.authenticate_user(payload.email, payload.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )

    # Retorna o token de acesso
    return LoginResponse(access_token=token)