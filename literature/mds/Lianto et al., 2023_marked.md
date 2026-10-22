---
source_file: "Lianto et al., 2023.pdf"
source_sha256: "948b27d60a0e9b8f64f31e9c4c974d1d9f54a2a00cef42444c5958890d454ade"
page_count: 13
converted_at: "2026-10-21T11:00:08Z"
converter: "markitdown"
---

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
Evaluasi Functional Suitability, Performance Efficiency,
Usability, dan Portability Berdasarkan ISO 25010 pada Aplikasi
VR Gamelan Slenthem
M E Lianto*1, C H Primasari2, E Marsella3, Y P Wibisono4, M Cininta5
1,2,3,4 Program Studi Sistem Informasi, Universitas Atma Jaya Yogyakarta
5 Program Studi Arsitektur, Universitas Atma Jaya Yogyakarta
E-mail: mikoezra25@gmail.com1, clara.hetty@uajy.ac.id2,
elisabeth.marsella@uajy.ac.id3, priadi.wibisono@uajy.ac.id4, mutiara.cininta@uajy.ac.id5
Abstrak. Penelitian ini dilakukan dengan tujuan untuk menjamin kualitas dari aplikasi VR Gamelan
Slenthem agar menghindari error serta menjamin berjalannya seluruh fungsi yang terdapat di
dalamnya dengan menggunakan standar ISO 25010 selama pengujiannya. Aplikasi ini diharapkan
dapat menjadi sarana pembelajaran alat musik gamelan, khususnya slenthem. Pengujian dilakukan
pada 4 karakteristik berdasarkan pada standar ISO 25010 yaitu functional suitability, performance
efficiency, usability, serta portability. Berdasarkan pengujian yang telah dilakukan, aplikasi VR
Gamelan Slenthem ini dapat disimpulkan memenuhi standar ISO 25010 dengan nilai karakteristik
functional suitability 1 (baik), karakteristik usability 93% (sangat layak), karakteristik performance
efficiency 80% (layak), dan karakteristik portability yang baik. Hasil penelitian ini diharapkan dapat
menjadi rekomendasi dalam pengembangan selanjutnya demi meningkatkan kualitas aplikasi VR
Gamelan Slenthem.
Kata Kunci: evaluasi; kualitas; aplikasi; virtual reality; ISO 25010
Abstract. The aim of the research was to ensure the quality of VR Gamelan Slenthem application to
avoid errors and ensure the operation of all the functions in the application by using ISO 25010
standard. Hopefully, this application can be a learning tool for gamelan musical instruments,
especially slenthem. Testing was conducted using 4 characteristics of ISO 25010 that were
functional suitability, performance efficiency, usability, and portability. Based on the testing, VR
Gamelan Slenthem application can be concluded that it meets ISO 25010 standard with the
functional suitability characteristic of 1 (good), usability characteristic of 86.16% (excellent),
performance efficiency characteristic of 80% (adequate), and good portability characteristic. The
result of this study can be used as a recommendation for further development to improve the quality
of the VR Gamelan Slenthem application.
Keywords: evaluation; quality; application; virtual reality; ISO 25010
24

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
1. Pendahuluan
Seiring berkembangnya teknologi, beragam macam kegiatan sehari-hari memerlukan bantuan teknologi
seperti gawai. Hal ini memberikan banyak hal positif pada berbagai bidang, khususnya dalam kegiatan
pembelajaran yang sekarang banyak dilakukan secara daring sehingga pembelajaran dapat dilakukan di
mana saja dan kapan saja [1]. Namun, hal negatif juga dirasakan seiring berkembangnya teknologi dan
bukan hanya dampak positif saja yang dirasakan [2]. Masyarakat menjadi memiliki ketergantungan pada
gawai yang mempermudah kegiatan sehari-hari, sehingga generasi muda Indonesia akan kurang mengenal
budaya mereka sendiri.
Indonesia merupakan negara dengan beragam suku dan budaya yang tersebar di seluruh daerahnya.
Masing-masing daerah memiliki budaya dengan ciri khas tersendiri, contohnya dalam bidang musik seperti
Kulintang dari Sulawesi Utara, Tifa dari Maluku dan Papua, dan Gamelan yang berasal dari Jawa dan Bali
[3]. Alat musik gamelan sendiri dapat dijumpai di berbagai daerah di pulau Jawa, seperti sekolah, keraton,
serta gedung budaya. Sekolah-sekolah menggunakan gamelan sebagai salah satu pelajaran dalam kegiatan
seni budaya dalam pembelajaran, namun hal ini hanya terdapat di beberapa sekolah karena besarnya biaya
yang dibutuhkan untuk mendapatkan satu set gamelan.
Mahalnya biaya yang dibutuhkan untuk mendapatkan satu set gamelan menjadi kendala bagi
seseorang yang tertarik dan ingin mempelajari gamelan [4]. Hal ini berdampak juga bagi institusi
pendidikan yang menggunakan gamelan dalam kegiatan pembelajarannya dikarenakan terbatasnya jumlah
gamelan sangat mempengaruhi kualitas pembelajaran yang diterima pelajar.
Semakin bergantungnya aktivitas sehari-hari yang dilakukan masyarakat, khususnya bagi pelajar
yang telah menjalani kegiatan pembelajaran secara online terus-menerus. Inovasi sangat diperlukan untuk
menjaga kualitas pembelajaran sehingga dapat meningkatkan rasa antusias pelajar [5]. Penerapan media
pembelajaran baru yang lebih menarik bagi kalangan pelajar akan menjadi solusi bagi permasalahan ini.
Melalui teknologi Virual Reality (VR), simulasi imersif memungkinkan pengguna untuk berinteraksi dan
merasakan media pembelajaran dalam dunia virtual.
Virtual Reality sendiri merupakan teknologi yang dapat memunculkan gambar-gambar dalam
bentuk tiga dimensi yang tampak seperti benda nyata sehingga menciptakan perasaan seolah-olah
penggunanya berada di dalamnya [6], [7]. Penggunaan Virtual Reality membutuhkan adanya perangkat
memadai yang telah dirancang sedemikian rupa untuk tujuan tertentu, banyak perangkat yang dapat
menunjang pengalaman pengguna selama menggunakan Virtual Reality seperti dengan menggunakan
joysticks, data gloves, treadmills, ataupun motion tracker.
Keterbatasan-keterbatasan di atas dapat diatasi dengan adanya penerapan Virtual Reality selama
pembelajaran berlangsung. Kegiatan pembelajaran menjadi lebih efisien dan efektif dengan menerapkan
Virtual Reality dalam kegiatan pembelajaran [8], [9]. Permasalahan seperti keterbatasan dana untuk
menambah set gamelan serta kurangnya efisiensi waktu dapat terselesaikan. Hal ini juga diharapkan dapat
membuat generasi muda saat ini mengenal dan tertarik pada budaya tradisional yang dimiliki oleh Indonesia
dan kembali melestarikannya. Pembelajaran dengan menerapkan teknologi di dalamnya akan memberikan
kesan baru bagi para pelajar dan akan meningkatkan ketertarikan mereka karena kehidupan sehari-hari yang
sudah bergantung pada teknologi [10].
Seiring dengan penerapan teknologi pada kegiatan pembelajaran khususnya untuk kegiatan
pembelajaran alat musik gamelan. Perlu adanya jaminan bahwa pembelajaran menggunakan VR Gamelan
dapat berjalan secara efisien dan efektif. Hal ini dapat diatasi dengan melakukan evaluasi SQA atau
Software Quality Assurance pada aplikasi VR Gamelan. Aplikasi ini diharapkan dapat menjadi
rekomendasi dalam pengembangan aplikasi VR Gamelan untuk kedepannya. Penelitian ini bertujuan untuk
mengevaluasi standar dari aplikasi VR Gamelan sesuai dengan model ISO 25010, sehingga hasilnya dapat
dijadikan rekomendasi untuk pengembangan aplikasi ke depannya.
Model ISO 25010 merupakan standar internasional untuk evaluasi kualitas sistem dan perangkat
lunak. Standar ini telah melewati tiga pembaharuan pada 2007, 2011, dan 2017 [11]. Standar ini merupakan
hasil pembaharuan dari pengembangan model sebelumnya yaitu model ISO 9126. Jumlah karakteristik
25

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
menjadi pembeda antar model ISO 9126 dengan model ISO 25010, dalam ISO 9126 hanya terdapat enam
karakteristik sedangkan pada ISO 25010 terdapat delapan karakteristik di dalamnya. Adapun karakteristik
dari model ISO 25010 antara lain functional suitability, performance efficiency, compatibility, usability,
reliability, security, maintainability, dan portability.
ISO 25010 telah digunakan untuk menguji kualitas beberapas sistem. Penelitian aplikasi Menu
Harianku memperoleh nilai functional suitability sebesar 84,1%, performance efficiency sebesar 84%,
usability sebesar 83,5%, tingkat keamanan menengah untuk karakteristik security, dan karakteristik
portability dapat dijalankan dengan baik pada 6 desktop & browser mobile [12]. Website E-Office milik
PT. KAI (Persero) menghasilkan functional suitability sebagai karakteristik dengan presentase tertinggi
sebesar 88%, kemudian usability sebesar 87%, portability sebesar 83%, reliability sebesar 83%, security
sebesar 80%, performance efficiency sebesar 73%, dan yang terendah yaitu compatibility sebesar 72% [13].
Selain itu, penelitian aplikasi jasa transportasi Go-Jek menggunakan model ISO 25010 menyatakan bahwa
aplikasi Go-Jek telah memiliki kualitas yang baik dari segi kualitas produk dan kualitas penggunaan
ataupun perspektif pengguna [14].
Beberapa aspek tidak menjadi bahan pengujian oleh penulis seperti maintainability, security,
compatibility, dan reliability. Hal ini dikarenakan aspek maintainability tidak digunakan karena tujuan
dilakukannya penelitian hanya untuk mengevaluasi aplikasi dari sudut pandang pengguna, sedangkan
maintainability lebih berfokus ke bagian pengembang. Selain itu, aspek security tidak diteliti karena
aplikasi bersifat offline dan data yang tersimpan bersifat lokal. Compatibility, dan reliability belum dapat
diuji karena terbatasnya sarana yang dapat digunakan untuk pengujian aplikasi Virtual Reality.
2. Metodologi
Adapun tahap-tahap dalam melaksankan penelian dapat dilihat pada Gambar 1.
Gambar 1. Tahapan Penelitan
2.1. Studi Literasi
Merupakan tahapan pengumpulan data yang dilakukan oleh penulis dengan mencari informasi-informasi
terkait penelitan yang relevan dan terpercaya.
26

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
2.2. Menentukan Tujuan dan Metode
Menentukan tujuan merupakan tahapan yang dilakukan untuk menentukan tujuan peneliti dalam melakukan
penelitian ini, yaitu untuk mengetahui kualitas dari aplikasi VR Gamelan Slenthem berdasarkan standar
ISO 25010.
Berdasarkan standar ISO 25010 terdapat 8 karakteristik yang dapat dinilai dalam melakukan
pengujian kualitas suatu perangkat lunak yaitu functional suitability, performance efficiency, compatibility,
usability, relialibility, security, maintability, dan portability. Dalam penelitan ini peneliti berfokus pada
empat karakteristik yaitu functional suitability, performance efficiency, usability, dan portability.
2.2.1. Functional suitability
Functional suitability merupakan karakteristik terkait kesesuaian perangkat lunak dalam menjalankan
fungsi-fungsi yang terdapat di dalamnya dan kesesuaiannya dengan kebutuhan pengguna [15]. Adapun sub
karakteristik yang dimiliki functional suitability adalah sebagai berikut:
⚫ Functional Completeness merupakan ukuran suatu fungsi yang mampu berjalan sesuai dengan
semestinya tanpa ada hambatan sedikitpun.
⚫ Functional Correctness merupakan kemampuan suatu fungsi yang terdapat dalam perangkat
lunak untuk memenuhi kebutuhannya dengan tepat.
⚫ Functional Appropirateness merupakan kemampuan suatu fungsi yang mampu menuntaskan
suatu tugas secara layak serta sesuai dengan tujuan dari fungsi tersebut.
Adapun instrumen pengujian Functional Suitability dapat dilihat pada Tabel 1.
Tabel 1. Instrumen Pengujian Functional Suitability
No. Fitur yang diuji Langkah pengujian Hasil yang diharapkan
FS1 Play Buka aplikasi VR Gamelan. Menampilkan tampilan permainan
Klik play. gamelan.
FS2 Pengguna dapat mengkontrol
pergerakan kamera dengan
menggunakan controller.
FS3 Pengguna dapat melakukan interaksi
dengan pemukul seperti
menggenggam dan melepaskan
pemukul.
FS4 About Buka aplikasi VR Gamelan. Menampilkan tampilan menu about.
Klik about.
FS5 Tutorial Buka aplikasi VR Gamelan. Menampilkan tampilan menu tutorial.
Klik tutorial.
FS6 Sound Buka aplikasi VR Gamelan. Mengeluarkan bunyi ketika kita
Klik play. melakukan interaksi pada bilah
Berjalan ke arah Slenthem. gamelan dengan menggunakan
Ayunkan pemukul ke arah pemukul yang tersedia.
FS7 bilah. Bunyi yang dihasilkan sesuai dengan
Slenthem asli.
FS8 Bilah mengeluarkan suara setelah
bilah dipukul oleh pengguna.
2.2.2. Performance efficiency
Performance efficiency merupakan karakteristik yang mengukur tingkat kinerja relatif dari suatu sumber
daya dalam suatu sistem atau aplikasi yang digunakan dalam kondisi tertentu [15]. Performance efficiency
sendiri memiliki subkarakteristik sebagai berikut:
27

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
⚫ Time-behaviour adalah responsivitas waktu pengolahan serta hasil dari suatu sistem ketika
fungsinya dijalankan.
⚫ Resource Utilization digunakan untuk mengetahui terpenuhinya syarat-syarat ketika
menjalankan suatu fitur dengan mengukur sumber daya suatu sistem.
⚫ Capacity adalah sub karakteristik untuk mengukur parameter sistem dapat mencapai batasan
tertentu.
Adapun instrumen pengujian Performance Efficiency dapat dilihat pada Tabel 2.
Tabel 2. Instrumen Pengujian Performance Efficiency
No. Kriteria
PE1 Dengan adanya aplikasi VR Gamelan Slenthem, kegiatan
pembelajaran gamelan menjadi lebih mudah dibandingkan tanpa
adanya aplikasi VR Gamelan Slenthem.
PE2 Permasalahan seperti keterbatasan gamelan menjadi terselesaikan
dengan adanya aplikasi VR Gamelan Slenthem.
PE3 Proses pembelajaran gamelan menjadi lebih cepat dengan
menggunakan aplikasi VR Gamelan Slenthem.
PE4 Setiap proses yang terdapat pada aplikasi VR Gamelan Slenthem
memberi respon sesuai dengan fungsinya masing-masing.
PE5 Dengan adanya aplikasi VR Gamelan Slenthem, pengguna dapat
mempelajari gamelan dengan lebih mudah.
2.2.3. Usability
Usability merupakan karakteristik untuk mengukur sejauh apa suatu perangkat lunak mampu digunakan
oleh pengguna dalam upaya mencapai tujuan tertentu dengan berfokus pada usefulness, ease of use, ease of
learn, dan satisfaction [15]. Adapun instrumen pengujian Usability dapat dilihat pada Tabel 3.
Tabel 3. Instrumen Pengujian Usability
No. Kriteria
Usefulness
U1 Aplikasi VR Gamelan Slenthem membantu saya menjadi lebih efektif
dalam pembelajaran gamelan.
U2 Aplikasi VR Gamelan Slenthem membantu saya menjadi lebih
produktif dalam pembelajaran gamelan.
U3 Aplikasi VR Gamelan Slenthem sangat bermanfaat.
U4 Aplikasi VR Gamelan Slenthem membantu saya terhadap tugas yang
saya lakukan.
U5 Aplikasi VR Gamelan Slenthem membuat hal-hal yang ingin saya
capai lebih mudah untuk dilakukan.
U6 Aplikasi VR Gamelan Slenthem menghemat waktu saya dalam
pembelajaran gamelan.
U7 Aplikasi VR Gamelan Slenthem sesuai dengan kebutuhan saya.
U8 Aplikasi VR Gamelan Slenthem bekerja sesuai apa yang saya
harapkan.
Ease of Use
U9 Aplikasi VR Gamelan Slenthem mudah digunakan.
U10 Aplikasi VR Gamelan Slenthem praktis untuk digunakan.
U11 Aplikasi VR Gamelan Slenthem mudah untuk dipahami.
28

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
No. Kriteria
U12 Langkah-langkah penggunaan aplikasi VR Gamelan Slenthem
praktis.
U13 Aplikasi VR Gamelan Slenthem dapat disesuaikan dengan kebutuhan.
U14 Saya tidak mengalami kesulitan saat menggunakan aplikasi VR
Gamelan Slenthem.
U15 Saya dapat menggunakan aplikasi VR Gamelan Slenthem tanpa
instruksi tertulis.
U16 Saya tidak melihat adanya ketidak konsistenan selama menggunakan
aplikasi VR Gamelan Slenthem.
U17 Pengguna yang jarang maupun rutin menggunakan akan menyukai
aplikasi VR Gamelan Slenthem.
U18 Saya dapat mengatasi kesalahan ketika menggunakan aplikasi VR
Gamelan Slenthem dengan cepat dan mudah.
U19 Saya dapat menggunakan aplikasi VR Gamelan Slenthem dengan
berhasil setiap kali saya menggunakannya.
Ease of Learning
U20 Saya belajar menggunakan aplikasi VR Gamelan Slenthem dengan
cepat.
U21 Saya dapat mengingat cara menggunakan aplikasi VR Gamelan
Slenthem dengan mudah.
U22 Saya dapat dengan mudah memahami cara penggunaan aplikasi VR
Gamelan Slenthem.
U23 Saya dapat dengan cepat terampil menggunakan aplikasi VR
Gamelan Slenthem.
Satisfaction
U24 Saya puas dengan aplikasi VR Gamelan Slenthem.
U25 Saya akan merekomendasikan aplikasi VR Gamelan Slenthem ke
teman.
U26 Aplikasi VR Gamelan Slenthem menyenangkan untuk digunakan.
U27 Aplikasi VR Gamelan Slenthem bekerja sesuai dengan keinginan
saya.
U28 Aplikasi VR Gamelan Slenthem sangat bagus.
U29 Saya perlu memiliki aplikasi VR Gamelan Slenthem untuk membantu
kegiatan pembelajaran gamelan.
U30 Aplikasi VR Gamelan Slenthem nyaman untuk digunakan.
2.2.4. Portability
Portability merupakan karakteristik untuk mengetahui keandalan perangkat lunak ketika dipindahkan dari
suatu perangkat keras ke perangkat keras lainnya [15]. Portability sendiri terbagi menjadi 3 sub karakteristik
yaitu adaptability, installability, dan replaceability.
2.3. Pengambilan Data
Dalam tahap ini, peneliti melakukan pengambilan data dengan memanfaatkan kuesioner. Adapun teknik
yang digunakan selama proses pengambilan data antara lain sebagai berikut.
29

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
2.3.1. USE Questionnaire
Terdapat 30 pernyataan yang terbagi dalam 4 parameter dalam USE Questionnaire. Pernyataan-pernyataan
tersebut digunakan untuk mewakili penilaian saat pengguna menggunakan aplikasi tersebut [16], [17].
Kuesioner ini terbagi menjadi 4 kriteria, yaitu usefulness untuk mengukur appropriateness recognisability,
ease of use untuk mengukur accessability dan user error protection, ease of learning untuk mengukur
learnability, dan satisfaction untuk mengukur user interface aesthetics. Jumlah pengguna aplikasi VR
Gamelan Slenthem untuk saat ini adalah 30 pengguna dan untuk responden yang dipilih untuk mengisi data
kuesioner dalam penelitian adalah seluruh pengguna yang melakukan pengujian terhadap aplikasi VR
Gamelan Slenthem yaitu 30 pengguna.
2.3.2. Skala Likert
Sugiyono [18] menjelaskan bahwa skala Likert digunakan untuk mengukur bagaimana sikap, pendapat,
serta persepsi seseorang tentang suatu fenomena sosial. Skala Likert menghasilkan jawaban seperti “Sangat
Setuju”; “Setuju”; “Netral”; “Tidak Setuju”; “Sangat Tidak Setuju”. Berikut rumus perhitungan dalam
pengujian performance efficiency dan usability (1):

𝑆𝑘𝑜𝑟𝑡𝑜𝑡𝑎𝑙 = (𝐽𝑆𝑆 𝑥 5)+(𝐽𝑆 𝑥 4)+(𝐽𝑁 𝑥 3)+(𝐽𝑇𝑆 𝑥 2)+(𝐽𝑆𝑇𝑆 𝑥 1) (1)
Di mana:
JSS = jumlah responden dengan jawaban sangat setuju.
JS = jumlah responden dengan jawaban setuju.
JN = jumlah responden dengan jawaban netral.
JTS = jumlah responden dengan jawaban tidak setuju.
JSTS = jumlah responden dengan jawaban sangat tidak setuju.
Hasil yang didapatkan dari kuesioner akan dihitung melalui analisis deskriptif dengan perhitungan dari
skor jawaban menggunakan persamaan (2).
𝑆𝑘𝑜𝑟𝑡𝑜𝑡𝑎𝑙 (2)
𝐾𝑒𝑙𝑎𝑦𝑎𝑘𝑎𝑛 (%)=
𝑆𝑘𝑜𝑟 𝑦𝑎𝑛𝑔 𝑑𝑖ℎ𝑎𝑟𝑎𝑝𝑘𝑎𝑛
Kemudian nilai kelayakan yang didapatkan akan disimpulkan menjadi nilai kualitatif sesuai dengan
interpretasi skala Likert pada Tabel 4 di bawah ini.
Tabel 4. Standar Kelayakan
No Presentase Kesimpulan
1 0% - 20% Sangat Kurang Layak
2 21% - 40% Kurang Layak
3 41% - 60% Cukup Layak
4 61% - 80% Layak
5 81% - 100% Sangat Layak
30

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
2.3.3. Skala Guttman
Penggunaan skala Guttman ini dilakukan dengan menggunakan hasil uji coba terhadap aplikasi yang
dilakukan oleh responden. Penggunaan skala ini akan menghasilkan jawaban yang tegas berupa “ya-tidak”;
“benar-salah”; “berhasil-gagal” dan lain-lain [19]. Hasil pengujian yang didapatkan akan diolah
menggunakan rumus dari matriks Feature Completeness [20]. Adapun rumus untuk menghitung feature
completeness adalah seperti berikut (3).
(3)
𝐼
𝑋 =
𝑃
Di mana:
I = Jumlah fungsi yang berhasil diimplementasikan
P = Jumlah fungsi yang dirancang
2.4. Analisis Data
Pada tahapan penulis melakukan analisis terhadap data yang telah didapatkan sebelumnya, dan memberi
kesimpulan terkait validitas serta reliabilitas data yang didapatkan sehingga mengetahui kelayakan data
untuk digunakan lebih lanjut. Adapun teknik yang digunakan selama menganalisis data antara lain sebagai
berikut.
2.4.1. Uji Validitas
Pengujian validitas untuk menemukan kekuatan dari hubungan antar variabel yang telah diuji dilakukan
dengan menggunakan korelasi Pearson yang menjadi syarat dalam pengujian analisis faktor ataupun
analisis komponen utama (Principal Component Analysis) [21].
Pedoman yang digunakan selama proses uji validitas ini adalah jika nilai r hitung > r tabel, maka
variabel pernyataan atau pertanyaan dalam kuesioner akan dinyatakan valid, namun jika r hitung < r tabel,
maka variabel pernyataan atau pertanyaan akan dinyatakan tidak valid. Nilai r tabel yang didapatkan dengan
jumlah responden sebanyak 30 dengan nilai signifikansi sebesar 0,05 adalah 0,361.
2.4.2. Uji Reliabilitas
Pengujian reliabilitas dilakukan dengan tujuan untuk menguji nilai koefisien yang dimiliki oleh setiap
variabel pernyataan atau pertanyaan dalam kuesioner dengan berdasarkan pada nilai Alpha’s Cronbach atau
alpha coeficient yang dimulai dari rentang 0 (tanpa reliabilitas) hingga rentang 1 (reliabilitas sempurna).
Berdasarkan ketentuan para ahli [21], nilai koefisien alpha adalah sebagai berikut:
1. Jika nilai reliabilitas = 0, maka variabel pernyataan atau pertanyaan dinyatakan tidak memiliki
reliabilitas (no reliability).
2. Jika nilai reliabilitas > 0.70, maka variabel pernyataan atau pertanyaan dinyatakan memiliki
reliabilitas yang dapat diterima (acceptable reliability).
3. Jika nilai reliabilitas > 0.80, maka variabel pernyataan atau pertanyaan dinyatakan memiliki
reliabilitas baik (good reliability).
4. Jika nilai reliabilitas > 0.90, maka variabel pernyataan atau pertanyaan dinyatakan memiliki
reliabilitas sangat baik (excellent reliability).
5. Jika nilai reliabilitas = 1, maka variabel pernyataan atau pertanyaan dinyatakan memiliki
reliabilitas sempurna (perfect reliability).
3. Hasil dan Pembahasan
3.1. Functional Suitability
Berdasarkan pengujian pada karakteristik functional suitability yang dilakukan oleh 30 pengguna sehingga
menghasilkan data sesuai pada Tabel 5.
31

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023

Tabel 5. Hasil Pengujian Functional Suitability
|     | No.  | Fitur yang diuji  |     |     | Berhasil  | Gagal  |     |
| --- | ---- | ----------------- | --- | --- | --------- | ------ | --- |
|     | FS1  | Play              |     |     | 30        |        | 0   |
|     | FS2  |                   |     |     | 30        |        | 0   |
|     | FS3  |                   |     |     | 30        |        | 0   |
|     | FS4  | About             |     |     | 30        |        | 0   |
|     | FS5  | Tutorial          |     |     | 30        |        | 0   |
|     | FS6  | Sound             |     |     | 30        |        | 0   |
|     | FS7  |                   |     |     | 30        |        | 0   |
|     | FS8  |                   |     |     | 30        |        | 0   |

Hasil yang terdapat pada Tabel 5 menjelaskan bahwa fitur-fitur yang telah diuji dapat berhasil
dilaksanakan oleh seluruh pengguna aplikasi VR Gamelan Slenthem. Dengan menggunakan persamaan (3)
maka akan memperoleh nilai rata-rata X yaitu 1 yang artinya fitur-fitur yang terdapat dalam aplikasi ini
berjalan 100% dari hasil yang diharapkan.

3.2. Performance Efficiency
Berdasarkan hasil uji validitas terhadap data yang didapatkan dari kuesioner yang diisi oleh 30 pengguna,
variabel  dari  karakteristik  performance  efficiency  yang  valid  yaitu:  PE1,  PE2,  PE3,  PE4  dan  PE5
memperoleh nilai r hitung > r tabel sehingga validitas dari seluruh data performance efficiency dianggap
valid.
Berdasarkan hasil uji reliabilitas terhadap variabel yang telah diuji validitasnya, variabel dalam
karakteristik performance efficiency memiliki nilai cronbach’s alpha 0.767 yang artinya reliabilitas dari
data yang didapatkan dapat diterima (acceptable reliability).

Tabel 6. Hasil Pengujian Performance Efficiency
|     |     | Variabel  | STS  | TS  | N  S   | SS  |     |
| --- | --- | --------- | ---- | --- | ------ | --- | --- |
|     |     | PE1       | 1    | 0   | 5      | 8   | 16  |
|     |     | PE2       | 0    | 4   | 4      | 9   | 13  |
|     |     | PE3       | 0    | 3   | 2      | 6   | 19  |
|     |     | PE4       | 1    | 5   | 7      | 6   | 11  |
|     |     | PE5       | 0    | 6   | 3  15  |     | 6   |

Skor yang diharapkan dari setiap variabel performance efficiency adalah 150 yang didapatkan jika
seluruh pengguna  mengisi  kuesioner  dengan  poin 5.  Pengujian  karakteristik  performance efficiency
dilakukan dengan menggunakan persamaan (2).  Tabel 6 menunjukkan hasil pengujian performance
efficiency. Secara keseluruhan, presentase kelayakan pada karakteristik performance efficiency adalah
80,26% berdasarkan perhitungan per parameter yang mana jika dibulatkan menjadi 80% dan dapat
diinterpretasikan layak sesuai dengan standar kelayakan di Tabel 4. Adapun hasil pengukuran presentase
nilai kelayakan performance efficiency dapat dilihat pada Tabel 7.

Tabel 7. Parameter Hasil Presentase Karakteristik Performance Efficiency
| Variabel  |     | Skor total  | Skor yang diharapkan  |      |            |     | Presentase  |
| --------- | --- | ----------- | --------------------- | ---- | ---------- | --- | ----------- |
| PE1       |     | 128         |                       | 150  |            |     | 85.33%      |
| PE2       |     | 121         |                       | 150  |            |     | 80.66%      |
| PE3       |     | 131         |                       | 150  |            |     | 87.33%      |
| PE4       |     | 111         |                       | 150  |            |     | 74%         |
| PE5       |     | 111         |                       | 150  |            |     | 74%         |
|           |     |             |                       |      | Rata-rata  |     | 80.26%      |
32

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023

3.3. Usability
Pengujian dilakukan oleh 30 orang yang telah menggunakan aplikasi VR Gamelan Slenthem sebelumnya,
data-data yang didapatkan tersebut kemudian diuji validitas serta reliabilitas dari data tersebut.
Berdasarkan hasil uji validitas, variabel dari karakteristik functional suitability yang valid yaitu:
U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11, U12, U13, U14, U15, U18, U20, U21, U22, U23, U24,
U25, U26, U27, U28, U29, U30. Variabel U16, U17, dan U19 sendiri dinyatakan tidak valid dikarenakan
nilai r hitung < r tabel sehingga variabel tersebut tidak akan diuji reliabilitasnya.
Berdasarkan hasil uji reliabilitas terhadap variabel yang telah diuji validitasnya, variabel dalam
karakteristik usability memiliki nilai cronbach’s alpha 0.932 yang artinya reliabilitas dari data yang
didapatkan adalah sangat baik (excellent reliability).
Pengujian  pada  karakteristik  usability  dilakukan  dengan  memanfaatkan  USE  Questionnaire
berisikan 30 pertanyaan terkait usabilitas pada aplikasi VR Gamelan Slenthem yang dilakukan oleh 30
pengguna, namun hanya 27 pertanyaan yang akan dihitung berdasarkan hasil uji validitas dan reliabilitas
yang telah dilakukan. Pengisian kuesioner dengan rentang jawaban 1 hingga 5 berdasarkan pertanyaan
positif yaitu STS=1; TS=2; N=3; S=4; dan SS=5. Hasil pengujian usability dapat dilihat pada Tabel 8.

Tabel 8. Hasil Pengujian Usability
| No.  Variabel  | Aspek             | STS  TS  | N  S   | SS  |
| -------------- | ----------------- | -------- | ------ | --- |
| 1  U1          | Usefulness        | 1  0     | 5  8   | 16  |
| 2  U2          |                   | 0  4     | 4  9   | 13  |
| 3  U3          |                   | 0  3     | 2  6   | 19  |
| 4  U4          |                   | 1  5     | 7  6   | 11  |
| 5  U5          |                   | 0  6     | 3  15  | 6   |
| 6  U6          |                   | 3  0     | 4  6   | 17  |
| 7  U7          |                   | 3  5     | 3  14  | 5   |
| 8  U8          |                   | 1  1     | 5  15  | 8   |
| 9  U9          | Ease of Use       | 2  1     | 4  15  | 8   |
| 10  U10        |                   | 2  1     | 3  8   | 17  |
| 11  U11        |                   | 2  1     | 3  8   | 16  |
| 12  U12        |                   | 0  6     | 2  16  | 6   |
| 13  U13        |                   | 0  0     | 1  9   | 20  |
| 14  U14        |                   | 0  5     | 1  7   | 17  |
| 15  U15        |                   | 3  1     | 2  9   | 15  |
| 16  U18        |                   | 2  2     | 3  14  | 9   |
| 17  U20        | Ease of Learning  | 0  2     | 1  6   | 21  |
| 18  U21        |                   | 0  0     | 2  9   | 19  |
| 19  U22        |                   | 0  0     | 4  6   | 22  |
| 20  U23        |                   | 0  2     | 6  8   | 14  |
| 21  U24        | Satisfaction      | 0  3     | 3  7   | 17  |
| 22  U25        |                   | 1  3     | 2  10  | 14  |
| 23  U26        |                   | 0  1     | 3  9   | 17  |
| 24  U27        |                   | 0  4     | 4  16  | 6   |
| 25  U28        |                   | 0  0     | 3  8   | 19  |
| 26  U29        |                   | 1  0     | 5  5   | 19  |
| 27  U30        |                   | 1  4     | 2  16  | 7   |

Skor yang diharapkan dari setiap variabel usability adalah 135 yang didapatkan jika seluruh
pengguna  mengisi  kuesioner  dengan  poin  5.  Pengujian  karakteristik  usability  dilakukan  dengan
menggunakan persamaan (2). Secara keseluruhan, presentase kelayakan pada karakteristik usability adalah
33

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
92,55% berdasarkan perhitungan per parameter yang mana jika dibulatkan menjadi 93% dan dapat
diinterpretasikan sangat layak sesuai dengan standar kelayakan di tabel 4. Adapun hasil pengukuran
presentase nilai kelayakan usability dapat dilihat pada Tabel 9.
Tabel 9. Parameter Hasil Presentase Karakteristik Usability
No. Parameter Skor Skor yang Presentase
Total diharapkan
1 Usefulness 947 1080 87,68%
2 Ease of Use 982 1080 90,92%
3 Ease of Learning 533 540 98,70%
4 Satisfaction 878 945 92,91%
Rata-rata 92,55%
3.4. Portability
Pengujian portability dilakukan dengan menggunakan dua perangkat berbeda untuk mengetahui
kemampuan perangkat dalam menjalankan aplikasi VR Gamelan Slenthem. Pengujian dilakukan pada
perangkat Occulus Quest 2, dan juga pada perangkat HP Reverb G2. Adapun hasil pengujian dari aspek
portability dapat dilihat pada Tabel 10.
Tabel 10. Hasil Pengujian Portability
No. Perangkat Adaptability Installability Replaceability
1 Occulus Quest 2 Berjalan baik Berjalan baik Berjalan baik
OS: Android 10
SoC: Qualcomm Snapdragon XR2
Memory: 6 GB LPDDR4X
Display: 1832 x 1920
Refresh Rate: 90 Hz
2 HP Reverb G2 PC-VR Berjalan baik Berjalan baik Berjalan baik
OS: Windows 10 64-bit
Processor: Intel i5 12400f
Memory: 16 GB
Display: 2160 x 2160
Refresh Rate: 90 Hz
Berdasarkan pengujian terhadap karakteristik functional suitability yang dilakukan oleh 30
pengguna untuk mengetahui kesesuaian fungsi yang terdapat dalam aplikasi VR Gamelan Slenthem
memperoleh keluaran nilai X berupa feature completeness dengan nilai 1 yang artinya aplikasi VR Gamelan
Slenthem memiliki fitur-fitur yang sesuai dengan ekspektasi.
Pengujian yang dilakukan terhadap karakteristik performance efficiency mendapatkan hasil jika
aplikasi VR Gamelan Slenthem memiliki tingkat performa yang layak yaitu sebesar 80% dan sesuai dengan
standar ISO 25010.
Pengujian terhadap karakteristik usability membuktikan kalau aplikasi VR Gamelan Slenthem
dapat digunakan dengan mudah oleh pengguna, hal ini terbukti dari didapatkannya nilai rata-rata presentase
kelayakan sebesar 93% dan dapat diinterpretasikan “sangat layak” serta sesuai dengan standar ISO 25010.
Menurut pengguna, yang mana mereka telah sering memainkan gamelan, aplikasi ini tergolong mudah
untuk digunakan. Namun menurut mereka, pengguna yang jarang atau bahkan belum pernah memainkan
gamelan akan mengalami kesulitan dalam menggunakan aplikasi ini secara mandiri. Hal ini dikarenakan
kurangnya informasi yang diberikan dalam menu “Tutorial” yang hanya memberikan contoh lagu yang
dapat dimainkan dan belum terdapat penjelasan terkait urutan bilah yang terdapat dalam slenthem.
34

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
Pada pengujian yang dilakukan terhadap karakteristik portability menghasilkan data berupa
aplikasi VR Gamelan Slenthem dapat berjalan dengan baik meskipun dijalankan pada perangkat berbeda,
baik Occulus Quest 2 maupun HP Reverb G2 PC-VR. Berdasarkan hasil tersebut, karakteristik portability
dapat dikatakan telah memenuhi standar ISO 25010.
4. Kesimpulan
Aplikasi VR Gamelan Slenthem telah diuji dan memenuhi standar ISO 25010 pada aspek: (1)Functional
suitability menyatakan seluruh fitur dan fungsi yang terdapat dalam aplikasi VR Gamelan Slenthem dapat
berjalan dengan lancar; (2)Performance efficiency menyatakan aplikasi membantu pengguna dalam
melakukan aktivitas pembelajaran gamelan secara mudah dan cepat, dan didukung dengan presentase
kelayakan sebesar 80% dengan interpretasi layak; (3)Usability menyatakan pengguna dapat dengan mudah
menggunakan aplikasi VR Gamelan Slenthem, dan didukung dengan presentase kelayakan sebesar 93%
dengan interpretasi sangat layak; (4)Portability menyatakan aplikasi dapat berjalan dengan baik tanpa
adanya error ketika dijalankan pada perangkat keras yang berbeda. Aplikasi VR Gamelan Slenthem ini
diharapkan untuk ke depannya dapat terus dikembangkan agar dapat menjadi aplikasi yang lebih baik lagi
supaya dapat digunakan sebagai solusi alternatif dalam pembelajaran gamelan khususnya untuk alat musik
slenthem.
5. Ucapan Terima Kasih
Puji syukur serta banyak terima kasih penulis sampaikan atas dukungan serta diskusi yang diberikan oleh
civitas akademika Universitas Atma Jaya Yogyakarta, Institut Seni Indonesia (ISI), dan pelatih UKM
Paskawijaya. Ucapan terima kasih juga penulis berikan untuk Kementerian Pendidikan, Budaya, Riset, dan
Teknologi (Kemendikbudristek) atas hibah Kedaireka Matching Fund dengan nomor SK
0540/E/KS.06.02/2022 yang telah mendukung proyek ini.
Referensi
[1] E. S. Soegoto, & C. Chandra, “Building Concept of High School Information Technology,” IOP
Conference Series: Materials Science and Engineering, 407(1), pp. 012022, 2018.
[2] S. A. Bhat, “The Positive and Negative Impact of New Technology on Accelerated Learning during
Covid-19 Pandemic,” International Journal of Applied Research, 2021.
[3] A. Harista, S. R. U. Aldo Sompie, S. D. E. Paturusi, “Learning Application for Introduction of Javanese
Gamelan Musical Instruments Based on Android Platform,” Jurnal Teknik Informatika, vol. 17, no. 1,
Januari-Maret 2022.
[4] F. G. Purnomo, “Pengaruh Kualitas Produk, Persepsi Harga Dan Promosi Terhadap Keputusan
Pembelian Produk Gamelan Siswosumartan Di Surakarta,” Skripsi thesis, Universitas Muhammadiyah
Surakarta, 2022.
[5] D. Allcoat, T. Hatchard, F. Azmat, “Education in the Digital Age: Learning Experience in Virtual and
Mixed Realities,” Journal of Educational Computing Research, vol. 59, no. 5, 2021.
[6] F. T. Moura, “Telepresence: The Extraordinary Power of Vitual Reality,” musicstats.org, 2017.
[7] M. Melatti and K. Johnsen, “Virtual Reality mediated instruction and learning,” 2017 IEEE Virtual
Reality Workshop on K-12 Embodied Learning through Virtual & Augmented Reality (KELVAR).
IEEE, 2017.
[8] G. A. Farsi, A. B. M. Yusof, A. Romli, “A Review of Virtual Reality Applications in Educational
Domain,” International Journal of Interactive Mobile Technologies, vol. 15, no. 22, 2021.
[9] A. R. Srinivasa, R. Jha, T. Ozkan, Z. Wang, “Virtual reality and its role in improving student
knowledge, self-efficacy, and attitude in the materials testing laboratory,” International Journal of
Mechanical Engineering Education, vol. 49, no. 4, 2021.
35

KONSTELASI: Konvergensi Teknologi dan Sistem Informasi
Vol.3 No.1, Juni 2023
[10] G. A. Farsi, A. B. M. Yusof, W J. B. Fauzi, “The Practicality of Virtual Reality Applications in
Education: Limitations and Recommendations,” Journal of Hunan University (Natural Sciences), vol.
48, no. 7, 2021.
[11] N. F. Naini, S. Santoso, T. S. Andriani, U. Claudia, Nurfadillah, “The Effect of Product Quality,
Service Quality, Customer Satisfaction on Customer Loyalty,” Journal of Consumer Sciences, 2022.
[12] D. A. Suryadi, E. Sulistiyani, “Evaluation of Information Quality Using ISO/IEC 25010:2011 (Case
Research: Menu Harianku Application),” International Journal of Innovation in Enterprise System,
vol. 06, no. 02, pp. 119-132, 2022.
[13] E. Saputra, L. Y. Banowosari, “Quality Analysis of E-Office Application PT. KAI (Persero) Use
Method ISO 25010,” International Research Journal of Advanced Engineering and Science, vol. 6,
issue 1, pp.96-100, 2021.
[14] M. Izzatillah, “Quality Measurement of Transportation Servis Application Go-Jek Using ISO 25010
Quality Model,” Jurnal SIMETRIS, vol. 10, no. 1, 2019.
[15] E. Peters, G. K. Aggrey, “An ISO 25010 Based Quality Model for ERP Systems,” Advances in
Science, Technology and Engineering Systems Journal, vol 5, no. 2, 578-583, 2020.
[16] Y. S. M. Putra and R. Tanamal, “Analisis Usability Menggunakan Metode USE Questionnaire Pada
Website Ciputra Enterprise System,” Teknika, 2020.
[17] E. S. Rahman and D. Vitalocca, “Analisis Usabilitas Menggunakan Use Questionnaire Pada Sistem
Informasi SMK Negeri 3 Makassar,” J. Mekom, 2018.
[18] R. Firmansyah, “Usability Testing dengan USE Questionnaire pada Aplikasi SIPOLIN Provinsi Jawa
Barat,” Swabumi, 2018.
[19] Sugiyono, “Metode Penelitian Research and Development,” Bandung: Alfabeta, 2015.
[20] A. Anal, S. Devadatta, “Assessing the Quality of M-Learning System using ISO/IEC 25010,”
International Journal of Advanced Computer Research, vol. 3, no. 3, 2013.
[21] D. Budiastuti, A. Bandur, “Validitas dan Reliabilitas Penelitian, Dilengkapi Analisis dengan NVIVO,
SPSS, dan AMOS,” Jakarta: Mitra Wacana Media, 2018.
36