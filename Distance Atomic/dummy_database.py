"""
@author : Abdoul wahab Soumare
"""
import numpy as np
import pandas as pd

def create_database(records):
    ids = list(range(1, records + 1))
    sexs = np.random.choice(['M', 'F'], p = [0, 1], size = records)
    ages = np.random.choice(range(15, 46), size = records)
    lifestyles = np.random.choice(['Bonne', 'Moyenne', 'Mauvaise'], p = [0.2, 0.3, 0.5], size = records)
    hydratation = np.random.choice(['Faible', 'Moyenne', 'Frequent'], p = [0.5, 0.3, 0.2], size = records)
    antibiotic_use = np.random.choice(['oui', 'non'], p = [0.6, 0.4], size = records)

    nationalities = np.random.choice(
        ['SENEGALAISE', 'GUINEENNE', 'TOGOLAISE', 'MALIENNE', 'IVORIENNE', 'MAURITANIENNE'],
        p = [0.4, 0.2, 0.1, 0.1, 0.1, 0.1],
        size = records
    )

    intimate_cleansing = np.where(
        (sexs == "F") & (ages >= 30) & (ages <= 45),
        np.random.choice(['Faible', 'Moyenne', 'Frequent'], p = [0.2, 0.3, 0.5], size = records),
        np.random.choice(['Faible', 'Moyenne', 'Frequent'], p = [0.3, 0.5, 0.2], size = records)
    )
    intimate_cleansing = np.where(sexs == "M", "Absent", intimate_cleansing)

    # prostate_disease = np.where(
    #     (sexs == "M") & (ages >= 50),
    #     np.random.choice(['oui', 'non'], p = [0.6, 0.4], size = records),
    #     "non"
    # )
    # prostate_disease = np.where(sexs == "F", "Absent", prostate_disease)

    sexual_activity = np.where(
        (ages >= 25) & (ages <= 45),
        np.random.choice([0, 1, 2, 3, 4, 5, 6], p = [0.1, 0.1, 0.3, 0.1, 0.2, 0.1, 0.1], size = records),
        np.random.choice([0, 1, 2], p = [0.6, 0.3, 0.1], size = records)
    )

    number_of_parteners = np.where(
        sexual_activity >= 3,
        np.random.choice([2, 3, 4, 5, 6], p = [0.1, 0.1, 0.2, 0.2, 0.4], size = records),
        np.random.choice([1, 2, 3], p = [0.7, 0.2, 0.1], size = records)
    )
    number_of_parteners = np.where(sexual_activity == 0, 0, number_of_parteners)

    contraceptive_use = np.where(
        (sexs == "F") & (ages >= 30) & (ages <= 45),
        np.random.choice(['oui', 'non'], p = [0.8, 0.2], size = records),
        np.random.choice(['oui', 'non'], p = [0.2, 0.8], size = records)
    )
    # contraceptive_use = np.where(sexs == "M", "Absent", contraceptive_use)

    diabetes = np.where(
        ages >= 35,
        np.random.choice(['oui', 'non'], p = [0.7, 0.3], size = records),
        np.random.choice(['oui', 'non'], p = [0.2, 0.8], size = records)
    )

    previous_urinary_tract_infections = np.where(
        (ages >= 35) & (sexs == "F"),
        np.random.choice(['oui', 'non'], p = [0.6, 0.4], size = records),
        np.random.choice(['oui', 'non'], p = [0.1, 0.9], size = records)
    )

    renal_diseases = np.where(
        (diabetes == 'oui') & (ages >= 45),
        np.random.choice(['oui', 'non'], p = [0.7, 0.3], size = records),
        np.random.choice(['oui', 'non'], p = [0.1, 0.9], size = records)
    )

    value_leukocytes_urine = np.random.exponential(scale=1.0, size = records)
    value_leukocytes_urine = np.clip(value_leukocytes_urine, 0, 20)
    value_leukocytes_urine = np.round(value_leukocytes_urine * 10, 2)

    value_red_blood_cells_urine = np.random.exponential(scale=1.0, size = records)
    value_red_blood_cells_urine = np.clip(value_red_blood_cells_urine, 0, 20)
    value_red_blood_cells_urine = np.round(value_red_blood_cells_urine * 10, 2)

    urinary_infection = np.where(
        (
            (sexs == "F") & (lifestyles == "Mauvaise") & (hydratation == "Faible")
            & (antibiotic_use == "oui") & (intimate_cleansing == "Frequent") & (sexual_activity >= 3)
            & (number_of_parteners >= 3) & (contraceptive_use == "oui") & (diabetes == "oui")
            & (previous_urinary_tract_infections == "oui") & (renal_diseases == "oui") & ((value_leukocytes_urine >= 10) | (value_red_blood_cells_urine >= 10)) )
        # ) | (
        #     (sexs == "M") & (lifestyles == "Mauvaise") & (hydratation == "Faible")
        #     & (antibiotic_use == "oui") & (sexual_activity >= 3)
        #     & (number_of_parteners >= 3) & (diabetes == "oui")
        #     & (previous_urinary_tract_infections == "oui") & (renal_diseases == "oui") & ((value_leukocytes_urine >= 10) | (value_red_blood_cells_urine >= 10))
        # ) #| (
            #(sexs == "M") & (prostate_disease == "oui") & ((value_leukocytes_urine >= 10) | (value_red_blood_cells_urine >= 10)))
            ,
        "oui",
        np.random.choice(['oui', 'non'], p = [0.1, 0.9], size = records)
    )
    urinary_infection = np.where(((value_leukocytes_urine < 10) & (value_red_blood_cells_urine < 10)), "non", "oui")

    death = np.where(
        urinary_infection == 'oui',
        np.random.choice(['oui', 'non'], p = [0.7, 0.3], size = records),
        np.random.choice(['oui', 'non'], p = [0.3, 0.7], size = records)
    )

    dummy_data = pd.DataFrame({
        "id" : ids,
        "sex" : sexs,
        "age" : ages,
        "nationality" : nationalities,
        "lifestyle" : lifestyles,
        # "prostate_disease" : prostate_disease,
        "antibiotic_use" : antibiotic_use,
        "intimate_cleansing" : intimate_cleansing,
        "sexual_activity" : sexual_activity,
        "number_of_parteners" : number_of_parteners,
        "contraceptive_use" : contraceptive_use,
        "diabetes" : diabetes,
        "previous_urinary_tract_infections" : previous_urinary_tract_infections,
        "renal_diseases" : renal_diseases,
        "value_leukocytes_urine" : value_leukocytes_urine,
        "value_red_blood_cells_urine" : value_red_blood_cells_urine,
        "urinary_infection" : urinary_infection,
        "death" : death
    })

    dummy_data.to_excel('dummy_database.xlsx', index=False, header=True)

if __name__ == '__main__' :
    create_database(1500)
