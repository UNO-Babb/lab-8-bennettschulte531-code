#ProcessData.py
#Name:Bennett Schulte
#Date:11/1/2025
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  header = inFile.readline()

  for line in inFile:
    parts = line.strip().split()

    if len(parts) < 7:
      continue

    firstName = parts[0]
    lastName = parts[1]
    email = parts[2]
    studentID = parts[3]
    dob = parts[4]
    year = parts[5]
    major = parts[6]

    firstInitial = firstName[0]
    lastThree = studentID[-3:]
    userID = firstInitial + lastName + lastThree

    if len(lastName) < 5:
      userID += "X"

    majorShort = major[:3].upper()

    yearLower = year.lower()
    if "fresh" in yearLower:
      yearShort = "FR"
    elif "soph" in yearLower:
      yearShort = "SO"
    elif "jun" in yearLower:
      yearShort = "JR"
    elif "sen" in yearLower:
      yearShort = "SR"
    else:
      yearShort = "NA"

    majorYear = majorShort + "-" + yearShort
  
    outLine = f"{lastName},{firstName},{userID},{majorYear}\n"
    outFile.write(outLine)

  
  



  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
