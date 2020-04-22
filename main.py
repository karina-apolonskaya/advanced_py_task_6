
import csv
import re


def read_csv_file():
    contacts_list = list()
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def parse_contact_list(contacts_list):
    new_contacts_list = list()
    for contact in contacts_list:
        new_contact = list()
        fio_str = ",".join(contact[:3])
        result = re.findall(r'(\w+)', fio_str)
        while len(result) < 3:
            result.append('')
        new_contact += result
        new_contact.append(contact[3])
        new_contact.append(contact[4])
        phone_pattern = re.compile(
            "(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*")
        changed_phone = phone_pattern.sub(r"+7(\3)\6-\8-\10 \12\13", contact[5])
        new_contact.append(changed_phone)
        new_contact.append(contact[6])
        new_contacts_list.append(new_contact)
    return new_contacts_list


def delete_duplicates(new_contacts_list):
    contact_book = dict()
    for contact in new_contacts_list:
        if contact[0] in contact_book:
            contact_value = contact_book[contact[0]]
            for i in range(len(contact_value)):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            contact_book[contact[0]] = contact
    return list(contact_book.values())


def write_csv_file(new_contacts_list):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)
    return f"Файл успешно записан!"



new_contacts_list = read_csv_file()
# print(new_contacts_list)

new_parsed_list = parse_contact_list(new_contacts_list)
# print(new_parsed_list)

contact_book_values = delete_duplicates(new_parsed_list)
# print(contact_book_values)

new_csv_file = write_csv_file(contact_book_values)
print(new_csv_file)