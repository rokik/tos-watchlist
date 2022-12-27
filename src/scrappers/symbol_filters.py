from abc import abstractmethod, ABC


class Filter(ABC):

    @abstractmethod
    def apply(self, target) -> bool:
        pass


class VolumeFilter(Filter):

    def __init__(self, min_volume: int):
        self.min_volume = min_volume

    def apply(self, target) -> bool:
        if target < self.min_volume:
            return True
        return False
