def read_file(filename: str) -> dict:
    pass


def set_mark(gradebook: dict, surname: str, activiry: str, grade: float | None) -> dict:
    pass


def set_mark_from_file(gradebook: dict, activity: str, filename: str) -> dict:
    pass


def add_activity(gradebook: dict, activities: dict, activity: str, max_marl: float) -> (dict, dict):
    pass


def del_activity(gradebook: dict, activities: dict, activity: str) -> (dict, dict):
    pass


def student_total(gradebook: dict, surname: str, activities_list: list) -> float:
    pass


def sort_students(gradebook: dict, sort_by: str, activity: str = None) -> dict:
    """
    Function which returns a sorted list of students, based on activity, activity type, or general academic success.
    pass an activity type to sort_by as second argument
    pass activity to activity as third argument
    pass "курс" to activity for general course points comparison

    >>> sort_students(\
{('Stone', 'Oleskandr', 'sasha.kaminb.pn@ucu.edu.ua', 'ba'):\
{"Лабораторні роботи":\
{"Лабораторна робота 1" : 1,\
"Лабораторна робота 2" : 1,\
"Лабораторна робота 3" : 1,\
"Лабораторна робота 4" : 1,\
"Лабораторна робота 5" : 1,\
"Лабораторна робота 6" : 1,\
"Лабораторна робота 7" : 1,\
"Лабораторна робота 8" : 1,\
"Лабораторна робота 9" : 1,\
"Лабораторна робота 10" : 1,\
"Лабораторна робота 11" : 1,\
"Лабораторна робота 12" : 1},\
"Проміжний іспит":\
{"Теоретичне завдання": 2,\
"Завдання на програмування": 2.3},\
"Тести по лекційним матеріалам":\
{"Тест 1" : 0.37,\
"Тест 2" : 0.37,\
"Тест 3" : 0.37,\
"Тест 4" : 0.37,\
"Тест 5" : 0.37,\
"Тест 6" : 0.37,\
"Тест 7" : 0.37,\
"Тест 8" : 0.37,\
"Тест 9" : 0.37,\
"Тест 10" : 0.37,\
"Тест 11" : 0.37},\
"Міні-проєкти":\
{"Міні-проєкт 1" : 5.45,\
"Міні-проєкт 2" : 5.45,\
"Міні-проєкт 3" : 5.45,},\
"Фінальний іспит":\
{"Теоретичне завдання": 7.56,\
"Завдання на програмування 1": 7.56,\
"Завдання на програмування 2": 7.56,\
"Завдання на програмування 3": 7.56},\
"Додаткові бали": 4},\
('Pupkin', 'Vitya', 'vitya.pn@ucu.edu.ua', 'cs'):\
{"Лабораторні роботи":\
{"Лабораторна робота 1" : 1,\
"Лабораторна робота 2" : 1,\
"Лабораторна робота 3" : 2,\
"Лабораторна робота 4" : 2,\
"Лабораторна робота 5" : 2,\
"Лабораторна робота 6" : 1,\
"Лабораторна робота 7" : 1,\
"Лабораторна робота 8" : 1,\
"Лабораторна робота 9" : 1,\
"Лабораторна робота 10" : 1,\
"Лабораторна робота 11" : 1,\
"Лабораторна робота 12" : 1},\
"Проміжний іспит":\
{"Теоретичне завдання": 1,\
"Завдання на програмування": 4.3},\
"Тести по лекційним матеріалам":\
{"Тест 1" : 0.17,\
"Тест 2" : 0.27,\
"Тест 3" : 0.17,\
"Тест 4" : 0.27,\
"Тест 5" : 0.17,\
"Тест 6" : 0.37,\
"Тест 7" : 0.37,\
"Тест 8" : 0.37,\
"Тест 9" : 0.37,\
"Тест 10" : 0.37,\
"Тест 11" : 0.37},\
"Міні-проєкти":\
{"Міні-проєкт 1" : 5.45,\
"Міні-проєкт 2" : 5.45,\
"Міні-проєкт 3" : 7.5,},\
"Фінальний іспит":\
{"Теоретичне завдання": 7.56,\
"Завдання на програмування 1": 7.56,\
"Завдання на програмування 2": 10,\
"Завдання на програмування 3": 1.56},\
"Додаткові бали": 10}},\
"Фінальний іспит")
    [('Stone', 'Oleskandr', 'sasha.kaminb.pn@ucu.edu.ua', 'ba'), ('Pupkin', 'Vitya', 'vitya.pn@ucu.edu.ua', 'cs')]

    >>> sort_students(\
{('Stone', 'Oleskandr', 'sasha.kaminb.pn@ucu.edu.ua', 'ba'):\
{"Лабораторні роботи":\
{"Лабораторна робота 1" : 1,\
"Лабораторна робота 2" : 1,\
"Лабораторна робота 3" : 1,\
"Лабораторна робота 4" : 1,\
"Лабораторна робота 5" : 1,\
"Лабораторна робота 6" : 1,\
"Лабораторна робота 7" : 1,\
"Лабораторна робота 8" : 1,\
"Лабораторна робота 9" : 1,\
"Лабораторна робота 10" : 1,\
"Лабораторна робота 11" : 1,\
"Лабораторна робота 12" : 1},\
"Проміжний іспит":\
{"Теоретичне завдання": 2,\
"Завдання на програмування": 2.3},\
"Тести по лекційним матеріалам":\
{"Тест 1" : 0.37,\
"Тест 2" : 0.37,\
"Тест 3" : 0.37,\
"Тест 4" : 0.37,\
"Тест 5" : 0.37,\
"Тест 6" : 0.37,\
"Тест 7" : 0.37,\
"Тест 8" : 0.37,\
"Тест 9" : 0.37,\
"Тест 10" : 0.37,\
"Тест 11" : 0.37},\
"Міні-проєкти":\
{"Міні-проєкт 1" : 5.45,\
"Міні-проєкт 2" : 5.45,\
"Міні-проєкт 3" : 5.45,},\
"Фінальний іспит":\
{"Теоретичне завдання": 7.56,\
"Завдання на програмування 1": 7.56,\
"Завдання на програмування 2": 7.56,\
"Завдання на програмування 3": 7.56},\
"Додаткові бали": 4},\
('Pupkin', 'Vitya', 'vitya.pn@ucu.edu.ua', 'cs'):\
{"Лабораторні роботи":\
{"Лабораторна робота 1" : 1,\
"Лабораторна робота 2" : 1,\
"Лабораторна робота 3" : 2,\
"Лабораторна робота 4" : 2,\
"Лабораторна робота 5" : 2,\
"Лабораторна робота 6" : 1,\
"Лабораторна робота 7" : 1,\
"Лабораторна робота 8" : 1,\
"Лабораторна робота 9" : 1,\
"Лабораторна робота 10" : 1,\
"Лабораторна робота 11" : 1,\
"Лабораторна робота 12" : 1},\
"Проміжний іспит":\
{"Теоретичне завдання": 1,\
"Завдання на програмування": 4.3},\
"Тести по лекційним матеріалам":\
{"Тест 1" : 0.17,\
"Тест 2" : 0.27,\
"Тест 3" : 0.17,\
"Тест 4" : 0.27,\
"Тест 5" : 0.17,\
"Тест 6" : 0.37,\
"Тест 7" : 0.37,\
"Тест 8" : 0.37,\
"Тест 9" : 0.37,\
"Тест 10" : 0.37,\
"Тест 11" : 0.37},\
"Міні-проєкти":\
{"Міні-проєкт 1" : 5.45,\
"Міні-проєкт 2" : 5.45,\
"Міні-проєкт 3" : 7.5,},\
"Фінальний іспит":\
{"Теоретичне завдання": 7.56,\
"Завдання на програмування 1": 7.56,\
"Завдання на програмування 2": 10,\
"Завдання на програмування 3": 1.56},\
"Додаткові бали": 10}},\
"Курс")
    [('Pupkin', 'Vitya', 'vitya.pn@ucu.edu.ua', 'cs'),\
('Stone', 'Oleskandr', 'sasha.kaminb.pn@ucu.edu.ua', 'ba')]
    """

    if sort_by == "Додаткові бали":
        return sorted(gradebook, key = lambda x: gradebook[x][sort_by], reverse = True)

    if sort_by == "Курс":
        gradebook_concise = {}
        for key, value in gradebook.items():

            gradebook_concise[key] = 0
            for activity_key, activity_value in value.items():
                if activity_key == "Додаткові бали":
                    gradebook_concise[key] += activity_value 
                else:
                    gradebook_concise[key] += sum(activity_value.values())

        return sorted(gradebook_concise, key = lambda x: gradebook_concise[x], reverse = True )

    if activity:
        return sorted(gradebook, key = lambda x: gradebook[x][sort_by][activity], reverse = True)

    return sorted(gradebook, key = lambda x: sum(gradebook[x][sort_by].values()), reverse = True)


def average_mark(gradebook: dict, activies_list: list) -> dict:
    pass


def mark_to_letter(gradebook: dict) -> dict:
    pass


def students_fail(gradebook: dict) -> list:
    pass

def gradebook_to_json(gradebook: dict, filename: str) -> None:
    pass


def student_gradebook_to_json(gradebook: dict, surname: str, filename: str) -> None:
    pass


def activity_missing(gradebook: dict, activity: str) -> list:
    pass
