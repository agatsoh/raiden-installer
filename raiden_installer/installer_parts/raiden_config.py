import os
from pathlib import Path


class PlainTxtPwd:
    '''
    Provides a method for storing the keystore pwd in a plain txt
    file which is necessary when initializing Raiden and a method
    for deleting that very same file.

    Intended for testnet use only with throwaway keystore account
    and pwd.
    '''
    def __init__(self, dest_dir: str, keystore_pwd: str):
        self.dest_dir = dest_dir
        self.keystore_pwd = keystore_pwd
        self.pwd_file = None

    def create_plain_txt_pwd_file(self):
        pwd_file = Path(self.dest_dir).joinpath('pwd.txt')

        with open(pwd_file, 'w') as f:
            f.write(self.keystore_pwd)

        self.pwd_file = pwd_file

    def delete_plain_txt_pwd_file(self):
        try:
            os.remove(self.pwd_file)
            self.pwd_file = None
        except (TypeError, FileNotFoundError) as err:
            print('No password file to delete')