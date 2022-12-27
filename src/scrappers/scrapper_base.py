from abc import abstractmethod

from omegaconf import DictConfig
from selenium import webdriver

from .selenium_handler import SeleniumHandler


class SymbolScrapperBase:

    def __init__(self, config: DictConfig):
        self.config = config

    def get_symbols(self) -> set:
        handler = SeleniumHandler()
        symbols_set = self._get_symbols(handler.get_webdriver)
        handler.close()
        return symbols_set

    @abstractmethod
    def _get_symbols(self, driver: webdriver) -> set:
        pass

    @property
    def get_config(self) -> DictConfig:
        return self.config
