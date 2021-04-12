import json
from exceptions import NotEnoughPlayers, UnauthorisedPlayers, DuplicatePlayer


class Game:
    def __init__(self, players: list[tuple[str, str]]):
        self.validate_players(players)
        self.players = [u for u, p in players]

    def validate_players(self, players: list[tuple[str, str]]):
        if len(players) < 2:
            raise NotEnoughPlayers()

        unauthorised = []
        authorised = []
        accounts = json.load(open('accounts.json'))

        for user, _pass in players:
            if accounts.get(user) != _pass:
                unauthorised.append(user)
            elif user in authorised:
                raise DuplicatePlayer(user)
            else:
                authorised.append(user)

        if len(unauthorised) > 0:
            raise UnauthorisedPlayers(unauthorised)
