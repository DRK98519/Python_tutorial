## Car Game

# while True:
#     command = input('>')
#     if command.upper() == 'HELP':
#         print('start - to start the car')
#         print('stop - to stop the car')
#         print('quit - to exit')
#     elif command.upper() == 'START':
#         print('Car started, ready to go.')
#     elif command.upper() == 'STOP':
#         print('Car stopped.')
#     elif command.upper() == 'QUIT':
#         print('Program terminates.')
#         break
#     else:
#         print("I don't understand that...")

## We repeated command.upper() multiple times in code above, not good.

# while True:
#     command = input('>').upper()
#     if command == 'HELP':
#         print('start - to start the car')
#         print('stop - to stop the car')
#         print('quit - to exit')
#     elif command == 'START':
#         print('Car started, ready to go.')
#     elif command == 'STOP':
#         print('Car stopped.')
#     elif command == 'QUIT':
#         print('Program terminates.')
#         break
#     else:
#         print("I don't understand that...")



## Improved Program:
# last_command = ''
# while True:
#     command = input('>').upper()
#     if command == 'HELP':
#         print('start - to start the car')
#         print('stop - to stop the car')
#         print('quit - to exit')
#     elif command == 'START':
#         if last_command != command:
#             print('Car started, ready to go.')
#         else:
#             print("Car has already started. Can't start again.")
#         last_command = command
#     elif command == 'STOP':
#         if last_command != command:
#             print('Car stopped.')
#         else:
#             print("Car has already stopped. Can't stop again.")
#         last_command = command
#     elif command == 'QUIT':
#         print('Program terminates.')
#         break
#     else:
#         print("I don't understand that...")


started = False
while True:
    command = input('>').upper()
    if command == 'HELP':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif command == 'START':
        if started:
            print("Car has already started. Can't start again.")
        else:
            print('Car started, ready to go.')
            started = True
    elif command == 'STOP':
        if not started:
            print("Car has already stopped. Can't stop again.")
        else:
            started = False
            print('Car stopped.')
    elif command == 'QUIT':
        print('Program terminates.')
        break
    else:
        print("I don't understand that...")