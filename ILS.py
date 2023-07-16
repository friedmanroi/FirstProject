class Ils:
    @classmethod
    def get_value(cls) -> float:
        return 0.28

    @classmethod
    def calculate(cls, value_to_convert):
        return value_to_convert * cls.get_value()
