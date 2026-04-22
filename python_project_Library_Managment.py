import csv
import os

FILE_NAME = "library.csv"

# ---------------------------
# Initialize file
# ---------------------------
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Book Name", "Author", "Status"])


# ---------------------------
# Add Book
# ---------------------------
def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([book_id, name, author, "Available"])

    print("✅ Book Added Successfully!")


# ---------------------------
# View Books
# ---------------------------
def view_books():
    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            print("\n--- Library Books ---")
            for row in reader:
                print(row)
    except:
        print("❌ No records found")


# ---------------------------
# Search Book
# ---------------------------
def search_book():
    search = input("Enter Book Name to search: ").lower()
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if search in row[1].lower():
                print("Found:", row)
                found = True

    if not found:
        print("❌ Book not found")


# ---------------------------
# Issue Book
# ---------------------------
def issue_book():
    book_id = input("Enter Book ID to issue: ")
    rows = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == book_id and row[3] == "Available":
                row[3] = "Issued"
                found = True
            rows.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if found:
        print("📕 Book Issued")
    else:
        print("❌ Book not available")


# ---------------------------
# Return Book
# ---------------------------
def return_book():
    book_id = input("Enter Book ID to return: ")
    rows = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == book_id and row[3] == "Issued":
                row[3] = "Available"
                found = True
            rows.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if found:
        print("📗 Book Returned")
    else:
        print("❌ Book was not issued")


# ---------------------------
# Delete Book
# ---------------------------
def delete_book():
    book_id = input("Enter Book ID to delete: ")
    rows = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != book_id:
                rows.append(row)
            else:
                found = True

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if found:
        print("🗑 Book Deleted")
    else:
        print("❌ Book not found")


# ---------------------------
# Update Book
# ---------------------------
def update_book():
    print("\nAvailable Books:")

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(f"ID: {row[0]} | Book: {row[1]} | Author: {row[2]} | Status: {row[3]}")

    book_id = input("\nEnter Book ID to update: ")
    rows = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == book_id:
                print("Old Data:", row)
                row[1] = input("python , AI: ")
                row[2] = input("Jhon , David: ")
                row[3] = input("Available:")
                found = True
            rows.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if found:
        print("✏️ Book Updated Successfully")
    else:
        print("❌ Book not found")


# ---------------------------
# Count Books
# ---------------------------
def count_books():
    count = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for _ in reader:
            count += 1

    print(f"📊 Total Books: {count}")


# ---------------------------
# Menu
# ---------------------------
def menu():
    init_file()

    while True:
        print("\n====== Library Menu ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Update Book")
        print("8. Count Books")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            update_book()
        elif choice == "8":
            count_books()
        elif choice == "9":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


# ---------------------------
# Run Program
# ---------------------------
if __name__ == "__main__":
    menu()