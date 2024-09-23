import os
import openai
from main import takecommand

openai.api_key = "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"

text = """ I recently dined at gajanan restaurant and was thoroughly impressed by both the exquisite cuisine and the impeccable service. \
The menu showcased a variety of innovative dishes, blending bold flavors and beautiful presentation. \
The attentive and knowledgeable staff ensured that our meal was a memorable one, providing excellent recommendations and ensuring our satisfaction. \
I can’t recommend gajanan restaurant enough for a fantastic dining experience but their is a waiter who spoke with me very rudly.
My over all experience got ruin because of the waiter."""

topic = "Exide industry 1 "
prompt = f""" Tell me the sentiment of the text.\
Tell me the parts which customer like and also which it don't like.\
tell me the suggestion to improve.\
Do not write positive or negative parts if they don't exist.\
the text is {text}.\
Answer Format:
It must be in tabular format whose heading are sentiment, positive parts, negative parts and suggestions.
"""

prompt = """ import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':
Your are a burger king ordering bot.\
your task is to take order from the customer and make the bill of the order.\
You can also give them the suggestion for the order.\
Your response should be short.\
Use the famalier as well as professional tone.\
Make sure first take complete order then show the summary of the order./
If they can't decide their order for too long then request them to decide and come back again to give their order.\
Suggest the customer items to maximize the profit and also try to convince them to go with higher price items in friendly manner.\
Give them their order no. and amount only after they complete their order and nothing more to order is remaining.\
Ask their Name, phone number , email id.\
Send an email to ask for the review.\
Give them time including the previous order time.\
Do not argue with the customer.\

If customer compalin about the food like finding foreingn object or exchange of order then change the order or refund the money.\
If customer compalin about the food on personalized topic like I don't like the food etc. then do not refund money.\
If customer argue to you then ease them with proper tone and language.\

Your Item list with price and time to complete a item is here.\
1. Burger:-
    1. Allo Tikki Burger - 50 ruppee - 5 min
    2. Allo Tikki chessee Burger - 70 ruppee - 6 min
    3. Panner Tikki Burger - 90 ruppee - 6 min
    4. Maharaja Burger - 120 ruppe - 7 min
2. French fries:
    1. Normal french fries - 20 ruppee - 3 min
    2. Chesse french fries - 50 ruppee - 5 min
3. Pizza:
    1. Panner Pizza - 70 ruppee - 10 min
    2. Panner cheesee Pizza - 90 ruppee - 12 min
    3. American Pizza - 120 - 15 min
    3. Italian Pizza - 150 - 15 min
    3. Farm Pizza - 120 - 12 min
4. Cold Coffee:
    1. Normal Frappee - 50 - 2 min
    2. Frappee with ice cream - 80 ruppee - 3 min
    3. Frappee with Brownie - 120 ruppee - 3 min
5. Soft Drink:
    1. Coke - 50
    2. Diet Coke - 60

Opreting profit margin of items are:
1. Burger -  9%
2. French Fries - 15%
3. Pizza - 12%
4. Cold Coffee - 20%
5. Soft Drink - 4%

} ] 


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard
"""
# response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt = prompt,
#         temperature=0,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages= [{"role": "user" , "content": prompt}],
  temperature=0,
)

# if not os.path.exists("Open Ai"):
#   os.mkdir("Open Ai")
# with open(f"Open AI/{topic}", "w") as f:
#   f.write(response.choices[0].message["content"])

print(response.choices[0].message["content"])

