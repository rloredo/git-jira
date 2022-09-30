from pathlib import Path
import yaml

CONFIG_FILE_PATH = Path(Path.home() / ".git-jira" / "config.yaml")

def write_config_file(config_dict)->None:
    """
    Write the config dictionary as a yaml in CONFIG_FILE_PATH
    """
    output_file = CONFIG_FILE_PATH
    output_file.parent.mkdir(exist_ok=True, parents=True)
    with open(output_file, 'w') as f:
        yaml.dump(config_dict, f)
    f.close()

def config_file_exists():
    """
    Test if the CONFIG_FILE_PATH exists
    """
    path = Path(CONFIG_FILE_PATH)
    return path.is_file()

def load_config():
    """
    Load the CONFIG_FILE as a dictionary
    """
    if config_file_exists():
        with open(CONFIG_FILE_PATH, 'r') as stream:
            config_dict = yaml.safe_load(stream)
        return config_dict
    else:
        raise Exception("No config file found. Run git jira config to generate.")
