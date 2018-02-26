def add_new(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option, ask_y_n
    import gen_info_tables
    print ("Enter new record for General Information")
    print("Enter Patient Biographical Information")
    gen_info_tables.bio_info(conn, cursor, file_number, table)
    print("Enter Patient habits")
    gen_info_tables.phys_act(conn, cursor, file_number, table)
    gen_info_tables.habits(conn, cursor, file_number, table)
    gen_info_tables.nut_supplements(conn, cursor, file_number, table)
    print("Enter Patient family and reproductive details")
    gen_info_tables.family_details(conn, cursor, file_number, table)
    gen_info_tables.repro_details(conn, cursor, file_number, table)
    print("Enter Patient and family medical history")
    gen_info_tables.med_history(conn, cursor, file_number, table)
    gen_info_tables.cancer_history(conn, cursor, file_number, table)
    gen_info_tables.family_cancer(conn, cursor, file_number, table)
    print("Enter Patient Symptoms")
    gen_info_tables.det_by(conn, cursor, table, file_number)
    gen_info_tables.breast_symptoms(conn, cursor, file_number, table)
    gen_info_tables.metastasis_symp(conn, cursor, file_number, table)

def update_record(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option, ask_y_n
    import gen_info_tables
    print("Update record for General Information")
    enter = ask_y_n("Enter Patient Biographical Information")
    if enter:
        gen_info_tables.bio_info(conn, cursor, file_number, table)
    enter = ask_y_n("Enter Patient habits")
    if enter:
        gen_info_tables.phys_act(conn, cursor, file_number, table)
        gen_info_tables.habits(conn, cursor, file_number, table)
        gen_info_tables.nut_supplements(conn, cursor, file_number, table)
    enter = ask_y_n("Enter Patient family and reproductive details?")
    if enter:
        gen_info_tables.family_details(conn, cursor, file_number, table)
        gen_info_tables.repro_details(conn, cursor, file_number, table)
    enter = ask_y_n("Enter Patient and family medical history?")
    if enter:
        gen_info_tables.med_history(conn, cursor, file_number, table)
        gen_info_tables.cancer_history(conn, cursor, file_number, table)
        gen_info_tables.family_cancer(conn, cursor, file_number, table)
    enter = ask_y_n("Enter Patient Symptoms?")
    if enter:
        gen_info_tables.det_by(conn, cursor, table, file_number)
        gen_info_tables.breast_symptoms(conn, cursor, file_number, table)
        gen_info_tables.metastasis_symp(conn, cursor, file_number, table)