import pyttsx3

if __name__ == '__main__':
    print("Welcome to speaker")
    x = input("Enter something: ")

    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
