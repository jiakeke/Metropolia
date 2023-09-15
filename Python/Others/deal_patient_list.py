patients = []
for item in [
    ('Gary Jia', 45, 'Flu'),
    ('Mike Lee', 30, 'Headache'),
    ('Jane White', 22, 'Cough'),
    ('John Black', 55, 'Running nose'),
    ('Qingyun Wang', 88, 'Bleeding')]:

    patients.append(item)

def search_patient(name):
    for patient in patients:
        if name == patient[0]:
            print('Your input name is exist in the patient list')
            print(f"Name: {patient[0]}")
            print(f"Age: {patient[1]}")
            print(f"Symptom: {patient[2]}")
            break
    else:
        print('The name is not in the patient list.')
        age = int(input('How old are you?\n'))
        symptom = input('What is your symptom?\n')
        patients.append((name, age, symptom))
        print('I have save the name into the patient list')

for patient in patients[:3]:
    print(f"Name: {patient[0]}")
    print(f"Age: {patient[1]}")
    print(f"Symptom: {patient[2]}")


while True:
    name = input('Please input the patient name, leave blank to quit: ')
    if not name:
        break

    search_patient(name)
