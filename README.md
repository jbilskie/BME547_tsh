# bme547tsh
Repository for TSH Test Data Conversion homework in BME 547

tsh_module.py is the module containing functionality for TSH diagnosis.
Functionality is included for:
- reading a data file of patient information
- storing that information as patient objects with properties of first name, last name, age, gender, and data
- outputting patient information onto the command line
- diagnosing hyper/hypothyroidism on the basis that hypo includes a TSH reading of > 4 and hyper includes a TSH reading of < 1
- creating patient specific json files with their information, diagnosis, and organized TSH readings

test_tsh.py includes the test for this project.
Tests included are:
- can a patient object be created correctly
- can a hypothyroid diagnosis be properly made
- can a hyperthyroid diagnosis be properly made
