def get_course_filters(
    active: bool | None = None,
    search: str | None = None,
):
    return {'active': active, 'search': search}
