from schema import Schema, SchemaError, Regex, Optional

from utils.exc import EmptyReposFileError

config_schema = Schema(
    {
        Optional("github"): [Regex(r"^[\w\.-]+\/[\w\.-]+$")],
        Optional("gitlab"): [Regex(r"^[\w\.-]+\/[\w\.-]+$")],
    }
)


def validate_providers(
    config_dict: dict[str, list[str]]
) -> tuple[bool, SchemaError | None]:
    # Verify empty repos configuration file
    if config_dict is None:
        return False, EmptyReposFileError

    # Validate Schema
    try:
        config_schema.validate(config_dict)
        return True, None
    except SchemaError as err:
        return False, err
