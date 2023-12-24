from yaml import safe_load

from src.scraper.utils.repos_validator import validate_repos


def test_good_repos():
    with open("samples/good_repos.yaml", "r") as file:
        config_dict = safe_load(file)
        assert validate_repos(config_dict=config_dict)[0] is True


def test_bad_repos():
    with open("samples/bad_repos.yaml", "r") as file:
        config_dict = safe_load(file)
        assert validate_repos(config_dict=config_dict)[0] is False
