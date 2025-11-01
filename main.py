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

# Головна функція (Спільна робота):
def main_discussion():
    # Дані учасників:
    # Член команди №1 (Годун)
    surname_u1 = "Годун"
    question_u1 = "Яка основна відмінність між режимами 'r', 'w' та 'a' при відкритті файлів у Python? Наведіть приклад використання режиму 'a' (append)."

    # Член команди №2 ("Прізвище члена команди №2")
    # surname_u2 = ""
    # answer_u2 = ""
    # question_u2 = ""
    
    # Створюємо пустий рядок для файлу
    full_content = ""
    
    # Додавання блоку Годун
    full_content += get_content_u1(surname_u1, question_u1)
    # Додавання блоку Члена команди №2
    # full_content += get_content_u2(surname_u2, answer_u2, question_u2)
    
    # Виведення у термінал
    print("="*50)
    print("Обговорення: Робота з файлами у Python\n")
    print("---------------------------------------------------\n")
    print(full_content)
    
    # Запис у файлу усього
    write_consolidated_file(full_content)


if __name__ == "__main__":
    main_discussion()
