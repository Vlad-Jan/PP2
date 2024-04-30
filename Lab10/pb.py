import psycopg2
import csv

# Establish the PostgreSQL connection
connection = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="pp2_2024",
    host="localhost",  # or your host
    port="5432"  # default PostgreSQL port
)

# Create a cursor object
cursor = connection.cursor()

# Create the PhoneBook table if it doesn't exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS PhoneBook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(50)
);
'''
cursor.execute(create_table_query)
connection.commit()

print("PhoneBook table created successfully.")


def insert_from_csv(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header
        for row in csvreader:
            cursor.execute(
                "INSERT INTO PhoneBook (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
                (row[0], row[1], row[2], row[3])
            )
    connection.commit()
    print("Data inserted from CSV file.")



def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email (optional): ")

    cursor.execute(
        "INSERT INTO PhoneBook (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, phone, email)
    )
    connection.commit()

    print("Data inserted from console.")

def update_contact(id, new_first_name=None, new_phone=None):
    if new_first_name:
        cursor.execute("UPDATE PhoneBook SET first_name = %s WHERE id = %s", (new_first_name, id))
    if new_phone:
        cursor.execute("UPDATE PhoneBook SET phone = %s WHERE id = %s", (new_phone, id))
    connection.commit()

    print("Contact updated.")

# Query by first name
def query_by_first_name(first_name):
    cursor.execute("SELECT * FROM PhoneBook WHERE first_name = %s", (first_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Query by phone number
def query_by_phone(phone):
    cursor.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# Delete by username (first name)
def delete_by_first_name(first_name):
    cursor.execute("DELETE FROM PhoneBook WHERE first_name = %s", (first_name,))
    connection.commit()
    print(f"Deleted contacts with first name {first_name}.")

# Delete by phone number
def delete_by_phone(phone):
    cursor.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    connection.commit()
    print(f"Deleted contacts with phone {phone}.")

cursor.close()
connection.close()

def main():

    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Query by first name")
        print("5. Query by phone")
        print("6. Delete by first name")
        print("7. Delete by phone")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            csv_path = input("Enter the path to the CSV file: ")
            insert_from_csv(csv_path)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            contact_id = int(input("Enter the contact ID to update: "))
            new_first_name = input("Enter new first name (or leave blank): ")
            new_phone = input("Enter new phone (or leave blank): ")
            update_contact(contact_id, new_first_name, new_phone)
        elif choice == "4":
            first_name = input("Enter the first name to query: ")
            query_by_first_name(first_name)
        elif choice == "5":
            phone = input("Enter the phone number to query: ")
            query_by_phone(phone)
        elif choice == "6":
            first_name = input("Enter the first name to delete: ")
            delete_by_first_name(first_name)
        elif choice == "7":
            phone = input("Enter the phone number to delete: ")
            delete_by_phone(phone)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()