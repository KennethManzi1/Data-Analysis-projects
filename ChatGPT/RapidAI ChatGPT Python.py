import requests
url = "https://open-ai21.p.rapidapi.com/conversationgpt"
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "8dcbe22431msh7b0dd55a8b9d96dp12f6cajsn3ff11564ed99", 
    "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
}
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