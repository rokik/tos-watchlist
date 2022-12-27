import hydra
from omegaconf import DictConfig, OmegaConf

from scrappers.oic import OicScrapper


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def start(config: DictConfig) -> None:
    oic_scrapper = OicScrapper(config.scrappers.oic)
    print(str(oic_scrapper.get_symbols()))


if __name__ == '__main__':
    start()
