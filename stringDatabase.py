import random

class StringDatabase:
    def __init__(self, filename):
        # Initialize the class with words loaded from the specified file
        self.words = self.load_words(filename)

    def load_words(self, filename):
        try:
            # Open the file and read words into a list
            with open(filename, 'r') as file:
                words = file.read().split()
            return words
        except FileNotFoundError:
            # Handle the case when the file is not found
            print(f"Error: File '{filename}' not found.")
            return []

    def get_random_word(self):
        # Check if there are words loaded in the database
        if not self.words:
            print("No words loaded.")
            return None
        # Return a randomly selected word from the loaded words
        return random.choice(self.words)
