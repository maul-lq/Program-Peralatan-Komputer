from math import pi

class Bangun_Datar:
    # membuat private atribut
    __sisi: int | float

    def __init__(self) -> None:
        self.__sisi = int(0)

    def info(self):
        print("Ini adalah sebuah bangun datar yang ber sisi {}".format(self.__sisi))


class Belah_Ketupat(Bangun_Datar):
    # membuat private atribut
    __sisi: int | float
    __diagonal: list[int | float]

    def __init__(self) -> None:
        super().__init__()

        self.__sisi = 0
        self.__diagonal = [0,0]

    def hitung_luas(self):
        return 0.5*self.__diagonal[0]*self.__diagonal[1]

    def hitung_keliling(self):
        return self.__sisi*4

    def set_sisi(self, sisi: int | float):
        if isinstance(sisi, int) or isinstance(sisi, float):
            self.__sisi = sisi
        else:
            raise Exception("Sisi harus berupa angka!")

    def set_diagonal(self, diagonal: list[int | float]):
        if (isinstance(diagonal[0], int) or isinstance(diagonal[0], float)) and (isinstance(diagonal[1], int) or isinstance(diagonal[1], float)):
            self.__diagonal = diagonal
        else:
            raise Exception("Sisi harus berupa angka!")

    def get_sisi(self):
        return self.__sisi
    def get_diagonal(self):
        return self.__diagonal

    def info(self):
        print(f"Ini adalah belah ketupat yang memiliki atribut:\n Sisi {self.__sisi}\n Diagonal 1: {self.__diagonal[0]}\n Diagonal 2: {self.__diagonal[1]}")

class Lingkaran(Bangun_Datar):
    __diameter: int | float
    __ruas: int | float

    def __init__(self) -> None:
        super().__init__()

        self.__ruas = 0
        self.__diameter = 0

    def hitung_luas(self):
        return pi*self.__ruas*self.__ruas

    def hitung_keliling(self):
        return pi*self.__diameter

    def set_ruas(self, ruas: float |int):
        self.__ruas = ruas

    def set_diameter(self, diameter:float |int):
        self.__diameter = diameter

    def get_ruas(self):return self.__ruas
    def get_diameter(self):return self.__diameter

    def info(self):
        print(f"Ini adalah Lingkaran yang memiliki atribut:\n Ruas {self.get_ruas()}\n Diameter: {self.get_diameter()}")

class Segitiga(Bangun_Datar):
    __sisi: list[int | float]
    __alas: int | float
    __tinggi: int | float

    def __init__(self) -> None:
        super().__init__()

        self.__sisi =[0,0,0]
        self.__alas=0
        self.__tinggi=0

    def hitung_luas(self):
        return 0.5*self.__alas*self.__tinggi

    def hitung_keliling(self):
        return self.__sisi[0]+self.__sisi[1]+self.__sisi[2]

    def set(self, **atribut):
        self.__sisi = atribut.get("sisi", [0,0,0])
        self.__alas = atribut.get('alas', 0)
        self.__tinggi = atribut.get('tinggi', 0)

    def get(self):return [self.__sisi, self.__alas, self.__tinggi]

    def info(self):
        print(f"Ini adalah Segitiga yang memiliki atribut:\n Sisi {self.__sisi}\n Alas: {self.__alas}\n Tinggu: {self.__tinggi}")

if __name__ == '__main__':
    l = Lingkaran()
    s = Segitiga()
    b = Belah_Ketupat()


    
    l.set_ruas(10)
    l.set_diameter(200)
    l.info()
    print(l.get_ruas())
    print(l.hitung_luas())
    print(l.hitung_keliling())

    s.set(sisi=[10,10,10], alas=10, tinggi=5)
    s.info()
    print(s.hitung_keliling())
    print(s.hitung_luas())

    b.set_diagonal([10,2.3])
    b.set_sisi(20)
    b.info()
    print(b.hitung_keliling())
    print(b.hitung_luas())
                    

                    
                    