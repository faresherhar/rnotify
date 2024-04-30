from schema import Schema, SchemaError, Regex, Optional, Or

from utils.exc import EmptyReposFileError


config_schema = Schema(
    {
        Optional("email"): {
            "receiver_email": Regex(
                r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$"
            ),
            "smtp_server": Regex(r"^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$"),
            "user_email": Regex(r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$"),
            "user_password": Regex(r"[A-Za-z0-9@#$%^&+=]{6,}"),
            "port": int,
            "message_type": Or("html", "md", "txt"),
        },
        Optional("slack"): {
            "bot_token": Regex(r"xox.-[0-9]{11,13}-[0-9]{11,13}-[0-9a-zA-Z]{24,32}"),
            "channel_id": str,
            "message_type": Or("html", "md", "txt"),
        },
        Optional("telegram"): {
            "bot_token": Regex(r"^[0-9]{8,10}:[a-zA-Z0-9_-]{35}$"),
            "chat_id": int,
            "message_type": Or("html", "md", "txt"),
        },
    }
)


def validate_platforms(
    config_dict: dict[str, dict[str]]
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
