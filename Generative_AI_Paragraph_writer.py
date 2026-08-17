
from google import genai
from google.genai import types


client = genai.Client(api_key= "Write your API key here")
def generate_AI(paragraph_topic):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"Write a paragraph about {paragraph_topic}.",
        config=types.GenerateContentConfig(
        max_output_tokens=5000,
        temperature = 0.7)
    )
    return response.text

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_AI(paragraph_topic))
  else:
    keep_writing = False