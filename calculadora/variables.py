import re
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent

FILES_FOLDER = ROOT_FOLDER / 'files'

WINDOW_ICON = FILES_FOLDER / 'icone_calculadora.png'

# ? Colors
PRIMARY_COLOR = '#1e81b0'
DARKER_P_COLOR = '#16658a'
DARKEST_P_COLOR = '#115270'

# ? Sizing
BIG_FONT_SIZE = 40
MID_FONT_SIZE = 24
SMALL_FONT_SIZE = 18

TEXT_MARGING = 15
MINIMUM_WIDTH = 500


# print(WINDOW_ICON.exists())

# ? Funções regulares
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def is_num_or_dot(string: str):
    # ? Determina se o caracter se encontra no intervalo definido
    return bool(NUM_OR_DOT_REGEX.search(string))


def is_empty(string: str):
    # ? Determina se é um caracter vazio
    return len(string) == 0


def is_valid_num(string: str):
    # ? Determina se o usuário está digitando números
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid


def convert_number(string: str):
    # ? Converte os números em float ou int
    new_number = float(string)
    if new_number.is_integer():
        new_number = int(float(string))
    return new_number
