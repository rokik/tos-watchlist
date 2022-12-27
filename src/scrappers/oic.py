from selenium import webdriver
from omegaconf import DictConfig
from selenium.webdriver.common.by import By
import time

from . symbol_filters import VolumeFilter
from . scrapper_base import SymbolScrapperBase


class OicScrapper(SymbolScrapperBase):

    def __init__(self, config: DictConfig):
        SymbolScrapperBase.__init__(self, config)
        self.volume_filters = set()
        self.volume_filters.add(VolumeFilter(config.min_volume))

    def _get_symbols(self, driver: webdriver) -> set:
        driver.get(self.config.base_url)
        time.sleep(self.config.wait_time_per_click)
        symbol_set = self.__get_stock_symbols(driver)

        driver.find_element(By.LINK_TEXT, "Index").click()
        time.sleep(self.config.wait_time_per_click)
        symbol_set.update(self.__get_index_symbols(driver))

        driver.find_element(By.LINK_TEXT, "ETF").click()
        time.sleep(self.config.wait_time_per_click)
        symbol_set.update(self.__get_etf_symbols(driver))

        return symbol_set

    def __get_index_symbols(self, driver: webdriver) -> set:
        index_data = driver.find_element(By.XPATH, '//*[@id="indexData"]/tbody')
        index_symbols = self.__parse_symbol_table_data(index_data.text)
        return self.__remap(index_symbols)

    def __get_stock_symbols(self, driver: webdriver) -> set:
        stock_data = driver.find_element(By.XPATH, '//*[@id="equityData"]/tbody')
        return self.__parse_symbol_table_data(stock_data.text)

    def __get_etf_symbols(self, driver: webdriver) -> set:
        etf_data = driver.find_element(By.XPATH, '//*[@id="etfData"]/tbody')
        return self.__parse_symbol_table_data(etf_data.text)

    def __parse_symbol_table_data(self, value_lines: str) -> set:
        value_set = set()
        for line in value_lines.split("\n"):
            columns = line.split(" ")
            should_ignore = False

            for volume_filter in self.volume_filters:
                if volume_filter.apply(float(columns[1])):
                    should_ignore = True
                    break

            if should_ignore:
                continue

            value_set.add(columns[0])
        return value_set

    @staticmethod
    def __remap(index_symbols) -> set:
        remapped_values = set()
        for symbol in index_symbols:
            remapped_values.add(symbol.split(".")[1])
        return remapped_values
