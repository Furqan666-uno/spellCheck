from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker() # create abject as self.spell & assign it to spellchecker()

    def correct_text(self, text):
        words = text.split()  # Splitting the input text into individual words
        correct_words = []    # List to hold corrected words

        for word in words:
            correct_word = self.spell.correction(word) # corrected word
            if correct_word != word:  # if corrected word is not equal to original word 
                print(f'Correcting {word} to {correct_word}')
                correct_words.append(correct_word)
            else:
                correct_words.append(word)  # Add unchanged word to the list 

        return ' '.join(correct_words)  # Join corrected words with a space

    def run(self):
        while True:
            text = input('Enter the text to check or type "exit" to quit: ')
            if text.lower() == 'exit':
                print('Closing the program.......')
                break
            
            corrected_text = self.correct_text(text) # sending text to line 7
            print(f'Corrected text is: {corrected_text}')

if __name__ == '__main__':
    SpellCheckerApp().run()
