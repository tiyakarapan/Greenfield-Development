from .app import App
from .controllers import init as init_controllers

def main() -> None:
    app = App()
    init_controllers(app)
    app.run(4000)


if __name__ == "__main__":
    main()