def load_patient_data():
    """This function takes in all the patient data from a test_data.txt file.

    :returns: list of patient objects
    """
    data_file = open("test_data.txt", "r")
    still_finding_patients = True
    my_patients = []
    while still_finding_patients is True:
        name_line = next(data_file)
        if name_line != "END":
            name_line = name_line.split()
            fname = name_line[0]
            lname = name_line[1]
            age = next(data_file).strip()
            gender = next(data_file).strip().casefold()
            tsh_data = next(data_file)
            tsh_data = tsh_data.strip().split(",")
            tsh_data.remove("TSH")
            new_patient = create_patient(fname, lname, age, gender, tsh_data)
            output_patient(new_patient)
            my_patients.append(new_patient)
        else:
            still_finding_patients = False
    data_file.close()
    return my_patients


def create_patient(firstname, lastname, age, gender, tsh_data):
    """This function creates a patient object.

    :param firstname: string of patient's first name
    :param lastname: string of patient's last name
    :param age: string of patient's age
    :param gender: string of patient's gender (male or female)
    :param tsh_data: list of strings of various tsh data from the patient

    :returns: patient object with each parameter as a property
    """
    new_patient = {"First": firstname,
                   "Last": lastname,
                   "Age": age,
                   "Gender": gender,
                   "TSH Data": tsh_data}
    return new_patient


def output_patient(patient):
    """This function outputs onto the commond line information about the patient.

    :param patient: patient object containing various properties
    """
    print("{} {} is a {} years old {}.".format(patient["First"],
                                               patient["Last"],
                                               patient["Age"],
                                               patient["Gender"],))
    print("Their TSH records are: {}.".format(patient["TSH Data"]))


def main_code():
    """Main code: accomplished the goals of the homework assignment
    """
    load_patient_data()


if __name__ == "__main__":
    main_code()
