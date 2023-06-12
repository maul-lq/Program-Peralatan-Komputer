import mysql.connector as mysql

konektor = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="db_peralatan_lab_komputer"
)


# menmbuat fungsi untuk mengambil data dari database ke tampilan program pada tabel
def pilih():
    perintah = konektor.cursor()
    perintah.execute("SELECT * FROM `tb_peralatan_lab_komputer`")

    # mengambil hasil data records dari tabel
    data = perintah.fetchall();

    # mengambil header dari tabel
    header = [header[0] for header in perintah.description]

    # memberikan sebuah tuple yang berisi kepala tabel dan data pada tabel
    return [header, data]

# membuat fungsi untuk menambah data dari program ke database
def tambah(no: int, nama: str, stok: int) -> int:
  """Fungsi untuk menambahkan data ke tabel di database

  Args:
      no (int): Nomor
      nama (str): Nama Barang
      stok (int): Stok Barang

  Returns:
      int: Mengembalikan berapa baris yang berhasil di tambahkan ke tabel.
  """
  queri = \
  f"INSERT INTO `tb_peralatan_lab_komputer`(`No`, `Nama Barang`, `Stok`) VALUES ('{no}','{nama}','{stok}');"
  
  perintah = konektor.cursor()
  perintah.execute(queri)

  konektor.commit()
  
  return perintah.rowcount

def hapus(no: int) -> int:
  """Fungsi untuk menghapus record yang sesuai dengan nomor

  Args:
      no (int): Nomor

  Returns:
      int: Mengembalikan berapa baris yang berhasil di hapus ke tabel.
  """
  queri = f"DELETE FROM `tb_peralatan_lab_komputer` WHERE `No`='{no}'"

  perintah = konektor.cursor()
  perintah.execute(queri)

  konektor.commit()

  x = perintah.rowcount

  return x

# membuat fungsi untuk memperbarui urutan nomor

if __name__ == "__main__":
    #   print(len(pilih()[1]))
    #   # print(tambah(6,"CPU", 20))
    #   print(hapus(no=6))
    pass

    print(pilih())
    print(tambah(10, "ABD", 200))
    print(pilih())

