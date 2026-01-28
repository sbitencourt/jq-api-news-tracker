from pathlib import Path

def get_project_root() -> Path:
    """
    Returns the absolute path to the project root directory.

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

def get_data_path() -> Path:
    """
    Returns the absolute path to the /data/ directory.

    Returns:
        Path: Full path to the /data/ directory.
    """
    return Path(__file__).resolve().parent.parent / 'data'

def get_raw_data_path() -> Path:
    """
    Returns the absolute path to the /data/raw/ directory.

    Relies on get_data_path to ensure path consistency.

    Returns:
        Path: Full path to the /data/raw/
    """
    return get_data_path() / 'raw'

def get_processed_data_path() -> Path:
    """
    Returns the absolute path to the /data/processed/ directory.

    Relies on get_data_path to ensure path consistency.

    Returns:
        Path: Full path to the /data/processed/
    """
    return get_data_path() / 'processed'