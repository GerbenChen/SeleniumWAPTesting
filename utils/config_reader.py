from pathlib import Path

import yaml


CONFIG_PATH = (
    Path(__file__)
    .resolve()
    .parent.parent
    / "config"
    / "config.yaml"
)


def load_config() -> dict:

    if not CONFIG_PATH.exists():

        raise FileNotFoundError(
            f"Config file not found:\n"
            f"{CONFIG_PATH}"
        )

    with open(
        CONFIG_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        config = yaml.safe_load(file)

    if not config:

        raise ValueError(
            "Config file is empty."
        )

    return config