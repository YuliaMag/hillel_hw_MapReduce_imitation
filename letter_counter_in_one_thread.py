import os


def count_letter_in_file(file_path, letter_to_find):
    count = 0
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            count = content.count(letter_to_find)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return count


def count_letter_in_directory(directory, letter_to_find):
    total_count = 0
    try:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                total_count += count_letter_in_file(file_path, letter_to_find)
    except Exception as e:
        print(f"Error processing directory {directory}: {e}")
    return total_count


# letter_count = count_letter_in_directory('directory_1', 'a')
# print(f"Total occurrences of 'a': {letter_count}")
