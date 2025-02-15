import argparse
from stringDatabase import StringDatabase
from Guess import Guess

def main():
    # Check if the correct number of command-line arguments is provided
    parser = argparse.ArgumentParser(description='Play or test the guessing game.')
    parser.add_argument('command', choices=['play', 'test'], help='Choose either play or test.')

    args = parser.parse_args()
    
    # Get the filename from the command-line arguments
    filename = "four_letters.txt"

    # Create a StringDatabase object using the specified filename
    string_db = StringDatabase(filename)

    # Create a Guess object, passing the StringDatabase object as an argument
    guess_game = Guess(string_db)  

    # Start the guessing game
    if args.command == 'play' or args.command == 'test':
        guess_game.play_game()
    else:
        exit(0)

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()

