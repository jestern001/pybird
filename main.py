from pathlib import Path
from app import App


config_dir = Path("configs")


if __name__ == "__main__":
    app = App(config_dir)
    app.run()
