from tkinter import *
from tkinter import ttk


class KeyDict(dict):
    def keylist(self, keys, value):
        for key in keys:
            self[key] = value


class Main_window():
    def reverse(self, num):
        return "".join(reversed([num[i:i + 2] for i in range(0, len(num), 2)]))

    def little_endian(self, num):
        res = ''
        for pack in reversed(range(0, len(num), 8)):
            res = res + num[pack:pack + 8]
        return self.reverse(res)

    def encrypt_ecb(self, input):
        input = input.zfill(16)

        A = int(input[8:16], 16)
        B = int(input[0: 8], 16)

        s_box = self.s_box

        d = KeyDict()
        d.keylist(('1', '9', '17', '32'), self.K1)  # dictionary of subkeys
        d.keylist(('2', '10', '18', '31'), self.K2)
        d.keylist(('3', '11', '19', '30'), self.K3)
        d.keylist(('4', '12', '20', '29'), self.K4)
        d.keylist(('8', '16', '24', '25'), self.K8)
        d.keylist(('5', '13', '21', '28'), self.K5)
        d.keylist(('6', '14', '22', '27'), self.K6)
        d.keylist(('7', '15', '23', '26'), self.K7)
