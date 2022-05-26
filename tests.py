import imp
import unittest
from main import get_word, display_guessed_letters, display_hangman


class TestHangman(unittest.TestCase):

    def test_randomize_word(self):
        word1 = get_word()
        word2 = get_word()
        self.assertNotEqual(word1, word2)
    

    def test_display_hangman_for_first_step(self):
        tries = 1
        hangman_steps = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # noose
                """
                   --------
                   |      |
                   |      
                   |    
                   |    
                   |     
                   -
                """,
                # upside L
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                #initial empty
                """
                """
    ]
        self.assertEqual(hangman_steps[tries], display_hangman(tries))
        

    
    def test_display_hangman_for_last_step(self):
        tries = 8
        hangman_steps = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # noose
                """
                   --------
                   |      |
                   |      
                   |    
                   |    
                   |     
                   -
                """,
                # upside L
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                #initial empty
                """
                """
    ]
        self.assertEqual(hangman_steps[tries], display_hangman(tries))
        
