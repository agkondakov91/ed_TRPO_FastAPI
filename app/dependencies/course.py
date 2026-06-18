from fastapi import Query


def get_course_filters(
    active: bool | None = None,
    search: str | None = None,
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return {
        'active': active,
        'search': search,
        'limit': limit,
        'offset': offset,
    }
