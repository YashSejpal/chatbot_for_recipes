from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
# Define the list of questions to ask the user
questions = [
    "What are your dietary preferences or restrictions?",
    "What type of dish are you looking for?",
    "Which ingredients do you have available with you?"
    "How much time do you want to spend on cooking?",
    "Do you have any cuisine preferences or flavor profiles in mind?"
    # Add more questions as needed
]

@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get user responses from the request
    user_responses = request.json['responses']

    # Check if all required information is collected
    if len(user_responses) < len(questions):
        # Ask the next question
        question = questions[len(user_responses)]
        response = {
            'question': question
        }
        return jsonify(response)
    
    # Generate prompt for OpenAI API
    prompt = generate_prompt(user_responses)

    # Call the OpenAI API to get recommended recipes
    recommended_recipes = call_openai_api(prompt)

    # Return the recommended recipes as the API response
    response = {
        'recipes': recommended_recipes
    }
    return jsonify(response)

def generate_prompt(responses):
    # Generate the prompt based on user responses
    # You can customize this function to format the prompt as per your requirements
    prompt = "User responses:\n"
    for i, response in enumerate(responses):
        prompt += f"{i+1}. {response}\n"
    return prompt

def call_openai_api(prompt):
    import openai
    import json
    with open("./secrets.json","r")as f:
        json_file=json.load(f)
    
    openai.api_key=json_file['api_key']
    response=openai.Completion.create(
        engine = "text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=4096,
        top_p=1.0,
        frequency_penalty=0.0,
        presense_penalty=0.0
    )
    return response['choices'][0]['text']
    # recommended_recipes = []
    # for choice in response.choices:
    #     recommended_recipes.append(choice.text.strip())
    
    # return recommended_recipes

if __name__ == '__main__':
    app.run()
