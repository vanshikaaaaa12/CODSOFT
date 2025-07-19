# chatbot.py

def chatbot():
    print("🤖 ChatBot: Hello! I am CodSoft AI Bot. Type 'exit' to end.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("🤖 ChatBot: Goodbye! Have a nice day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("🤖 ChatBot: Hello! How can I help you today?")
        
        elif "your name" in user_input:
            print("🤖 ChatBot: I'm CodSoft AI Chatbot.")

        elif "how are you" in user_input:
            print("🤖 ChatBot: I'm just a bot, but I'm doing great! 😄")
        
        elif "internship" in user_input:
            print("🤖 ChatBot: CodSoft provides internships in AI, Web Dev, and more!")

        elif "thanks" in user_input or "thank you" in user_input:
            print("🤖 ChatBot: You're welcome! 😊")
        
        else:
            print("🤖 ChatBot: Sorry, I didn't understand that. Can you try something else?")


# Chatbot run karega
chatbot()
