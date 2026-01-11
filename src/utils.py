from pathlib import Path

def get_project_root() -> Path:
    """
    Returns the absolute path to the project root directory.

    This ensures the code functions correctly regardless of the execution context 
    (whether the script is run from within '/src' or from the project root).

    Returns:
        Path: The Path object pointing to the root directory (jq-api-news-tracker).
    """
    return Path(__file__).resolve().parent.parent

def get_env_path() -> Path:
    """
    Returns the absolute path to the .env file located in the config directory.

    Relies on get_project_root to ensure path consistency.

    Returns:
        Path: Full path to the .env file.
    """
    return get_project_root() / 'config' / '.env'