import json
import re
from general_info import themes_terms_meanings 

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
        -top_3 (list): list of the top three dream themes in order of most
                        overlap to least
        -top_theme (str): the top theme based on overlap
        -theme_terms (dict): a dictionary of all the key term (values) 
        for all of the themes (keys) in themes_terms_meanings
        -general_terms (list): all the term variations present in 
        themes_terms_meanings
        -themes_variations (dict): a dictionary of all the variations of key 
        terms (values) for all of the themes (keys) in themes_terms_meanings
        -general_terms (list): all the term variations present in 
        themes_terms_meanings
        -count_word (dict): the number of occurances of each term variation 
        in deam_contents
        -count_theme (dict): the number of times a term variation of a given
        theme occurs (theme is key, occurace is value)
        -term_overlap (dict): similar to count_word, but the keys are the key
        terms and the values are the occurances of any variation of the key
        term
        """
        self.dream_id = Dream.dream_counter
        self.date = None 
        self.time = None 
        self.dream_contents = None 
        self.dream_patterns = []
        self.term_overlap = {}
        self.top_3 = []
        self.top_theme = None
        self.theme_terms = {}
        self.general_terms = []
        self.themes_variations = {}
        self.count_word = {}
        self.count_theme = {}
        

    def dream_info(self): #KHOA DO
        """
        Collects and validates the date, time, and narrative contents of a dream 
        from user input. It ensures that date and time are in the standard ISO 
        format (YYYY-MM-DD and HH:MM respectively). The validated input is then 
        assigned to the instance attributes and aggregated into dictionaries 
        which are appended to class-level lists for subsequent data handling and 
        visualization.

        This method performs the following steps:
        - Prompt the user for the date, time, and content of the dream.
        - Validate each input using regular expressions to match expected patterns.
        - Raise a ValueError with an informative message if the input does not 
          match the pattern.
        - If input validation is successful, store the data in instance attributes.
        - Construct dictionaries containing the dream's metadata and narrative.
        - Append these dictionaries to corresponding class-level lists.
        - Persist the updated lists to external JSON files for future retrieval and analysis.
        
        The method ensures the collection of cleanly formatted and consistent data
        for each dream entry, facilitating reliable analysis in subsequent processes.

        Raises:
            ValueError: If any of the inputs do not conform to their expected format.
        """
         # Ask for user input and validate it
        self.date = input("Enter the date of the dream (YYYY-MM-DD): ")
        if not re.match(r'\d{4}-\d{2}-\d{2}', self.date):
            raise ValueError("Date is not in the correct format (YYYY-MM-DD).")
        
        self.time = input("Enter the time you woke up (HH:MM): ")
        if not re.match(r'\d{2}:\d{2}', self.time):
            raise ValueError("Time is not in the correct format (HH:MM).")
        
        self.dream_contents = input("Describe your dream: ")
        if not self.dream_contents:
            raise ValueError("Dream description cannot be empty.")

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
        for theme_name, term_list in themes_terms_meanings.items():
            for term_dict in term_list:
                variations = term_dict.get("variations")
                if variations:
                    self.general_terms.extend(variations)    
                    
        for theme_name, terms_data in themes_terms_meanings.items():
            terms = [term_data['term'] for term_data in terms_data]
            self.theme_terms[theme_name] = terms
        
        return self.general_terms, self.theme_terms

    def find_dream_theme(self): #MAYA
        """
        Sets up information for analysis by finding important terms in the 
        user's dream contents. 
        
        Side effects:
            Updates attributes: dream_patterns, themes_variations, count_word,
            term_overlap, count_theme, top_3, and top_theme. 
        """
        #cross check each word in contents to general_terms
        words = self.dream_contents.split()
        for term in self.general_terms:
            matches = [word.lower() for word in words if word.lower() == term]
            self.dream_patterns.extend(matches)
        
        #shows all variation terms per each theme
        for theme, terms in themes_terms_meanings.items():
            theme_variations = []
            for term in terms:
                variations = term["variations"]
                theme_variations.extend(variations)
                self.themes_variations[theme] = theme_variations
        
        # finds the amount of times a variation of a term is present
        for word in self.dream_patterns:
            for theme_variations in self.themes_variations.values():
                if word in theme_variations:  
                    self.count_word[word] = self.count_word.get(word, 0) + 1

        # Update term overlap with counts for variations
        for word, occurrence in self.count_word.items():
            for theme, terms in themes_terms_meanings.items():
                for term_data in terms:
                    if word in term_data["variations"]:
                        term = term_data["term"]
                        self.term_overlap[term] = self.term_overlap.get(term, 0) + occurrence
          
        #finds the amount of times a variation/term of a certain theme
        for word in self.dream_patterns: 
            for theme, theme_variations in self.themes_variations.items():
                if word in theme_variations:
                    self.count_theme[theme] = self.count_theme.get(theme, 0) + 1

        #find top theme and top 3 and assign back to attribute of instance
        self.top_3 = sorted(self.count_theme, key=self.count_theme.get, reverse=True)[:3]
        self.top_theme = self.top_3[0]#need to allow for instances with less than three
    
    def dream_analysis(self): #MALIK
        raise NotImplementedError
    
    def __repr__(self): #EVERYONE - will not be written for this submission
        raise NotImplementedError


    
