class Game:
    # Maintain information about a specific game
    def __init__(self, word, status, bad_guesses, missed_letters, score):
        # Initialize a Game object with the given attributes
        self.word = word
        self.status = status
        self.bad_guesses = bad_guesses
        self.missed_letters = missed_letters
        self.score = score