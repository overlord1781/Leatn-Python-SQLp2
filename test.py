import csv

with open('salary.csv', 'r', encoding='utf-8') as f:
    fields = ['name', 'city_name', 'street_address','large_company'
        'job', 'phone_number', 'free_email', 'date_of_birth', 'salary'    
        ]

    reader = csv.DictReader(f,fields,delimiter=';')
    print(reader[0])