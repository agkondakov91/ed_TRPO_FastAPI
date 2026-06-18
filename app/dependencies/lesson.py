from fastapi import Query


def get_lesson_filters(
    course_id: int | None = None,
    active: bool | None = None,
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return {'course_id': course_id, 'active': active, 'limit': limit, 'offset': offset}
