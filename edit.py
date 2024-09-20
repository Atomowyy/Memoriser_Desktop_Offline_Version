import os


def clear() -> None:
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def create_directory() -> None:
    category_name: str = input('Enter name for your category: ')
    while not category_name:
        category_name = input('Name cannot be empty! Try again: ')
    os.mkdir(f'content/{category_name}')


def setup() -> None:
    clear()
    categories_dirs: list[str] = os.listdir('./content')
    if not categories_dirs:
        print('It\'s seems that you are a new user. Create your first category!')
        create_directory()

    print("Select your category:")
    categories_dirs: list[str] = os.listdir('./content')
    for i in range(len(categories_dirs)):
        print(f'{i+1}: {categories_dirs[i]}')
    print(f'{len(categories_dirs)+1}: Create new directory')


if __name__ == '__main__':
    setup()
