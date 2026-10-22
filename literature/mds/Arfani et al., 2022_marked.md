---
conversion_metadata:
  converted_at: "2026-10-21T11:48:28Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Arfani et al., 2022.pdf"
  source_pdf_sha256: "7caa5cea06acfeab2c450462b746fe326c7ec32da5c5c176929944750246ab9c"
  page_count: 26
  markdown_char_count: 56224
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

PENGUJIAN APLIKASI PRESENSI MENGGUNAKAN

METODE BLACK BOX TESTING

SKRIPSI

Diajukan Untuk Memenuhi Syarat Guna 
Memperoleh Gelar Sarjana Komputer ( S.Kom )  
Pada Prodi Teknik Informatika

OLEH :

A. RIFQI YARZUQ ARFANI 
NPM : 18.1.03.02.0142

UNIVERSITAS NUSANTARA PERSATUAN GURU REPUBLIK INDONESIA

FAKULTAS TEKNIK (FT)

UN PGRI KEDIRI

2022

---

<!-- PAGE 2 -->

ii

---

<!-- PAGE 3 -->

iii

---

<!-- PAGE 4 -->

HALAMAN PERNYATAAN

Yang bertanda tangan dibawah ini :

Nama

: A. Rifqi Yarzuq Arfani

Jenis Kelamin

: Laki-Laki

Tempat/Tanggal Lahir

: Brebes, 11 Januari 2000

NPM

: 18.1.03.02.0142

Fak/Jur/Prodi

: FT/S1 Teknik Informatika

Menyatakan  dengan  sebenarnya,  bahwa  dalam  skripsi  ini  tidak  terdapat  karya

yang  pernah  diajukan  untuk  memperoleh  gelar  kesarjanaan  di  suatu  perguruan

tinggi, dan sepanjang pengetahuan saya tidak terdapat karya tulis atau pendapat

yang pernah diterbitkan oleh orang lain, kecuali secara sengaja dan tertulis diacu

dalam naskah ini dan disebutkan dalam daftar pustaka.

Kediri: 22 Juli 2022 
Yang Menyatakan,

A. RIFQI YARZUQ ARFANI 
NPM: 18.1.03.02.0142

iv

---

<!-- PAGE 5 -->

MOTTO DAN PERSEMBAHAN

MOTTO

“Meneng, Ngalah, Menang.” 
KH. A. Dimyathi Romly

PERSEMBAHAN

Allah  SWT,  karena  atas  rahmat  dan  hidayah-Nya,  saya  dapat 
menyelesaikan tugas akhir skripsi dengan lancar. Terima kasih kepada seluruh 
keluarga besar saya yang terus mendoakan dan mendukung saya, serta menjadi 
alasan saya untuk tetap semangat dalam menyelesaikan tugas akhir ini.

v

---

<!-- PAGE 6 -->

ABSTRAK

A.  Rifqi  Yarzuq  Arfani  Pengujian  Aplikasi  Presensi  Menggunakan  Metode 
Black Box Testing, Skripsi, Teknik Informatika, FT UN PGRI Kediri, 2022.

Kata  Kunci:  Presensi,  Pengujian  Perangkat  Lunak,  Black  Box  Testing, 
Equivalence Partitioning, Boundary Value Analysis

Presensi perkuliahan adalah hal penting dalam dunia perkuliahan, karena 
kehadiran  mahasiswa  merupakan  salah  satu  faktor  dari  penilaian  suatu  mata 
kuliah.  Tetapi  presensi  manual  dengan  menggunakan  media  tulis  memiliki 
kekurangan seperti rekapitulasi manual dan transparansi data. Memanfaatkan fitur 
pada  gawai  seperti  gps  dibuatlah  sebuah  aplikasi  presensi  untuk  mengatasi 
masalah  diatas.  Melihat  pentingnya  data  presensi,  maka  wajib  dilakukannya 
pengujian perangkat lunak pada aplikasi tersebut, dimana hasil dari pengujian ini 
dapat  membantu  pengembang  dalam  menemukan  kesalahan,  memastikan 
kelayakan  dan  kesesuaian  dengan  kebutuhan  pengguna.  Metodologi  yang 
digunakan dalam pengujian perangkat lunak ini menggunakan metode Black Box 
Testing, dimana didalamnya terdapat alur untuk melakukan perancangan skenario 
pengujian  dengan  menggunakan  teknik  Equivalence  Partitioning  dan  Boundary 
Value  Analysis.  Hasil  dari  penelitian  ini  adalah  kesimpulan  untuk  memastikan 
perangkat lunak yang diuji dapat berjalan dengan baik dan sesuai kebutuhan yang 
sudah  ditentukan.  Berdasarkan  hasil  pengujian  perangkat  lunak  yang  telah 
dilakukan, maka hasil uji yang dihasilkan dapat berguna sebagai bahan evaluasi 
dimasa mendatang.

vi

---

<!-- PAGE 7 -->

KATA PENGANTAR

Puji Syukur Kami panjatkan kehadirat Allah Tuhan Yang Maha Kuasa,

karena hanya atas perkenan-Nya penyusunan skripsi ini dapat diselesaikan.

Skripsi  dengan  judul  “Pengujian  Aplikasi  Presensi  Menggunakan

Metode  Black  Box  Testing”  ini  ditulis  guna  memenuhi  sebagian  syarat  untuk

memperoleh gelar Sarjana Komputer, pada Jurusan Teknik Informatika FT UN

PGRI Kediri.

Pada kesempatan ini diucapkan terimakasih dan penghargaan  kepada

setulus-tulusnya kepada:

1.  Dr.  Zainal  Afandi,  M.Pd.  selaku  Rektor  Universitas  Nusantara  PGRI

Kediri, yang selalu memberikan dorongan motivasi kepada mahasiswa.

2.  Dr.  Suryo  Widodo,  M.Pd.  selaku  Dekan  Fakultas  Teknik  yang  selalu

memberikan dukungan moral kepada mahasiswa.

3.  Ahmad Bagus Setiawan, S.T., M.M., M.Kom. selaku Ketua Program Studi

Teknik Informatika yang selalu memberikan arahan kepada mahasiswa.

4.  Patmi Kasih, M. Kom. dan Danar Putra Pamungkas, M.Kom selaku Dosen

Pembimbing yang selalu memberikan bimbingan kepada mahasiswa.

5.  Kedua orang tua saya dan keluarga besar saya atas dukungan dan doanya.

6.  Teman-teman  yang  selalu  membantu  dan  mendukung  saya  dalam

pengerjaan penyusunan skripsi ini.

Disadari bahwa skripsi ini masih banyak kekurangan, maka diperlukan

tegur sapa, kritik dan saran-saran dari berbagai pihak sangat diharapkan.

Akhirnya,  disertai  harapan  semoga  skripsi  ini  bermanfaat  bagi  kita

semua, khususnya bagi dunia komputer.

Kediri, 22 Juli 2022

A. Rifqi Yarzuq Arfani 
NPM: 18.1.03.02.0142

vii

---

<!-- PAGE 8 -->

DAFTAR ISI

HALAMAN JUDUL ....................................................................................... i

HALAMAN PERSETUJUAN ....................................................................... ii

HALAMAN PENGESAHAN ....................................................................... iii

HALAMAN PERNYATAAN ....................................................................... iv

MOTTO DAN PERSEMBAHAN ................................................................... v

ABSTRAK .................................................................................................... vi

KATA PENGANTAR .................................................................................. vii

DAFTAR ISI ............................................................................................... viii

DAFTAR TABEL ......................................................................................... xi

DAFTAR GAMBAR .................................................................................... xv

DAFTAR LAMPIRAN ............................................................................... xvi

BAB I PENDAHULUAN ............................................................................... 1

A. Latar Belakang ................................................................................ 1

B. Identifikasi Masalah ........................................................................ 3

C. Rumusan Masalah ........................................................................... 3

D. Batasan Masalah ............................................................................. 3

E. Tujuan Penelitian ............................................................................ 4

F.  Manfaat dan Kegunaan Penelitian ................................................... 4

G. Metode Penelitian ........................................................................... 5

H. Jadwal Penelitian ............................................................................ 7

I.  Sistematis Penulisan Laporan ......................................................... 7

viii

---

<!-- PAGE 9 -->

BAB II TINJAUAN PUSTAKA ..................................................................... 9

A. Landasan Teori ................................................................................ 9

1.  Pengujian Secara Umum ............................................................ 9

2.  Definisi Pengujian .................................................................... 10

3.  Kualitas Perangkat Lunak ......................................................... 11

4.  Sasaran dan Prinsip Pengujian .................................................. 12

5.  Tujuan Pengujian Perangkat Lunak .......................................... 12

6.  Black-Box Testing ..................................................................... 13

7.  Skenario Pengujian ................................................................... 16

8.  Desain Template Skenario Pengujian ....................................... 16

B. Kajian Pustaka .............................................................................. 19

BAB III ANALISIS DAN PERANCANGAN PENGUJIAN........................ 21

A. Deskripsi Umum Aplikasi ............................................................. 21

B. Daftar Kebutuhan .......................................................................... 24

C. Tampilan Aplikasi ......................................................................... 26

D. Diagram Use Case ......................................................................... 35

E. Equivalence Partitioning ............................................................... 36

F.  Boundary Value Analysis ............................................................. 42

G. Skenario Pengujian ....................................................................... 48

BAB IV HASIL PENGUJIAN ...................................................................... 67

A. Pengaturan Lingkungan Pengujian ................................................ 67

B. Kesimpulan Pelaksanaan Pengujian .............................................. 69

C. Rekomendasi Perbaikan ................................................................ 70

ix

---

<!-- PAGE 10 -->

BAB V PENUTUP ........................................................................................ 71

A. Kesimpulan ................................................................................... 71

B. Saran ............................................................................................. 71

DAFTAR PUSTAKA ................................................................................... 72

LAMPIRAN .................................................................................................. 74

x

---

<!-- PAGE 11 -->

DAFTAR TABEL

Tabel                                                                                                         Halaman

1.1 Jadwal Penelitian ................................................................................... 7

2.1 Contoh Equivalence Partitioning ......................................................... 15

2.2 Tabel Template Skenario Pengujian .................................................... 17

3.1 Spesifikasi Kebutuhan Fungsional Mahasiswa .................................... 24

3.2 Spesifikasi Kebutuhan Fungsional Administrator ................................ 24

3.3 Spesifikasi Kebutuhan Non-Fungsional ............................................... 25

3.4 Equivalence Partitioning Registrasi Valid ........................................... 36

3.5 Equivalence Partitioning Registrasi Invalid ........................................ 37

3.6 Equivalence Partitioning Login Valid ................................................. 37

3.7 Equivalence Partitioning Login Invalid ............................................... 37

3.8 Equivalence Partitioning Presensi Valid ............................................. 38

3.9 Equivalence Partitioning Presensi Invalid ........................................... 38

3.10 Equivalence Partitioning Cuti Valid .................................................. 38

3.11 Equivalence Partitioning Cuti Invalid ............................................... 39

3.12 Equivalence Partitioning Update Profil Valid ................................... 39

3.13 Equivalence Partitioning Update Profil Invalid ................................. 40

3.14 Equivalence Partitioning Admin Registrasi Valid ............................. 40

3.15 Equivalence Partitioning Admin Registrasi Invalid ........................... 40

3.16 Equivalence Partitioning Admin Login Valid .................................... 41

xi

---

<!-- PAGE 12 -->

3.17 Equivalence Partitioning Admin Login Invalid .................................. 41

3.18 Equivalence Partitioning Admin Tambah Lokasi Valid .................... 41

3.19 Equivalence Partitioning Admin Tambah Lokasi Invalid .................. 42

3.20 Boundary Value Analysis Registrasi Valid ........................................ 42

3.21 Boundary Value Analysis Registrasi Invalid ...................................... 43

3.22 Boundary Value Analysis Presensi Valid ........................................... 44

3.23 Boundary Value Analysis Presensi Invalid ........................................ 44

3.24 Boundary Value Analysis Cuti Valid ................................................. 44

3.25 Boundary Value Analysis Cuti Invalid ............................................... 45

3.26 Boundary Value Analysis Update Profil Valid ................................... 45

3.27 Boundary Value Analysis Update Profil Invalid ................................ 46

3.28 Boundary Value Analysis Admin Registrasi Valid ............................ 46

3.29 Boundary Value Analysis Admin Registrasi Invalid .......................... 47

3.30 Boundary Value Analysis Admin Tambah Lokasi Valid .................... 47

3.31 Boundary Value Analysis Admin Tambah Lokasi Invalid ................. 48

3.32 Skenario Pengujian Registrasi Mahasiswa ......................................... 48

3.33 Skenario Pengujian Login Mahasiswa ............................................... 51

3.34 Skenario Pengujian Mencatat Presensi .............................................. 52

3.35 Skenario Pengujian Input Cuti ........................................................... 53

3.36 Skenario Pengujian Update Profil ...................................................... 55

3.37 Skenario Pengujian Melakukan Logout ............................................. 58

xii

---

<!-- PAGE 13 -->

3.38 Skenario Pengujian Registrasi Admin ................................................ 59

3.39 Skenario Pengujian Login Admin ...................................................... 61

3.40 Skenario Pengujian Menambahkan Data Lokasi ................................ 62

3.41 Skenario Pengujian Menampilkan Data Presensi dan Cuti ................ 64

3.42 Skenario Pengujian Mengatur Data Jadwal ........................................ 64

3.43 Skenario Pengujian Melakukan Logout Admin ................................. 65

4.1 Lingkungan Perangkat Lunak .............................................................. 67

4.2 Lingkungan Perangkat Keras Gawai .................................................... 68

4.3 Lingkungan Perangkat Keras Laptop ................................................... 68

4.4 Hasil Pengujian Test Case.................................................................... 69

4.5 Rekomendasi Perbaikan ....................................................................... 70

A.1 Data Uji Registrasi Mahasiswa Valid ................................................. 74

A.2 Data Uji Registrasi Mahasiswa Invalid ............................................... 75

A.3 Data Uji Login Mahasiswa Valid ........................................................ 76

A.4 Data Uji Login Mahasiswa Invalid ...................................................... 76

A.5 Data Uji Presensi Mahasiswa Valid .................................................... 76

A.6 Data Uji Presensi Mahasiswa Invalid .................................................. 76

A.7 Data Uji Cuti Mahasiswa Valid .......................................................... 77

A.8 Data Uji Cuti Mahasiswa Invalid ........................................................ 77

A.9 Data Uji Update Profil Mahasiswa Valid ............................................ 78

A.10 Data Uji Update Profil Mahasiswa Invalid ....................................... 79

A.11 Data Uji Registrasi Administrator Valid ........................................... 80

xiii

---

<!-- PAGE 14 -->

A.12 Data Uji Registrasi Administrator Invalid......................................... 80

A.13 Data Uji Login Administrator Valid .................................................. 81

A.14 Data Uji Login Administrator Invalid ............................................... 81

A.15 Data Uji Administrator Tambah Lokasi Valid .................................. 81

A.16 Data Uji Administrator Tambah Lokasi Invalid ................................ 82

xiv

---

<!-- PAGE 15 -->

DAFTAR GAMBAR

Gambar                                                                                                       Halaman

1.1 Diagram Waterfall Metode Penelitian.................................................... 5

3.1 Tampilan Registrasi Mahasiswa .......................................................... 26

3.2 Tampilan Login Mahasiswa ................................................................. 27

3.3 Tampilan Presensi Mahasiswa ............................................................. 27

3.4 Tampilan Input Cuti Mahasiswa .......................................................... 28

3.5 Tampilan Edit Profil Mahasiswa .......................................................... 29

3.6 Tampilan Profil dan Logout Mahasiswa .............................................. 29

3.7 Tampilan Registrasi Administrator ...................................................... 30

3.8 Tampilan Login Administrator ............................................................ 31

3.9 Tampilan Daftar dan Hapus Lokasi ..................................................... 31

3.10 Tampilan Tambah Lokasi .................................................................. 32

3.11 Tampilan Riwayat Cuti ...................................................................... 32

3.12 Tampilan Riwayat Kehadiran ............................................................ 33

3.13 Tampilan Atur Jadwal ........................................................................ 34

3.14 Tampilan Profil dan Logout ............................................................... 34

3.15 Use Case Diagram Aplikasi Presensi ................................................. 35

xv

---

<!-- PAGE 16 -->

DAFTAR LAMPIRAN

Lampiran                                                                                                             Halaman

A Rancangan Kasus Uji Skenario Pengujian ............................................. 74

B Surat Pernyataan Validasi Penelitian Skripsi ......................................... 83

xvi

---

<!-- PAGE 17 -->

BAB I

PENDAHULUAN

Pendahuluan  merupakan  sebuah  dasar  awal  yang  dibutuhkan  dalam

sebuah penelitian. Dalam pendahuluan terdiri atas beberapa bagian seperti latar

belakang,  identifikasi  masalah,  rumusan  masalah,  batasan  masalah,  tujuan

penelitian dan manfaat penelitian.

A.  Latar Belakang

Presensi  perkuliahan  adalah  sebuah  catatan  atas  hadir  atau

tidaknya  seorang  mahasiswa  dalam  kegiatan  perkuliahannya.  Dalam

kegiatan perkuliahan daftar hadir seorang mahasiswa adalah poin penting

yang sangat diperhatikan dan diawasi oleh dosen pengampu. Karena hasil

rekap  atas  daftar  hadir  mahasiswa  tersebut  dapat  berpengaruh  terhadap

penilaian masing masing mata kuliah dan dapat sebagai syarat mahasiswa

dalam  mengikuti ujian akhir sekolah. Daftar hadir yang dilakukan dengan

cara  manual,  yaitu  dengan  memberikan  tanda  tangan  mahasiswa  masing-

masing dalam setiap mata kuliah.

Presensi  manual  menggunakan  media  tulis  adalah  sistem  yang

sering diterapkan sebagai alat presensi saat ini seperti di perkuliahan Teknik

Informatika. Sistem presensi dengan media alat tulis dapat membantu dosen

dalam  pencatatan  data  kehadiran.  Tetapi  presensi  manual  atau  dengan

menggunakan media tulis ini memiliki kekurangan, yaitu data rekapitulasi

1

---

<!-- PAGE 18 -->

2

dari  presensi  bersifat  transparan  yang  artinya  disini  dosen  pengampu

masing-masing mata kuliah tidak mengetahui kebenarannya.

Aplikasi presensi merupakan jawaban dari  masalah diatas, dosen

atau  admin  dapat  mengisi  area  yang  diperbolehkan  untuk  mahasiswa

melakukan  presensi,  dan  mahasiswa  akan  menggunakan  aplikasi  tersebut

untuk mengisi presensi. Memanfaatkan fitur  gps yang ada pada perangkat

smartphone  dan  algoritma  haversine,  aplikasi  ini  memastikan  bahwa

mahasiswa  dapat  mengisi  presensi  jika  berada  pada  lokasi  yang  telah

ditentukan sebelumnya. Selain presensi mahasiswa juga dapat mengisi izin

maupun  cuti  perkuliahan  yang  bisa  dilihat  pada  web  dashboard

administrator.

Software testing (Pengujian Perangkat Lunak) adalah  hal penting

untuk menjamin  kualitas perangkat lunak  yang  menyajikan  bagian  utama

atau  dasar  atas  desain,  spesifikasi,  dan  pengkodean.  Software  testing

dilakukan dengan tujuan untuk memastikan apakah kualitas dari perangkat

lunak yang digunakan telah memenuhi syarat. Pengujian perangkat lunak

ini  dapat  dilakukan  dengan  pengeksekusian  program  mencari  adanya

kesalahan  sintaks  program,  lalu  mengadakan  verifikasi  program  guna

menyesuaikan  perangkat  dengan  kebutuhan  user.  Software  testing  dalam

penelitian ini dilakukan menggunakan metode black box.

Menurut Ayuliana (2009) pengujian black-box adalah

Sebuah pengujian yang dilakukan dengan melihat dan mengamati 
hasil  dari  pengeksekusian  program  serta  memeriksa  fungsi 
perangkat lunak. Dapat dikatakan black-box adalah sebagai kotak

---

<!-- PAGE 19 -->

3

hitam  yang  dimana  kita  hanya  melihat  bagian  luar  tanpa 
mengetahui  isi  dari  kotak  hitam  tersebut.  Hal  ini  memiliki 
kesamaan  dalam  melakukan  pengujian  black-box,  dimana 
melakukan evaluasi dengan mengamati bagian luar atau interface-
nya saja tanpa melihat proses detail yang terjadi didalamnya.

B.  Identifikasi Masalah

Berdasarkan  latar  belakang  masalah  yang  telah  diuraikan  diatas

dapat  diidentifikasi  bahwa  masalah  pada  penelitian  yaitu  perlunya

memastikan kelayakan fungsi terhadap aplikasi absensi secara menyeluruh.

C.  Rumusan Masalah

Berdasarkan  latar  belakang  masalah  ini,  rumusan  masalah  yang

akan  dibahas  adalah  bagaimana  persiapan  pengujian  dan  cara  melakukan

pengujian aplikasi Presensi menggunakan metode black-box testing.

D.  Batasan Masalah

Pembatasan masalah digunakan agar menghindari perluasan topik

masalah  agar  penelitian

lebih

terarah  dan  mempermudah  dalam

pembahasan  sehingga  mencapai  tujuan  penelitian.  Berikut  ini  beberapa

batasan masalah penelitian ini sebagai berikut :

1.  Penelitian membahas hasil pengujian aplikasi.

2.  Pengujian aplikasi menggunakan metode black-box testing.

3.  Aplikasi yang akan diuji adalah aplikasi Presensi.

---

<!-- PAGE 20 -->

4

4.  Penggunaan  metode  dalam  black  box  testing  yang  digunakan  adalah

Equivalence  Partitioning  (Partisi  Ekuivalensi)  dan  Boundary  Value

Analysis (Analisis Nilai Batas).

E.  Tujuan Penelitian

Tujuan  yang  diperoleh  dari  penelitian  “Pengujian  Aplikasi

Presensi  Menggunakan  Metode  Black-box  Testing”  adalah  melakukan

pengujian  perangkat  lunak  dengan  metode  black-box  testing  terhadap

aplikasi  Presensi  untuk  memastikan  kelayakan  dan  kesalahan  aplikasi,

sehingga  memastikan  meminimalisir  kesalahan  yang  akan  muncul  ketika

penggunaan aplikasi.

F.  Manfaat dan Kegunaan Penelitian

Manfaat  yang  diperoleh  dari  penelitian  “Pengujian  Aplikasi

Absensi Menggunakan Metode Black Box Testing” adalah :

1.  Mengetahui apakah metode  black box  testing sesuai untuk  pengujian

aplikasi Presensi.

2.  Dapat mengetahui kelebihan dan kekurangan pada aplikasi Presensi.

3.  Dapat meminimalisir error pada aplikasi sehingga error yang ada dapat

diselesaikan sebelum aplikasi diimplementasikan.

---

<!-- PAGE 21 -->

5

G.  Metode Penelitian

1.  Teknik Penelitian

Teknik penelitian yang  dilakukan adalah  kualitatif  deskriptif

yaitu metode penelitian yang berlandaskan ada sumber referensi jurnal

guna  menunjang  penelitian  yang  dilakukan.  Pengumpulan  data

menggunakan  instrumen  penelitian  dengan  tujuan  untuk  mengacu

hipotesis yang telah ditetapkan (Sugiyono 2017:8).

2.  Prosedur Penelitian

Dalam  prosedur  penelitian  ini  penulis  melakukan  beberapa

metode  untuk  diterapkan  dalam  penelitian  ini  diantaranya  sebagai

berikut :

Gambar 1.1 Diagram Waterfall Metode Penelitian

---

<!-- PAGE 22 -->

6

a.  Studi Literatur

Dalam studi literatur ini mempelajari buku-buku referensi, jurnal

penelitian,  buku  dan  sumber  lainnya  yang  sekiranya  berkaitan

dengan masalah yang diteliti

b.  Observasi

Sebelum  melakukan  pengujian  perangkat  lunak,  diperlukan  data

dan informasi yang lengkap dan menyeluruh mengenai perangkat

lunak yang akan diuji. Pada tahap ini akan dilakukan pengumpulan

data dan studi kasus.

c.  Perencanaan Pengujian

Tahap  awal  dari  pengujian  perangkat

lunak  merupakan

perencanaan  pengujian  akan  dilakukan.  Tahap

ini  adalah

menentukan  metode  dan  teknik  pengujian  terhadap  aplikasi

Absensi

d.  Pelaksanaan Pengujian

Pada  tahap  pelaksanaan  pengujian  ini  akan  dilakukan  dengan

berdasarkan  perencanaan  yang  berisi  metode  dan  teknik  yang

sudah disiapkan pada tahap sebelumnya.

e.  Penulisan Laporan

Penulisan  laporan  adalah  tahap  akhir  atas  pengujian  perangkat

lunak  yang  dimana  berupa  analisis  laporan  hasil  pengujian  yang

telah dilakukan.

---

<!-- PAGE 23 -->

7

H.  Jadwal Penelitian

Tabel 1.1 Jadwal Penelitian

Bulan

Bulan

Bulan

Bulan

Ke- 1

Ke-2

Ke-3

Ke-4

Bulan

Ke-5

1  2  3  4  1  2  3  4  1  2  3  4  1  2  3  4  1  2  3  4

No.

Jenis

Kegiatan

1.

2.

3.

4.

5.

Studi

Literatur

Observasi

Perencanaan

Pengujian

Pelaksanaan

Pengujian

Penulisan

Laporan

I.  Sistematis Penulisan Laporan

BAB I PENDAHULUAN

Dalam  bab  ini  dijelaskan  perihal  pembahasan  masalah  secara

umum  meliputi  latar  belakang,  identifikasi  masalah,  rumusan  masalah,

batasan  masalah,  tujuan  penelitian,  manfaat  dan  kegunaan  penelitian,

metode penelitian, jadwal penelitian, dan sistematika penulisan laporan.

BAB II TINJAUAN PUSTAKA

Bab  ini  memuat  teori-teori  yang  mendukung  dalam  pengerjaan

tugas  akhir.  Pada  bab  ini  dikemukakan  definisi,  teori  dan  konsep  yang

diperlukan  khususnya  teknik  black-box  dengan  metode  equivalence

---

<!-- PAGE 24 -->

8

partitioning dan boundary value analysis sebagai pustaka untuk membantu

penelitian.

BAB III ANALISIS DAN PERENCANAAN PENGUJIAN

Bab ini berisi rancangan pengujian aplikasi yang berisi pembuatan

test  case  dan  pemilihan  metode  yang  akan  dilakukan  pada  pengujian

aplikasi.

BAB IV HASIL PENGUJIAN

Bab ini  berisi  hasil  pengujian  atau  Testing dengan menggunakan

metodologi Black-box Testing. Hasil ini berguna untuk mengetahui kualitas

aplikasi presensi sesuai dengan kebutuhan yang telah ditentukan.

BAB V PENUTUP

Bab  ini  berisi  kesimpulan  dari  penelitian  yang  sudah  dilakukan,

saran yang bisa digunakan untuk pengembangan kasus uji black-box testing

dan daftar pustaka dari penelitian yang digunakan sebagai referensi.

---

<!-- PAGE 25 -->

DAFTAR PUSTAKA

Fatkhurrokhman,  M.  (2014).  Analisis  Pengujian  Sistem  Informasi  Akademik

STMIK El Rahma Yogyakarta.

Kusuma, A. a. (2016). Implementasi Dan Pengujian Web  E-Commerce Untuk

Produk Unggulan Desa.

M.Bachtiar,  A.,  Dharmayanti,  D.,  &  S,  M.  K.  (2007).  Analisis  Kualitas 
Perangkat Lunak Terhadap Sistem Informasi. Majalah Ilmiah UNIKOM 
Vol.11 No. 2, 224-233.

Murad,  D.  F.,  Kusniawati,  N.,  &  Asyanto,  A.  (2013).  Aplikasi  Intelligence 
Website  Untuk  Penunjang  Laporan  PAUD  Pada  Himpaudi  Kota 
Tangerang. CCIT Journal, 7(1), 44-58.

Mustaqbal,  M.  S.,  Firdaus,  R.  F.,  &  Rahmadi,  H.  (Jurnal  Ilmiah  Teknologi 
Informasi  Terapan  Volume  I,  No  3,  10  Agustus  2015).  PENGUJIAN 
APLIKASI MENGGUNAKAN BLACK BOX TESTING BOUNDARY 
VALUE  ANALYSIS  (Studi  Kasus  :  Aplikasi  Prediksi  Kelulusan 
SNMPTN). Jurnal Ilmiah Teknologi Informasi Terapan, 31-36.

Myers, G. J., Sandler, C., & Badgett, T. (2011). The Art of Software Testing.

NURSEHA, I. (IRVAN NURSEHA). PERANCANGAN SISTEM INFORMSI 
QUALITY CONTROL STOCK EXPIRED DI PT. CATUR SENTOSA 
ANUGERAH.

Sasmito,  G.  W.  (2017).  Penerapan  Metode  Waterfall  Pada  Desain  Sistem 
Jurnal 
Industri

Informasi 
Informatika:Jurnal Pengembangan IT (JPIT) 2, 6-12.

Kabupaten

Geografis

Tegal.

Sergey, S. (2002). Software Testing: Black-box Techniques,.

Setiawan,  G.  W.

(2011).  PENGUJIAN  PERANGKAT  LUNAK 
MENGGUNAKAN METODE BLACK BOX STUDI KASUS EXELSA 
UNIVERSITAS SANATA DHARMA.

72

---

<!-- PAGE 26 -->

Umi, H., Alit, R., & Sugiarto, S. (2016). Penggunaan Metode  Black-Box Pada

Pengujian Sistem Informasi Surat Keluar Masuk. 19-25.

William, L. (n.d.). Testing Overview and Black-box Testing Techniques. 2006.

William, P. (1995). Effective Methods for Software Testing. 3-430.

73

<!-- MARKITDOWN CONVERSION -->

<!-- The following is the full MarkItDown conversion for formatting fidelity. -->

PENGUJIAN APLIKASI PRESENSI MENGGUNAKAN
METODE BLACK BOX TESTING
SKRIPSI
Diajukan Untuk Memenuhi Syarat Guna
Memperoleh Gelar Sarjana Komputer ( S.Kom )
Pada Prodi Teknik Informatika
OLEH :
A. RIFQI YARZUQ ARFANI
NPM : 18.1.03.02.0142
FAKULTAS TEKNIK (FT)
UNIVERSITAS NUSANTARA PERSATUAN GURU REPUBLIK INDONESIA
UN PGRI KEDIRI
2022

ii

iii

HALAMAN PERNYATAAN
Yang bertanda tangan dibawah ini :
Nama : A. Rifqi Yarzuq Arfani
Jenis Kelamin : Laki-Laki
Tempat/Tanggal Lahir : Brebes, 11 Januari 2000
NPM : 18.1.03.02.0142
Fak/Jur/Prodi : FT/S1 Teknik Informatika
Menyatakan dengan sebenarnya, bahwa dalam skripsi ini tidak terdapat karya
yang pernah diajukan untuk memperoleh gelar kesarjanaan di suatu perguruan
tinggi, dan sepanjang pengetahuan saya tidak terdapat karya tulis atau pendapat
yang pernah diterbitkan oleh orang lain, kecuali secara sengaja dan tertulis diacu
dalam naskah ini dan disebutkan dalam daftar pustaka.
Kediri: 22 Juli 2022
Yang Menyatakan,
A. RIFQI YARZUQ ARFANI
NPM: 18.1.03.02.0142
iv

MOTTO DAN PERSEMBAHAN
MOTTO
“Meneng, Ngalah, Menang.”
KH. A. Dimyathi Romly
PERSEMBAHAN
Allah SWT, karena atas rahmat dan hidayah-Nya, saya dapat
menyelesaikan tugas akhir skripsi dengan lancar. Terima kasih kepada seluruh
keluarga besar saya yang terus mendoakan dan mendukung saya, serta menjadi
alasan saya untuk tetap semangat dalam menyelesaikan tugas akhir ini.
v

ABSTRAK
A. Rifqi Yarzuq Arfani Pengujian Aplikasi Presensi Menggunakan Metode
Black Box Testing, Skripsi, Teknik Informatika, FT UN PGRI Kediri, 2022.
Kata Kunci: Presensi, Pengujian Perangkat Lunak, Black Box Testing,
Equivalence Partitioning, Boundary Value Analysis
Presensi perkuliahan adalah hal penting dalam dunia perkuliahan, karena
kehadiran mahasiswa merupakan salah satu faktor dari penilaian suatu mata
kuliah. Tetapi presensi manual dengan menggunakan media tulis memiliki
kekurangan seperti rekapitulasi manual dan transparansi data. Memanfaatkan fitur
pada gawai seperti gps dibuatlah sebuah aplikasi presensi untuk mengatasi
masalah diatas. Melihat pentingnya data presensi, maka wajib dilakukannya
pengujian perangkat lunak pada aplikasi tersebut, dimana hasil dari pengujian ini
dapat membantu pengembang dalam menemukan kesalahan, memastikan
kelayakan dan kesesuaian dengan kebutuhan pengguna. Metodologi yang
digunakan dalam pengujian perangkat lunak ini menggunakan metode Black Box
Testing, dimana didalamnya terdapat alur untuk melakukan perancangan skenario
pengujian dengan menggunakan teknik Equivalence Partitioning dan Boundary
Value Analysis. Hasil dari penelitian ini adalah kesimpulan untuk memastikan
perangkat lunak yang diuji dapat berjalan dengan baik dan sesuai kebutuhan yang
sudah ditentukan. Berdasarkan hasil pengujian perangkat lunak yang telah
dilakukan, maka hasil uji yang dihasilkan dapat berguna sebagai bahan evaluasi
dimasa mendatang.
vi

KATA PENGANTAR
Puji Syukur Kami panjatkan kehadirat Allah Tuhan Yang Maha Kuasa,
karena hanya atas perkenan-Nya penyusunan skripsi ini dapat diselesaikan.
Skripsi dengan judul “Pengujian Aplikasi Presensi Menggunakan
Metode Black Box Testing” ini ditulis guna memenuhi sebagian syarat untuk
memperoleh gelar Sarjana Komputer, pada Jurusan Teknik Informatika FT UN
PGRI Kediri.
Pada kesempatan ini diucapkan terimakasih dan penghargaan kepada
setulus-tulusnya kepada:
1. Dr. Zainal Afandi, M.Pd. selaku Rektor Universitas Nusantara PGRI
Kediri, yang selalu memberikan dorongan motivasi kepada mahasiswa.
2. Dr. Suryo Widodo, M.Pd. selaku Dekan Fakultas Teknik yang selalu
memberikan dukungan moral kepada mahasiswa.
3. Ahmad Bagus Setiawan, S.T., M.M., M.Kom. selaku Ketua Program Studi
Teknik Informatika yang selalu memberikan arahan kepada mahasiswa.
4. Patmi Kasih, M. Kom. dan Danar Putra Pamungkas, M.Kom selaku Dosen
Pembimbing yang selalu memberikan bimbingan kepada mahasiswa.
5. Kedua orang tua saya dan keluarga besar saya atas dukungan dan doanya.
6. Teman-teman yang selalu membantu dan mendukung saya dalam
pengerjaan penyusunan skripsi ini.
Disadari bahwa skripsi ini masih banyak kekurangan, maka diperlukan
tegur sapa, kritik dan saran-saran dari berbagai pihak sangat diharapkan.
Akhirnya, disertai harapan semoga skripsi ini bermanfaat bagi kita
semua, khususnya bagi dunia komputer.
Kediri, 22 Juli 2022
A. Rifqi Yarzuq Arfani
NPM: 18.1.03.02.0142
vii

DAFTAR ISI
HALAMAN JUDUL ....................................................................................... i
HALAMAN PERSETUJUAN ....................................................................... ii
HALAMAN PENGESAHAN ....................................................................... iii
HALAMAN PERNYATAAN ....................................................................... iv
MOTTO DAN PERSEMBAHAN ................................................................... v
ABSTRAK .................................................................................................... vi
KATA PENGANTAR .................................................................................. vii
DAFTAR ISI ............................................................................................... viii
DAFTAR TABEL ......................................................................................... xi
DAFTAR GAMBAR .................................................................................... xv
DAFTAR LAMPIRAN ............................................................................... xvi
BAB I PENDAHULUAN ............................................................................... 1
A. Latar Belakang ................................................................................ 1
B. Identifikasi Masalah ........................................................................ 3
C. Rumusan Masalah ........................................................................... 3
D. Batasan Masalah ............................................................................. 3
E. Tujuan Penelitian ............................................................................ 4
F. Manfaat dan Kegunaan Penelitian ................................................... 4
G. Metode Penelitian ........................................................................... 5
H. Jadwal Penelitian ............................................................................ 7
I. Sistematis Penulisan Laporan ......................................................... 7
viii

BAB II TINJAUAN PUSTAKA ..................................................................... 9
A. Landasan Teori ................................................................................ 9
1. Pengujian Secara Umum ............................................................ 9
2. Definisi Pengujian .................................................................... 10
3. Kualitas Perangkat Lunak ......................................................... 11
4. Sasaran dan Prinsip Pengujian .................................................. 12
5. Tujuan Pengujian Perangkat Lunak .......................................... 12
6. Black-Box Testing ..................................................................... 13
7. Skenario Pengujian ................................................................... 16
8. Desain Template Skenario Pengujian ....................................... 16
B. Kajian Pustaka .............................................................................. 19
BAB III ANALISIS DAN PERANCANGAN PENGUJIAN........................ 21
A. Deskripsi Umum Aplikasi ............................................................. 21
B. Daftar Kebutuhan .......................................................................... 24
C. Tampilan Aplikasi ......................................................................... 26
D. Diagram Use Case ......................................................................... 35
E. Equivalence Partitioning ............................................................... 36
F. Boundary Value Analysis ............................................................. 42
G. Skenario Pengujian ....................................................................... 48
BAB IV HASIL PENGUJIAN ...................................................................... 67
A. Pengaturan Lingkungan Pengujian ................................................ 67
B. Kesimpulan Pelaksanaan Pengujian .............................................. 69
C. Rekomendasi Perbaikan ................................................................ 70
ix

BAB V PENUTUP ........................................................................................ 71
A. Kesimpulan ................................................................................... 71
B. Saran ............................................................................................. 71
DAFTAR PUSTAKA ................................................................................... 72
LAMPIRAN .................................................................................................. 74
x

DAFTAR TABEL
Tabel Halaman
1.1 Jadwal Penelitian ................................................................................... 7
2.1 Contoh Equivalence Partitioning ......................................................... 15
2.2 Tabel Template Skenario Pengujian .................................................... 17
3.1 Spesifikasi Kebutuhan Fungsional Mahasiswa .................................... 24
3.2 Spesifikasi Kebutuhan Fungsional Administrator ................................ 24
3.3 Spesifikasi Kebutuhan Non-Fungsional ............................................... 25
3.4 Equivalence Partitioning Registrasi Valid ........................................... 36
3.5 Equivalence Partitioning Registrasi Invalid ........................................ 37
3.6 Equivalence Partitioning Login Valid ................................................. 37
3.7 Equivalence Partitioning Login Invalid ............................................... 37
3.8 Equivalence Partitioning Presensi Valid ............................................. 38
3.9 Equivalence Partitioning Presensi Invalid ........................................... 38
3.10 Equivalence Partitioning Cuti Valid .................................................. 38
3.11 Equivalence Partitioning Cuti Invalid ............................................... 39
3.12 Equivalence Partitioning Update Profil Valid ................................... 39
3.13 Equivalence Partitioning Update Profil Invalid ................................. 40
3.14 Equivalence Partitioning Admin Registrasi Valid ............................. 40
3.15 Equivalence Partitioning Admin Registrasi Invalid ........................... 40
3.16 Equivalence Partitioning Admin Login Valid .................................... 41
xi

3.17 Equivalence Partitioning Admin Login Invalid .................................. 41
3.18 Equivalence Partitioning Admin Tambah Lokasi Valid .................... 41
3.19 Equivalence Partitioning Admin Tambah Lokasi Invalid .................. 42
3.20 Boundary Value Analysis Registrasi Valid ........................................ 42
3.21 Boundary Value Analysis Registrasi Invalid ...................................... 43
3.22 Boundary Value Analysis Presensi Valid ........................................... 44
3.23 Boundary Value Analysis Presensi Invalid ........................................ 44
3.24 Boundary Value Analysis Cuti Valid ................................................. 44
3.25 Boundary Value Analysis Cuti Invalid ............................................... 45
3.26 Boundary Value Analysis Update Profil Valid ................................... 45
3.27 Boundary Value Analysis Update Profil Invalid ................................ 46
3.28 Boundary Value Analysis Admin Registrasi Valid ............................ 46
3.29 Boundary Value Analysis Admin Registrasi Invalid .......................... 47
3.30 Boundary Value Analysis Admin Tambah Lokasi Valid .................... 47
3.31 Boundary Value Analysis Admin Tambah Lokasi Invalid ................. 48
3.32 Skenario Pengujian Registrasi Mahasiswa ......................................... 48
3.33 Skenario Pengujian Login Mahasiswa ............................................... 51
3.34 Skenario Pengujian Mencatat Presensi .............................................. 52
3.35 Skenario Pengujian Input Cuti ........................................................... 53
3.36 Skenario Pengujian Update Profil ...................................................... 55
3.37 Skenario Pengujian Melakukan Logout ............................................. 58
xii

3.38 Skenario Pengujian Registrasi Admin ................................................ 59
3.39 Skenario Pengujian Login Admin ...................................................... 61
3.40 Skenario Pengujian Menambahkan Data Lokasi ................................ 62
3.41 Skenario Pengujian Menampilkan Data Presensi dan Cuti ................ 64
3.42 Skenario Pengujian Mengatur Data Jadwal ........................................ 64
3.43 Skenario Pengujian Melakukan Logout Admin ................................. 65
4.1 Lingkungan Perangkat Lunak .............................................................. 67
4.2 Lingkungan Perangkat Keras Gawai .................................................... 68
4.3 Lingkungan Perangkat Keras Laptop ................................................... 68
4.4 Hasil Pengujian Test Case.................................................................... 69
4.5 Rekomendasi Perbaikan ....................................................................... 70
A.1 Data Uji Registrasi Mahasiswa Valid ................................................. 74
A.2 Data Uji Registrasi Mahasiswa Invalid ............................................... 75
A.3 Data Uji Login Mahasiswa Valid ........................................................ 76
A.4 Data Uji Login Mahasiswa Invalid ...................................................... 76
A.5 Data Uji Presensi Mahasiswa Valid .................................................... 76
A.6 Data Uji Presensi Mahasiswa Invalid .................................................. 76
A.7 Data Uji Cuti Mahasiswa Valid .......................................................... 77
A.8 Data Uji Cuti Mahasiswa Invalid ........................................................ 77
A.9 Data Uji Update Profil Mahasiswa Valid ............................................ 78
A.10 Data Uji Update Profil Mahasiswa Invalid ....................................... 79
A.11 Data Uji Registrasi Administrator Valid ........................................... 80
xiii

A.12 Data Uji Registrasi Administrator Invalid......................................... 80
A.13 Data Uji Login Administrator Valid .................................................. 81
A.14 Data Uji Login Administrator Invalid ............................................... 81
A.15 Data Uji Administrator Tambah Lokasi Valid .................................. 81
A.16 Data Uji Administrator Tambah Lokasi Invalid ................................ 82
xiv

DAFTAR GAMBAR
Gambar Halaman
1.1 Diagram Waterfall Metode Penelitian.................................................... 5
3.1 Tampilan Registrasi Mahasiswa .......................................................... 26
3.2 Tampilan Login Mahasiswa ................................................................. 27
3.3 Tampilan Presensi Mahasiswa ............................................................. 27
3.4 Tampilan Input Cuti Mahasiswa .......................................................... 28
3.5 Tampilan Edit Profil Mahasiswa .......................................................... 29
3.6 Tampilan Profil dan Logout Mahasiswa .............................................. 29
3.7 Tampilan Registrasi Administrator ...................................................... 30
3.8 Tampilan Login Administrator ............................................................ 31
3.9 Tampilan Daftar dan Hapus Lokasi ..................................................... 31
3.10 Tampilan Tambah Lokasi .................................................................. 32
3.11 Tampilan Riwayat Cuti ...................................................................... 32
3.12 Tampilan Riwayat Kehadiran ............................................................ 33
3.13 Tampilan Atur Jadwal ........................................................................ 34
3.14 Tampilan Profil dan Logout ............................................................... 34
3.15 Use Case Diagram Aplikasi Presensi ................................................. 35
xv

DAFTAR LAMPIRAN
Lampiran Halaman
A Rancangan Kasus Uji Skenario Pengujian ............................................. 74
B Surat Pernyataan Validasi Penelitian Skripsi ......................................... 83
xvi

BAB I
PENDAHULUAN
Pendahuluan merupakan sebuah dasar awal yang dibutuhkan dalam
sebuah penelitian. Dalam pendahuluan terdiri atas beberapa bagian seperti latar
belakang, identifikasi masalah, rumusan masalah, batasan masalah, tujuan
penelitian dan manfaat penelitian.
A. Latar Belakang
Presensi perkuliahan adalah sebuah catatan atas hadir atau
tidaknya seorang mahasiswa dalam kegiatan perkuliahannya. Dalam
kegiatan perkuliahan daftar hadir seorang mahasiswa adalah poin penting
yang sangat diperhatikan dan diawasi oleh dosen pengampu. Karena hasil
rekap atas daftar hadir mahasiswa tersebut dapat berpengaruh terhadap
penilaian masing masing mata kuliah dan dapat sebagai syarat mahasiswa
dalam mengikuti ujian akhir sekolah. Daftar hadir yang dilakukan dengan
cara manual, yaitu dengan memberikan tanda tangan mahasiswa masing-
masing dalam setiap mata kuliah.
Presensi manual menggunakan media tulis adalah sistem yang
sering diterapkan sebagai alat presensi saat ini seperti di perkuliahan Teknik
Informatika. Sistem presensi dengan media alat tulis dapat membantu dosen
dalam pencatatan data kehadiran. Tetapi presensi manual atau dengan
menggunakan media tulis ini memiliki kekurangan, yaitu data rekapitulasi
1

2
dari presensi bersifat transparan yang artinya disini dosen pengampu
masing-masing mata kuliah tidak mengetahui kebenarannya.
Aplikasi presensi merupakan jawaban dari masalah diatas, dosen
atau admin dapat mengisi area yang diperbolehkan untuk mahasiswa
melakukan presensi, dan mahasiswa akan menggunakan aplikasi tersebut
untuk mengisi presensi. Memanfaatkan fitur gps yang ada pada perangkat
smartphone dan algoritma haversine, aplikasi ini memastikan bahwa
mahasiswa dapat mengisi presensi jika berada pada lokasi yang telah
ditentukan sebelumnya. Selain presensi mahasiswa juga dapat mengisi izin
maupun cuti perkuliahan yang bisa dilihat pada web dashboard
administrator.
Software testing (Pengujian Perangkat Lunak) adalah hal penting
untuk menjamin kualitas perangkat lunak yang menyajikan bagian utama
atau dasar atas desain, spesifikasi, dan pengkodean. Software testing
dilakukan dengan tujuan untuk memastikan apakah kualitas dari perangkat
lunak yang digunakan telah memenuhi syarat. Pengujian perangkat lunak
ini dapat dilakukan dengan pengeksekusian program mencari adanya
kesalahan sintaks program, lalu mengadakan verifikasi program guna
menyesuaikan perangkat dengan kebutuhan user. Software testing dalam
penelitian ini dilakukan menggunakan metode black box.
Menurut Ayuliana (2009) pengujian black-box adalah
Sebuah pengujian yang dilakukan dengan melihat dan mengamati
hasil dari pengeksekusian program serta memeriksa fungsi
perangkat lunak. Dapat dikatakan black-box adalah sebagai kotak

3
hitam yang dimana kita hanya melihat bagian luar tanpa
mengetahui isi dari kotak hitam tersebut. Hal ini memiliki
kesamaan dalam melakukan pengujian black-box, dimana
melakukan evaluasi dengan mengamati bagian luar atau interface-
nya saja tanpa melihat proses detail yang terjadi didalamnya.
B. Identifikasi Masalah
Berdasarkan latar belakang masalah yang telah diuraikan diatas
dapat diidentifikasi bahwa masalah pada penelitian yaitu perlunya
memastikan kelayakan fungsi terhadap aplikasi absensi secara menyeluruh.
C. Rumusan Masalah
Berdasarkan latar belakang masalah ini, rumusan masalah yang
akan dibahas adalah bagaimana persiapan pengujian dan cara melakukan
pengujian aplikasi Presensi menggunakan metode black-box testing.
D. Batasan Masalah
Pembatasan masalah digunakan agar menghindari perluasan topik
masalah agar penelitian lebih terarah dan mempermudah dalam
pembahasan sehingga mencapai tujuan penelitian. Berikut ini beberapa
batasan masalah penelitian ini sebagai berikut :
1. Penelitian membahas hasil pengujian aplikasi.
2. Pengujian aplikasi menggunakan metode black-box testing.
3. Aplikasi yang akan diuji adalah aplikasi Presensi.

4
4. Penggunaan metode dalam black box testing yang digunakan adalah
Equivalence Partitioning (Partisi Ekuivalensi) dan Boundary Value
Analysis (Analisis Nilai Batas).
E. Tujuan Penelitian
Tujuan yang diperoleh dari penelitian “Pengujian Aplikasi
Presensi Menggunakan Metode Black-box Testing” adalah melakukan
pengujian perangkat lunak dengan metode black-box testing terhadap
aplikasi Presensi untuk memastikan kelayakan dan kesalahan aplikasi,
sehingga memastikan meminimalisir kesalahan yang akan muncul ketika
penggunaan aplikasi.
F. Manfaat dan Kegunaan Penelitian
Manfaat yang diperoleh dari penelitian “Pengujian Aplikasi
Absensi Menggunakan Metode Black Box Testing” adalah :
1. Mengetahui apakah metode black box testing sesuai untuk pengujian
aplikasi Presensi.
2. Dapat mengetahui kelebihan dan kekurangan pada aplikasi Presensi.
3. Dapat meminimalisir error pada aplikasi sehingga error yang ada dapat
diselesaikan sebelum aplikasi diimplementasikan.

5
G. Metode Penelitian
1. Teknik Penelitian
Teknik penelitian yang dilakukan adalah kualitatif deskriptif
yaitu metode penelitian yang berlandaskan ada sumber referensi jurnal
guna menunjang penelitian yang dilakukan. Pengumpulan data
menggunakan instrumen penelitian dengan tujuan untuk mengacu
hipotesis yang telah ditetapkan (Sugiyono 2017:8).
2. Prosedur Penelitian
Dalam prosedur penelitian ini penulis melakukan beberapa
metode untuk diterapkan dalam penelitian ini diantaranya sebagai
berikut :
Gambar 1.1 Diagram Waterfall Metode Penelitian

6
a. Studi Literatur
Dalam studi literatur ini mempelajari buku-buku referensi, jurnal
penelitian, buku dan sumber lainnya yang sekiranya berkaitan
dengan masalah yang diteliti
b. Observasi
Sebelum melakukan pengujian perangkat lunak, diperlukan data
dan informasi yang lengkap dan menyeluruh mengenai perangkat
lunak yang akan diuji. Pada tahap ini akan dilakukan pengumpulan
data dan studi kasus.
c. Perencanaan Pengujian
Tahap awal dari pengujian perangkat lunak merupakan
perencanaan pengujian akan dilakukan. Tahap ini adalah
menentukan metode dan teknik pengujian terhadap aplikasi
Absensi
d. Pelaksanaan Pengujian
Pada tahap pelaksanaan pengujian ini akan dilakukan dengan
berdasarkan perencanaan yang berisi metode dan teknik yang
sudah disiapkan pada tahap sebelumnya.
e. Penulisan Laporan
Penulisan laporan adalah tahap akhir atas pengujian perangkat
lunak yang dimana berupa analisis laporan hasil pengujian yang
telah dilakukan.

7

H.  Jadwal Penelitian
Tabel 1.1 Jadwal Penelitian
|     | Bulan   | Bulan   | Bulan   | Bulan   | Bulan   |
| --- | ------- | ------- | ------- | ------- | ------- |
Jenis
|     | Ke- 1  | Ke-2  | Ke-3  | Ke-4  | Ke-5  |
| --- | ------ | ----- | ----- | ----- | ----- |
No.
Kegiatan
|        | 1  2  3  | 4  1  2  3  | 4  1  2  3  | 4  1  2  3  | 4  1  2  3  4  |
| ------ | -------- | ----------- | ----------- | ----------- | -------------- |
| Studi  |          |             |             |             |                |
1.
Literatur
|     |       |         |         |         |           |
| --- | ----- | ------- | ------- | ------- | --------- |
2.  Observasi
| Perencanaan  |       |         |         |         |           |
| ------------ | ----- | ------- | ------- | ------- | --------- |
3.
Pengujian
| Pelaksanaan  |       |         |         |         |           |
| ------------ | ----- | ------- | ------- | ------- | --------- |
4.
Pengujian
| Penulisan  |       |         |         |         |           |
| ---------- | ----- | ------- | ------- | ------- | --------- |
5.
Laporan

I.  Sistematis Penulisan Laporan
BAB I PENDAHULUAN
Dalam  bab  ini  dijelaskan  perihal  pembahasan  masalah  secara
umum meliputi latar belakang, identifikasi masalah,  rumusan masalah,
batasan  masalah,  tujuan  penelitian,  manfaat  dan  kegunaan  penelitian,
metode penelitian, jadwal penelitian, dan sistematika penulisan laporan.
BAB II TINJAUAN PUSTAKA
Bab ini memuat teori-teori yang mendukung dalam pengerjaan
tugas akhir. Pada bab ini dikemukakan definisi, teori  dan konsep yang
diperlukan  khususnya  teknik  black-box  dengan  metode  equivalence

8
partitioning dan boundary value analysis sebagai pustaka untuk membantu
penelitian.
BAB III ANALISIS DAN PERENCANAAN PENGUJIAN
Bab ini berisi rancangan pengujian aplikasi yang berisi pembuatan
test case dan pemilihan metode yang akan dilakukan pada pengujian
aplikasi.
BAB IV HASIL PENGUJIAN
Bab ini berisi hasil pengujian atau Testing dengan menggunakan
metodologi Black-box Testing. Hasil ini berguna untuk mengetahui kualitas
aplikasi presensi sesuai dengan kebutuhan yang telah ditentukan.
BAB V PENUTUP
Bab ini berisi kesimpulan dari penelitian yang sudah dilakukan,
saran yang bisa digunakan untuk pengembangan kasus uji black-box testing
dan daftar pustaka dari penelitian yang digunakan sebagai referensi.

DAFTAR PUSTAKA
Fatkhurrokhman, M. (2014). Analisis Pengujian Sistem Informasi Akademik
STMIK El Rahma Yogyakarta.
Kusuma, A. a. (2016). Implementasi Dan Pengujian Web E-Commerce Untuk
Produk Unggulan Desa.
M.Bachtiar, A., Dharmayanti, D., & S, M. K. (2007). Analisis Kualitas
Perangkat Lunak Terhadap Sistem Informasi. Majalah Ilmiah UNIKOM
Vol.11 No. 2, 224-233.
Murad, D. F., Kusniawati, N., & Asyanto, A. (2013). Aplikasi Intelligence
Website Untuk Penunjang Laporan PAUD Pada Himpaudi Kota
Tangerang. CCIT Journal, 7(1), 44-58.
Mustaqbal, M. S., Firdaus, R. F., & Rahmadi, H. (Jurnal Ilmiah Teknologi
Informasi Terapan Volume I, No 3, 10 Agustus 2015). PENGUJIAN
APLIKASI MENGGUNAKAN BLACK BOX TESTING BOUNDARY
VALUE ANALYSIS (Studi Kasus : Aplikasi Prediksi Kelulusan
SNMPTN). Jurnal Ilmiah Teknologi Informasi Terapan, 31-36.
Myers, G. J., Sandler, C., & Badgett, T. (2011). The Art of Software Testing.
NURSEHA, I. (IRVAN NURSEHA). PERANCANGAN SISTEM INFORMSI
QUALITY CONTROL STOCK EXPIRED DI PT. CATUR SENTOSA
ANUGERAH.
Sasmito, G. W. (2017). Penerapan Metode Waterfall Pada Desain Sistem
Informasi Geografis Industri Kabupaten Tegal. Jurnal
Informatika:Jurnal Pengembangan IT (JPIT) 2, 6-12.
Sergey, S. (2002). Software Testing: Black-box Techniques,.
Setiawan, G. W. (2011). PENGUJIAN PERANGKAT LUNAK
MENGGUNAKAN METODE BLACK BOX STUDI KASUS EXELSA
UNIVERSITAS SANATA DHARMA.
72

Umi, H., Alit, R., & Sugiarto, S. (2016). Penggunaan Metode Black-Box Pada
Pengujian Sistem Informasi Surat Keluar Masuk. 19-25.
William, L. (n.d.). Testing Overview and Black-box Testing Techniques. 2006.
William, P. (1995). Effective Methods for Software Testing. 3-430.
73