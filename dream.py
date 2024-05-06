import json
import re
import sys
import datetime 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#update the list of dicts directly while still calling from it
with open('general_info.py', 'r') as file:
    themes_terms_meanings = json.load(file)['themes_terms_meanings'] 

class Dream:
    dream_counter = 0
    dream_data_list = []

    def __init__(self):  # EVERYONE
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
        # Load existing dream data if available
        try:
            with open('dream_data.json', 'r') as file:
                Dream.dream_data_list = json.load(file)
                if Dream.dream_data_list:
                    Dream.dream_counter = Dream.dream_data_list[-1]['dream_id']
        except FileNotFoundError:
            # File doesn't exist, will be created on the first dream entry
            Dream.dream_data_list = []

        self.dream_id = Dream.dream_counter + 1
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
        self.dream_contents_list = []
        self.dream_data_list = []
        self.dream_mode = None
        self.set_dream_mode()

    def dream_info(self):  # KHOA DO
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
        # Ask user to input and validate the date with a loop
        while True:
            self.date = input("Enter the date of the dream (YYYY-MM-DD): ")
            if not re.match(r'\d{4}-\d{2}-\d{2}', self.date):
                print("Date is not in the correct format (YYYY-MM-DD). Please try again.")
                continue
            try:
                # Try to create a datetime object to validate the date
                datetime.datetime.strptime(self.date, '%Y-%m-%d')
                break  # Exit the loop if the date is valid
            except ValueError:
                print("Date is invalid. Please enter a valid date.")

        # Validate the time with a loop
        while True:
            self.time = input("Enter the time you woke up (HH:MM): ")
            if not re.match(r'\d{2}:\d{2}', self.time):
                print("Time is not in the correct format (HH:MM). Please try again.")
                continue
            try:
                # Try to create a time object to validate the time
                datetime.datetime.strptime(self.time, '%H:%M')
                break  # Exit the loop if the time is valid
            except ValueError:
                print("Time is invalid. Please enter a valid time.")

        self.dream_contents = input("Describe your dream: ")
        if not self.dream_contents:
            raise ValueError("Dream description cannot be empty.")
        self.find_dream_theme()
        # Prepare dictionaries for the lists
        dream_data_dict = {
            'dream_id': self.dream_id,
            'date': self.date,
            'time': self.time,
            'dream_contents': self.dream_contents,
            'top_theme': self.top_theme
        }

        # Append the new dream data
        Dream.dream_data_list.append(dream_data_dict)

        # Store the data in an external file
        with open('dream_data.json', 'w') as file:
            json.dump(Dream.dream_data_list, file, indent=4)

        print(f"Dream with ID {self.dream_id} has been recorded.")

    def generalize_dream(self):  # STINA
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

     def set_dream_mode(self):
        while True:
            mode = input("Do you want to input a new dream or read a previous one? (input/read): ").lower().strip()
            if mode == "input":
                self.dream_mode = "input"
                break
            elif mode == "read":
                self.dream_mode = "read"
                break
            else:
                print("Invalid choice. Please enter 'input' or 'read'.")

            if self.dream_mode == "input":
                self.dream_info() 
            elif self.dream_mode == "read":
                self.read_previous_dream() 

    def read_previous_dream(self):
        """
        Read and display previous dreams stored in the dream_data_list.
        """
        if not self.dream_data_list:
            print("No previous dreams found.")
            return

        print("Previous Dreams:")
        for dream in self.dream_data_list:
            print(f"Dream ID: {dream['dream_id']}, Date: {dream['date']}, Time: {dream['time']}")
        
        dream_id = input("Enter the ID of the dream you want to read: ")
        found_dream = False
        for dream in self.dream_data_list:
            if str(dream['dream_id']) == dream_id:
                print("Dream Contents:")
                print(dream['dream_contents'])
                found_dream = True
                break
            
        if not found_dream:
            print("Dream not found.")


    def find_dream_theme(self):  # MAYA
        """
        Analyzes dream contents to find top three most prevalent themes.

        Args:
            none

        Side effects:
            Updates attributes of class's instance for:
                -dream_patterns
                -themes_variations
                -count_word
                -term_overlap
                -count_theme
                -top_3
                -top_theme
        """
        self.generalize_dream()
        words = self.dream_contents.split()

        for term in self.general_terms:
            matches = [word.lower() for word in words if word.lower() == term]
            self.dream_patterns.extend(matches)

        try:
            if not self.dream_patterns:
                raise ValueError
        except ValueError:
            print("No matches found in dream contents for analysis.")
            return

        # shows all variation terms per each theme
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

        # finds the amount of times a variation/term of a certain theme
        for word in self.dream_patterns:
            for theme, theme_variations in self.themes_variations.items():
                if word in theme_variations:
                    self.count_theme[theme] = self.count_theme.get(theme, 0) + 1

        # find top theme and top 3 and assign back to attribute of instance
        self.top_3 = sorted(self.count_theme, key=self.count_theme.get, reverse=True)[:3]

        self.top_theme = self.top_3[0] if self.top_3 else None

    def dream_analysis(self):  # MALIK
        """
        Writes unique f-string analysis dependant on top_theme. A uniquely
        formatted f-string should be written for each theme.

        Returns the appropriate f-string.

        Concepts:
        - Conditional Expressions
        - F-strings Containing Expressions
        """
        intro = f"Your top three themes were {', '.join(self.top_3)}. Among those your most prevelant theme was {self.top_theme}."

        if self.top_theme == "stress and anxiety":
            return (
                f"{intro} Your dream indicates you are feeling high levels of stress and anxiety. Imagery such as {', '.join(self.dream_patterns)} are often "
                f"associated with high stress levels increased anxiety.")
        elif self.top_theme == "transitions and changes":
            return (
                f"{intro} Your dream indicates you are in a period of transitions and change. Imagery such as {', '.join(self.dream_patterns)} are often "
                f"associated with high stress levels")
        elif self.top_theme == "positive emotional states.":
            return (
                f"{intro} Your dream indicates you are in a positive emotional state currently in your life. Imagery such as {', '.join(self.dream_patterns)} are"
                f"often associated with positive emotional states.")
        elif self.top_theme == "needs and wants":
            return (
                f"{intro} Your dream indicates you are currently in need of something or have a strong desire for something specific."
                f" Imagery such as {', '.join(self.dream_patterns)} are often associated with a subconcious desire for something.")
        elif self.top_theme == "relationships":
            return (
                f"{intro} Your dream indicates you are currently focused on relationships, and it is weighing heavily on your mind."
                f" Imagery such as {', '.join(self.dream_patterns)} are often associated with your subconcious thoughts about a relationship in your life.")
        elif self.top_theme == "reflection":
            return (
                f"{intro} Your dream indicates you are currently in a deep state subconcious state of reflection, Imagery such as {self.dream_patterns} are"
                f" often associated with a deep mental state of reflection.")
        elif self.top_theme == "fears":
            return (
                f"{intro} Your dream indicates you have been thinking critically about fear, and is currently a large part of your subconcious."
                f" Imagery such as {', '.join(self.dream_patterns)} are often associated with a high subconcious level of fear.")
        elif self.top_theme == "spiritual insights":
            return (
                f"{intro} Your dream indicates you subconciously long for spirtual insight. It is often associated with a desire for change, or the"
                f" end of something. Imagery such as {', '.join(self.dream_patterns)} are most associated with these ideologies.")
        elif self.top_theme == None:
            return ("There is not enough content for an analysis.")


# instantiate Dream class
dream_instance = Dream()
dream_instance.dream_info()
dream_instance.generalize_dream()
analysis = dream_instance.dream_analysis()
print(analysis)


class UpdateGeneralInfo:  # MAYA this will be very last class in the code
    def __init__(self):
        self.run_program = None
        self.theme_identity = None
        self.key_word = None
        self.variants = []
        self.meanings = []
        self.cont = None

    def theme_update(self):
        self.run_program = input("Are you trying to update the dream information term list? Enter 'yes' or 'no'.\n"
                                 "\n"
                                 "\n")
        if self.run_program.lower().strip() == "yes":
            pass
        elif self.run_program.lower().strip() == "no":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            return

        theme_dict = {
            1: "stress and anxiety",
            2: "transitions and changes",
            3: "positive emotional states",
            4: "needs and wants",
            5: "relationships",
            6: "reflection",
            7: "fears",
            8: "spiritual insights"}

        while True:
            theme_value = input('Enter the number corresponding to the theme of your term:\n'
                                '1: Stress and anxiety\n'
                                '2: Transitions and changes\n'
                                '3: Positive emotional states\n'
                                '4: Needs and wants\n'
                                '5: Relationships\n'
                                '6: Reflection\n'
                                '7: Fears\n'
                                '8: Spiritual insights\n')

            try:
                theme_value = int(theme_value)
                if theme_value not in theme_dict:
                    raise ValueError("Invalid number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 8.")

        self.theme_identity = theme_dict[theme_value]

        self.key_word = input("Enter the key word:""\n"
                              "For example:\n"
                              "skeleton""\n"
                              "\n"
                              "\n").lower().strip()

        self.variants = [variant.strip() for variant in
                         input("Enter the variations of the key term with commas to separate:\n"
                               "For example:\n"
                               "bones, skull, dead body, carcass\n"
                               "\n"
                               "\n").lower().split(',')]

        self.meanings = [meaning.strip() for meaning in
                         input("Enter the dream meanings of the key term with commas to separate:\n"
                               "For example:\n"
                               "secrets, subconscious worry, thoughts of death, guilt\n"
                               "\n"
                               "\n").lower().split(',')]

        # Finished updating attributes. Now will use to alter the general_info doc.

        new_term = {"term": self.key_word, "variations": self.variants, "meanings": self.meanings}
        themes_terms_meanings[self.theme_identity].append(new_term)
        
        data_to_dump = {"themes_terms_meanings": themes_terms_meanings}

        # updates general_info.py
        with open('general_info.py', 'w') as file:
            json.dump(data_to_dump, file, indent=4)

        print("Term added successfully.")

        self.cont = input("Any other terms to add? Type 'yes' or 'no': \n"
                          "\n")
        if self.cont.lower().strip() == "yes":
            self.theme_update()
        elif self.cont.lower().strip() == "no":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.theme_update()

        # Start the updating process for general_info


updater = UpdateGeneralInfo()
updater.theme_update()
