from pathlib import Path
from app import App


config_dir = Path("settings")


if __name__ == "__main__":
    app = App(config_dir)
    app.run()
