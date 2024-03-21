import json
import difflib

with open("data.json", "r") as file:
    y = json.load(file)


# print(y["abandoned industrial site"])

def get_definition(user_data, dict):
    user_data =user_data.lower()
    if user_data in dict:
        return dict[user_data]
    else:
        similar_words = difflib.get_close_matches(user_data,dict.keys(), n=3,cutoff=0.8)
        if similar_words:
            suggestion = similar_words[0]
            return f"Word not Found. Did you mean '{suggestion}'?"
        else:
            return "Word not found."


while True:
    # Take input from the user
    user_input = input("Enter a word or type 0 to exit: ")
    if user_input.lower() =='0':
        print("Exiting...")
        break
    search_result = get_definition(user_input,y)

     # Print the result
    if len(search_result) == 1:
        print(search_result[0])  # If only one definition, print it
    else:
        print(search_result)