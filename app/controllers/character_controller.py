import random

from app.models.base_model import MudaeModel
from app.models.waifu_anime_dataset import anime_waifus
from app.models.waifu_game_dataset import game_waifus
from app.models.husbando_anime_dataset import anime_husbandos
from app.models.husbando_game_dataset import game_husbandos


class CharacterController:
    def __init__(self):
        for dataset in [anime_waifus, game_waifus, anime_husbandos, game_husbandos]:
            random.shuffle(dataset)

        self.__anime_waifus_dataset = iter(anime_waifus)
        self.__game_waifus_dataset = iter(game_waifus)
        self.__anime_husbandos_dataset = iter(anime_husbandos)
        self.__game_husbandos_dataset = iter(game_husbandos)

        self.__global_dataset = {
            'wa': self.__anime_waifus_dataset,
            'wg': self.__game_waifus_dataset,
            'ha': self.__anime_husbandos_dataset,
            'hg': self.__game_husbandos_dataset,
        }

    def get(self, command: str) -> MudaeModel:
        try:
            return next(self.__global_dataset[command])
        except StopIteration:
            self.__init__()
            self.get(command)
