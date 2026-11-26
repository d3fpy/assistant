from processor import process_and_execute


def main():
    try:
        while True:
            text = input(">>> ")
            process_and_execute(text)
    except KeyboardInterrupt:
        print('\nДо встречи!')


if __name__ == '__main__':
    main()
