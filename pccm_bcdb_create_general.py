import sqlite3
from add_update_sql import add_columns
import os.path

folder = "DB"
db_name = "PCCM_BreastCancerDB_GeneralInfo_26022018_2.db"
path = os.path.join(folder, db_name)

if os.path.isfile(path):
    print (path + " file already exists")
else:
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    table_name1 = "Patient_Information_History"
    columns1 = "File_number, MR_number, Name, Consent, Aadhaar_Card, FirstVisit_Date, Permanent_Address, Current_Address, Phone, Email_ID, " \
       "Gender, Age_yrs, Date_of_Birth, Place_Birth, Height_cm, Weight_kg, BMI"
    cursor.execute('CREATE TABLE {tn} ({nf})'\
                   .format(tn= table_name1, nf= columns1))

    phys_act = "Physical_Activity_y_n", "Type_Physical_Activity", "Frequency_Physical_Activity"
    add_columns(cursor, table_name1, phys_act)

    habits = "Diet", "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week", "Duration_alcohol", \
            "Comments_alcohol", "Tobacco_y_n", "Exposure_Mode", "Type_Passive", "Type_tobacco","Tobacco_consumption_age_yrs", \
              "Tobacco_Frequency","Quantity_tobacco_per_week", "Duration_tobacco", "Comments_tobacco",\
              "Other_Deleterious_Habits"
    add_columns(cursor, table_name1, habits)

    nut_supp = "Nutritional_supplements_y_n", "Type_Nutritional_supplements", "Quantity_Nutritional_supplements", \
			            "Duration_Nutritional_supplements",
    add_columns(cursor, table_name1, nut_supp)

    family_details = "Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons"
    add_columns(cursor, table_name1, family_details)

    repro_details = "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period", "Period_Type", \
                    "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child", "Age_first_pregnancy", \
                    "Age_last_child", "Age_last_pregnancy", "Two_births_in_year", "Breast_feeding", \
                    "Child_Breast_feeding", "Duration_Breast_feeding", "Breast_Usage_Breast_feeding", \
                    "Type_birth_control_used", "Details_birth_control", "Duration_birth_control"
    add_columns(cursor, table_name1, repro_details)

    other_tables_y_n =  "Any_Other_Medical_History_y_n", "Type_Any_Other_Medical_History", \
                       "Diagnosis_Date_Any_Other_Medical_History", "Treatment_Any_Other_Medical_History",\
                       "Previous_Cancer_History_y_n", "Type_Previous_Cancer", "Year_Diagnosed_Previous_Cancer", \
                       "Treatment_Previous_Cancer", "Treatment_Type_Previous_Cancer",\
                       "Treatment_Duration_Previous_Cancer","FamilyCancer_history_y_n", \
                       "Type_DegreeRelation_TypeRelation_Age_FamilyCancer"
    add_columns(cursor, table_name1, other_tables_y_n)

    symptoms = "Current_Breast_Cancer_Detected_By", "Current_Breast_Cancer_Detected_Date", "RB_symptoms", \
               "RB_symptoms_duration", "LB_symptoms", "LB_symptoms_duration", "RB_Other_Symptoms", \
			  "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "LB_Other_Symptoms_duration", "Metatasis_Symptoms"
    add_columns(cursor, table_name1, symptoms)
    

# additional tables
    table_name2 = "General_Medical_History"
    columns2 = "File_number, Condition, Diagnosis_date, Treatment"

    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name2, nf=columns2))
    table_name3 = "Family_Cancer_History"
    columns3 = 'File_number, Type_Cancer, Relation_to_Patient, Type_Relation, Age_at_detection_yrs'
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name3, nf=columns3))
    table_name4 = "Previous_Cancer_History"
    columns4 = "File_number, Type_Cancer, Year_diagnosis, Surgery, Type_Surgery, Duration_Surgery, Radiation," \
               "Type_Radiation,Duration_Radiation,Chemotherapy,Type_Chemotherapy,Duration_Chemotherapy,Hormone," \
               "Type_Hormone,Duration_Hormone,Alternative,Type_Alternative,Duration_Alternative,HomeRemedy," \
               "Type_HomeRemedy,Duration_HomeRemedy"

    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name4, nf=columns4))
    table_name5 = "Nutritional_Supplements"
    columns5 = "File_number, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, " \
               "Duration_nutritional_supplements"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name5, nf=columns5))
    table_name7 = "Physical_Activity"
    columns7 = "File_number, Type_activity, Frequency_activity"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name7, nf=columns7))
    table_name8 = "Breast_Feeding"
    columns8 = "File_number, Child_number, Feeding_duration, Breast_usage_feeding"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name8, nf=columns8))
    conn.commit()
    print (path + (" file created"))
    conn.close()
