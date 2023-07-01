def ask(query):
    import openai
    import json
    with open("./secrets.json","r")as f:
        json_file=json.load(f)
    
    openai.api_key=json_file['api_key']
    response=openai.Completion.create(
        engine = "text-davinci-003",
        prompt=query,
        temperature=0.5,
        max_tokens=4096,
        top_p=1.0,
        frequency_penalty=0.0,
        presense_penalty=0.0
    )
    return response['choices'][0]['text']