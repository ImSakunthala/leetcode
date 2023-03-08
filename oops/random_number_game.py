import random
import secrets


class SecretLocker:
    def __init__(self, user_input):
        self.user_input = input(int('Enter the length locker password [1/2/3/4]:'))

    def select_password(self, user_input: int) -> int:
        if user_input == 1:
            locker_password = secrets.choice(range(0, 10))
        if user_input == 2:
            locker_password = secrets.choice(range(10, 100))
        if user_input == 3:
            locker_password = secrets.choice(range(100, 1000))
        if user_input == 4:
            locker_password = secrets.choice(range(1000, 10000))

        return locker_password
