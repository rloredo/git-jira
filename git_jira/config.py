from pathlib import Path
import yaml

def config_params_to_str(jira_server_url:str, jira_username:str, jira_api_token:str, jira_default_project_key:str)->str:
    """
    Format the config params to be printed
    """
    return  f"jira_server_url: {jira_server_url}\njira_username: {jira_username}\njira_api_token: {jira_api_token}\njira_default_project_key: {jira_default_project_key}"

def write_config_file(jira_server_url:str, jira_username:str, jira_api_token:str, jira_default_project_key:str)->None:
    """
    Write the config dictionary as a yaml in .git-jira/config.yaml
    """
    jira_config = {
        'jira': {
                'server_url' : jira_server_url,
                'username': jira_username,
                'jira_api_token': jira_api_token,
                'jira_default_project_key' : jira_default_project_key,
                },
    }
    output_file = Path.home() / ".git-jira" / "config.yaml"
    output_file.parent.mkdir(exist_ok=True, parents=True)
    with open(output_file, 'w') as f:
        yaml.dump(jira_config, f)
    f.close()

def config_file_exists():
    path = Path(Path.home() / ".git-jira" / "config.yaml")
    return path.is_file()


    