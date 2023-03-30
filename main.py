import os

filename = "text.txt"
#keyword = input("Enter keyword: ")
keyword = "damage"


def delete_from_file (filename, keyword):
    with open(filename, "r") as f_in, open("filtered.txt", "w") as f_out:
        # читаємо кожен рядок вхідного файлу
        for line in f_in:
            # перевіряємо, чи містить рядок ключове слово
            if keyword in line:
                # якщо так, записуємо рядок у вихідний файл
                f_out.write(line)

    print("Filtered file saved as filtered.txt")

if __name__ == "__main__":
    filename = "text.txt"
    keyword = "damage"

    delete_from_file(filename, keyword)