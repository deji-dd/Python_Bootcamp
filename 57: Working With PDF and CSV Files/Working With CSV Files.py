import csv

data = open('example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
all_emails = []
full_names = []
for line in data_lines[1:]:
    all_emails.append(line[3])
for line in data_lines[1:]:
    full_names.append(f'{line[1]} {line[2]}')
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
file_to_output.close()
