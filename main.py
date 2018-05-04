import requests
import csv
import datetime
import xml.etree.ElementTree as ET


request = {"data": """<?xml version="1.0" encoding="UTF-8"?>
        <request>
            <key>9724qc6jsxk8ax5a</key>
            <method>GetPartners</method>
        </request>"""}

r = requests.post('https://c1613.affilbox.cz/api/', data=request)
result = r.text

with open('/data/out/tables/AffilBoxPartners.csv', mode='wt', encoding='utf-8') as out_file:
    fieldnames = [
      'affilid',
      'email',
      'person_name',
      'person_surname',
      'group',
      '_id',
      'phone',
      'notifikace',
      'doporucil',
      'register',
      'last_login',
      'allow',
      'street',
      'city',
      'psc',
      'company_name',
      'ic',
      'dic',
      'description',
      'dph'
    ]
    writer = csv.writer(out_file, lineterminator='\n')
    writer.writerow(fieldnames)

    tree = ET.fromstring(result)

    for person, address, company in zip(tree.findall('./partner/person'), tree.findall('./partner/address'),tree.findall('./partner/company')):
        row = []
        affilid = person.find('affilid').text
        row.append(affilid)
        email = person.find('email').text
        row.append(email)
        name = person.find('name').text
        row.append(name)
        surname = person.find('surname').text
        row.append(surname)
        group = person.find('group').text
        row.append(group)
        _id = person.find('id').text
        row.append(_id)
        phone = person.find('phone').text
        row.append(phone)
        notifikace = person.find('notifikace').text
        row.append(notifikace)
        doporucil = person.find('doporucil').text
        row.append(doporucil)
        register = person.find('register').text
        row.append(register)
        last_login = person.find('last_login').text
        row.append(last_login)
        allow = person.find('allow').text
        row.append(allow)
        street = address.find('street').text
        row.append(street)
        city = address.find('city').text
        row.append(city)
        psc = address.find('psc').text
        row.append(psc)
        name = company.find('name').text
        row.append(name)
        ic = company.find('ic').text
        row.append(ic)
        dic = company.find('dic').text
        row.append(dic)
        description = company.find('description').text
        row.append(description)
        dph = company.find('dph').text
        row.append(dph)
        writer.writerow(row)
