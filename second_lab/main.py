#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'litleleprikon'


def user_logged(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_user_logged():
            raise AccessSystem.UserNotLoggedException()
        return func(self, *args, **kwargs)
    return wrapper


class AccessSystem:
    __ACCESS_DICT = {
        'first': [1, 2, 3],
        'second': [2, 3, 5],
        'third': [7, 7, 7],
        'fourth': [3, 6, 2],
        'fifth': [1, 2, 3],
        'sixth': [3, 6, 7],
        'seventh': [1, 2, 4]
    }

    class UserNotLoggedException(Exception):
        def __init__(self):
            super().__init__('User is not logged.\n')

    class UserHaventRightsException(Exception):
        def __init__(self):
            super().__init__('User have not rights for this operation\n')

    class UserNotRegisteredException(Exception):
        def __init__(self):
            super().__init__('User is not registered\n')

    def __init__(self):
        self._logged_user = None

    def is_user_logged(self):
        return bool(self._logged_user)

    @user_logged
    def can_read(self, file_num):
        accessible_nums = [4, 5, 6, 7]
        return self.__ACCESS_DICT[self._logged_user][file_num] in accessible_nums

    def read(self, file_num):
        if self.can_read(file_num):
            print("Readed!\n")
        else:
            raise AccessSystem.UserHaventRightsException()

    @user_logged
    def can_write(self, file_num):
        accessible_nums = [2, 3, 6, 7]
        return self.__ACCESS_DICT[self._logged_user][file_num] in accessible_nums

    def write(self, file_num):
        if self.can_write(file_num):
            print("Writed!\n")
        else:
            raise AccessSystem.UserHaventRightsException()

    @user_logged
    def can_grant(self, file_num):
        accessible_nums = [1, 3, 5, 7]
        return self.__ACCESS_DICT[self._logged_user][file_num] in accessible_nums

    def grant(self, file_num, granted_user):
        if not self.can_grant(file_num):
            raise AccessSystem.UserHaventRightsException
        if granted_user in self.__ACCESS_DICT.keys():
            self.__ACCESS_DICT[granted_user][file_num] |= 1
        else:
            raise AccessSystem.UserNotRegisteredException()

    def logout(self):
        self._logged_user = None

    def identificate(self, name):
        if name in self.__ACCESS_DICT.keys():
            self._logged_user = name
            return
        raise AccessSystem.UserNotRegisteredException


def main():
    access_system = AccessSystem()
    while True:
        commands = ['read', 'write', 'identificate', 'grant', 'logout']
        try:
            command = input('Input command >>> ').lower()
            command = command.split(' ')
            if len(command) == 1 and command[0] == commands[-1]:
                access_system.logout()
            elif len(command) < 2:
                print('Bad command format.\n')
            if command[0] not in commands:
                print('Bad command.\n')
            else:
                if command[0] == commands[0]:
                    access_system.read(int(command[1]))
                elif command[0] == commands[1]:
                    access_system.write(int(command[1]))
                elif command[0] == commands[2]:
                    access_system.identificate(command[1])
                elif command[0] == commands[3]:
                    access_system.grant(int(command[1]), command[2])
        except Exception as exp:
            print(exp)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ex:
        print("Keyboard interrupt")