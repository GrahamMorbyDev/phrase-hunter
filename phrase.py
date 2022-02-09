class Phrase:
    # __init__ this is the actual phrase the Phrase object is representing
    def __init__(self, phrase):
        self.phrase = phrase
        self.phrase_guess = [False] * len(phrase)
        self.check_letters(' ')

    def __str__(self):
        string = ' '
        for i, letter in enumerate(self.phrase_guess):
            if letter:
                string += self.phrase[i]
            else:
                string += '_ '

            if letter == ' ':
                string += '  '

        return string

    def display(self):
        """Prints self to console."""
        print(self)

    def check_letters(self, guess):
        """Checks for user letter in active phrase.

        Returns:
            Bool:Returning value
        """
        value = False
        for i, letter in enumerate(self.phrase):
            if guess == letter.lower():
                self.phrase_guess[i] = True
                value = True
        return value

    def check_complete(self):
        """Checks to see if phrase is guessed.

        Returns:
            Bool:Returning value
        """
        for letter in self.phrase_guess:
            if not letter:
                return False

        return True
