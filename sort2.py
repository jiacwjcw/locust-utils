import csv, operator

with open('./1639549331-sta-wap-api-failure-data.csv',newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    sortedlist = sorted(spamreader, key=lambda row:(row['Name'], int(row['Occurrences'])), reverse=True)

with open('sorted2.csv', 'w') as f:
    fieldnames = ['Method','Name','Error','Occurrences']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in sortedlist:
        writer.writerow(row)

# with open('sorted.csv', 'w') as f:
#     fieldnames = ['Type', 'Name', 'Request Count', 'Failure Count', 'Median Response Time', 'Average Response Time', 'Min Response Time', 'Max Response Time', 'Average Content Size', 'Requests/s', 'Failures/s', '50%', '66%', '75%', '80%', '90%', '95%', '98%', '99%', '99.9%', '99.99%', '100%']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in sortedlist:
#         writer.writerow(row)