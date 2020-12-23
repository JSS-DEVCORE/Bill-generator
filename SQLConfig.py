import time

pwd = input("Enter your sql password: ")

try:

    f = open('SQL Dump/db.txt', 'w')
    f.write(pwd)
    f.close()
    print('Successfully updated password')
    time.sleep(10)

except:

    print('Unable to fetch configuration file')
    time.sleep(10)
