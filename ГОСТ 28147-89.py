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
        for index in range(1,33):

            key = (d[str(index)])

            F = bin(((A + key) & int('FFFFFFFF', 16)))[2:].zfill(32)

            F1 = s_box[0][int(F[28:32],2)]
            F2 = s_box[1][int(F[24:28],2)]
            F3 = s_box[2][int(F[20:24],2)]
            F4 = s_box[3][int(F[16:20],2)]
            F5 = s_box[4][int(F[12:16],2)]
            F6 = s_box[5][int(F[ 8:12],2)]
            F7 = s_box[6][int(F[ 4: 8],2)]
            F8 = s_box[7][int(F[ 0: 4],2)]

            F = F8 + F7 + F6 + F5 + F4 + F3 + F2 + F1
            F = F[11:32] + F[0:11]

            if index != 32 :
                An = int(F,2) ^ B
                Bn = A
            else :
                Bn = int(F,2) ^ B
                An = A

            A = An
            B = Bn

        output = hex(B << 32 | A)[2:].zfill(16)
        return output
    
     def decrypt(self):
        self.result_text.delete(1.0, END)

        with open(self.s_box_dict[self.s_box_var.get()]) as file:
            s_box_input = file.read()
        file.close()

        self.s_box = [[] for _ in range(8)]

        for index in range(0,16) :
            for row in range(0,8) :
                self.s_box[row].append(bin(int(s_box_input[index*2 + 32*row],16))[2:].zfill(4))

        key = self.reverse(self.key_var.get()[0:64])

        self.K8 = int(key[ 0: 8],16)
        self.K7 = int(key[ 8:16],16)
        self.K6 = int(key[16:24],16)
        self.K5 = int(key[24:32],16)
        self.K4 = int(key[32:40],16)
        self.K3 = int(key[40:48],16)
        self.K2 = int(key[48:56],16)
        self.K1 = int(key[56:64],16)

        input = self.base_text.get(1.0, END)[:-1]

        if self.method_var.get() == 'ECB mode':
            output = ''
            for block_num in range ((len(input[:-1])//16)+1):
                output = output + self.decrypt_ecb(input[0+block_num*16:16+block_num*16])
            self.result_text.insert(1.0, output)
            return output
  


    
    Main_window().window.mainloop()
