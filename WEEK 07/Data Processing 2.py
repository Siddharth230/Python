def courses_sorted_by_enrollment(student_courses: dict) -> list:
    """
    Given a dictionary of student roll numbers
    with the list of courses they chose,
    find the courses sorted from the
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Args:
    student_courses (dict):
        a dictionary where keys are student roll numbers and
        values are lists of courses they chose

    Returns:
    list:
        a list of courses sorted by the number of students enrolled
        in descending order
    """
    c = {}

    for courses in student_courses.values():
        for course in courses:
            c[course] = c.get(course, 0) + 1

    sorted_list = sorted(c, key=c.get, reverse=True)

    return sorted_list
