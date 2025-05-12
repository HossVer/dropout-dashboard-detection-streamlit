# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Background
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini, ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

## Business Understanding
Perusahaan aya Jaya Institut yang fokus pada penyediaan layanan pendidikan berbasis teknologi mengalami masalah dalam tingkat dropout mahasiswa. Oleh karena itu, sistem yang dikembangkan bertujuan untuk menganalisis dan memprediksi kemungkinan dropoutmahasiswa berdasarkan data yang ada.

### Permasalahan Bisnis
Permasalahan utama yang ingin diselesaikan adalah menurunkan tingkat dropout mahasiswa dengan mendeteksi siswa yang mungkin akan melakukan dropout agar dapat sgera mendapat bimbingan khusus. Penyelesaian masalah ini dilakukan menggunakan menggunakan data analitik dan machine learning yaitu model deteksi dengan menggunakan data dari mahasiswa terdahulu yang telah lulus ataupun yang melakukan dropout.

### Cakupan Proyek
Proyek ini mencakup pengembangan dashboard analitik yang digunakan untuk menganalisis faktor-faktor yang mempengaruhi tingkat dropout mahasiswa, serta pembuatan model machine learning untuk memprediksi kemungkinan dropout. Juga pembuatan prototipe deteksi dropout.

### Persiapan

Sumber data: Dataset yang berisi data mahasiswa yang telah dilengkapi dengan status kelulusan (lulus/tidak lulus).

Setup environment:


### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md

Setup environment:
Install Streamlit
pip install streamlit

Install TensorFlow
pip install tensorflow

Install Pandas
pip install pandas

Install Matplotlib
pip install matplotlib

Install scikit-learn
pip install scikit-learn

## Business Dashboard
Dashboard bisnis yang telah dibuat memberikan wawasan tentang tingkat dropout mahasiswa berdasarkan berbagai faktor, termasuk usia saat pendaftaran, status debitor, dan hasil akademik. Dashboard ini juga memperlihatkan persentase dropout di antara  mahasiswa.

Dashboard ini dapat diakses melalui link berikut:
[Dashboard Business Tableau](https://public.tableau.com/app/profile/hosea.verico.dwi.kristianto/viz/JayaJayaInstituteDropoutAnalysis/DropoutParameterDashboard)

## Menjalankan Sistem Machine Learning
Sistem machine learning yang dikembangkan untuk memprediksi kemungkinan dropout mahasiswa berbasis pada data yang ada. Aplikasi ini memanfaatkan model TensorFlow untuk melakukan prediksi, menggunakan fitur-fitur seperti usia, status beasiswa, status debitor, dan lainnya.

Untuk menjalankan prototype sistem machine learning:
1. Pastikan kamu telah mengonfigurasi lingkungan dengan benar (lihat bagian Persiapan).
2. Jalankan aplikasi dengan perintah: streamlit run app.py

Model akan memproses data mahasiswa yang diunggah dan memberikan prediksi apakah seorang mahasiswa berpotensi untuk dropout atau tidak.

Prototype dapat diakses di Streamlit melalui link berikut:
[Deploy Streamlit App](https://dropout-dashboard-detection-app-dwp4dhbdgztu5sscgtjtf6.streamlit.app/)

## Conclusion
Proyek ini berhasil mengembangkan dashboard analitik yang memberikan wawasan yang jelas tentang faktor-faktor yang mempengaruhi dropout yaitu faktor atau variabel sebagai berikut:
        "Tuition_fees_up_to_date",
        "Scholarship_holder",
        "Application_mode",
        "Debtor",
        "Age_at_enrollment",
        "Curricular_units_1st_sem_enrolled",
        "Curricular_units_1st_sem_approved",
        "Curricular_units_1st_sem_grade",
        "Curricular_units_2nd_sem_enrolled",
        "Curricular_units_2nd_sem_approved",
        "Curricular_units_2nd_sem_grade",
variabel variabel tersebut terbukti berpengaruh besar pada hasil akhir seorang mahmasiswa apakah mereka mampu lulus atau akan melakukan dropout di tengah studinya. hal ini juga didukung dengan pengembangan model deteksi berbasis deep learning yang mendapatkan hasil akurasi sebesar 88% pada data training dan testing. data testing didapat dari memisahkan mahasisw dengan status enrolled menjadi sebuah dataframe terpisah: 
https://github.com/HossVer/dropout-dashboard-detection-streamlit/blob/main/df_test.csv


### Rekomendasi Action Items
Recommendation Action Items:
1. Penyediaan Beasiswa untuk Mahasiswa Berpotensi Dropout
Berdasarkan data di dashboard, terdapat tren yang menunjukkan bahwa status keuangan (seperti Debtor) mempengaruhi tingkat dropout mahasiswa. Oleh karena itu, salah satu langkah yang dapat diambil adalah menambah jumlah beasiswa untuk mahasiswa yang kesulitan secara finansial. Mengidentifikasi mahasiswa yang memiliki risiko tinggi untuk dropout dan menawarkan program beasiswa atau bantuan keuangan untuk membantu mereka tetap melanjutkan pendidikan.

2. Program Bimbingan Akademik
Dari data Curricular Units Enrolled dan Approved, terlihat bahwa mahasiswa yang memiliki kinerja akademik rendah atau gagal menyelesaikan mata kuliah cenderung memiliki risiko lebih tinggi untuk dropout. Oleh karena itu, disarankan untuk menyediakan program bimbingan akademik atau kelas remedial untuk mahasiswa yang kesulitan dalam mata kuliah tertentu. Pendampingan akademik dapat diberikan dalam bentuk tutor atau sesi belajar kelompok, terutama untuk mahasiswa yang berada pada kategori dengan nilai rendah.

3. Intervensi Dini Berdasarkan Usia Pendaftaran
Berdasarkan grafik Dropout Rate Based on Age of Enrollment, mahasiswa yang mendaftar pada usia yang lebih tua menunjukkan tingkat dropout yang lebih tinggi. Jaya Jaya Institut dapat melakukan intervensi dini dengan memberikan dukungan psikologis atau bimbingan karir untuk mahasiswa yang lebih tua dan merasa kesulitan dalam menyeimbangkan kehidupan akademik dan pribadi. Program khusus dapat disediakan untuk mahasiswa dewasa yang kembali ke dunia pendidikan setelah beberapa tahun bekerja atau mengambil cuti.

4. Meningkatkan Kesadaran untuk Mahasiswa yang Berpotensi Dropout

Dashboard menunjukkan bahwa mahasiswa yang tidak memenuhi persyaratan akademik, seperti Curricular Units yang tidak disetujui, berisiko lebih tinggi untuk dropout. Untuk itu, penting untuk mengidentifikasi mahasiswa berisiko lebih awal dan melakukan pendekatan yang lebih pribadi. Mengadakan sesi pengarahan atau workshop motivasi untuk mahasiswa yang berada dalam kategori berisiko, dengan memberikan mereka panduan tentang bagaimana mengelola tugas akademik dan kehidupan sosial mereka dengan lebih baik. data dari mahasiswa dengan status enrolled dapat dimasukkan ke model prediksi dan bagi mahasiswa dengan hasil prediksi dropout dapat menjadi target utama aksi ini, prediksi dapat dilakukan dengan mengupload file test_df.csv pada folder data 

5. Optimalisasi Sistem Pemberian Tugas dan Ujian
Data yang menunjukkan mahasiswa yang tidak menyelesaikan mata kuliah atau tidak lulus ujian cenderung memiliki tingkat dropout lebih tinggi, bisa menjadi indikasi bahwa sistem evaluasi atau penugasan mungkin perlu dioptimalkan. Mengubah cara penilaian tugas atau ujian agar lebih relevan dan dapat diakses oleh semua mahasiswa, misalnya dengan mengurangi beban tugas besar di awal semester dan menyediakan penilaian berkala untuk memberi umpan balik yang lebih cepat.

6. Analisis Lanjutan untuk Faktor Eksternal
Meskipun data di dashboard memberikan wawasan tentang faktor internal yang mempengaruhi dropout, mungkin ada faktor eksternal (seperti situasi sosial atau kesehatan) yang juga memainkan peran besar dalam tingkat dropout. Oleh karena itu, Jaya Jaya Institut dapat mempertimbangkan untuk mengumpulkan data eksternal dan melakukan analisis lebih lanjut untuk mengidentifikasi faktor-faktor yang lebih luas. Dengan analisis ini, mereka dapat menyesuaikan strategi intervensi yang lebih holistik untuk membantu mahasiswa bertahan hingga lulus.

