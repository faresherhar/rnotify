from schema import Schema, SchemaError, Regex, Optional


config_schema = Schema({Optional("github"): [Regex(r"^[\w\.-]+\/[\w\.-]+$")]})


def valid_config_file(config_dict: dict[str, object]) -> bool:
    try:
        config_schema.validate(config_dict)
        return True, None
    except SchemaError as se:
        return False, se
