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
    
def theme_update():
    """
    Allows users to update external dictionary of dream themes with associated 
    terms and meanings.
    
    Prompts user to select the theme associated with their term then instructs
    them to enter the key term, variations, and associated meanings.
    
    Raises:
        ValueError: If the entered theme number is invalid.
        
    Side effects:
        Appends term dictionary as an item to the corresponding term in external
        file, general_info.py.
    """
    theme_dict = {
            1: "stress and anxiety",
            2: "transitions and changes",
            3: "positive emotional states",
            4: "needs and wants",
            5: "relationships",
            6: "reflection",
            7: "fears",
            8: "spiritual insights"}

    
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
    except ValueError:  
        print("\n\n\nInvalid input. Please enter a number between 1 and 8.\n\n\n")  
        theme_update()

    theme_identity = theme_dict[theme_value]

    key_word = input("Enter the key word:""\n"
                              "For example:\n"
                              "skeleton""\n\n\n").lower().strip()

    variants = [variant.strip() for variant in 
                input("Enter the variations of the key term with commas to separate:\n"
                               "For example:\n"
                               "bones, skull, dead body, carcass\n\n\n").lower().split(',')]

    meanings = [meaning.strip() for meaning in
                         input("Enter the dream meanings of the key term with commas to separate:\n"
                               "For example:\n"
                               "secrets, subconscious worry, thoughts of death, guilt\n\n\n").lower().split(',')]

    new_term = {"term": key_word, "variations": variants, "meanings": meanings}
    themes_terms_meanings[theme_identity].append(new_term)
        
    data_to_dump = {"themes_terms_meanings": themes_terms_meanings}

    # updates general_info.py
    with open('general_info.py', 'w') as file:
        json.dump(data_to_dump, file, indent=4)

    print("Term added successfully.")

    cont = input("Any other terms to add? Type 'yes' or 'no': \n\n\n")
    if cont.lower().strip() == "yes":
        theme_update()
    elif cont.lower().strip() == "no":
        pass
        print("\n\n\n")
    else:
        print("Invalid input. If you wish to use another function simply call the script again.")

def plot_most_repeated_dreams(json_file): 
    """
    KHOA WRITE DOCSTRING
    """
    # Load the JSON data into a DataFrame
    df = pd.read_json(json_file)

    # Prepare the figure for plotting
    plt.figure(figsize=(12, 8))

    # Showing only the top 10 (if the dataset is large)
    top_dreams = df['top_theme'].value_counts().head(10)

    # Create a bar plot for the most common dream contents
    sns.barplot(x=top_dreams.values, y=top_dreams.index, hue=top_dreams.index, palette='coolwarm')

    # Add titles and labels
    plt.title('Most Repeated Dream Themes')
    plt.xlabel('Frequency')
    plt.ylabel('Themes')

    # Disable the legend
    plt.legend([], frameon=False)

    # Improve layout
    plt.tight_layout()

    # Show the plot
    plt.show()


def dream_pandas():
    """
    Reads dream data from the JSON and filters based on date, dream ID, or top theme, or includes option to return all dream data based on 
    paramaters set by the user.
    Note: collabrative coding efforts with Khoa and Maya to connect dream_pandas() to dream_info(), and dream_update() with permission from Khoa and Maya.

    Parameters:
        None

    Returns:
        None

    Raises:
        ValueError: If the date format is incorrect or an invalid date is entered.
        NotImplementedError: If the selected filter is not implemented yet.

    """
    df = pd.read_json("dream_data.json")
    
    filter_choice = input("Return all, or limit by date, dream id"
                          ", or top theme?\n\n"
                          "enter(all/date/dream id/top theme): ").lower().strip()
    
    if filter_choice == "all": 
        filtered_df = df

    elif filter_choice == "date":
        date = input("Enter the date of the dream (YYYY-MM-DD): ")
        if not re.match(r'\d{4}-\d{2}-\d{2}', date):
            print("Date is not in the correct format (YYYY-MM-DD). Please try again.")
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Date is invalid. Please enter a valid date.")
                
        desire = input("\n\nDo you want a single date's data or to display"
                       " all data before or after the base date?\n\n"
                       "enter (base/before/after)\n\n")
        
        if desire in ["base", "before", "after"]:
            pass
         
        else:
            raise ValueError("Invalid command. Please run again.")
        
        if desire == "base":
            filtered_df = df[df["date"] == date]
        if desire == "before":
            filtered_df = df[df["date"] <= date]
        if desire == "after":
            filtered_df = df[df["date"] >= date]
            
    elif filter_choice == "dream id":
        dream_id = int(input("Enter the dream ID you want to search: "))
        
        desire = input("\n\nDo you want a single dream id's data or to display"
                       " all data before or after the base dream id?\n\n"
                       "enter (base/before/after)\n\n")
        
        if desire in ["base", "before", "after"]:
            pass
         
        else:
            raise ValueError("Invalid command. Please run again.")
        
        if desire == "base":
            filtered_df = df[df["dream_id"] == dream_id]
        if desire == "before":
            filtered_df = df[df["dream_id"] <= dream_id]
        if desire == "after":
            filtered_df = df[df["dream_id"] >= dream_id]

    elif filter_choice == "top theme":
        
        theme_dict = {
            1: "stress and anxiety",
            2: "transitions and changes",
            3: "positive emotional states",
            4: "needs and wants",
            5: "relationships",
            6: "reflection",
            7: "fears",
            8: "spiritual insights"}

    
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
        except ValueError:  
            print("\n\n\nInvalid input. Please enter a number between 1 and 8.\n\n\n")  
            dream_pandas()

        theme_identity = theme_dict[theme_value]
        filtered_df = df[df['top_theme'] == theme_identity]

    else:
        raise NotImplementedError("Selected filter is not implemented yet."
                                  "Please run program again.")
    
    print(filtered_df)
class Dream:
    """
    Takes user inputted dream data and returns analysis, stores data to external
    files, allows for dream lookup by dream ID, and allows for external 
    fucntions to be called for data visualization or external file alteration.
     
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
        -theme_terms  STINA
        -general_terms  STINA
        -themes_variations  STINA
        -count_word (dict): counts the number of occurance for terms in 
        dream_patterns. Key is the term and value is the number of occurances.
        -count_theme (dict): counts the number of terms in dream_patterns that 
        correspond with each theme. Key is theme name and value is the number of
        occurances.
        -dream_contents_list  KHOA
        -dream_data_list   KHOA
        -dream_mode  STINA
        -set_dream_mode()  STINA
    """
    dream_counter = 0
    dream_data_list = []

    def __init__(self):  
        """
        Initializes Dream class.
        """
        # Load existing dream data if available
        try:
            with open('dream_data.json', 'r') as file:
                Dream.dream_data_list = json.load(file)
                if Dream.dream_data_list:
                    Dream.dream_counter = Dream.dream_data_list[-1]['dream_id']
        except FileNotFoundError:
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

    def dream_info(self):
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

    def generalize_dream(self): 
        '''
        Processes a dictionary of themes to extract term variations and main terms.

        Returns:
            tuple:
                - A list of all term variations from the themes.
                - A dictionary mapping each theme to its list of main terms.

        This function iterates through the dictionary where all of the themes 
        are linked to terms and their variations. It compiles a list of all 
        variations and a dictionary that connect each theme to its primary terms.

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
        """
        Provide the user with an interactive menu in which they can select from a series of options to interact with their dream jornual. 
        The user is able to input new dreams, read previous ones, update themes, plot theme data, retrieve a dataframe, or exit the program.
        
        Raises:
            SystemExit: Exits the program when the user chooses to exit.
        Side Effects:
            Reads from dream_data.json
            Interacts with user via command line
        """
        while True:
            mode = input("Do you want to:\n"
                         "input a new dream\n"
                         "read a previous one\n"
                         "update the terms\n"
                         "plot theme data for all dreams\n"
                         "get a dataframe of dreams (df)\n"
                         "exit the program\n"
                         "\n"
                         "enter:(input/read/update/plot/df/exit): ").lower().strip()
            if mode == "input":
                self.dream_info()  
                self.dream_analysis()
                break
            elif mode == "read":
                self.read_previous_dream() 
                break
            elif mode == "update":
                theme_update()
                break
            elif mode == "exit":
                print("Goodbye!")
                sys.exit()
            elif mode == "plot":
                plot_most_repeated_dreams('dream_data.json')
            elif mode == "df":
                dream_pandas()
            else:
                print("Invalid choice.")

    def read_previous_dream(self):
        """
        Display a list of previous dreams from a JSON file and allow the user to select the dream that they want to view.
        The dreams are identified by their  ID, and the user inputs the ID of the dream they want to read, the selected dream is then displayed
        
        Raises:
            FileNotFoundError: If the 'dream_data.json' file does not exist.

        Side Effects:
            Reads from a file named 'dream_data.json' 
            interacts with the user via the command line.
            This method might print an error messages if the dream is not found.
        """
        with open('dream_data.json', 'r') as file:
            dream_data_list = json.load(file)

        print("Previous Dreams:")
        for dream in dream_data_list:
            print(f"Dream ID: {dream['dream_id']}, Date: {dream['date']}, Time: {dream['time']}")
            
        dream_id = input("Enter the ID of the dream you want to read:")
        
        for dream in dream_data_list:
            if str(dream['dream_id']) == dream_id:
                print("Dream Contents:")
                print(dream['dream_contents'])
                break
            
            if not dream in dream_data_list:
                print("Dream not found.")
            
    def find_dream_theme(self): 
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

    def dream_analysis(self):  
        """
        Writes unique f-string analysis dependant on top_theme. A uniquely
        formatted f-string should be written for each theme.

        Returns the appropriate f-string.

        Concepts:
        - Conditional Expressions
        - F-strings Containing Expressions
        """
        intro = f"\n\n\nYour top themes were {', '.join(self.top_3)}. Among those your most prevelant theme was {self.top_theme}.\n\n\n"

        if self.top_theme == "stress and anxiety":
            print(
                f"{intro} Your dream indicates you are feeling high levels of stress and anxiety. Imagery such as {', '.join(self.dream_patterns)} are often "
                f"associated with high stress levels increased anxiety.\n\n\n")

        elif self.top_theme == "transitions and changes":
            print(
                f"{intro} Your dream indicates you are in a period of transitions and change. Imagery such as {', '.join(self.dream_patterns)} are often "
                f"associated with high stress levels.\n\n\n")
               
        elif self.top_theme == "positive emotional states":
            print(
                f"{intro} Your dream indicates you are in a positive emotional state currently in your life. Imagery such as {', '.join(self.dream_patterns)} are"
                f"often associated with positive emotional states.\n\n\n")
              
        elif self.top_theme == "needs and wants":
            print(
                f"{intro} Your dream indicates you are currently in need of something or have a strong desire for something specific."
                f" Imagery such as {', '.join(self.dream_patterns)} are often associated with a subconcious desire for something.\n\n\n")
             
        elif self.top_theme == "relationships":
            print(
                f"{intro} Your dream indicates you are currently focused on relationships, and it is weighing heavily on your mind."
                f" Imagery such as {', '.join(self.dream_patterns)} are often associated with your subconcious thoughts about a relationship in your life.\n\n\n")
            
        elif self.top_theme == "reflection":
            print(
                f"{intro} Your dream indicates you are currently in a deep state subconcious state of reflection, Imagery such as {self.dream_patterns} are"
                f" often associated with a deep mental state of reflection.\n\n\n")
           
        elif self.top_theme == "fears":
            print(
                f"{intro} Your dream indicates you have been thinking critically about fear, and is currently a large part of your subconcious."
                f" Imagery such as {', '.join(self.dream_patterns)} are often associated with a high subconcious level of fear.\n\n\n")
            
        elif self.top_theme == "spiritual insights":
            print(
                f"{intro} Your dream indicates you subconciously long for spirtual insight. It is often associated with a desire for change, or the"
                f" end of something. Imagery such as {', '.join(self.dream_patterns)} are most associated with these ideologies.\n\n\n")
           
        elif self.top_theme == None:
            print("\n\n\nThere is not enough content for an analysis.\n\n\n")

if __name__ == "__main__":
    dream_instance = Dream()
    dream_instance.set_dream_mode() 







