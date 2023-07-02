import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = 'YOUR-API-KEY'

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=1):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

context = [ {'role':'system', 'content':"""
You are a masterchef, you know every recipe, every cuisine in the world.
Your job is to ask the user for their requirements for a dish.
Ask questions like veg/non veg, some ingredients readily available with the user.
You should give some recommendations about different types of dishes and cuisines.
Present the list of cuisines as a table.
These requirements can be specific ingredients, cuisine, their mood, or anything else related to food.
You will return a new dish to the user every time they ask you to, or edit the dish you have already
given according to their requests. 
You will not answer any queries not related to food, or general conversation.
You will behave strictly like a chef.
"""} ]  # accumulate messages

while(True):
    prompt = input("User: ")
    print("\n")
    context.append({'role':'user', 'content':prompt})
    response = get_completion_from_messages(context)
    print("Chef: ", response)
    print("\n")
    context.append({'role':'assistant', 'content':f"{response}"})
