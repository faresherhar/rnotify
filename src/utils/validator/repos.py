from schema import Schema, SchemaError, Regex, Optional
import logging

import utils.logging_config as logging_config


# Define logger
logger = logging.getLogger(__name__)

config_schema = Schema(
    {
        Optional("github"): [Regex(r"^[\w\.-]+\/[\w\.-]+$")],
        Optional("gitlab"): [Regex(r"^[\w\.-]+\/[\w\.-]+$")],
    }
)


def validate_repos(config_dict: dict[str, list[str]]) -> (bool, SchemaError | None):
    try:
        logger.info(f"Validating Configuration {config_dict}")
        config_schema.validate(config_dict)
        return True, None
    except SchemaError as err:
        logger.error(f"Unvalid Configuration {config_dict}")
        return False, err
