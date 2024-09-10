# cis6930fa24 -- Assignment0
Name - Rushit Varma Gadiraju

Description
In this assignment we have to create a python package where we have to extract data from a given API and JSON formatted and reform it in Thorn-seperated format and print the output.

How to install
Pip install pipenv
Create the directory - mkdir cise6930fa24-assignment0
                                   Cd cise6930fa24-assignment0
Pipenv —python 3.10
Pipenv install requests
Write the code in main.py - download data from FBI API
                                            Load data from file
                                            Parse the loaded data
                                            Print the thorn separated data
                                            Main function to run
Create json file
Run the code -  pipenv run python main.py —page 1

Functions
download_data(page).    This function download data from FBI API
load_from_file.    This function reads json file 
parse_dtaa(data).  This function processes the JSON data from API and extracts (title, subjects, and field_offices) then formats them as thorn-separate values
print_data(thorn_seperated_data).  This function prints the thorn-separated data
main(). This function processes the data

Main.py
                                           download data from FBI API
                                            Load data from file
                                            Parse the loaded data
                                            Print the thorn separated data
                                            Main function to run

Bugs 
Type Error - the error occurs because some fields in the data may not be in a list format or maybe None. The code assumes these fields are always lists, which leads to error
Error handling

Assumptions
FBI API structures - the code assumes API response always contains the “items”, “title”, “subject”, and “field_offices”. If the api changes its structure the code ll fail.
API response size - the download_data function assumes that the api will return a manageable amount of data for each page and processes it.
