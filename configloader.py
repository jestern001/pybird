import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class GameConfig:
    start_room_name: str
    update_rate: int


@dataclass
class RoomConfig:
    name: str


class ConfigLoader:
    def __init__(self, config_dir: Path) -> None:

        # get config directory
        if not config_dir.exists():
            raise FileNotFoundError(f"Game config directory not found: {config_dir}")

        # get game config
        game_config_path = config_dir.joinpath("game.json")
        if not game_config_path.exists():
            raise FileExistsError(f"Game config file not found: {game_config_path}")
        game_config_data = json.loads(game_config_path.read_text())
        self.game_config = GameConfig(**game_config_data)

        # get room configs directory
        room_config_dir = config_dir.joinpath("rooms")
        if not room_config_dir.exists():
            raise FileExistsError(f"Room config directory not found: {room_config_dir}")

        # get room config files
        room_config_paths = list(room_config_dir.iterdir())
        room_configs: list[RoomConfig] = []
        for path in room_config_paths:
            data = json.loads(path.read_text())
            config = RoomConfig(**data)
            room_configs.append(config)
        self.room_configs = room_configs

    def get_room_by_name(self, name: str) -> RoomConfig:
        return next(filter(lambda config: config.name == name, self.room_configs))
