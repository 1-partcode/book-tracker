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


def add_book(books):
    print("\n--- Добавить книгу ---")
    title = input("Название: ").strip()
    author = input("Автор: ").strip()

    for b in books:
        if b["title"].lower() == title.lower() and b["author"].lower() == author.lower():
            print("Такая книга уже есть в списке!")
            return books

    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть от 1 до 5")
        except ValueError:
            print("Введите целое число")
    date = input("Дата прочтения (например, 2024-06-10): ").strip()
    books.append({"title": title, "author": author, "rating": rating, "date": date})
    save_books(books)
    print(f'Книга "{title}" добавлена!')
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
        if choice == "1":
            books = add_book(books)
        elif choice == "6":
            print("Пока!")
            break
        else:
            print("Функция пока не реализована")


if __name__ == "__main__":
    main()
