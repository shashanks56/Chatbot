import os
import datetime


#for tracking user & bot conversation
chat_history = []

# for saving user and bot messages
def log_message(sender, message):
    chat_history.append(f"{sender}: {message}")


def greeting():
    msg = "Hi there! How can I help you today?"
    print(f"Chatbot: {msg}")
    log_message("Chatbot", msg)


def date_time(requested_part):
    now = datetime.datetime.now()
    if requested_part == 'date':
        print(f"Chatbot: Today's date is {now.strftime('%d %B %Y')}")
        log_message("Chatbot", f"Today's date is {now.strftime('%d %B %Y')}")
    elif requested_part == 'time':
        print(f"Chatbot: Current time is {now.strftime('%I:%M %p')}")
        log_message("Chatbot", f"Current time is {now.strftime('%I:%M %p')}")
    else:
        print(f"Chatbot: It's {now.strftime('%d %B %Y, %I:%M %p')}")
        log_message("Chatbot", f"It's {now.strftime('%d %B %Y, %I:%M %p')}")
    
    print("Chatbot: How else can I assist you?")
    log_message("Chatbot", "How else can I assist you?")



def list_operations():
    print("Chatbot: Please enter a list of integers (comma separated integer):")
    log_message("Chatbot", "Please enter a list of integers (comma separated integer):")

    while True:
        user_input = input("User: ").strip()
        log_message("User", user_input)

        if not valid_int_list(user_input):
            print("Chatbot: Error! List should have only numbers separated by commas.")
            log_message("Chatbot", "Error! List should have only numbers separated by commas.")
            continue

        nums = list(map(int, user_input.split(',')))
        
        #initial result
        print(f"Chatbot: Sum: {sum(nums)}")
        print(f"\t Maximum: {max(nums)}")
        print(f"\t Minimum: {min(nums)}")
        print(f"\t Reversed List: {list(reversed(nums))}")
        log_message("Chatbot", f"Sum: {sum(nums)}")
        log_message("Chatbot", f"Maximum: {max(nums)}")
        log_message("Chatbot", f"Minimum: {min(nums)}")
        log_message("Chatbot", f"Reversed List: {list(reversed(nums))}")
        
        print("Chatbot: Would you like to remove duplicates? (yes/no)")
        log_message("Chatbot", "Would you like to remove duplicates? (yes/no)")

        while True:
            choice = input("User: ").strip().lower()
            log_message("User", choice)

            if choice not in ['yes', 'no']:
                print("Chatbot: Enter correct keyword")
                log_message("Chatbot", "Enter correct keyword")
                continue

            if choice == "yes":
                nums = list(set(nums)) 
                print(f"Chatbot: Updated List: {nums}")
                log_message("Chatbot", f"Updated List: {nums}")
                
                #result after removing duplicates
                print(f"\t Sum: {sum(nums)}")
                print(f"\t Maximum: {max(nums)}")
                print(f"\t Minimum: {min(nums)}")
                print(f"\t Reversed List: {list(reversed(nums))}")
                log_message("Chatbot", f"Sum: {sum(nums)}")
                log_message("Chatbot", f"Maximum: {max(nums)}")
                log_message("Chatbot", f"Minimum: {min(nums)}")
                log_message("Chatbot", f"Reversed List: {list(reversed(nums))}")

            print("Chatbot: How else can I assist you?")
            log_message("Chatbot", "How else can I assist you?")
            return


def valid_int_list(data):
    try:
        numbers = []
        for x in data.split(','):
            numbers.append(int(x.strip()))
        return True
    except ValueError:
        return False



def prime_generation():
    print("Chatbot: Enter range (start and end):")
    log_message("Chatbot" , "Enter range (start and end):")
    
    while True:
        user_input = input("User: ").strip()
        log_message("User" , user_input)

        if not valid_int_list(user_input) or len(user_input.split(',')) != 2:
            print("Chatbot: Error! List should have only numbers separated by commas.")
            log_message("Chatbot", "Error! List should have only numbers separated by commas.")
            continue

        start, end = map(int, user_input.split(','))

        primes = []
        for x in range(start, end + 1):
            if is_prime(x):
                primes.append(x)

        print(f"Chatbot: Prime Numbers: {primes}")
        log_message("Chatbot", f"Prime Numbers: {primes}")
        print("Chatbot: How else can I assist you?")
        log_message("Chatbot", "How else can I assist you?")
        return

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#Search Chat
def search_history():
    print("Chatbot: Enter the keyword to search in chat history:")
    log_message("Chatbot", "Enter the keyword to search in chat history:")
    
    keyword = input("User: ").strip()
    log_message("User", keyword)

    found = []
    for line in chat_history:
        if keyword.lower() in line.lower():
            found.append(line)

    if found:
        print("Chatbot: Found the following lines:")
        log_message("Chatbot", "Found the following lines:")
        for line in found:
            print(f"- \"{line}\"")
            log_message("Chatbot", f"- \"{line}\"")
    else:
        print("Chatbot: No matching messages found.")
        log_message("Chatbot", "No matching messages found.")
    
    print("Chatbot: How else can I assist you?")
    log_message("Chatbot", "How else can I assist you?")


def chat_summary():
    commands = []
    for line in chat_history:
        if line.startswith("User:"):
            commands.append(line.split(": ")[1].strip().lower())

    command_count = {}
    for cmd in commands:
        if cmd in command_count:
            command_count[cmd] += 1
        else:
            command_count[cmd] = 1

    if commands:
        most_common = max(command_count, key=command_count.get)
    else:
        most_common = "None"

    print(f"Chatbot: Here's a summary of your session:")
    print(f" Commands Used: {len(commands)}")
    print(f" Most Frequent Command: {most_common}")
    log_message("Chatbot", f"Here's a summary of your session:")
    log_message("Chatbot", f" Commands Used: {len(commands)}")
    log_message("Chatbot", f" Most Frequent Command: {most_common}")
    
    print("Chatbot: Do you want to save this summary? (yes/no)")
    log_message("Chatbot", "Do you want to save this summary? (yes/no)")

    while True:
        save_choice = input("User: ").strip().lower()
        log_message("User", save_choice)

        if save_choice not in ['yes', 'no']:
            print("Chatbot: Enter correct keyword")
            log_message("Chatbot", "Enter correct keyword")
            continue

        if save_choice == 'yes':
            save_summary(commands, most_common) 
            filename = f"summary_{datetime.datetime.now().strftime('%d%m%Y')}.txt"
            print(f"Chatbot: Summary saved to Desktop as '{filename}'")
            print(" -> Goodbye! Have a great day!")
        else:
            print("Chatbot: Alright, not saving.")
            print("Chatbot: Bye, have a good day!!")
        break

def save_summary(commands, most_common):
    filename = f"summary_{datetime.datetime.now().strftime('%d%m%Y')}.txt"
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    full_path = os.path.join(desktop, filename)

    with open(full_path, "w") as file:
        file.write("Session Summary\n")
        file.write(f"Date: {datetime.datetime.now().strftime('%d %B %Y, %I:%M %p')}\n")
        file.write(f"Commands Used: {len(commands)}\n")
        file.write(f"Most Frequent Command: {most_common}\n\n")
        file.write("Full Chat History:\n")
        file.writelines(line + "\n" for line in chat_history)


def main():
    print("Chatbot: Hello! I'm your assistant! How can I help you today?")
    log_message("Chatbot", "Hello! I'm your assistant! How can I help you today?")

    while True:
        command = input("User: ").strip().lower()
        log_message("User", command)

        if command == 'hello' or command == 'hi' or command == 'hey':
            greeting()
        elif command == 'date':
            date_time('date')
        elif command == 'time':
            date_time('time')
        elif command == 'date and time':
            date_time('both')
        elif command == 'list operations':
            list_operations()
        elif command == 'generate prime':
            prime_generation()
        elif command == 'search history':
            search_history()
        elif command == 'bye':
            chat_summary()
            break
        else:
            print("Chatbot: Enter correct keyword")
            log_message("Chatbot", "Enter correct keyword")

if __name__ == "__main__":
    main()