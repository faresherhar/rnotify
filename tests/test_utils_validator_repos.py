from yaml import safe_load

from src.utils.validator.repos import validate_repos


def test_good_repos():
    with open("./tests/data/repos/good_repos.yaml") as file:
        config_dict = safe_load(file)
        assert validate_repos(config_dict=config_dict)[0] is True


def test_bad_repos():
    with open("./tests/data/repos/bad_repos.yaml") as file:
        config_dict = safe_load(file)
        assert validate_repos(config_dict=config_dict)[0] is False
