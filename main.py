from src.display import Display
from src.screens import Greetings

display = Display(Greetings())


def main():
    action: str | None = None
    while True:
        display.show()
        action = display.prompt()

        if action == "q":
            break


if __name__ == "__main__":
    main()
