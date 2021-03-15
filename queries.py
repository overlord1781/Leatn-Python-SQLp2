from sqlalchemy.sql import func
from sqlalchemy.sql.expression import desc
from model import  Salary
from db import db_session

def top_salary(num_rows):
    top_salary = Salary.query.order_by(Salary.salary.desc()).limit(num_rows)

    for s in top_salary:
        print(f'З/П {s.salary}')

def city_salary(city_name):
    top_salary = Salary.query.filter(Salary.city == city_name).order_by(Salary.salary.desc())
    for s in top_salary:
        print(f'З/П для города {city_name} - {s.salary} р.')

def top_salary_by_email(domain, rows):
    top_salary = Salary.query.filter(Salary.email.ilike(f'%{domain}')).order_by(Salary.salary.desc()).limit(rows)
    for s in top_salary:
        print(f'С доменом {domain} - {s.salary} р.')

def average_salary():
    avg_salary = db_session.query(func.avg(Salary.salary)).scalar()
    print(f'Средняя з/п {avg_salary:.2f}')

def count_distinct_sities():
    count_cities = db_session.query(Salary.city).group_by(Salary.city).count()
    print(count_cities)

def top_avg_salary_by_city(num_rows):
    top_salary = db_session.query(
        Salary.city,
        func.avg(Salary.salary).label('avg_salary')
    ).group_by(Salary.city).order_by(desc('avg_salary')).limit(num_rows)

    for city, salary in top_salary:
        print(f'Город {city} - з/п {salary:.2f} р.')

if __name__ == '__main__':
    top_avg_salary_by_city(10)