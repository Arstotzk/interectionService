import os
from config_read import Settings


def SaveFile(file, file_name):
    settings = Settings()
    file.save(os.path.join(settings.filePath, file_name))
