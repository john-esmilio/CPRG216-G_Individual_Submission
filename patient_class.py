"""
Assignment: Classes
Details: Alberta Hospital (AH) requires that their management system application meets the following criteria.
Author: John Esmilio
ID: 000654298
Date: Dec 09, 2022
Version: 2.0
"""

class Patient:
  
  def __init__(self):
    pass
  
  def formatPatientInfo(self, patient_list):
    # formats patient info to be put into the file
    format_patient = ''
    
    for patient_info in patient_list:
      patient_info = patient_info[0] + "_" + patient_info[1] + '_' + patient_info[2] + "_" + patient_info[3] + "_" + patient_info[4] + "\n"
      format_patient += patient_info
      
    return format_patient
  
  def enterPatientInfo(self):
    # Takes the users inputs for a new patient entry and returns the values
    self.pid = input("Enter Patient id:\n\n")
    self.name = input("Enter Patient name:\n\n")
    self.disease = input("Enter Patient disease:\n\n")
    self.gender = input("Enter Patient gender:\n\n")
    self.age = input("Enter Patient age:\n\n")
    return self.pid, self.name, self.disease, self.gender, self.age
  
  def readPatientsFile(self):
    # Opens the patients file and stores it into a patient list
    patient_list = []
    patients_obj = open("patients.txt", "r")
    
    for patients in patients_obj:
      patient_text = patients.strip().split("_")
      patient_list.append(patient_text)
      
    patients_obj.close()
    return patient_list
  
  def searchPatientById(self, patient_list):
    # Searches the patient list by the patient ID and formats the output
    pid = input(" Enter the Patient Id: \n\n")
    for patient in patient_list:
      if pid in patient:
        print(f"{patient[0]:<5} {patient[1]:<15} {patient[2]:<20} {patient[3]:<10} {patient[4]:<10}\n")
        return patient

    print("\nCan't find the Patient with the same id on the system\n")

  def displayPatientInfo(self):
    # Displays patient list
    Patient().displayPatientsList()
  
  def editPatientInfo(self, patient_list):
    pid = input("Please enter the id of the Patient that you want to edit their information: \n\n")
    # Takes the user ID and edits that user with the matching ID
    for edit_patient in patient_list:
      if pid in edit_patient:
        edit_patient[1] = input("\nEnter new Name:\n\n")
        edit_patient[2] = input("\nEnter new disease:\n\n")
        edit_patient[3] = input("\nEnter new gender: \n\n")
        edit_patient[4] = input("\nEnter new age: \n\n")

        """
        Stores the user edit into its original 
        position and is stored into the patient list
        """
        edited_patient = patient_list.index(edit_patient)
        patient_list[edited_patient] = edit_patient
        
        return patient_list
      
    print("\nCan't find the Patient with the same id on the system\n")

  def displayPatientsList(self, patient_list):
    display_patients_list = ''
    
    for patient in patient_list:
      # Displays the patient list to match the output format
      display_patients_list += f"{patient[0]:<5}{patient[1]:<15}{patient[2]:<20}{patient[3]:<10}{patient[4]:<10}\n\n"
      
    return display_patients_list
  
  def writeListOfPatientsToFile(self, format_patient):
    # Writes the edited or new patient to the original file
    patients_obj_write = open("patients.txt", 'w')
    patients_obj_write.write(format_patient)
    patients_obj_write.close()
    
  def addPatientToFile(self, patient_list):
    # takes the user info from .enterPatientInfo() and stores it into the list
    self.enterPatientInfo()
    add_patient = [self.pid, self.name, self.disease, self.gender, self.age]
    patient_list.append(add_patient)
    return patient_list
  
# Code to test the patients menu to be used in group submission
main_menu = "Back to the previous Menu"
patient_menu = True
patient_list = Patient().readPatientsFile()

while patient_menu:
  print("Patients Menu:")
  patient_input = input("1 - Display patients list \n2 - Search for patient by ID\n"
                        "3 - Add patient \n4 - Edit patient info \n5 - Back to the Main Menu\n\n")
      
  if patient_input == "1":
    # Displays patient list for the user
    print(Patient().displayPatientsList(patient_list))
    print(main_menu)
      
  elif patient_input == "2":
    # Searches for patient by their ID
    Patient().searchPatientById(patient_list)
    print(main_menu)
        
  elif patient_input == "3":
    #Adds patient info from the user, formats it, and writes the edit into the patient file
    add_new_patient = Patient().addPatientToFile(patient_list)
    format_new_patient = Patient().formatPatientInfo(add_new_patient)
    Patient().writeListOfPatientsToFile(format_new_patient)
    print(main_menu)

  elif patient_input == "4":
    #Edits patient info from the user, formats it, and writes the edit into the patient file
    edit_patient = Patient().editPatientInfo(patient_list)
    format_edited_patient = Patient().formatPatientInfo(edit_patient)
    Patient().writeListOfPatientsToFile(format_edited_patient)
    print(main_menu)
        
  elif patient_input == "5":
    # Back to the main menu
    patient_menu = False

  else:
    print("\nPlease enter the correct input.\n")
