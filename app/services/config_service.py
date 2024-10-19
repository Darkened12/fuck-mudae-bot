import json


class ConfigService:
    def __init__(self):
        with open('config.json', 'r') as file:
            self.__json_data = json.load(file)

    @property
    def dm_delay(self) -> int:
        return self.__json_data['dm_delay']

    @property
    def rickroll_logging_channel(self) -> int:
        return self.__json_data['rickroll_logging_channel']

    @property
    def timeout_logging_channel(self) -> int:
        return self.__json_data['timeout_logging_channel']