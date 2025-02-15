from Game import Game
import os

class Guess:
    def __init__(self, string_db):
        # Initialize the Guess object with necessary attributes
        self.string_db = string_db
        self.word_to_guess = string_db.get_random_word()
        self.mode = " "
        self.mode_flag = True
        self.current_guess = "----"
        self.letters_guessed = []
        self.badGuesses = 0
        self.missedLetters = 0
        self.gameStatus = "-"
        self.games = []  


    def clear_console(self):
        # Use the 'os' module to clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        


    def game_mode(self):
        # Allow the user to choose between play ('p') and test ('t') modes
        self.clear_console()
        G_mode = input("Enter the mode for your game; p = play , t = test : ")
        while True:
            if G_mode.lower() == 'p':
                self.mode = 1
                break
            elif G_mode.lower() == 't':
                self.mode = 2
                break
            else:
                G_mode = input("Invalid Option. Please re-enter: ")



    def display_menu(self):
        # Display the current state of the game
        print("++\n++ The great guessing game\n++\n")
        if self.mode == 2:
            print("Current word: ", self.word_to_guess)
        print(f"Current Guess: {self.current_guess}")
        print(f"Letters Guessed: {', '.join(self.letters_guessed)}")
        print("\ng = guess, t = tell me, l for a letter, q to quit\n")



    def guess_word(self):
        # Ask the user to guess the entire word
        user_guess = input("\nEnter your guess: ")
        if user_guess.lower() == self.word_to_guess.lower():
            self.gameStatus = "Success"
            print("\n@@\n@@ FEEDBACK: You're right, Einstein!\n@@\n")
            input("Press any key to continue... ")
            self.new_game()
        else:
            self.badGuesses += 1
            print("\n@@\n@@ FEEDBACK: Try again, Loser!\n@@\n")
            input("Press any key to continue... ")
            self.play_game()



    def tell_me_word(self):
        # Provide the user with the correct word and start a new game
        self.gameStatus = "Gave up"
        print(f"\n@@\n@@ FEEDBACK: You really should have guessed this...'{self.word_to_guess}'\n@@\n ")
        input("Press any key to continue... ")
        self.new_game()



    def guess_letter(self):
        # Ask the user to guess a letter
        letter = input("\nEnter a letter: ")
        self.letters_guessed.append(letter)
        letter_lower = letter.lower()
        count = 0
        match_found = False

        for i in range(len(self.word_to_guess)):
            if self.word_to_guess[i].lower() == letter_lower:
                # Update the current guess if the letter is found in the word
                self.current_guess = (
                    self.current_guess[:i] + letter + self.current_guess[i + 1:]
                )
                count += 1
                match_found = True

        if (self.current_guess.lower() == self.word_to_guess.lower()):
            # User successfully guessed the entire word and lose all points though win the game
            self.gameStatus = "Success"
            self.missedLetters += count
            print("\n@@\n@@ FEEDBACK: Woo Hoo, You guessed all the right letters!\n@@\n")
            input("Press any key to continue... ")
            self.new_game()
        elif (match_found):
            # User found at least one letter in the word
            self.missedLetters += count
            print(f"\n@@\n@@ FEEDBACK: Woo Hoo, You found {count} letter(s)\n@@\n")
            input("Press any key to continue... ")
        else:
            # No match found for the guessed letter
            print("\n@@\n@@ FEEDBACK: Not a single match, Genius\n@@\n")
            input("Press any key to continue... ")



    def play_game(self):
        # Main game loop
        if self.mode_flag:
            # Determine the game mode if not set
            self.game_mode()
            self.mode_flag = False

        display_menu_flag = True

        while True:
            if display_menu_flag:
                self.clear_console()
                self.display_menu()
                choice = input("Enter Option: ")

            if choice.lower() == "g":
                self.guess_word()
                break
            elif choice.lower() == "t":
                self.tell_me_word()
                break
            elif choice.lower() == "l":
                self.guess_letter()
            elif choice.lower() == "q":
                # Quit the game and generate a final report
                print("\nQuitting the game...")
                self.generate_final_report()
                exit(0)
            else:
                # Handle invalid options
                choice = input("Invalid Option. Please re-enter: ")
                display_menu_flag = False
                continue

            display_menu_flag = True
            



    def new_game(self):
        # Store game information in the games list
        game_score = self.calculate_score(
            self.word_to_guess,  # Current word
            self.badGuesses,  # Bad guesses
            len(self.letters_guessed)  # Letter Guesses
        )
        game_info = Game(
            self.word_to_guess, # Current word
            self.gameStatus, #Game status
            self.badGuesses, # Bad guesses
            self.missedLetters, # Missed letters
            game_score
        )
        self.games.append(game_info)

        # Start a new game 
        self.word_to_guess = self.string_db.get_random_word()
        self.current_guess = "----"
        self.letters_guessed = []
        self.bad_guesses = 0
        self.missedLetters = 0
        # Play the next game
        self.play_game()


    
    def calculate_score(self, word, bad_guesses, letter_guesses):
        # Calculate the score based on the word, bad guesses, and letter guesses
        letter_frequencies = {
            'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23,
            'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03,
            'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99,
            's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
            'y': 1.97, 'z': 0.07
        }

        total_score = 0
        for letter in word:
            if letter.lower() in letter_frequencies and letter.lower() not in self.current_guess:
                total_score += letter_frequencies[letter.lower()]

        if letter_guesses > 0:
            total_score /= letter_guesses

        if bad_guesses > 0:
            total_score *= 0.1 * bad_guesses  # 10% penalty for each incorrect guess

        if self.gameStatus == "Gave up":
            total_score *= -1 

        return round(total_score, 2)

 

    def generate_final_report(self):
        # Display the final game report
        self.clear_console()
        print("\n++\n++ Game Report\n++\n")
        print("Game\tWord\tStatus\tBad Guesses\tMissed Letters\tScore")
        print("----\t----\t------\t-----------\t--------------\t-----")

        for idx, game in enumerate(self.games, start=1):
            print(f"{idx}\t{game.word}\t{game.status}\t\t{game.bad_guesses}\t\t{game.missed_letters}\t{game.score}")

        final_score = round(sum(game.score for game in self.games) , 2)
        print(f"\nFinal Report: {final_score}")

