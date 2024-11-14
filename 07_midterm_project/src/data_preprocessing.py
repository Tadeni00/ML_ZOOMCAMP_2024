# src/data_preprocessing.py
import pandas as pd
import logging
from src.logger import logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Renaming columns to more descriptive names")
    column_rename_map = {
    "fecha_dato": "data_date",
    "ncodpers": "customer_code",
    "ind_empleado": "employee_index",
    "pais_residencia": "country_of_residence",
    "sexo": "gender",
    "age": "age",
    "fecha_alta": "registration_date",
    "ind_nuevo": "new_customer_index",
    "antiguedad": "customer_seniority",
    "indrel": "customer_type_end",
    "ult_fec_cli_1t": "last_primary_date",
    "indrel_1mes": "customer_type_start",
    "tiprel_1mes": "relationship_type",
    "indresi": "residence_index",
    "indext": "foreigner_index",
    "conyuemp": "spouse_of_employee",
    "canal_entrada": "join_channel",
    "indfall": "deceased_indicator",
    "tipodom": "primary_address",
    "cod_prov": "province_code",
    "nomprov": "province_name",
    "ind_actividad_cliente": "activity_index",
    "renta": "gross_income",
    "ind_ahor_fin_ult1": "savings_account",
    "ind_aval_fin_ult1": "guarantees",
    "ind_cco_fin_ult1": "current_account",
    "ind_cder_fin_ult1": "derivada_account",
    "ind_cno_fin_ult1": "payroll_account",
    "ind_ctju_fin_ult1": "junior_account",
    "ind_ctma_fin_ult1": "mas_particular_account",
    "ind_ctop_fin_ult1": "particular_account",
    "ind_ctpp_fin_ult1": "particular_plus_account",
    "ind_deco_fin_ult1": "short_term_deposits",
    "ind_deme_fin_ult1": "medium_term_deposits",
    "ind_dela_fin_ult1": "long_term_deposits",
    "ind_ecue_fin_ult1": "e_account",
    "ind_fond_fin_ult1": "investment_funds",
    "ind_hip_fin_ult1": "mortgage",
    "ind_plan_fin_ult1": "pension_plan",
    "ind_pres_fin_ult1": "loan",
    "ind_reca_fin_ult1": "taxes",
    "ind_tjcr_fin_ult1": "credit_card",
    "ind_valo_fin_ult1": "securities",
    "ind_viv_fin_ult1": "home_account",
    "ind_nomina_ult1": "payroll_recent",
    "ind_nom_pens_ult1": "pensions_recent",
    "ind_recibo_ult1": "direct_debit"
}
    df.rename(columns=column_rename_map, inplace=True)
    logging.info("Columns renamed successfully")
    return df

def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Converting data types of categorical and boolean columns")
    categorical_columns = [
        'employee_index', 'country_of_residence', 'gender', 'new_customer_index',
        'customer_type_end', 'customer_type_start', 'relationship_type',
        'residence_index', 'foreigner_index', 'join_channel', 'deceased_indicator',
        'primary_address', 'province_code', 'province_name', 'customer_code',
        'data_date', 'registration_date', 'last_primary_date'
    ]
    df[categorical_columns] = df[categorical_columns].astype('category')
    
    boolean_columns = [
        'savings_account', 'guarantees', 'current_account', 'derivada_account',
        'payroll_account', 'junior_account', 'mas_particular_account',
        'particular_account', 'particular_plus_account', 'short_term_deposits',
        'medium_term_deposits', 'long_term_deposits', 'e_account', 'investment_funds',
        'mortgage', 'pension_plan', 'loan', 'taxes', 'credit_card', 'securities',
        'home_account', 'payroll_recent', 'pensions_recent', 'direct_debit'
    ]
    df[boolean_columns] = df[boolean_columns].astype(bool)
    logging.info("Data type conversion completed")
    
    return df
