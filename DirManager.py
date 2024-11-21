from pathlib import Path
import logging


def check_or_create_directory(path: Path, directory_name: str, logger: logging.Logger) -> None:
    """
    Checks if a directory exists, and creates it if not.

    Args:
        path (Path): Path object for the directory.
        directory_name (str): Name of the directory for logging purposes.
        logger (logging.Logger): Logger instance for logging messages.
    """
    if not path.exists():
        path.mkdir()
        logger.info(f"{directory_name} directory created.")
    else:
        logger.info(f"{directory_name} directory exists.")


def dir_check(logger: logging.Logger) -> int:
    """
    Ensures 'mod' and 'translated' directories exist and validates their contents.

    Args:
        logger (logging.Logger): Logger instance for logging messages.

    Returns:
        int: Status code (0 for success, -1 for 'mod' error, -2 for 'translated' warning).
    """
    mod_path = Path('./mod')
    translated_path = Path('./translated')

    # Check 'mod' directory
    check_or_create_directory(mod_path, "MOD", logger)
    logger.info("Checking MOD directory...")
    if mod_file_check(mod_path, logger) == -1:
        return -1  # Do not log again here, `mod_file_check` already logs the error.

    # Check 'translated' directory
    check_or_create_directory(translated_path, "Translated", logger)
    logger.info("Checking Translated directory...")
    if translated_file_check(translated_path, logger) == -2:
        return -2  # Do not log again here, `translated_file_check` already logs the warning.

    logger.info("Directory checks completed successfully.")
    return 0


def mod_file_check(path: Path, logger: logging.Logger) -> int:
    """
    Checks if the 'mod' directory contains any files.

    Args:
        path (Path): Path object for the 'mod' directory.
        logger (logging.Logger): Logger instance for logging messages.

    Returns:
        int: Status code (0 for success, -1 for error).
    """
    file_count = sum(1 for _ in path.glob('*'))
    if file_count == 0:
        logger.error("Mod Directory Status: Error - No files found in 'mod' directory!")
        return -1

    logger.info("Mod Directory Status: Good - Files found.")
    return 0


def translated_file_check(path: Path, logger: logging.Logger) -> int:
    """
    Checks if the 'translated' directory is empty or contains files.

    Args:
        path (Path): Path object for the 'translated' directory.
        logger (logging.Logger): Logger instance for logging messages.

    Returns:
        int: Status code (0 for success, -2 for warning if files exist).
    """
    file_count = sum(1 for _ in path.glob('*'))
    if file_count > 0:
        logger.warning("Translated Directory Status: Warning - Files exist in 'translated' directory.")
        for file in path.glob('*'):
            logger.info(f"\t- {file}")
        return -2

    logger.info("Translated Directory Status: Good - No files found.")
    return 0
