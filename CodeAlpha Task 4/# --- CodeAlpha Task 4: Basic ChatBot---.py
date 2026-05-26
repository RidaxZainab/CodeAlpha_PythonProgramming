def basic_chatbot():
    print("=== WELCOME TO CODEALPHA BASIC CHATBOT ===")
    print("Type your message below (Type 'bye' to exit the chat)")
    print("-----------------------------------------")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi! How can I help you today?")
            
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm fine, thanks! How about you?")
            
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I am a simple rule-based chatbot built for CodeAlpha.")
            
        elif user_input in ["fine", "good", "i am fine"]:
            print("Chatbot: Glad to hear that!")
            
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        else:
            print("Chatbot: I am sorry, I am a basic bot and didn't understand that. Can you try again?")

if __name__ == "__main__":
    basic_chatbot()