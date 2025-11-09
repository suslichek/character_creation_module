from random import randint
from graphic_arts.start_game_banner import run_screensaver
from typing import Dict, Type, Union, Callable

DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (1, 5)
    SPECIAL_SKILL: str = "Удача"
    SPECIAL_BUFF: int = 10
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'

    def __init__(self, name: str) -> None:
        self.name: str = name

    def attack(self) -> str:
        value_attack: int = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        message: str = (f'{self.name} нанёс урон противнику равный '
                   f'{value_attack}')
        return message
    
    def defence(self) -> str:
        value_defence: int = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        message: str = (f'{self.name} блокировал {value_defence} урона')
        return message
    
    def special(self) -> str:
        message: str = (f'{self.name} применил специальное умение '
                   f'"{self.SPECIAL_SKILL}{self.SPECIAL_BUFF}"')
        return message
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


    


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple[int, int] = (3, 5)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (5, 10)
    SPECIAL_SKILL: str = "Выносливость"
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple[int, int] = (5, 10)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (-2, 2)
    SPECIAL_SKILL: str = "Атака"
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple[int, int] = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (2, 5)
    SPECIAL_SKILL: str = "Защита"
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30


def choice_char_class(char_name: str) -> Character:

    game_classes: dict[str, Type[Character]] = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: Union[str, None] = None
    
    while approve_choice != 'y':
        selected_class: str = input('Введи название персонажа, за которого хочешь '
                           'играть: Воитель — warrior,'
                           'Маг — mage,'
                           'Лекарь — healer: ')
        if selected_class  in game_classes:
            char_class: Character = game_classes[selected_class](char_name)
            print(char_class)
        else:
            print('Такого персонажа нет в списке, выберете персонажа из списка')
            continue
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(char_class) -> str:
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    commands: dict[str, Callable[[], str]] = {'attack': char_class.attack, 'defence': char_class.defence, 'special': char_class.special}
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print(commands[cmd]())
        else:
            print('Такая команда не прусмотрена, попробуй еще!')
    return 'Тренировка окончена.'


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: Character = choice_char_class(char_name)
    print(start_training(char_class))

