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


def list_books(books):
    print("\n--- Все книги ---")
    if not books:
        print("Список пуст")
        return
    for i, b in enumerate(books, 1):
        print(f"{i}. «{b['title']}» — {b['author']} | Оценка: {b['rating']}/5 | Прочитана: {b['date']}")


def average_rating(books):
    print("\n--- Средняя оценка ---")
    if not books:
        print("Список пуст")
        return
    avg = sum(b["rating"] for b in books) / len(books)
    print(f"Средняя оценка по {len(books)} книгам: {avg:.2f}")


def author_stats(books):
    print("\n--- Статистика по авторам ---")
    if not books:
        print("Список пуст")
        return
    stats = {}
    for b in books:
        stats[b["author"]] = stats.get(b["author"], 0) + 1
    for author, count in sorted(stats.items()):
        print(f"  {author}: {count} кн.")


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
        elif choice == "2":
            list_books(books)
        elif choice == "3":
            average_rating(books)
        elif choice == "4":
            author_stats(books)
        elif choice == "6":
            print("Пока!")
            break
        else:
            print("Функция пока не реализована")


if __name__ == "__main__":
    main()
