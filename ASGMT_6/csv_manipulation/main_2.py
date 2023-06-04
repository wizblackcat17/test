from convert_csv_to_list import convert_to_list
from sql_connector import DatabaseConnector
from database_credentials import database_credentials

'''
1. check if table exists
2. if table does not exists, create table
3. if table exists, insert data
'''


def main(db_connector):
    # check if table exists
    res = db_connector.connect_to_db("SELECT * FROM loans;", False)
    if res is None:
        print("Sorry this table does not exists")
        # customer_id,age,gender,occupation,marital_status,family_size,income,expenditure,use_frequency,loan_category,loan_amount,overdue,_debt_record,_returned_cheque,_dishonour_of_bill
        db_connector.connect_to_db("CREATE TABLE `loans`( `id` int(11) NOT NULL AUTO_INCREMENT, `customer_id` VARCHAR(200) NOT NULL, `age` INT(11) NOT NULL, `gender` VARCHAR(50) NOT NULL,`occupation` VARCHAR(50) NOT NULL,`marital_status` VARCHAR(50) NOT NULL,`family_size` VARCHAR(50) NOT NULL,`income` VARCHAR(100) NOT NULL,`expenditure` VARCHAR(50) NOT NULL,`use_frequency` VARCHAR(50) NOT NULL,`loan_category` VARCHAR(50) NOT NULL,`loan_amount` VARCHAR(50) NOT NULL,`overdue` VARCHAR(50) NOT NULL,`_debt_record` VARCHAR(50) NOT NULL,`_returned_cheque` VARCHAR(50) NOT NULL,`_dishonour_of_bill` VARCHAR(50) NOT NULL, `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id`)) ENGINE=InnoDB  DEFAULT CHARSET=utf8", True)
    else:
        print("yeah the table exists", res)
        apple = convert_to_list("csvs/loan.csv")
        print(len(apple), list(apple[0].keys()))
        # Apply filters => This is the filter the data and only permit entries of filters that match the rest we will ignore that data
        # apple = list(filter(lambda a: a['active']=="0", apple))

        
        # apple = list(map(lambda a: a, apple))
        # insert data
        for entry in apple:
            print(entry)
            db_connector.connect_to_db(f"INSERT INTO loans (customer_id,age,gender,occupation,marital_status,family_size,income,expenditure,use_frequency,loan_category,loan_amount,overdue,_debt_record,_returned_cheque,_dishonour_of_bill) VALUES ('{entry['customer_id']}', {entry['age']}, '{entry['gender']}', '{entry['occupation']}', '{entry['marital_status']}', '{entry['family_size']}', '{entry['income']}', '{entry['expenditure']}', '{entry['use_frequency']}', '{entry['loan_category']}', '{entry['loan_amount']}', '{entry['overdue']}', '{entry['_debt_record']}', '{entry['_returned_cheque']}', '{entry['_dishonour_of_bill']}')", True)

    pass


if __name__ == "__main__":
    database = database_credentials
    db_connector = DatabaseConnector(database["db_name"], database["db_user"], database["db_password"], database["db_host"], database["db_port"])
    main(db_connector)
