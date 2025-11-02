FILE_NAME = "team_discussion.txt"

# Функція тім-ліда Годун:
def get_content_u1(surname: str, question: str) -> str:
    content = (
        f"Член команди №1 (Прізвище: {surname}):\n"
        "  -> Запитання до Учасника 2:\n"
        f"     {question}\n\n"
        "---------------------------------------------------\n"
    )
    return content
    
# Функція консолідації тім-ліда Годун
def write_consolidated_file(full_content: str):
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"Файл '{FILE_NAME}' успішно оновлено/перезаписано з усіма блоками учасників.")
    except IOError as e:
        print(f"Помилка: Не вдалося записати файл '{FILE_NAME}': {e}")
    except Exception as e:
        print(f"Невідома помилка при записі файлу: {e}")


# ✅ Функція учасника №2 (ДОДАНО)
def get_content_u2(surname: str, answer: str, question: str) -> str:
    content = (
        f"Член команди №2 (Прізвище: {surname}):\n"
        "  -> Відповідь на питання Учасника 1:\n"
        f"     {answer}\n\n"
        "  -> Запитання до Учасника 3:\n"
        f"     {question}\n\n"
        "---------------------------------------------------\n"
    )
    return content

# ✅ Функція допису в файл (режим "a")
def append_user_block(content: str):
    try:
        with open(FILE_NAME, 'a', encoding='utf-8') as f:
            f.write(content)
        print("Блок учасника успішно додано (режим 'a').")
    except Exception as e:
        print(f"Помилка при додаванні блоку: {e}")


def main_discussion():
    # Дані учасників:
    # Член команди №1 (Годун)
    surname_u1 = "Годун"
    question_u1 = "Яка основна відмінність між режимами 'r', 'w' та 'a' при відкритті файлів у Python? \n Наведіть приклад використання режиму 'a' (append).\n"

    # Член команди №2 (Бондар)
    surname_u2 = "Бондар"
    answer_u2 = "Режим 'a' додає дані у файл, не видаляючи попередній вміст."
    question_u2 = "Чим відрізняється метод write() від writelines() у Python?\n"
    
    # Створюємо пустий рядок для файлу
    full_content = ""
    
    # Додавання блоку Годун
    full_content += get_content_u1(surname_u1, question_u1)

    
    # Запис у файлу усього
    write_consolidated_file(full_content)

    # Додати блок учасника №2
    block_u2 = get_content_u2(surname_u2, answer_u2, question_u2)
    append_user_block(block_u2)

    # Показати результат роботи після запису
    print("\n=== Поточний вміст файлу ===\n")
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        print(f.read())


if __name__ == "__main__":
    main_discussion()
