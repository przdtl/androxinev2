import yaml
import logging.config

from pathlib import Path


def setup_logging(config_file: str | None = None) -> None:
    if config_file is None:
        config_file = ".logging.yml"

    config_path = Path(config_file)

    if config_path.exists():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
