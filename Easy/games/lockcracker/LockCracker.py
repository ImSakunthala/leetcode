# get locker key length form user
# random key generation with given key length
import random


# initiate guessing process
# get user guessed key

# check key length is matched, otherwise throw error
# if n digit(s) is matched and position is also matched, then print 'n digit(s) is correct and well-placed'
# if n digit(s) is matched but not in correct position, then print 'n digit(s) correct'
# if no digits is matched then print no digits matched. Better luck next time.
# if key matched exactly, then print 'Lock opened successfully..!'

# continue the loop until user guess the correct key

# e.g.
# Key Length: 2
# System generated key: 15
# Attempt 1: User guessed key 78, Result: No digit(s) matched. Better Luck next time.!
# Attempt 2: User guessed key 41, Result: 1 digit(s) matched.
# Attempt 3: User guessed key 16, Result: 1 digit(s) matched and 1 digit(s) well-placed.
# Attempt 4: User guessed key 15, Result: Lock opened successfully..!

class LockCracker:
    @staticmethod
    def get_key_length() -> int:
        key_length = 0

        while key_length == 0:
            user_input = None
            try:
                user_input = input('Please enter locker key length:')
                key_length = int(user_input)
            except ValueError:
                print(f'{user_input} is not a valid key length.')
        return key_length

    @staticmethod
    def generate_locker_key(length:int) -> str:
        start_range = 10 ** (length - 1)
        end_range = 10 ** length - 1
        return str(random.randrange(start_range, end_range))

    @staticmethod
    def get_key_from_user(length: int) -> str:
        key = ''
        while len(key) == 0:
            try:
                user_input = input('Please Guess the key:')
                if len(user_input) != length:
                    raise Exception('Invalid key length')
                elif not user_input.isdigit():
                    raise Exception('Invalid key type')
                else:
                    key = user_input
            except Exception as e:
                print(e.args)
        return key

    @staticmethod
    def is_key_matched(correct_key: str, guessed_key: str) -> bool:
        return correct_key == guessed_key

    @staticmethod
    def get_matched_digits_count(correct_key: str, guessed_key: str) -> int:
        return len([ch for ch in correct_key if ch in guessed_key])

    @staticmethod
    def get_well_placed_digits_count(correct_key: str, guessed_key: str) -> int:
        return len([ch1 for ch1, ch2 in zip(correct_key, guessed_key) if ch1 == ch2])

    @staticmethod
    def check(correct_key: str, guessed_key: str) -> bool:
        if LockCracker.is_key_matched(correct_key, guessed_key):
            print('Lock opened successfully..!')
            return True
        else:
            matched_digits = LockCracker.get_matched_digits_count(correct_key, guessed_key)
            well_placed_digits = LockCracker.get_well_placed_digits_count(correct_key, guessed_key)
            if well_placed_digits > 0:
                print(f'{matched_digits} digit(s) matched and {well_placed_digits} digit(s) well-placed')
            elif matched_digits > 0:
                print(f'{matched_digits} digit(s) matched.')
            else:
                print(f'No digit(s) matched. Better Luck next time.!')
            return False

    def start(self):
        key_length = LockCracker.get_key_length()
        correct_key = LockCracker.generate_locker_key(key_length)
        is_key_correct = False
        no_of_attempts = 1

        while not is_key_correct:
            print(f'Attempt: {no_of_attempts}')
            guessed_key = LockCracker.get_key_from_user(key_length)
            is_key_correct = LockCracker.check(correct_key, guessed_key)
            no_of_attempts += 1

        print("------------- END --------------")


lockCracker = LockCracker()
lockCracker.start()
