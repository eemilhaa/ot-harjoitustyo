import os
from dotenv import load_dotenv


def get_display_size(display_height):
    """Calculates the display dimensions.

    Args:
        display_height: The desired window height in pixels

    Returns:
        A tuple with the display dimension. The aspect ratio is always 4:3.
    """

    try:
        display_height = int(display_height)
    except ValueError:
        display_height = 900
        print("invalid display height value in .env, using defaults")

    return (
        display_height / 0.75,
        display_height
    )


dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass


DISPLAY_SIZE = get_display_size(
    display_height=os.getenv("DISPLAY_HEIGHT") or 900
)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.db"
DATABASE_FILEPATH = os.path.join(dirname, '..', "data", DATABASE_FILENAME)
