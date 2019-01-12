import csv

data = open("PatientInformation.csv", encoding="utf-8")
csvData = csv.reader(data)

# If CSV has some special characters like @ symbol throws UnicodeDecodeError,
# To resolve  encoding errors, open the file with 'utf-8' encoding
data_lines = list(csvData)

# for line in data_lines:
# print(line)

full_names = []
# Skip the first line which is an header and till the end of the list
for row in data_lines[1:]:
    full_names.append(row[2] + " " + row[3] + " " + row[4])

print(full_names)

# CSV module allows to create a new file and write it to file system
# if the file already exists with the name, it completely overwrites it
# open the file with appending mode, if the file is already exists
output_file = open("created_file.csv", "w", newline="")

csv_writer = csv.writer(output_file, delimiter=",")
csv_writer.writerow(["col1", "col2", "col3"])

# use writerows() to write multiple rows
csv_writer.writerows([[1, 2, 3], [4, 5, 6]])
output_file.close()
