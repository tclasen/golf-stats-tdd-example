class InvalidThrowValue(ValueError):
    pass


class TooManyThrows(ValueError):
    pass


class Player:
    def __init__(self) -> None:
        self._throws: int = 0
        self._score: list[int] = []

    def add_round(self, throws: int) -> None:
        if throws <= 0:
            raise InvalidThrowValue

        self._throws += 1

        if self._throws > 18:
            raise TooManyThrows

        self._score.append(throws)

    def score(self) -> int:
        return sum(self._score)

    def throws(self) -> int:
        return self._throws

    def all_scores(self) -> list[int]:
        return self._score

    def __len__(self) -> int:
        return len(self._score)
