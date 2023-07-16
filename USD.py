class USD:
    @classmethod
    def get_value(cls) -> float:
        return 3.68

    @classmethod
    def calculate(cls, value_to_convert):
        return value_to_convert * cls.get_value()
