from schema import Schema, SchemaError, Regex, Optional


config_schema = Schema(
    {"version": 1.0, Optional("github"): [Regex(r"^[\w\.-]+\/[\w\.-]+$")]}
)


def validate_repos(config_dict: dict[str, list[str]]) -> (bool, SchemaError | None):
    try:
        print(config_dict)
        config_schema.validate(config_dict)
        return True, None
    except SchemaError as se:
        return False, se
