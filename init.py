import os
import platform
from colorama import init, Fore

init(autoreset=True)  # Initialize Colorama for colored terminal output

class Entry:
    def __init__(self, title, description, tags):
        self.title = title
        self.description = description
        self.tags = tags

class Database:
    def __init__(self):
        self.entries = []
        self.tags = set()

    def add_entry(self, entry):
        self.entries.append(entry)
        self.tags.update(entry.tags)

    def browse_entries(self):
        os.system(clear_command())
        print(Fore.CYAN + "Browsing Entries\n")
        for index, entry in enumerate(self.entries, start=1):
            print(Fore.LIGHTYELLOW_EX + f"Entry {index} - Title: {Fore.GREEN + entry.title}")
            print(Fore.LIGHTBLACK_EX + f"Description: {entry.description}")
            print(Fore.RED + f"Tags: {' '.join(entry.tags)}\n")
        input("Press Enter to continue...")

    def save_entries_to_file(self, filename):
        with open(filename, 'w') as f:
            for index, entry in enumerate(self.entries, start=1):
                f.write(f"Entry {index} - Title: {entry.title}\n")
                f.write(f"Description: {entry.description}\n")
                f.write(f"Tags: {' '.join(entry.tags)}\n\n")
        print(Fore.GREEN + f"Entries saved to {filename}")

    def show_tags(self):
        os.system(clear_command())
        print(Fore.MAGENTA + "Available tags:")
        for tag in self.tags:
            print(Fore.RED + tag)
        input("Press Enter to continue...")

    def count_tags(self):
        os.system(clear_command())
        print(Fore.MAGENTA + "Tag Counts:")
        tag_counts = {tag: 0 for tag in self.tags}
        for entry in self.entries:
            for tag in entry.tags:
                tag_counts[tag] += 1
        for tag, count in tag_counts.items():
            print(Fore.RED + f"{tag}: {count}")
        input("Press Enter to continue...")

    def search_by_tag(self, tag):
        os.system(clear_command())
        print(Fore.CYAN + f"Entries with tag '{tag}':\n")
        found_entries = [entry for entry in self.entries if tag in entry.tags]
        for index, entry in enumerate(found_entries, start=1):
            print(Fore.LIGHTYELLOW_EX + f"Entry {index} - Title: {Fore.GREEN + entry.title}")
            print(Fore.LIGHTBLACK_EX + f"Description: {entry.description}")
            print(Fore.RED + f"Tags: {' '.join(entry.tags)}\n")
        input("Press Enter to continue...")

def clear_command():
    system_name = platform.system()
    if system_name == "Windows":
        return "cls"
    else:
        return "clear"

def main():
    db = Database()

    while True:
        os.system(clear_command())
        print(Fore.LIGHTBLACK_EX + "1. Add new entry")
        print("2. Browse entries")
        print("3. Save entries to file")
        print("4. Show available tags")
        print("5. Count tag occurrences")
        print("6. Search entries by tag")
        print(Fore.LIGHTBLACK_EX + "7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            os.system(clear_command())
            title = input("Enter title: ")
            description = input("Enter description: ")
            tags = input("Enter tags (separated by spaces): ").split()
            new_entry = Entry(title, description, tags)
            db.add_entry(new_entry)
            print(Fore.GREEN + "Entry added!\n")
            input("Press Enter to continue...")
        elif choice == "2":
            db.browse_entries()
        elif choice == "3":
            os.system(clear_command())
            filename = input("Enter filename to save entries: ")
            db.save_entries_to_file(filename)
            input("Press Enter to continue...")
        elif choice == "4":
            db.show_tags()
        elif choice == "5":
            db.count_tags()
        elif choice == "6":
            tag = input("Enter tag to search: ")
            db.search_by_tag(tag)
        elif choice == "7":
            os.system(clear_command())
            print(Fore.RED + "Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
