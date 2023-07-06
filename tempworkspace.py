#1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
import pickle

#2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

#3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

#4) Adjust the logic to load the file content to work with pickled/ json data.



waiting_for_input = True
user_input_list = []

while waiting_for_input:
    print('Please choose')
    print('1: Enter text and save')
    print('2: load and output')
    print('q: Quit')
    user_choice = input('Your Choice: ')
    if user_choice == '1':
        tx_data = input('Your Text: ')
        user_input_list.append(tx_data)
        with open('daFile.txt', mode='wb') as f:
            f.write(pickle.dumps(user_input_list))
    elif user_choice == '2':
        with open('daFile.txt', mode='rb') as f:
            file_content = pickle.loads(f.read())
            for line in file_content:
                print(line)
    elif user_choice == 'q':
        # This will lead to the loop to exist because it's running condition becomes False
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')