from yaml import safe_load, safe_load_all

from utils.validator.providers import validate_providers


def test_good_providers():
    valid_configs = list()
    with open("./tests/data/providers/providers_good.yaml") as file:
        for config_dict in safe_load_all(file):
            valid_configs.append(validate_providers(config_dict=config_dict)[0])

    assert all(valid_configs) is True


def test_bad_providers():
    valid_configs = list()
    with open("./tests/data/providers/providers_bad.yaml") as file:
        for config_dict in safe_load_all(file):
            valid_configs.append(
                validate_providers(config_dict=config_dict)[0] is False
            )

    assert all(valid_configs) is True


def test_empty_providers():
    with open("./tests/data/providers/providers_empty.yaml") as file:
        config_dict = safe_load(file)
        assert validate_providers(config_dict=config_dict)[0] is False
