# How to Activate ChatGPT in Python in Visual Studio Code and Jupyter Notebook

## Table of Contents
- [Problem](#Problem) 
- [Solution 1](#Solution-1)
- [Solution 2](#Solution-2) 
- [Solution 3](#Solution-3)
- [Links](#Links)

***

## Problem
- Are you a Python programmer that uses ChatGPT but don't want to go on the OpenAI website to paste your code there as you want another way for the AI can give you feedback? Do you want access to ChatGPT directly on your Jupyter Notebook file?

- Well look no further as you can actually create your own ChatGPT program where the AI will answer your questions automatically whether you are writing your script in an IDE such as Visual Studio Code or on a Open Document Format such as Jupyter notebook.

- There are three ways to accomplish this and I will go through each method as each are uniquely different and provide different alternatives of activating ChatGPT on your program and giving you the best value possible on optimizing your python scripts in order to create the solutions that you need to bring value to your peers.



***

## Solution 1

- Here is the first way to do it and this is where you'll need an open AI account because you'll need to generate an API Key which you'll need to run the script. Make sure you use pip install openAI if you don't have the library in your python

```Python
pip install openai 
from openai import OpenAI
```

- To get the Open AI API key. I'll walk you through on my screen on how to get it. You can create an Open AI account and get API Key on the Open AI website [here](https://platform.openai.com/)

- Please be aware that you'll get free usage on a certain limit and if you go over the limit(meaning if you run the code too many times and it exceeds the limit) you'll get the message that you exceeded the limit and may have to wait until the limit resets or will need to pay to increase the limit usage. 

- Walkthrough below on generating an Open API Key:

https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/9e6e38f1-258d-4b5b-a56b-51ae5a422184

- Once you have your API key. Now the fun Begins!!!1

- You will be prompted to input the key:

```Python
openaiAPI = input("Enter Your API Key: ")
openaiAPI
```

- Then the ChatGPT AI program will be called through a function that I picked up from this github Python Open API [link](https://github.com/openai/openai-python/discussions/742) using client.chat.completions.create

```Python
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
```
- Essentially what the code above does is that the Open API key will be used to allow the user to ask the program a prompt and then the program will generate a response

- To keep the conversation going as many times as you want, I created the following code below using a while loop that allows the AI to ask you for assistance until you stop. 

- Also there is an option for the AI to ask you if you have any follow up questions and you'll have the option to say yes or no.

```Python
##Enter Your Question as many times as you want until you say quit, exit, and bye in which the code stops

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
```

- This code can be implemented in Jupyter notebook or Visual Studio Code. Here is a below example





https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/63ee3575-09d6-49ec-8904-70ba4ca547b9




- And here is another example but in Jupyter Notebook this time.



https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/93168e89-a10f-4e30-8d08-b860c06e86a9








***

## Solution 2

- This method doesn't require any code and won't take too long either. If you have Jupyter notebook and you do most of your python there, All you need to do is to get Chat GPT Jupyter AI assistant extension [here](https://chromewebstore.google.com/detail/chatgpt-jupyter-ai-assist/dlipncbkjmjjdpgcnodkbdobkadiejll?pli=1) for Jupyter notebook and the extension will be available on Jupyter notebook when you restart. 

- You'll need your OpenAI API Key for this as well. Please be alert of how much usage you have on your Open AI Key so that you don't run into issues when you exceed the usage. The extension may stop working or you may have to pay a fee to keep using it.

- Quick guide on getting the extension below.

  

https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/2ef1ec89-3c36-44ea-a60e-3c7d3a8a8023




***

## Solution 3

- This final solution utilizes a different API called Rapid API. The Python code created for this solution utilizes an Open AI Rapid API Key and the python script from the website [here](https://rapidapi.com/hub).
- You'll need to create an account and search for the Open AI API name on the API search bar. After that, you'll click on pricing and subscribe to the BASIC subscription which is free but once you hit 50 requests before the end of the month, you'll have to wait until the month ends for it to reset to 0 or you'll need to upgrade to get more requests.
- The Python code will consume the requests as it is pulling data through the Open AI key that you'll grab from the Open AI API python script
- The following video below will walk you through how to get into the Rapid AI website, subscribe to the Open AI Key and where to locate the API key and the Python script.

  

https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/25cb68bf-5121-400b-a5e1-6aad97fcc853

- So we will copy that Python Script from the requests page that you'll see on the video and we will use that to write a Python code to ask questions to chat gpt until we decide to stop. Here is the full code that I created.

- We will need to import the requests library 
```Python
import requests
```

- Grab the API URL and and its contents
```Python
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": YOUR API KEY HERE, ## You will input your API key once you get your Open AI API after you create a Rapid AI account
    "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
}
```

- We will create a while loop that will continously allow the AI to ask you to provide a question. It will stop once you decide to stop or exit. Once you ask a question and it answers, the AI will then ask if you have another question. If yes then it will ask for that question. If not then the loop ends and the code stops.

```Python
# While loop to continuously prompt for user input
while True:
    user_input = input("Hello, how can I assist you today? (Type 'stop', 'done', or 'exit' to exit): ")

    if user_input.lower() in ("stop", "done", "exit"):
        print("No Worries. Let me know Whether I can further assist you. Have a Nice Day!!!")
        break  # Exit the loop if 'stop', 'done', or 'exit' is entered

    payload = {
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ],
        "web_access": False,
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256
    }

    response = requests.post(url, json=payload, headers=headers)

    json_response = response.json()
    if 'result' in json_response:
        print(json_response['result'])  # Extract and print the 'result' field
    else:
        print("No result found in the response.")
    
    # Ask if the user wants to ask another question
    continue_chat = input("\nWould you like to ask another question? (Type 'yes' or 'no'): ")
    if continue_chat.lower() == 'no':
        print("No Worries. Let me know Whether I can further assist you. Have a Nice Day!!!")
        break

```

- Example output in Jupyter Notebook. This code can be used in Visual Studio code as well

  




https://github.com/KennethManzi1/Data-Analysis-projects/assets/120513764/0f93a502-ac60-410f-b426-995cfdee4d83


- And that is all folks. Those are the ways you can use Python to generate chat GPT in your IDE environments or open sourced notebook using Python. The cool thing about solution 3 is that as you'll see in the video, the open AI Rapid API scripts are in different languages outside python which means that you can call chat GPT in other programming languages outside of Python.
- I may use that API to try to create chat GPT in R as it is similar to Python but it may take more effort due to syntax differences.
- Let me know if you have any questions or concerns. Feel Free to reach out to me on Linkedln!!!

***

## Links
- [OpenAI ChatGPT Code](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/ChatGPT/OpenAI%20ChatGPT%20Python.py)
- [RapidAI ChatGPT Code](https://github.com/KennethManzi1/Data-Analysis-projects/blob/main/ChatGPT/RapidAI%20ChatGPT%20Python.py)
- [Open AI Website](https://platform.openai.com/)
- [Open AI Python Github resources](https://github.com/openai/openai-python/discussions/742)
- [ChatGPT Jupyter AI Extension](https://chromewebstore.google.com/detail/chatgpt-jupyter-ai-assist/dlipncbkjmjjdpgcnodkbdobkadiejll?pli=1)
- [Rapid AI Website](https://rapidapi.com/hub)
- Find me on Linkedln [here](https://www.linkedin.com/in/kenneth-kaijage-951a02141/)
