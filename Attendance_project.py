from datetime import datetime
import csv



def csv_input(n):
    no = 0
    for i in range(n):
        no=no+1
        print(f'Enter student info {no}')
        sub = input('Enter Your Subject: ')
        name = input('Enter Your Name: ')
        dt = datetime.now().strftime('%y-%m-%d')
        std_data = [sub,name,dt]
        with open('std_data.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(std_data)
        
def csv_output():
    with open('std_data.csv','r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            
noOfStudents = int(input('How many students : '))
csv_input(noOfStudents)
csv_output()