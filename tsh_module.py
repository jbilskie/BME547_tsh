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
                   "TSH Data": tsh_data,
                   "TSH Result": "unknown"}
    return new_patient


def output_patient(patient):
    """This function outputs onto the commond line information about the patient.

    :param patient: patient object containing various properties
    """
    print("{} {} is a {} years old {}.".format(patient["First"],
                                               patient["Last"],
                                               patient["Age"],
                                               patient["Gender"],))
    print("TSH data: {}.".format(patient["TSH Data"]))
    print("{} {}'s result is {} .\n".format(patient["First"],
                                          patient["Last"],
                                          patient["TSH Result"],))
    return


def declare_result(patient):
    """This function outputs whether the patient has hyper/hypothyroidism or not.

    :param patient: patient object containing various properties

    :returns: output string of diagnosis
    """
    patient["TSH Data"].sort()
    if float(patient["TSH Data"][-1]) > 4:
        result = 'hypothyroidism'
    elif float(patient["TSH Data"][0]) < 1:
        result = 'hyperthyroidism'
    else:
        result = 'normal thyroid function'
    return result


def file_output(patient):
    """This function outputs into a json the patient information.

    :param patient: patient object containing various properties
    """
    import json
    out_file = open("{}-{}.json".format(patient["First"], patient["Last"]),"w")
    patient_dictionary = {}
    patient_dictionary["First Name"] = patient["First"]
    patient_dictionary["Last Name"] = patient["Last"]
    patient_dictionary["Age"] = patient["Age"]
    patient_dictionary["Gender"] = patient["Gender"]
    patient_dictionary["Diagnosis"] = patient["TSH Result"]
    patient_dictionary["TSH"] = patient["TSH Data"]
    json.dump(patient_dictionary, out_file)
    out_file.close()
    return


def main_code():
    """Main code: accomplished the goals of the homework assignment
    """
    my_patients = load_patient_data()
    for patient in my_patients:
        result = declare_result(patient)
        patient["TSH Result"] = result
        output_patient(patient)
        file_output(patient)


if __name__ == "__main__":
    main_code()
