# A Chatbot for Recipes

  This is an interactive chatbot made using the openAI GPT3.5 API.  
  The chatbot is capable of maintaining a conversation with the user, recommending various dishes based on the user's input such as ingredients, cuisine, etc.   
  There are two ways to use this chatbot: the first is through the API endpoint we have created, and the second is through the CLI.

# Track
  This submission is for the AI track.
  
# Techstack Used
    OpenAI API  
    Django

# API Endpoint
  The API has been deployed using pythonanywhere.  
  The link to the API endpoint is aaditnayyar.pythonanywhere.com/api/chat  
  It cannot be accessed directly through a web browser. To access the endpoint, the user has to use an API tool like Postman to generate an HTTP request.  
  Two parameters need to be passed in the POST request, prompt and context. The prompt is the user input, and the context is the text of the ongoing conversation. The context also needs to include the system message. The context should look like this initially:  
    
     {'role':'system', 'content':"""  
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
       """}  

# CLI
  To use the CLI, you first have to create an openAI API key.  
  Then, download the chatbot.py file, replace 'YOUR-API-KEY' with your actual key and run it on a Python IDE.  
  Make sure to install the required packages from requirements_cli.txt file.
