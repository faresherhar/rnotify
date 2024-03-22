from yaml import safe_load, safe_load_all

from utils.validator.platforms import validate_platforms


def test_good_platforms():
    valid_configs = list()
    with open("./tests/data/platforms/platforms_good.yaml") as file:
        for config_dict in safe_load_all(file):
            valid_configs.append(validate_platforms(config_dict=config_dict)[0])

    assert all(valid_configs) is True


def test_bad_platforms():
    valid_configs = list()
    with open("./tests/data/platforms/platforms_bad.yaml") as file:
        for config_dict in safe_load_all(file):
            valid_configs.append(
                validate_platforms(config_dict=config_dict)[0] is False
            )

    assert all(valid_configs) is True


def test_empty_platforms():
    with open("./tests/data/platforms/platforms_empty.yaml") as file:
        config_dict = safe_load(file)
        assert validate_platforms(config_dict=config_dict)[0] is False
