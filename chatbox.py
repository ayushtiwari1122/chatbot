import random
import json
import datetime
res_path = 'responses.json'
with open(res_path, 'r') as file:
    responses = json.load(file)
names = ['Ali', 'ayu', 'sem', 'lor', 'Casy']
names = random.choice(names)
u_name = input("Hello, what can I call you: ")
print(f"Hello {u_name}! I am {names}, your assistant. How are you? How can I help you today?")
logFile = f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
def log_interaction(user, agent, message, response):
    with open(logFile, 'a') as f:
        f.write(f"{user} said: {message}\n")
        f.write(f"{agent} replied: {response}\n")
keywords = {
    "sport": "sport",
    "admission": "admission",
    "weather": "weather",
    "yes": "yes",
    "hello": "hello",
    "bye": "bye",
    "international studies": "international studies"
}
while True:  
    you_give = input(f"{u_name}: ").lower()
    if 'exit' in you_give or you_give == 'bye':
        print(f"{names}: Later, {u_name}!")
        log_interaction(u_name, names, you_give, "Goodbye message")
        break
    log_interaction(u_name, names, you_give, you_give)
    response_is = False
    for key, keyword in keywords.items():
        if keyword in you_give:
            if key in responses['responses']:
                c_responses = responses['responses'][key]
                chat = random.choice(c_responses)
                print(f"{names}: {chat}")
                log_interaction(names, u_name, you_give, chat)
                response_is = True
                break
    if not response_is:
        random_response = random.choice(responses.get("random_response", ["Haha, I don't know. Call the college."]))
        print(f"{names}: {random_response}")
        log_interaction(names, u_name, you_give, random_response)
print(f"Chat log saved to {logFile}")
