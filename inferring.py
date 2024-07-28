import openai 
from dotenv import load_dotenv 
import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 
import os 


file_path = r"C:\Users\BARRY\Desktop\chat-gpt-prompt-Engineering\env"

load_dotenv(file_path)

os.getenv("OPENAI_API_KEY")

# in this section we gonna see how to use llm to infer articles . Inferring or deduction in french means to deduct something based on a content . 



client = openai.OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


# let's implemnent some examples 

lamp_review = """
Needed a nice lamp for my bedroom, and this one had \
additional storage and not too high of a price point. \
Got it fast.  The string to our lamp broke during the \
transit and the company happily sent over a new one. \
Came within a few days as well. It was easy to put \
together.  I had a missing part, so I contacted their \
support and they very quickly got me the missing piece! \
Lumina seems to me to be a great company that cares \
about their customers and products!!
"""

# Sentiment (positive/negative)


prompt = f"""

        What is the sentiment of the following product review , wich is delimited with triple backticks ? 

        Review text : ````{lamp_review}````

       """

response = get_completion(prompt)

# print(response)


prompt = f""""

what is the sentiment of the following product review , wich is delimited with triple backsticks ? 

Give your answer as single word , either " positive" \
or "negative" .


Review text : '''{lamp_review}'''

"""

response = get_completion(prompt)

print(response)



## Identify types of emotions

