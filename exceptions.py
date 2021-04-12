class NotEnoughPlayers(Exception):
    def __str__(self):
        return "2 or more players needed to start."


class UnauthorisedPlayers(Exception):
    def __init__(self, players: list[str]):
        self.players = ', '.join(players)

    def __str__(self):
        return f"Players: {self.players} are unauthorised."


class DuplicatePlayer(Exception):
    def __init__(self, player: str):
        self.player = player

    def __str__(self):
        return f"Player: {self.player} has been selected twice."


class InvalidCredentials(Exception):
    def __init__(self, reason: str):
        self.reason = reason

    def __str__(self):
        return self.reason
