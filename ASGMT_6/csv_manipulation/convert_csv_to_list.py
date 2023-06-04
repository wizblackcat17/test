import csv




def convert_to_list(csv_file):
    try:
        # Open the CSV file
        with open(csv_file, newline='') as csvfile:

            # Create a reader object
            reader = csv.DictReader(csvfile)

            # Create an empty list to hold the dictionaries
            data = []

            # Iterate over the rows in the CSV file
            for row in reader:

                # Append the row as a dictionary to the list
                data.append(dict(row))

        # Return the list of dictionaries
        return data
    except Exception as err:
        print("Error caught when converting...", err)
        return []


