#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'litleleprikon'


def user_logged(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_user_logged():
            raise AccessSystem.UserNotLoggedException()
        return func(self, *args, **kwargs)
    return wrapper


class UserRight:

    class RightsChangingNotPossibleException(Exception):
        def __init__(self):
            super().__init__('Rights changing not possible')

    def __init__(self, layer):
        self.current_layer = self.start_layer = layer

    def change_rights(self, layer):
        if self.current_layer >= layer:
            self.current_layer = layer
        else:
            raise UserRight.RightsChangingNotPossibleException()

    def rights_to_defolt(self):
        self.current_layer = self.start_layer

    def __eq__(self, other):
        return self.current_layer == other

    def __le__(self, other):
        return self.current_layer <= other

    def __ge__(self, other):
        return self.current_layer >= other


class AccessSystem:
    _ACCESS_RIGHTS = [
        3,
        2,
        1,
        0
    ]

    _USERS_RIGHTS = {
        'first': UserRight(1),
        'second': UserRight(3),
        'third': UserRight(1),
        'fourth': UserRight(2),
        'fifth': UserRight(2),
        'sixth': UserRight(0),
        'seventh': UserRight(0)
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
        return self._ACCESS_RIGHTS[file_num] <= self._USERS_RIGHTS[self._logged_user]

    def read(self, file_num):
        if self.can_read(file_num):
            print("Readed!\n")
        else:
            raise AccessSystem.UserHaventRightsException()

    @user_logged
    def can_write(self, file_num):
        return self._ACCESS_RIGHTS[file_num] >= self._USERS_RIGHTS[self._logged_user]

    def write(self, file_num):
        if self.can_write(file_num):
            print("Writed!\n")
        else:
            raise AccessSystem.UserHaventRightsException()

    @user_logged
    def change_rights(self, layer):
        self._USERS_RIGHTS[self._logged_user].change_rights(layer)

    @user_logged
    def right_to_defolt(self):
        self._USERS_RIGHTS[self._logged_user].rights_to_defolt()

    def logout(self):
        self._logged_user = None

    def identificate(self, name):
        if name in self._USERS_RIGHTS.keys():
            self._logged_user = name
            print('User rights:')
            for user in self._USERS_RIGHTS.items():
                print(user[0], ': ', user[1].current_layer)
            print('Files layers: ')
            for file, right in enumerate(self._ACCESS_RIGHTS):
                print(file, ': ', right)
            return
        raise AccessSystem.UserNotRegisteredException


def main():
    access_system = AccessSystem()
    while True:
        commands = ['read', 'write', 'identificate', 'change', 'logout', 'defolt']
        try:
            command = input('Input command >>> ').lower()
            command = command.split(' ')
            if len(command) == 1 and command[0] in commands[-2:]:
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
                    access_system.change_rights(int(command[1]))
        except Exception as exp:
            print(exp)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ex:
        print("Keyboard interrupt")