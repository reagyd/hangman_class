from words import DICIONARY
import random # used to generate random word from the words list

#import array as arr
"""This will be my hangman program that I am making"""

class Hangman:
    current_stack = ""
    num_wrong_guesses = 0 # the number of wrong gussees
    user_guess = "" # the users current guesses
    current_word = "word" # the current work
    guess_to_check = True # is the currnent guess in the current word
    blank = "_"
    guessed_letters = "".upper()

    def __init__(self):
        # TODO: this will initialize the hangman class
        self.current_word = random.choice(DICIONARY).upper()
        # self.guess_to_check = False # 
        

    def add_wrong_guess(self):
        if self.user_guess in self.current_word and self.user_guess not in self.guessed_letters:
          pass
        else:
          self.num_wrong_guesses += 1 # self.add_wrong_guess
          self.guessed_letters.appennd(self.user_guess)

    def current_user_guess(self):
        guess = input("what is your guess: ").upper()     
        self.user_guess = guess

    def draw_hangman(self):
        if self.num_wrong_guesses == 1:
            print(

                                            """
                                            |
                                            |
                                            """
                   )    
        elif self.num_wrong_guesses  == 2:
          #  self.add_to_wrong_guses()
            print(
                                            """
                                             ____   
                                            |
                                            |
                                            |
                                            """
                   )
        elif self.num_wrong_guesses  == 3:
            # self.add_to_wrong_guses()                
                print(
                                              """
                                             ____   
                                            |    |
                                            |    0
                                            |
                                            """
                   )    
        elif self.num_wrong_guesses  == 4:
            #  self.add_to_wrong_guses()
             print(
                                            """
                                             ____   
                                            |    |
                                            |    O
                                            |   / \\
                                            """
                   )              

        elif self.num_wrong_guesses  == 5:
             # self.add_to_wrong_guses()
             print(
                                            """
                                             ____   
                                            |    |
                                            |    O
                                            |   /|\\  
                                            |    
                                            """
            )
        elif self.num_wrong_guesses == 6:
             # self.add_to_wrong_guses()
             print(
                                            """
                                             ____   
                                            |    |
                                            |    O
                                            |   /|\\  
                                            |   / \\
                                            """
                  )

    def current_stack(self):
      self.current_stack = list(self.current_word)
      print(self.current_stack)

    def stack_to_word(self):
      pass  

    def get_current_word(self):
        # this is only for debbugging
        print(self.current_word)
        self.draw_hangman()

        
    def main_loop(self):
        #word = self.current_word
        guess = self.current_user_guess
        #for i in range(6):
        # TODO: the loop
        # self.user_guess()
        self.current_user_guess()
        self.draw_hangman()
        print(self.user_guess)
        #i = 0
        # if guess not in list(self.current_word):
        while self.num_wrong_guesses in range(6) or self.guess_to_check == False:
            self.add_wrong_guess()
                #self.set_user_guess()
        else:
            exit("yess you win")
            #self.check_win()

        print(self.num_wrong_guesses)
        #else:
         #   pass
            
    
hm = Hangman()
#hm.init_stack()
hm.get_current_word()
hm.current_stack()
hm.main_loop()