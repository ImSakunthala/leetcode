"""
Encapsulation -> the bundling of data with the mechanisms or methods that operate on the data. It may also refer to the
limiting of direct access to some of that data, such as an object's components
"""

import random


class LoginService:
    # Limit field visibility to private
    __db_conn = 'confidential db conn properties'
    __db_username = 'confidential db user name'
    __db_password = 'confidential db password'

    def login(self, username:str, password: str) -> bool:
        # return True if login success, otherwise False

        # calls sensitive operation
        return self.__login_process(username, password)

    # limiting method visibility to private
    def __login_process(self, username, password):
        # establish db connection to check whether the login credentials correct or not
        return random.choice([True, False])


class StudentApplication:

    def login(self):
        loginService = LoginService()
        # trying to access private fields
        print(loginService.db_conn)
        print(loginService.db_username)
        print(loginService.db_password)

        # trying to access private methods
        print(loginService.__login_process('username', 'password'))
