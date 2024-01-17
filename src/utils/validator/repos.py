from schema import Schema, SchemaError, Regex, Optional


config_schema = Schema(
    {
        Optional("github"): [Regex(r"^[\w\.-]+\/[\w\.-]+$")],
        Optional("gitlab"): [Regex(r"^[\w\.-]+\/[\w\.-]+$")],
    }
)


def validate_repos(config_dict: dict[str, list[str]]) -> (bool, SchemaError | None):
    try:
        config_schema.validate(config_dict)
        return True, None
    except SchemaError as err:
        return False, err
