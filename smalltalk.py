import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_MODEL = os.getenv('GROQ_MODEL')

groq_client = Groq()

prompt = """"
Answer anything about AI, world, universe, vehicle, science, mathematics, geography, movies, songs, bollywood, hollywood, social science, art, music, drama, history

QUESTION: {query}
"""

def smalltalk_chain(query):
    completion = groq_client.chat.completions.create(
        model=os.environ['GROQ_MODEL'],
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    query = "what's the country with largest population?"
    answer = smalltalk_chain(query)
    print(answer)
