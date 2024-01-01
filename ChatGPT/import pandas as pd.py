import pandas as pd
from openai import OpenAI
openaiAPI = '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'
openaiAPI
#function to run chat GPT in Jupyter using the client.chat.completions.create script from 
#https://github.com/openai/openai-python/discussions/742
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key= openaiAPI
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

##Enter Your Question as many times as you want until you say quit, exit, and bye in which the code stops
if __name__ == "__main__":
    while True:
        user_input = input("Hello How can I assist You?: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("No Worries. Let me know Whether I can further assist you. Have a Nice Day!!!")
            break
        response = chat_gpt(user_input)
        print(response)
        
            # Ask if the user wants to ask another question
        continue_chat = input("\nWould you like to ask another question? (Type 'yes' or 'no'): ")
        if continue_chat.lower() == 'no':
            print("No Worries. Let me know Whether I can further assist you. Have a Nice Day!!!")
            break
