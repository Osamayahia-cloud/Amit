from chatbot
def main(): 
    print("chatbot : can i help you ?")
    while True:
        userinput = input("user :").lower
        response = get_response(userinput)
        print("chatbot:",response)
        if userinput=="goodbye":break