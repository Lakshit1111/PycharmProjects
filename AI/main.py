import speech_recognition as sr
import openai
import win32com.client
import webbrowser
import time
import AppOpener
import pywhatkit as pk
import os

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# a = speaker.GetVoices("Language=409").Item(0)
# # speaker.Speak("आप कैसे हैं?")
# print(a.show())


chatStr = ""

# def chat(query):
#     global chatStr
#     openai.api_key = "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"
#     text = f"Chatbot response for Prompt: {query} \n *************************\n\n"
#     chatStr += f"Sir: {query}\n Jarvis: "
#
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt =chatStr ,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     say(response['choices'][0]['text'])
#     chatStr += f"{response['choices'][0]['text']}\n"
#     return chatStr


# def open_ai(prompt):
#     openai.api_key = "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"
#     text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
#
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt = prompt,
#         temperature=0,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#
#     text += response["choices"][0]["text"]
#     if not os.path.exists("Open Ai"):
#         os.mkdir("Open Ai")
#     with open(f"Open AI/{prompt}", "w") as f:
#        f.write(response["choices"][0]["text"])




def say(text):
    speaker.Speak(text)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try :
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "error"


if __name__ == '__main__':
    print("pycharm")
    say("Hi Sir")
    query = " "
    while ("stop" not in query.lower()):
        print("listening....")
        query = takecommand()
        if(query == "error"):
            print("Error")
            continue


        # todo:  Open up the sites
        # sites = [["youtube",'http://youtube.com'] , ["google",'http://google.com']]
        # for site in sites :
        #     if f"Open {site[0]}".lower() in query.lower():
        #         say(f"Opening {site[0]} sir...")
        #         webbrowser.open(site[1])
        #
        # # todo: Know Time
        # if("the time" in query.lower()):
        #     tim = time.strftime("%H:%M:%S")
        #     say(f"Sir Time is {tim}")
        #
        # # todo: Open an app
        # elif("open" in query.lower()):
        #     say(f"Opening {query.split(' ')[1]} sir...")
        #     AppOpener.open(query.split(' ')[1])
        #
        # # elif ("close" in query.lower()):
        # #     say(f"Closing {query.split(' ')[1]} sir...")
        # #     close(query.split(' ')[1])
        #
        # # todo: play on Youtube
        # elif("play" in query.lower()):
        #     say(f"Playing song {query} sir...")
        #     # print(" ".join(query[1:]))
        #     pk.playonyt(" ".join(query))
        #
        # elif("Search" in query.lower()):
        #     say(f"Searching {query.split(' ')[1]} sir...")
        #     pk.search(query.split(' ')[1])
        #
        # # elif("AI" in query.lower()):
        # #     say("Hi sir How can I help you.")
        # #
        # #     while True:
        # #         print("jarvis is listening....")
        # #         prompt = takecommand()
        # #         print(prompt)
        # #         if "exit" in prompt.lower():
        # #             break
        # #         try:
        # #             response = open_ai(prompt)
        # #             # say(response["choices"][0]["text"])
        # #         except Exception as e:
        # #             continue
        #
        #
        # elif ("bye" or "buy" or "tata" or "exit" or "stop" or "close" or "quit") in query.lower():
        #     say("Bye sir")
        #     break
        #
        # # else:
        # #     chat(query)
        #
