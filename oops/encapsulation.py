import random


class LoginService:
    __db_conn = 'confidential db conn properties'
    __db_username = 'confidential db user name'
    __db_password = 'confidential db password'

    def login(self, username:str, password: str) -> bool:
        # return True if login success, otherwise False

        # calls sensitive operation
        return self.__login_process(username, password)

    def __login_process(self, username, password):
        # establish db connection to check whether the login credentials correct or not
        return random.choice([True, False])


class StudentApplication:

    def login(self):
        loginService = LoginService()
        print(loginService.db_conn)
        print(loginService.db_username)
        print(loginService.db_password)
