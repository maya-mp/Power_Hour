import json
import re
from general_info import themes_terms_meanings 
#from (py doc of dict) import (dict name) PUT IN AFTER MAKING FILE

class Dream:
    dream_counter = 0
    def __init__(self): #EVERYONE
        Dream.dream_counter += 1
        """
        Initializes Dream class.

        Attributes:
        - dream_id (int): A unique identifier for each dream.
        - date (str): The date entered.
        - time (str): The time entered.
        - dream_contents (str): The user's dream recount.
        - dream_patterns (list): A list to store patterns found in the dream 
                                 populated in INSERT METHOD.
        -term_overlap (dict): keys are the terms present in dream_contents and
        general_terms and values are the count of their presence
        -top_3 (list): list of the top three dream themes in order of most
                        overlap to least
        -top_theme (str): the top theme based on overlap
        -dream_symbols: (dict) contains master container of general dream
                        symbols
        """
        self.dream_id = Dream.dream_counter
        self.date = None 
        self.time = None 
        self.dream_contents = None 
        self.dream_patterns = []
        self.term_overlap = {}
        self.top_3 = []
        self.top_theme = None

    def dream_info(self): #KHOA DO
        """
               Initializes Dream class.

        Attributes:
        - dream_id (int): A unique identifier for each dream.
        - date (str): The date entered.
        - time (str): The time entered.
        - dream_contents (str): The user's dream recount.
        - dream_patterns (list): A list to store patterns found in the dream 
                                 populated in INSERT METHOD.
        -term_overlap (dict): keys are the terms present in dream_contents and
        general_terms and values are the count of their presence
        -top_3 (list): list of the top three dream themes in order of most
                        overlap to least
        -top_theme (str): the top theme based on overlap 
        """
         # Ask for user input and validate it
        date = input("Enter the date of the dream (YYYY-MM-DD): ")
        if not re.match(r'\d{4}-\d{2}-\d{2}', date):
            raise ValueError("Date is not in the correct format (YYYY-MM-DD).")
        
        time = input("Enter the time you woke up (HH:MM): ")
        if not re.match(r'\d{2}:\d{2}', time):
            raise ValueError("Time is not in the correct format (HH:MM).")
        
        dream_contents = input("Describe your dream: ")
        if not dream_contents:
            raise ValueError("Dream description cannot be empty.")

        # Assign values to the instance
        self.date = date
        self.time = time
        self.dream_contents = dream_contents

        # Prepare dictionaries for the lists
        dream_data_dict = {
            'dream_id': self.dream_id,
            'date': self.date,
            'time': self.time,
        }
        dream_contents_dict = {
            'dream_id': self.dream_id,
            'dream_contents': self.dream_contents
        }

        # Append the dictionaries to the class-level lists
        Dream.dream_data_list.append(dream_data_dict)
        Dream.dream_contents_list.append(dream_contents_dict)
        
        # Store the data in an external file
        with open('dream_data.json', 'w') as file:
            json.dump(Dream.dream_data_list, file, indent=4)
        with open('dream_contents.json', 'w') as file:
            json.dump(Dream.dream_contents_list, file, indent=4)

        print(f"Dream with ID {self.dream_id} has been recorded.")

    raise NotImplementedError

def generalize_dream(self):#STINA
'''
 Processes a dictionary of themes to extract term variations and main terms.

    Returns:
        tuple:
            - A list of all term variations from the themes.
            - A dictionary mapping each theme to its list of main terms.

    This function iterates through the dictionary where all of the themes are linked to terms and
    their variations. It compiles a list of all variations and a dictionary that connect each theme to its primary terms.
    
'''    
    general_terms = []

    for theme_name, term_list in themes_terms_meanings.items():
        for term_dict in term_list:
            variations = term_dict.get("variations")
            if variations:
                general_terms.extend(variations)

theme_terms = {}
    
    for theme_name, terms_data in themes_terms_meanings.items():
        terms = [term_data['term'] for term_data in terms_data]
        theme_terms[theme_name] = terms
        
    return general_terms, theme_terms

def find_dream_theme(self): #MAYA
    raise NotImplementedError
    
def dream_analysis(self): #MALIK
    raise NotImplementedError
    
def __repr__(self): #EVERYONE - will not be written for this submission
    raise NotImplementedError


    
