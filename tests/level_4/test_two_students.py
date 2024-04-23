from functions.level_4.two_students import get_student_by_tg_nickname


def test__get_student_by_tg_nickname__return_student_if_nickname_in_list(make_student):
    students = [
        make_student(telegram_account="alfa"),
        make_student(telegram_account="beta"),
        make_student(telegram_account="gamma"),
        make_student(telegram_account=None),
    ]

    assert get_student_by_tg_nickname("alfa", students) == students[0]


def test__get_student_by_tg_nickname__return_none_if_no_such_nickname(make_student):
    students = [
        make_student(telegram_account="alfa"),
        make_student(telegram_account="beta"),
        make_student(telegram_account="gamma"),
        make_student(telegram_account=None),
    ]

    assert get_student_by_tg_nickname("epsilon", students) is None


def test__get_student_by_tg_nickname__return_none_if_no_students():
    students = []

    assert get_student_by_tg_nickname("alfa", students) is None
