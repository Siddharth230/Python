command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print(
            """
start       To start the car
stop        To stop the car 
quit        To quit
        """
        )
    elif command == "quit":
        break
    else:
        print("It is not a valid command       try help")
