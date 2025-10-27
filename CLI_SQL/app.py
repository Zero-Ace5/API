from db import init_db, add_note, list_notes, delete_note


def menu():
    print("\n=== Notes App ===")
    print("1. Add note")
    print("2. View all notes")
    print("3. Delete note")
    print("4. Exit")


def main():
    init_db()  # ensure DB exists

    while True:
        menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            add_note(title, content)
            print("Note added.")

        elif choice == "2":
            notes = list_notes()
            if not notes:
                print("No notes found.")
            else:
                for n in notes:
                    print(f"{n[0]}. {n[1]} — {n[2]}")

        elif choice == "3":
            note_id = input("Enter note ID to delete: ")
            delete_note(note_id)
            print("Note deleted.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
