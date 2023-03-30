import os


def removal_by_word_file (filename, keyword):
    try:
        with open(filename, "r") as f_in, open("filtered.txt", "w") as f_out:
            # зчитуєм всі рядки з обраного файлу
            for line in f_in:
                # перевіряємо, чи знаходиться в обраному рядку ключове слово
                if keyword in line:
                    # якщо так, записуємо рядок у вихідний файл
                    f_out.write(line)
        if os.path.exists(filename):
            print("Filtered file saved as filtered.txt")
        else:
            print("No matches in file")
    except:
        print(f"File {filename} do not exist here")


if __name__ == "__main__":
    filename = "text.txt"
    keyword = "damage"

    #filename = input("Enter file name: ")
    #keyword = input("Enter keyword: ")

    format_file = ".txt"

    if not format_file in filename:
        filename += format_file

    removal_by_word_file(filename, keyword)