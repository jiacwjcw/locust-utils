import csv, operator

with open('./1639549331-sta-wap-api-stats-data.csv',newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    sortedlist = sorted(spamreader, key=lambda row:(float(row['Failures/s'])), reverse=True)

for i in range(10):
        item = sortedlist[i]
        if item['Type']:
            print(f"{item['Type']} {item['Name']}")
            print("- Failure Rate: %.2f" % float(item['Failures/s']))
        else:
            continue

with open('sorted.csv', 'w') as f:
    fieldnames = ['Type', 'Name', 'Failures/s', 'Average Response Time', 'Request Count', 'Failure Count', 'Median Response Time', 'Min Response Time', 'Max Response Time', 'Average Content Size', 'Requests/s', '50%', '66%', '75%', '80%', '90%', '95%', '98%', '99%', '99.9%', '99.99%', '100%']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    i = 0
    for row in sortedlist:
        if i<10:
            writer.writerow(row)
            i+=1
        else:
            break
    

# with open('sorted.csv', 'w') as f:
#     fieldnames = ['Type', 'Name', 'Request Count', 'Failure Count', 'Median Response Time', 'Average Response Time', 'Min Response Time', 'Max Response Time', 'Average Content Size', 'Requests/s', 'Failures/s', '50%', '66%', '75%', '80%', '90%', '95%', '98%', '99%', '99.9%', '99.99%', '100%']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in sortedlist:
#         writer.writerow(row)