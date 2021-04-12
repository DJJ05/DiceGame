from game import Game
from exceptions import InvalidCredentials
from string import ascii_uppercase, punctuation
import subprocess
import sys
import stdiomask
import json
import time


def sign_up():
    try:
        accounts = json.load(open('accounts.json'))
        user = input('Enter new username: ')

        if user in accounts:
            raise InvalidCredentials('Account with that username already exists.')
        if len(user)<4:
            raise InvalidCredentials('Username must be at least 4 characters long.')

        _pass = stdiomask.getpass(prompt='Enter new password: ', mask='*')
        print('-'*60)

        if len(_pass)<6:
            raise InvalidCredentials('Password must be at least 6 characters long.')
        if not any([p in _pass for p in punctuation]) or not any([u in _pass for u in ascii_uppercase]):
            raise InvalidCredentials('Password must contain at least 1 digit and 1 uppercase letter.')

        print('Account created successfully.')
        time.sleep(3)

        accounts[user] = _pass
        json.dump(accounts, open('accounts.json', 'w'), indent=4)
    except KeyboardInterrupt:
        ...

    return main()


def main():
    subprocess.call('clear')
    print(f"{'-'*60}\nWelcome to the homepage\n{'-'*60}")

    players = []

    while True:
        selection = input(f'Please select:\n  a to sign up\n  b to play game\n{"-"*60}\n').lower()
        print('-'*60)

        if selection not in ('a', 'b'):
            continue

        elif selection == 'a':
            return sign_up()

        else:
            accounts = json.load(open('accounts.json'))
            while True:
                try:
                    user = input(f'Enter player {len(players)+1} username (^c to start game): ')
                    if user not in accounts:
                        print('That account name does not exist.')
                        continue
                    if user in [u for u, p in players]:
                        print('That player has already been selected.')
                        continue

                    _pass = stdiomask.getpass(prompt=f'Enter {user} password: ', mask='*')
                    if accounts[user] != _pass:
                        print('That password is incorrect.')
                        continue

                    players.append((user, _pass))
                except KeyboardInterrupt:
                    break
            break

    game = Game(players)


if __name__ == '__main__':
    main()
