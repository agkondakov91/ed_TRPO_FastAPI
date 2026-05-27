from fastapi import HTTPException, status


def raise_not_found(resource_name: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f'{resource_name} not found'
    )
