import json
from pathlib import Path

__all__ = (
    'STOP_KEY',
    'LOSE_IMAGE_PATH',
    'TOKENS_LOCATIONS',
    'AVAILABLE_TOKENS',
    'FIELDS_LOCATIONS',
    'CLEAR_TABLE_POINT',
    'SPIN_ROULETTE_POINT',
    'SKIP_POINT',
    'PROGRAM_START_DELAY_TIME',
    'RESULTS_WAIT_TIME',
    'SPIN_WAIT_TIME',
    'WIN_RATE',
    'START_MONEY',
    'FIRST_BET',
)

STOP_KEY = 'esc'

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'data'
IMAGES_PATH = DATA_PATH / 'images'
LOSE_IMAGE_PATH = IMAGES_PATH / 'lose_image.png'

MOUSE_POINTS_PATH = DATA_PATH / 'mouse_points.json'
with open(MOUSE_POINTS_PATH) as file:
    mouse_points = json.load(file)

TOKENS_LOCATIONS = mouse_points['tokens_locations']
AVAILABLE_TOKENS = sorted([int(token) for token in TOKENS_LOCATIONS.keys()], reverse=True)
FIELDS_LOCATIONS = mouse_points['fields_locations']
CLEAR_TABLE_POINT = mouse_points['clear_table_point']
SPIN_ROULETTE_POINT = mouse_points['spin_roulette_point']
SKIP_POINT = mouse_points['skip_point']

PROGRAM_START_DELAY_TIME = 5
RESULTS_WAIT_TIME = 1
SPIN_WAIT_TIME = 0.5

WIN_RATE = 36
START_MONEY = 2_500
FIRST_BET = AVAILABLE_TOKENS[-1]
