# https://www.247roulette.org/

from time import sleep as wait

import keyboard
import pyautogui

from settings import *


def get_safe_bet(expenses: int) -> int:
    return expenses // (WIN_RATE - 1) + 1


def get_required_tokens(money_amount: int) -> dict:
    result = {}

    for token in AVAILABLE_TOKENS:
        quantity, money_amount = divmod(money_amount, token)
        result[str(token)] = quantity

    return result


def make_a_bet(current_bet: int, destination_field: str = None) -> None:
    global last_bet
    destination_field = destination_field or next(iter(FIELDS_LOCATIONS))

    if last_bet > current_bet:
        pyautogui.click(*CLEAR_TABLE_POINT)
        last_bet = current_bet
    elif last_bet <= current_bet:
        current_bet, last_bet = current_bet - last_bet, current_bet

    for token, quantity in get_required_tokens(current_bet).items():
        for _ in range(quantity):
            pyautogui.click(*TOKENS_LOCATIONS[token])
            pyautogui.click(*FIELDS_LOCATIONS[destination_field])


def get_bet_result() -> str:  # 'win' / 'lose'
    pyautogui.click(*SPIN_ROULETTE_POINT)
    pyautogui.doubleClick(*SKIP_POINT)

    wait(RESULTS_WAIT_TIME)
    try:
        pyautogui.locateOnScreen(str(LOSE_IMAGE_PATH))
        return 'lose'
    except pyautogui.ImageNotFoundException:
        return 'win'
    finally:
        pyautogui.click(*SKIP_POINT)
        wait(SPIN_WAIT_TIME)


if __name__ == '__main__':
    money = START_MONEY
    bet = FIRST_BET
    last_bet = 0
    expenses = 0

    wait(PROGRAM_START_DELAY_TIME)
    while money > 0 and not keyboard.is_pressed(STOP_KEY):
        credit = bet if bet < money else money

        make_a_bet(credit)
        expenses += credit
        money -= credit

        if get_bet_result() == 'win':
            money += credit * WIN_RATE
            bet, expenses = FIRST_BET, 0
        else:
            bet = get_safe_bet(expenses)
