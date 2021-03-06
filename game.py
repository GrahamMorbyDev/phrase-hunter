import random
import phrase


class Game:
    # __init__ to contain missed, phrases, active phrase, guesses
    def __init__(self):
        self.missed = 0
        self.guesses = 0
        self.phrases = [phrase.Phrase('A bird in the hand is worth two in the bush'),
                        phrase.Phrase('A watched pot never boils'),
                        phrase.Phrase('Its time to bite the bullet'),
                        phrase.Phrase('Take it with a grain of salt'),
                        phrase.Phrase('Up the creek without a paddle')]
        self.active_phrase = None
        self.user_lives = 5

    def start(self):
        """Starts the game and manages user lives."""
        self.welcome()
        self.get_random_phrase()
        self.game_running()
        self.game_over()

    def game_running(self):
        while self.missed < self.user_lives:
            guess = self.get_guess()
            if not self.active_phrase.check_letters(guess):
                self.missed += 1
                print(f'You have used {self.missed} lives! You have {self.user_lives - self.missed} lives remaining')
            if self.active_phrase.check_complete():
                break

    def get_random_phrase(self):
        """Grabs a random phrase from list and sets the game instance phrase."""
        self.active_phrase = random.choice(self.phrases)
        return self.active_phrase

    @staticmethod
    def welcome():
        """Welcome message is printed out."""
        print("Are you ready to play Phrase Hunter?")
        print("Do you have what it takes?")
        print("Lets get going!")

    def get_guess(self):
        """Grabs the user guessed input and handles invalid input."""
        while True:
            self.active_phrase.display()
            letter = input('What letter would you like to choose?  ')
            if len(letter) > 1 or not letter.isalpha():
                print('Invalid input, please select a single letter')
            else:
                self.guesses += 1
                return letter

    def game_over(self):
        """Handles the end of game instance and checks for new game play."""
        if self.active_phrase.check_complete():
            print('Well done! You beat the Phrase Hunters!!')
            print('{} was the correct answer'.format(self.active_phrase))
        else:
            print('You did not manage to beat my game! HAHAHAHAHAH....')

        new_game = input('Would you like to play again? y/n ')
        if new_game.lower() == 'y':
            new_game = Game()
            new_game.start()
        elif new_game.lower() == 'n':
            print('Thank you for playing my game!')
        else:
            print('Sorry that input is invalid')
            self.game_over()
