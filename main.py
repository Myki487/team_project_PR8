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
    
# Функція консолідації тім-ліда Годун (записує файл з нуля в режимі w)
def write_consolidated_file(full_content: str):
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"Файл '{FILE_NAME}' успішно оновлено/перезаписано з усіма блоками учасників.")
    except IOError as e:
        print(f"Помилка: Не вдалося записати файл '{FILE_NAME}': {e}")
    except Exception as e:
        print(f"Невідома помилка при записі файлу: {e}")


# ✅ Новий блок: Функція учасника №2 (режим 'a')
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

def append_user_block(content: str):
    try:
        with open(FILE_NAME, 'a', encoding='utf-8') as f:  # режим APPEND
            f.write(content)
        print("Блок учасника успішно додано (режим 'a').")
    except Exception as e:
        print(f"Помилка при додаванні блоку: {e}")


# Головна функція (Спільна робота):
def main_discussion():
    # Дані тім-ліда (Учасник 1)
    surname_u1 = "Годун"
    question_u1 = "Яка основна відмінність між режимами 'r', 'w' та 'a' при відкритті файлів у Python? Наведіть приклад використання режиму 'a' (append)."

    # Дані Учасника №2
    surname_u2 = "Бондар"
    answer_u2 = "Режим 'a' дозволяє додавати дані у файл, не видаляючи попередній вміст."
    question_u2 = "Чим відрізняється метод write() від writelines() у Python?"

    # Створюємо пустий рядок для файлу
    full_content = ""

    # Додавання блоку Годун (створення файлу)
    full_content += get_content_u1(surname_u1, question_u1)

    print("="*50)
    print("Обговорення: Робота з файлами у Python\n")
    print("---------------------------------------------------\n")
    print(full_content)

    # ✅ 1) Тім-лід створює файл
    write_consolidated_file(full_content)

    # ✅ 2) Учасник №2 додає свій блок в режимі "a"
    block_u2 = get_content_u2(surname_u2, answer_u2, question_u2)
    append_user_block(block_u2)


if __name__ == "__main__":
    main_discussion()
