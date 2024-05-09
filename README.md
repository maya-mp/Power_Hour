# Power_Hour Final Project

What files exist in our program's directory:

    -dream.py
        -The main script which is responsible for instantiating Dream class instances
        to obtain dream data and return an analysis of dream theme patterns to the
        user. Additionally, the user can pull from dream_data.json to read the 
        dream contents of any logged dream from dream id. The script also pulls
        from dream_data.json to allow users to see a graph of the top themes for
        each inputted dream and the frequency of each pre-set theme as a top theme.
        A data frame of contents from dream_data.json is also generated.
        The script also allows users to update the complex dictionary structure in 
        general_info.py in the command line with input statements. The user is able
        to access any of these functions in the command line through an input statement
        when the program is run.

    -general_info.py
        -The master dictionary of themes, key dream pattern terms, variations of 
        the key terms, and the dream interpretations of the key terms. It is structured 
        in a way where the keys are the theme names (stress and anxiety, transitions and changes,
        positive emotional states, needs and wants, relationships, reflection,
        fears, and spirital insights) and the values are lists with each item being
        a dictionary for each term with the respective keys and values:
            -term : the key term (str)
            -variations : key term variations (list of str)
            -meanings : meanings of key term in a dream context (list of str)

        The terms and variations in this dictionary are used to parse the dream
        contents the user enters for their Dream class instances. From the overlapping
        terms, the most prevelant themes based on word overlap are able to be determined
        for dream analysis in dream.py. This script is also modifiable in the command
        line within a method in dream.py.

    -dream_data.json
        -An external list of dream data dictionaries that is created in dream.py 
        and updated every time the input dream function in dream.py is called.
        Each inputted dream is assigned a unique dream id and has a dictionary item
        of its basic data appended to the list. Sample data is already inputted
        for the sake of demonstration.

        The keys and values for each item within the list are as follows:
            - dream_id : (int) the unique primary key assigned to each Dream 
                        instance where data is inputted
            - date : (str) YYYY-MM-DD 
                    the date in which the dream is logged
            -time : (str) HH:MM 
                    the time at which the dream is logged
            -dream_contents : (str) the inputted message of the dream as recalled
                              by the user
            -top_theme : (str) the theme from general_info.py that has the most
                        term overlap with the dream's dream_contents

How to run dream.py in the command line/how to interpret:

    What to input to get it to run: python dream.py

    The program requires no command line arguments as most of the methods are
    internal to the Dream class and do not take parameters.

    Note: after entering "python dream.py" in the command line instructions will
          pop up with options to call on different methods and functions within
          the script. Enter the specified instructional term that corresponds with
          the desired function. 

          If an error is raised and the method does not repeat, simply re-run the
          program and re-select the desired method. 

          Also, if the general_info.py is updated or more data is added to 
          dream_data.json, save the files before re-running the script if you desire
          to access the newly inputted terms or dreams.

          Finally, if you set the mode to input and enter a dream that does not have 
          overlapping terms with general_info.py no analysis will be returned as 
          returned in the terminal. Feel free to test whatever dream input you might 
          want to run. If not, here is some good sample code. Make sure to paste
          as a single line or an error will occur:

Sample dream: 

          I woke up at 3 am. A particulary supernatural time said to be when the
          spirits are most active. In my dream, I was in my bathroom and turned the
          shower on. While the water was heating up, I was shaving in the mirror.
          When I looked up to rinse my face, a skeleton was in the mirror looking 
          back at me. I jumped in fear as the skeleton slowly turned into a more
          human-like decayed ghost. The spirit did not seem friendly. It jumped
          out of the mirror and I was being chased around my house by the ghost.


Attribution:

| Method/Function        | Primary Author | Techniques Demonstrated       |
|------------------------|----------------|-------------------------------|
| theme_update           | Maya Patel     | json.dump()                   |
| plot_most_repeated_dreams | Khoa Do      | Visualizing data with pyplot |
| dream_pandas           | Malik Oumarou  | Operations on Pandas dataframes |
| Dream.__init__         | everyone       | N/A                           |
| Dream.dream_info       | Khoa Do        | Regular expressions           |
| Dream.generalize_dream | Stina Drill    | container comprehensions      |
| Dream.set_dream_mode   | Stina Drill    | OVERLAP                       |
| Dream.read_previous_dream | Stina Drill | With statement                |
| Dream.find_dream_theme | Maya Patel     | use of sorted() key function  |
| Dream.dream_analysis   | Malik Oumarou  | F-strings containing expressions |

Annotations:
    KHOA do the site for your dream_info regarding datetime and strptime. 
    - dream_info: Method Documentation

- Purpose: dream_info method is designed to collect, validate, and store user inputs regarding dream records. 
- Data Collection: The method prompts the user to enter the date, time, and content of a dream. 
- Data Validation: User input data will be validated using regex to confirm validation to expected formats (YYYY-MM-DD for date and HH:MM for time). Following regex validation, the method using Python's datetime library to construct datetime objects, making sure the inputs represent valid date and time values.
- Error Handling: The method raises a ValueError if inputs fail to match the specified patterns or if the dream description is left empty.
- Data Storage: Validated and formatted data is stored in dictionary format within a class-level list and stored externally in a JSON file, for future use and analysis for pandas.
- Date Validation: Utilizes the re.match function to validate the date format and datetime.datetime.strptime to confirm its validity as a date.
- Time Validation: Employs a similar approach as date validation, using re.match for format checking and datetime.datetime.strptime(date_string, format) is a method available from datetime module to ensure the string format appears in a logical time/date
- Dream Description: Captures an input from the user. If the input is absent, a ValueError is raised to enforce the requirement of dream content.
- The strptime function is part of the datetime module and stands for "string parse time".
- “Python Strptime().” Programiz, www.programiz.com/python-programming/datetime/strptime.
  
    - plot_most_repeated_dreams function:
      
-Purpose: The plot_most_repeated_dreams function is designed to visualize the frequency of recurring dream themes based on dream records stored in a JSON file. 
- Data Loading: The function reads dream data from a specified JSON file into a pandas DataFrame.
- Data Visualization: Using matplotlib and seaborn libraries to create a bar plot that displays the top 10 most frequent dream themes.
- Customization and Layout: Adjusts the size of the plot for clarity and disables the legend for a cleaner visual presentation, ensuring the focus remains on the data.
- Plotting: A seaborn bar plot (sns.barplot) is used for its advanced styling and easy integration with pandas data structures.
- json_file: A string representing the path to the JSON file containing the dream data.
-If the JSON file is not found or is invalid, a file-related error will be raised (e.g., FileNotFoundError).




Sources- I used all three of these sources to create the general_info.py
https://www.dreamdictionary.org/
https://www.dreambible.com/
https://www.dreammoods.com/


