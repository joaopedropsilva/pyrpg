class LevelInfo(object):
    def __init__(self, level_code, level_number, chapter_name):
        self.level_code = level_code
        self.level_number = level_number
        self.chapter_name = chapter_name

    @property
    def level_code(self):
        return self._level_code

    @level_code.setter
    def level_code(self, new_level_code):
        self._level_code = new_level_code
