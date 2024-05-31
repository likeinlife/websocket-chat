from fastapi import APIRouter, Response, status

router = APIRouter()


@router.get(
    "/health/",
    summary="Проверка состояния сервиса",
    status_code=status.HTTP_200_OK,
)
def healthcheck() -> Response:
    """Check if service healthy."""
    return Response(status_code=status.HTTP_200_OK)
