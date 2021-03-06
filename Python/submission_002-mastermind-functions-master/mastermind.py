import random
# code = [0,0,0,0]
correct = False
turns = 0
answer = ''
correct_digits_and_position = 0
correct_digits_only = 0

# TODO: Decompose into functions
def check_for_win():
    global correct_digits_and_position, correct_digits_only, correct
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: '+str(12 - turns))
    correct_digits_and_position = 0
    correct_digits_only = 0
    
def print_output():
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    
    
def check_correct_digit_and_position():
    global correct_digits_and_position, correct_digits_only
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

def generate_random_code():
    global code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

def run_game():
    global answer, turns, correct, correct_digits_and_position, correct_digits_only
    generate_random_code()
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        check_correct_digit_and_position()
        print_output()
        turns += 1
        check_for_win()
    print('The code was: '+str(code))
    correct = False
    turns = 0
    answer = ''
    correct_digits_and_position = 0
    correct_digits_only = 0
    

if __name__ == "__main__":
    run_game()