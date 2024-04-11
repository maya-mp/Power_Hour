import json
import re

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
        """
        #all of this will be populated in later methods
        self.dream_id = Dream.dream_counter
        self.date = None #will be str
        self.time = None #will be str
        self.dream_contents = None #will be str
        self.dream_patterns = []
        self.term_overlap = {}
        self.top_3 = []
        self.top_theme = None #will be str
        self.dream_symbols = dream_symbols

        
    def dream_info(self): #KHOA
        """
        Initializes dream data (using 3 input statements and raise value errors 
        based on regular expressions to ensure inuput is in correct format).
        
        Will assign self.date, self.time, self.dream_contents
        
        Assigns unique id to dream instance (dream_id). Assigns attribute 
        self.dream_id 
        
        Stores this data into 2 lists of dicts (one item per class instance). 
        This will be used in the next class we write which pretains more to 
        data and visualization. This data will be stored into an external file
        that will be imported into this script once we do class 2 in the next
        submission. 
        
            1. a list with each item being a dictionary with 
            keys: dream_id, date, time, dream_inst_words (list populated in 
            find_dream_theme() method)
            
            2. a list with each item being a dictionary with
            keys: dream_id, dream_contents
            
        Concepts:
        - With Statements: file operations for storing/loading dream data.
        """
        raise NotImplementedError
    
    def generalize_dream(self): #STINA
        """
        Step 1: create 5-10 lists that represent the different themes we 
        will use. The contents will be terms that are present in dreams of 
        the repective theme. 
        -note: account for terms that could be said multiple ways
                    with nested lists so that it only counts as one item in the
                    overall list. This will help when we use the max function
                    to find the most overlap to determine theme in 
                    find_dream_theme() method.
        
        Step 2:
        create master list of general dream terms called (general_terms) that
        is ALL of the terms from the themes list WITH NO OVERLAP. 
            -this will be helpful in parsing the dream_contents  
            
        Concepts:
        - Comprehension          
        """
        dream_themes = []
        for theme, symbol in self.dream_symbols.items():
            theme_list = []
            for symbol, meaning in symbols.items():
                theme_list.extend(meanings)
            dream_themes.append(set(theme_list))

        dream_terms = []
        for theme_list in dream_theme:
            for term in theme_list:
                if term not in theme_list:
                    dream_term.append(term)

        return dream_terms
                
            
        raise NotImplementedError
    
    def find_dream_theme(self): #MAYA
        """
        Uses theme lists from generalize_dreams() method. Parses dream_contents
        to fill attribute self.dream_patterns list with terms that overlap with 
        general_terms list using regular expressions. 
        
        Uses dictionary to find the count of times each present term in 
        general_terms occurs in dream_contents. Return this in a dictionary 
        where the key is the word and the value is the count. The dictionary is
        called term_overlap and is an attribute of the class object. This will
        be helpful if the number of overlaping terms is the same for multiple 
        themes and for the second class. 
        
        Uses the set() function and intersect method of sets to find the top 3
        themes called top_3. This is an attribute of the class that will be 
        filled. Uses max()
        
        Returns the theme with the most overlap as top_theme (attribute of class).
        If there is a tie in the max overlap between multiple themes, use the 
        contents of term_overlap dict to settle which one will be top_theme. 
        
        Concepts:
        - Set Operations on Set
        - Use of a Key Function: Determine the top dream themes
        - Regular Expressions
        """
        raise NotImplementedError
    
    def dream_analysis(self): #MALIK
        """
        Writes unique f-string analysis dependant on top_theme. A uniquely
        formatted f-string should be written for each theme. 
        
        Optionally: Based on the theme, it can ask the user specfific questions 
        (using input statements) to enrich the f-string results. Would use 
        if statements to see which questions to ask based on the user's answer. 
        
        Returns the appropriate f-string.   
        
        Concepts:
        - Conditional Expressions
        - F-strings Containing Expressions

        Parameters:
        - top_theme (str): The top theme based on overlap.
        """
        
        raise NotImplementedError
    
    def __repr__(self): #EVERYONE - will not be written for this submission
        raise NotImplementedError
