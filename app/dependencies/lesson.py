def get_lesson_filters(
    course_id: int | None = None,
    active: bool | None = None,
):
    return {'course_id': course_id, 'active': active}
