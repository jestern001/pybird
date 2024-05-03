import json
from dataclasses import dataclass, field
from pathlib import Path
from tkinter import PhotoImage
from typing import Any

from gameobjects.gameobject import GameObject
from gameobjects.player import Player


@dataclass
class GameConfig:
    start_room_name: str
    update_rate: int


@dataclass
class RoomConfig:
    name: str
    game_objects: list[dict[str, Any]] = field(default_factory=list)


class GameObjectFactory:
    @staticmethod
    def get(data: dict[str, Any]) -> GameObject | Player:
        mapping = {
            "player": Player,
            "object": GameObject
        }
        # extract the class name
        class_key: str = data.pop("object_class")

        # get the class from the name
        object_class = mapping[class_key]

        # initialize the class with the kwargs
        game_object: GameObject | Player = object_class(**data)


        # add sprite
        if game_object.image_path:
            game_object.sprite = PhotoImage(file=game_object.image_path)
        
        return game_object


class GameSettings:

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
        for room_config_path in room_config_paths:

            # read the room data
            data: dict[str, Any] = json.loads(room_config_path.read_text())

            # build the config
            room_configs.append(RoomConfig(**data))

        self.room_configs = room_configs

    def get_room_settings(self, room_name: str) -> RoomConfig:
        return next(filter(lambda config: config.name == room_name, self.room_configs))
