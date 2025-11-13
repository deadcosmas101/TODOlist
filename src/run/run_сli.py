from adapters.composites import create_task_service
from src.adapters.cli.cli import CLI


def main():
    cli = CLI(create_task_service())
    while True:
        cli.show_menu()
    

if __name__ == '__main__':
    main()
