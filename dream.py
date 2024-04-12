import json
import re
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

def dream_info(self): #KHOA
    raise NotImplementedError

def generalize_dream(self):#STINA
    raise NotImplemented

def find_dream_theme(self): #MAYA
    raise NotImplementedError
    
def dream_analysis(self): #MALIK
    raise NotImplementedError
    
def __repr__(self): #EVERYONE - will not be written for this submission
    raise NotImplementedError


    