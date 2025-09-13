import re

def bot():
    print("Erik: Hi! Ask me something. Type 'bye' to exit.")
    
    while True:
        user = input("You: ").lower()
        
        if re.search(r"\bhello\b|\bhi\b|\bhey\b|\byo\b|\berik\b", user):
            print("Erik: Hello there! 👋")
        elif re.search(r"how are you\b|\bsup\b", user):
            print("Erik: I'm fine, thank you!.What about you?")
        elif re.search(r"name\b|\bgot a name?\b|\bwho are you?\b", user):
            print("Erik: I'm Erik, your personalized chatbot. Is there anything I can help u with?")
        elif re.search(r"bye", user):
            print("Erik: Bye! Remind me, if you need me .")
            break
        else:
            print("Erik: Hmm... I don't have a reply for that.")
            
bot()
   