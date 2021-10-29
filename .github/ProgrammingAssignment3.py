# Jonathan Ramos
# October 28th, 2021
# Programming Assignment 3
# CS 151
# Dr.Rajeev

# Function used to calculate a quarterback's rating
def quarterback_rating(completions, attempts, passing_yards, touchdown_passes, interceptions):
    if attempts != 0:
        com_att = (((completions / attempts) - 0.3) * 5)
        pass_att = (((passing_yards / attempts) - 3) * 0.25)
        touch_att = ((touchdown_passes / attempts) * 20)
        inter_att = (2.375 - ((interceptions / attempts) * 25))
    else:
        return 0
    rating = round(100 * com_att + pass_att + touch_att + inter_att / 6, 2)
    return rating

# Function used to calculate the score for one team in quidditch
def quidditch_score(goals, check_snitch):
    score = goals * 10
    if check_snitch == "yes":
        score += 30
    return score

# Function used to find the total score of one gymnast
def gymnast_score(difficulty_score, total_execution):
    avg_execution_score = total_execution / 5
    total_score = avg_execution_score + difficulty_score
    return total_score

# Function used to validate if user entered an integer
def int_input_validation(variable_to_validate, message):
    variable_to_validate = input(message)
    while variable_to_validate.isdigit() != True:
        variable_to_validate = input(message)
    variable_to_validate = int(variable_to_validate)
    return variable_to_validate


def main():
    # User input to decide where program will go (to decide which calculation will run)
    primary_choice = input("Choice of sport (football, quidditch, gymnastics):  ").lower().strip()

    # User input validation to make sure input matches one of three choices only
    while primary_choice != "football" and primary_choice != "quidditch" and primary_choice != "gymnastics":
        primary_choice = input("Please choose between; football, quidditch, gymnastics:  ").lower().strip()

    # Will run only when the user chooses the "football" option
    if primary_choice == "football":
        print("Enter the following for chosen QB\n")

        # Initializing variables where users valid input will be stored
        attempts_i = None
        completions_i = None
        passing_yards_i = None
        touchdown_passes_i = None
        interceptions_i = None

        # Asking User for following inputs of QB and Validating to make sure a digit is entered
        attempts_i = int_input_validation(attempts_i, "Enter number of attempts: ")
        completions_i = int_input_validation(completions_i, "Enter number of completions: ")
        passing_yards_i = int_input_validation(passing_yards_i, "Enter number of passing yards: ")
        touchdown_passes_i = int_input_validation(touchdown_passes_i, "Enter number of touchdown passes: ")
        interceptions_i = int_input_validation(interceptions_i, "Enter number of interceptions: ")

        # Calling quarterback rating calculation function to get the rating of the users quarterback
        qb_rating = quarterback_rating(completions_i, attempts_i, passing_yards_i, touchdown_passes_i, interceptions_i)

        # Checking to see if the users quarterback is a perfect passer with a perfect rating of 158.3
        if qb_rating == 158.3:
            perfect_passer = "is a perfect passer"
        elif qb_rating > 158.3:
            qb_rating = 158.3
            perfect_passer = "is a perfect passer"
        else:
            perfect_passer = "is not a perfect passer"
        print("\nYour Quarterback has a rating of " + str(qb_rating) + " and " + perfect_passer)

    # Will run only when the user chooses the "quidditch" option
    elif primary_choice == "quidditch":
        print("Enter the following for one team")

        # Initializing variable where a valid input will be stored
        goals_i = None
        # Asking User for following input of quidditch team and Validating to make sure correct value is entered
        goals_i = int_input_validation(goals_i,"How many goals did this team score: ")

        # User input to check if team caught the snitch or not which adds 30 points if caught
        check_snitch_i = input("Did this team catch the snitch? (yes/no): ").lower().strip()
        # User input validation to make sure input matches one of two choices only
        while check_snitch_i != "yes" and check_snitch_i != "no":
            check_snitch_i = input("Did this team catch the snitch? (yes/no): ").lower().strip()

        # Storing the score of one team into score variable using the quidditch_score function previously made
        score = quidditch_score(goals_i, check_snitch_i)
        print("\nThe score for this quidditch team is " + str(score))

    # Will run only when the user chooses the "gymnastics" option
    elif primary_choice == "gymnastics":
        print("Enter the following scores for one gymnast")

        # initializes variable and asks user for difficulty score then validates if input is an integer
        difficulty_score_i = None
        difficulty_score_i = int_input_validation(difficulty_score_i,"What is the difficulty score (0-10): ")

        # Initializes array where execution scores will be stored
        execution_scores_i = []
        # Initializes loop counter variable
        i = 0
        # Initializes variable where the sum of all execution scores is stored
        total_execution_score = 0
        # Loops 5 times to get the remaining 5 execution scores
        while i < 5:
            # Asks the user for execution scores and validates if the input value is an integer then stores in variable
            execution_scores_j = int_input_validation(execution_scores_i,("Execution score " + str(i + 1) + ": "))
            # Adds the user input score to the array of all execution scores
            execution_scores_i.append(execution_scores_j)
            # Total execution score variable is updated by the value inputted by the user at the current index
            total_execution_score += execution_scores_i[i]
            # Updates the loop counter variable in order to move on to the next iteration of loop
            i += 1

        # Gymnast function is used to get the total score of the gymnast using the users inputs
        total_score = gymnast_score(difficulty_score_i, total_execution_score)
        print("\nThe final score for this gymnast is " + str(total_score))


main()
