import json
import os

BOOKS_FILE = "books.json"


def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)


def delete_book(books):
    print("\n--- Удалить книгу ---")
    if not books:
        print("Список пуст")
        return books
    for i, b in enumerate(books, 1):
        print(f"{i}. «{b['title']}» — {b['author']}")
    try:
        idx = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= idx < len(books):
            removed = books.pop(idx)
            save_books(books)
            print(f'Удалена: «{removed["title"]}»')
        else:
            print("Неверный номер")
    except ValueError:
        print("Введите число")
    return books


def main():
    books = load_books()
    while True:
        print("\n=== Трекер прочитанных книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выбор: ").strip()
        if choice == "5":
            books = delete_book(books)
        elif choice == "6":
            print("Пока!")
            break
        else:
            print("Функция пока не реализована")


if __name__ == "__main__":
    main()
