import time

from file_generator import file_generator
from letter_counter_in_n_threads import count_letter_in_directory_multithread
from letter_counter_in_one_thread import count_letter_in_directory


def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


def main():
    directory = 'directory_1'
    number_of_files = 100
    file_size = 500
    letter_to_find = 'a'
    number_of_threads = 4

    # Step 1: Generate files
    print(f"Generating {number_of_files} files in '{directory}'")
    file_generator(directory, number_of_files, file_size)

    # Step 2: Count letters using a single thread
    print("Count letters using a single thread:")
    count, time_single = measure_execution_time(count_letter_in_directory, directory, letter_to_find)
    print(f"Total occurrences of '{letter_to_find}' (single-threaded): {count}")
    print(f"Execution time (single-threaded): {time_single:.4f} seconds")

    # Step 3: Count letters using multiple threads
    print("Count letters using multiple threads:")
    count, time_multi = measure_execution_time(count_letter_in_directory_multithread, directory, letter_to_find,
                                               number_of_threads)
    print(f"Total occurrences of '{letter_to_find}' (multi-threaded): {count}")
    print(f"Execution time (multi-threaded): {time_multi:.4f} seconds")

    # Step 4: Cleanup
    import shutil
    shutil.rmtree(directory)


if __name__ == '__main__':
    main()
