patients = (
    ('Gary Jia', 45, 'Flu'),
    ('Mike Lee', 30, 'Headache'),
    ('Jane White', 22, 'Cough'),
    ('John Black', 55, 'Running nose'),
    ('Qingyun Wang', 88, 'Bleeding')
)

print(patients)

def format_patient(patient):
    return (
        f"Name: {patient[0]}, "
        f"Age: {patient[1]}, "
        f"Symptom: {patient[2]}")


for patient in patients:
    print(format_patient(patient))
