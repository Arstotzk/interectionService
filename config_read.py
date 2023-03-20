import yaml


class Settings:

    def __init__(self):
        """
        Инициализация настроек
        """
        config = self.read_yaml("config.yaml")

        self.rabbitLogin = config["rabbitLogin"]
        self.rabbitPassword = config["rabbitPassword"]
        self.rabbitHost = config["rabbitHost"]
        self.rabbitPort = config["rabbitPort"]
        self.rabbitVirtualHost = config["rabbitVirtualHost"]

        self.dbName = config["dbName"]
        self.dbUser = config["dbUser"]
        self.dbPassword = config["dbPassword"]
        self.dbHost = config["dbHost"]
        self.dbPort = config["dbPort"]


    def read_yaml(self, _file_path):
        """
        Получить параметры из config.yaml.
        :param _file_path: Путь до config.yaml.
        :return: Параметры из config.yaml.
        """
        with open(_file_path, "r") as file:
            return yaml.safe_load(file)
