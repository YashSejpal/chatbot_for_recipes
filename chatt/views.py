from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

openai.api_key = 'YOUR_API_KEY'

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=1):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message["content"]

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = request.POST
        prompt = data.get('prompt')
        context = data.get('context')
        context = eval(context) if context else []
        context.append({'role': 'user', 'content': prompt})
        response = get_completion_from_messages(context)
        context.append({'role': 'assistant', 'content': response})
        return JsonResponse({'response': response, 'context': str(context)})

    return JsonResponse({'error': 'Invalid request method'})
