import os
import random
import string


def generate_random_content(size):
    characters = string.ascii_letters + string.digits + string.punctuation
    length = random.randint(size // 2, size)
    return ''.join(random.choice(characters) for _ in range(length))


def file_generator(directory, number_of_files, size):
    os.makedirs(directory, exist_ok=True)

    for i in range(number_of_files):
        file_name = os.path.join(directory, f'random_file_{i + 1}.txt')
        content = generate_random_content(size)
        with open(file_name, 'w') as file:
            file.write(content)
        print(f'File: {file_name} created')


# file_generator('directory_1', 10, 100)
