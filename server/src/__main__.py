from .controllers import app, init

def main() -> None:
    init()
    app.run(debug=True, port=4000)


if __name__ == "__main__":
    main()