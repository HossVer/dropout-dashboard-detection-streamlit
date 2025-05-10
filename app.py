##-- ===================================================== 
##-- ==========          Libraries           ============= 
##-- ===================================================== 
import streamlit as st
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler, LabelEncoder




##-- ===================================================== 
##-- ==========          Functions           ============= 
##-- =====================================================

##-- Load Dashboard 
def load_dashboard():
    # Gambar snapshot dari Tableau (ganti URL sesuai dengan dashboard kamu)
    tableau_image_url = "assets/dashboard/Dashboard 1.png"
    tableau_url = "https://public.tableau.com/views/EmployeeAttritionAnalysis_17453257769940/Dashboard1"
    
    # Menampilkan gambar statis dengan tautan ke Tableau Public
    st.image(tableau_image_url, caption="Klik untuk melihat Dashboard Tableau")
    
    # Membuat tautan ke Tableau dashboard yang bisa diklik
    st.markdown(f"[Klik di sini untuk melihat Dashboard Tableau]({tableau_url})", unsafe_allow_html=True)

##-- Load model h5
def load_model():
    model = tf.keras.models.load_model("model/model_deeplearning.h5")  # Menyesuaikan path model
    return model

##-- Load data from csv file
def load_csv_file(uploaded_file):
    df = pd.read_csv(uploaded_file)  # Memuat file CSV yang diupload
    return df

##-- Create dataframe from manually inserted variable
def get_manual_input():
    st.sidebar.header("Masukkan Data Manual untuk Prediksi")
    
    # Tuition Fees (Binary)
    tuition_fees = st.sidebar.selectbox("Tuition Fees Up to Date", ["Yes", "No"])
    scholarship = st.sidebar.selectbox("Scholarship Holder", ["Yes", "No"])
    
    # Dropdown untuk Application Mode dengan deskripsi kode
    application_modes = {
        1: "1st phase - general contingent",
        2: "Ordinance No. 612/93", 
        5: "1st phase - special contingent (Azores Island)", 
        7: "Holders of other higher courses", 
        10: "Ordinance No. 854-B/99", 
        15: "International student (bachelor)", 
        16: "1st phase - special contingent (Madeira Island)", 
        17: "2nd phase - general contingent", 
        18: "3rd phase - general contingent", 
        26: "Ordinance No. 533-A/99, item b2) (Different Plan)", 
        27: "Ordinance No. 533-A/99, item b3 (Other Institution)", 
        39: "Over 23 years old", 
        42: "Transfer", 
        43: "Change of course", 
        44: "Technological specialization diploma holders", 
        51: "Change of institution/course", 
        53: "Short cycle diploma holders", 
        57: "Change of institution/course (International)"
    }
    application_mode = st.sidebar.selectbox(
        "Application Mode",
        list(application_modes.items()), format_func=lambda x: f"{x[0]} - {x[1]}"
    )[0]  # Mengambil kode (angka) sebagai nilai yang akan diproses

    debtor = st.sidebar.selectbox("Debtor", ["Yes", "No"])
    age = st.sidebar.number_input("Age at Enrollment", min_value=17)
    curricular_units_1st_sem_enrolled = st.sidebar.number_input("Curricular Units 1st Sem Enrolled", min_value=0)
    curricular_units_1st_sem_approved = st.sidebar.number_input("Curricular Units 1st Sem Approved", min_value=0)
    curricular_units_1st_sem_grade = st.sidebar.number_input("Curricular Units 1st Sem Grade", min_value=0)
    curricular_units_2nd_sem_enrolled = st.sidebar.number_input("Curricular Units 2nd Sem Enrolled", min_value=0)
    curricular_units_2nd_sem_approved = st.sidebar.number_input("Curricular Units 2nd Sem Approved", min_value=0)
    curricular_units_2nd_sem_grade = st.sidebar.number_input("Curricular Units 2nd Sem Grade", min_value=0)

    data = {
        "Tuition_fees_up_to_date": 1 if tuition_fees == "Yes" else 0,
        "Scholarship_holder": 1 if scholarship == "Yes" else 0,
        "Application_mode": application_mode,
        "Debtor": 1 if debtor == "Yes" else 0,
        "Age_at_enrollment": age,
        "Curricular_units_1st_sem_enrolled": curricular_units_1st_sem_enrolled,
        "Curricular_units_1st_sem_approved": curricular_units_1st_sem_approved,
        "Curricular_units_1st_sem_grade": curricular_units_1st_sem_grade,
        "Curricular_units_2nd_sem_enrolled": curricular_units_2nd_sem_enrolled,
        "Curricular_units_2nd_sem_approved": curricular_units_2nd_sem_approved,
        "Curricular_units_2nd_sem_grade": curricular_units_2nd_sem_grade
    }
    
    return pd.DataFrame([data])

##-- Make df use
def make_df_use(df):
    use = ["Tuition_fees_up_to_date",
        "Scholarship_holder",
        "Application_mode",
        "Debtor",
        "Age_at_enrollment",
        "Curricular_units_1st_sem_enrolled",
        "Curricular_units_1st_sem_approved",
        "Curricular_units_1st_sem_grade",
        "Curricular_units_2nd_sem_enrolled",
        "Curricular_units_2nd_sem_approved",
        "Curricular_units_2nd_sem_grade"]
    
    df = df[use]
    return df

def normalization(df):
    columns = df.columns  # Memperbaiki penulisan 'collumns' menjadi 'columns'
    scaler = MinMaxScaler()

    df[columns] = scaler.fit_transform(df[columns])
    return df  # Memastikan nilai df yang telah dinormalisasi dikembalikan

##-- Preprocessing
def datapreprocessing(df):
    ##-- Variabe isolation
    used_df = make_df_use(df)
    
    ##-- Label Encoding untuk Application Mode
    label_encoder = LabelEncoder()
    used_df["Application_mode"] = label_encoder.fit_transform(used_df["Application_mode"])
    
    ##-- Minmax Scalling Normalization
    used_df = normalization(used_df)
    return used_df

##-- Predict
def predict_dropout(data):
    ##-- Load model    
    model = load_model()

    ##-- Predict
    predict = model.predict(data)  # Memastikan prediksi dilakukan pada data yang diproses
    y_pred_classes = (predict > 0.5).astype(int)
    
    # Mengganti hasil prediksi dengan "Predicted Dropout" atau "Graduate"
    y_pred_classes = pd.DataFrame(y_pred_classes, columns=["Predicted Status"])
    y_pred_classes["Predicted Status"] = y_pred_classes["Predicted Status"].replace({1: "Predicted Dropout", 0: "Graduate"})
    
    # Mengubah indeks mulai dari 1
    y_pred_classes.index = y_pred_classes.index + 1
    
    # Menampilkan hasil prediksi
    st.write("Hasil Prediksi Dropout:", y_pred_classes.style.set_properties(subset=["Predicted Status"], align="left"))  # Align ke kiri





##-- ===================================================== 
##-- ==========        Main Program          ============= 
##-- ===================================================== 

# Menampilkan dashboard Tableau
st.subheader("Dashboard Analitik")
load_dashboard()

st.title("Deteksi Dropout - Model Prediksi")

# Upload CSV file
uploaded_file = st.file_uploader("Pilih file CSV untuk diproses", type="csv")

if uploaded_file is not None:
    data = load_csv_file(uploaded_file)
    st.write("Data yang diunggah:", data.head())  # Menampilkan beberapa baris pertama data yang diunggah
    
    # Melakukan prediksi dropout untuk data yang diunggah
    if st.button("Prediksi Dropout untuk Data CSV"):
        processed_data = datapreprocessing(data)
        predict_dropout(processed_data)

# Memasukkan data manual untuk prediksi
manual_data = get_manual_input()
if st.button("Prediksi Dropout dengan Data Manual"):
    processed_manual_data = datapreprocessing(manual_data)
    predict_dropout(processed_manual_data)

