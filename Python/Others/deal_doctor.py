doctor = {
    'title': 'Specialist',
    'name':'Gary Jia',
    'employment_year': '1997'
}

print(doctor)

doctor['gender'] = 'Male'

def format_doctor(doctor_info):
    return (
        f"Title: {doctor_info['title']}\n"
        f"Name: {doctor_info['name']}\n"
        f"Employment year: {doctor_info['employment_year']}\n"
        f"Gender: {doctor_info['gender']}"
    )


print(format_doctor(doctor))


doctors = [doctor]

doctors.append({
    'title': 'Specialist',
    'name':'June Lee',
    'employment_year': '2002',
    'gender': 'Female',
})
doctors.append({
    'title': 'Jr',
    'name':'Neng Liu',
    'employment_year': '2022',
    'gender': 'Male',
})
doctors.append({
    'title': 'Jr',
    'name':'Neng Lee',
    'employment_year': '2021',
    'gender': 'Female',
})
doctors.append({
    'title': 'Jr',
    'name':'Neng An',
    'employment_year': '2021',
    'gender': 'Male',
})


def search_doctor(title):
    founded = False
    for doctor in doctors:
        if doctor['title'] == title:
            founded = True
            print(format_doctor(doctor))
    if not founded:
        print(f'There is no doctor with title: {title}')

while True:
    title = input('Please input the title of the doctor, leave blank to quit: ')
    if not title:
        break

    search_doctor(title)
