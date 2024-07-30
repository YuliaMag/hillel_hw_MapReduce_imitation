import os
from concurrent.futures import ThreadPoolExecutor


def count_letter_in_file(file_path, letter_to_find):
    count = 0
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            count = content.count(letter_to_find)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return count


def count_letter_in_file_group(file_paths, letter_to_find):
    total_count = 0
    for file_path in file_paths:
        total_count += count_letter_in_file(file_path, letter_to_find)
    return total_count


def count_letter_in_directory_multithread(directory, letter_to_find, number_of_threads):
    try:
        all_files = [os.path.join(directory, file_name) for file_name in os.listdir(directory)
                     if os.path.isfile(os.path.join(directory, file_name))]

        num_files = len(all_files)
        if number_of_threads > num_files:
            number_of_threads = num_files

        files_per_thread = (num_files + number_of_threads - 1) // number_of_threads
        file_groups = [all_files[i:i + files_per_thread] for i in range(0, num_files, files_per_thread)]

        total_count = 0
        with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
            future_to_group = {executor.submit(count_letter_in_file_group, group, letter_to_find): group
                               for group in file_groups}

            for future in future_to_group:
                try:
                    total_count += future.result()
                except Exception as e:
                    print(f"Error during thread execution: {e}!")

        return total_count
    except Exception as e:
        print(f"Error processing directory {directory}: {e}")
        return 0


# letter_count = count_letter_in_directory_multithread('directory_1', 'a', 4)
# print(f"Total occurrences of 'a': {letter_count}")
