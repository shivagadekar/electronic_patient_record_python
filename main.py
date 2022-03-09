from tkinter import *
from tkinter import colorchooser
from datetime import datetime
from tkcalendar import DateEntry  # To add date as input/ Entry field
import json
import pandas as pd
"""
---------------------------------------------------Readme-------------------------------------------------------
Hello Guys, This is basic software program that is used for data entry purpose.
This software consists of basic OPD filling forms, which are necessary for initial treatment
This form, helps doctor to know patient better. 
By using this soft you can add, 
Name, Middle Name, Surname, Personal phone number, email, relative phone no, blood group,
any basic symptoms that are happening right now, then any other symptoms, Blood pressure, Sugar Level, 
Patient's work out status, eating habits, gender, then height, weight, covid positive status, vaccine status,
vision problem status, any type of color blindness with color selection(Lol).
Finally address. At each stage, comments will help you to understand purpose of code.
I know, there are many silly code blocks, that make no sense and comprehension can be done, but still 
this can be improved and there many effective ways of doing this. But it works, so i avoided to change it.
As time passes, and i will get to know more about python, i will upgrade the code similarly.
Thank you for Your Time, Enjoy my code"
-----------Future Upgrade May Include-----------
1. Keep Tracing of Previous visit symptoms, as this data overrides while updating data.
This will help doctor to understand patient more clearly.
2. This new feature will tell you about your bmi and caloric calculations if you are over or under weight.
3. This feature will help you to plan your diet and food consumption based on what food you eats.
4. After selecting birth date, program will automatically calculates your birth date and shows in window.
5. We will work on Improving user interface by setting calendar with drop down list, so no need to click hundred times
to select birth year of 1960
6. Useless entry tags will be removed
7. Will add, new feature saving user attachments in specific folder with same file name used as to save JSON file 

"""
# ---- Constants ------ #
# 1. Font For Labels
FONT_HEADER = ('Roboto Slab', 24, 'bold')
FONT = ('Roboto Slab', 12, 'bold')
FONT_SAVED = ('Arial', 8, 'bold')
# 2. Padding to Labels
PADX = 10
PADY = 10


# ---------------------------------------------- Converting into Excel ---------------------------------------------- #
# last_saved = '01_01_2021'
def add_date():
    """
    This function saves date, when user exports Exel File.
    File only included date of Exporting file.
    :return: This function returns nothing.
    """
    # currentSecond = datetime.now().second
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    data_to_save = f'{current_day}_{current_month}_{current_year}'
    with open('save_date.txt', 'w') as data:
        data.write(data_to_save)


def read_saved_date():
    """
    This function read's last saved date, when opens our program.
    File only contains date of Exporting file.
    :return: This function returns only date in string format
    """
    with open('save_date.txt', 'r') as read_data:
        read = read_data.read()
    last_saved_date = Label(text=read, font=FONT_SAVED)
    last_saved_date.grid(row=9, column=8)
    return read


def save_to_csv():
    """
    This function converts .txt file into .csv file for further processing.
    :return: This function generates .csv file in same folder structure
    """
    # Get data to Save File
    current_second = datetime.now().second
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    file_name = f'{current_second}_{current_day}_{current_month}_{current_year}.xlsx'
    read_file = pd.read_csv('bank_data.txt')
    read_file.to_csv('csv_file.csv', index=None)
    df_new = pd.read_csv('csv_file.csv')
    gfg = pd.ExcelWriter(file_name)
    df_new.to_excel(gfg, index=False)
    read__ = read_saved_date()
    last_saved_file = Label(text=read__, font=FONT_SAVED)
    last_saved_file.grid(row=9, column=8)
    add_date()
    gfg.save()
# ------------------------- Search User Data in JSON FILE AND ENTER ------------------------------------------------- #


def clear():
    """
    This function clears all false entry input, entered by user.
    :return: Returns nothing, works as backspace/ delete for all Entries.
    """
    # first_name_entry.delete(0, END)
    middle_name_entry.delete(0, END)
    # surname_entry.delete(0, END)
    relative_phone_number_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    other_symptoms_entry.delete(0, END)
    birth_date_entry.delete(0, END)
    blood_group_entry.delete(0, END)
    sugar_level_entry.delete(0, END)
    blood_pressure_entry.delete(0, END)
    weight_kg_entry.delete(0, END)
    height_entry.delete(0, END)
    address_entry.delete(0, END)


def search_user():
    """
    Basically this function searches user presence in our JSON file, for time saving.
    This function searches user based on their first name and last name.
    If true, then it automatically fills entries which are constant such as
        1. First Name, Middle Name, Surname
        2. Phone NO, Email, Relative Phone No,
        3. DOB, Blood Group, Address, Weight and Height
    :return: This function returns nothing but, autofill entries
    """
    user_name = f'{first_name_entry.get()}{surname_entry.get()}'.lower()
    clear()
    with open('bank_data.json') as data_file:
        data = json.load(data_file)
        if user_name in data:
            # first_name_af = data[user_name]['First Name']
            # first_name_entry.insert(0, first_name_af)
            middle_name_af = data[user_name]['Middle Name']
            middle_name_entry.insert(0, middle_name_af)
            # surname_name_af = data[user_name]['Surname']
            # surname_entry.insert(0, surname_name_af)
            phone_no_af = data[user_name]['Phone No']
            phone_number_entry.insert(0, phone_no_af)
            email_af = data[user_name]['Email']
            email_entry.insert(0, email_af)
            relative_ph_af = data[user_name]['Relative Phone No']
            relative_phone_number_entry.insert(0, relative_ph_af)
            blood_group_af = data[user_name]['Blood Group']
            blood_group_entry.insert(0, blood_group_af)
            # last_v_af = data[user_name]['Last Visit Symptoms']
            height_af = data[user_name]['Height']
            height_entry.insert(0, height_af)
            weight_af = data[user_name]['Weight']
            weight_kg_entry.insert(0, weight_af)
            # exercise_af = data[user_name]['Exercise Status']
            # food_af = data[user_name]['Food']
            address_af = data[user_name]['Address']
            address_entry.insert(0, address_af)
# save_to_csv()
# ----------------------------------------------- Function Definitions ---------------------------------------------- #


def save_data():
    # Get User Entered Data From Inputs
    get_first_name = first_name_entry.get()
    get_middle_name = middle_name_entry.get()
    get_surname = surname_entry.get()
    get_phone_no = phone_number_entry.get()
    get_email = email_entry.get()
    get_relative_phone = relative_phone_number_entry.get()

    get_symptoms_cough = 'Cough,' if symptom_var_cough.get() else ','
    get_symptoms_fever = 'Fever,' if symptom_var_fever.get() else ','
    get_symptoms_cold = 'Cold,' if symptom_var_cold.get() else ','
    get_symptoms_body_pain = 'Body Pain,' if symptom_var_bodyPain.get() else ','

    get_other_symptoms = other_symptoms_entry.get()
    get_blood_group = blood_group_entry.get()
    get_sugar_level = sugar_level_entry.get()
    get_blood_pressure = blood_pressure_entry.get()
    get_weight = weight_kg_entry.get()
    get_height = height_entry.get()
    get_address = address_entry.get()
    get_birth_date = birth_date_entry.get()
    # Local Variables
    person_gender = ''

    # Get Gender Status
    if var_gender.get() == 1:
        person_gender = 'Male'
    elif var_gender.get() == 2:
        person_gender = 'Female'
    elif var_gender.get() == 3:
        person_gender = 'Other'

    # Get Foodie Type/ Person Type
    if var_food.get() == 1:
        food_type = 'Veg'
    elif var_food.get() == 2:
        food_type = 'Non-Veg'
    else:
        food_type = 'Vegan'

    # Get Workout Status
    if var_exercise.get() == 1:
        exercise_status = 'Yes'
    elif var_exercise.get() == 2:
        exercise_status = 'No'
    else:
        exercise_status = 'Sometimes'

    # Get Covid positive Status
    if cov_pos_var.get() == 1:
        covid_status = 'Positive'
    else:
        covid_status = 'Negative'

    # Get Vaccinated Status
    vaccine_status = ''
    if vaccine_var.get() == 1:
        vaccine_status = 'First Dose Done'
    elif vaccine_var.get() == 2:
        vaccine_status = 'Second Dose Done'
    elif vaccine_var.get() == 3:
        vaccine_status = 'Need To Get Vaccinated'

    # Get Vision Problem Status

    if vision_prob.get() == 1:
        vision_prob_ = 'Yes'
    else:
        vision_prob_ = 'No'

    # Get Color Blindness
    if color_B_var.get() == 1:
        color_night_bn = 'Yes'
    else:
        color_night_bn = 'No'

    """
    Don't delete, If still code execution fails, then we will use this
    Initially this code was implemented to check whether user enters value or not, if he lefts entry blank
    then need to add comma in between two entries.
    """
    # Check Presence of Data inside Field
    # data_list = [get_first_name, get_middle_name, get_surname, get_phone_no, get_email,
    #              get_relative_phone, get_other_symptoms, get_blood_group, get_sugar_level,
    #              get_blood_pressure, get_weight, get_height, get_address, get_symptoms_cough, get_symptoms_fever,
    #              get_symptoms_cold, get_symptoms_body_pain, get_birth_date, person_gender, food_type,
    #              exercise_status, covid_status, vaccine_status, vision_prob_, color_night_bn]
    # for i in data_list:
    #     # print(len(i))
    #     if len(i) == 0:
    #         i = ','

# ------------------------- Save all user entered data in Text File ------------------------------------------------- #
    with open("bank_data.txt", 'a') as data:
        """
        This block of code, saves all entry data inside text file
        """
        data.write(
            f"{get_first_name},{get_middle_name},{get_surname},"  # No Errors After CSV to Excel
            f"{get_phone_no},{get_email},{get_relative_phone},"  # No Errors After CSV to Excel
            f"{get_symptoms_cough}{get_symptoms_fever}{get_symptoms_cold}{get_symptoms_body_pain}{get_other_symptoms},"
            f"{get_birth_date},{get_blood_group},{person_gender},"
            f"{get_sugar_level},{get_blood_pressure},{exercise_status},"
            f"{get_weight},{get_height},{food_type},"
            f"{covid_status},{vaccine_status},"
            f"{vision_prob_},{color_night_bn},"
            f"{get_address}\n")

# ------------------------- Save all user entered data in Text File ------------------------------------------------- #
    """
    At the same time of saving data in text file, we need to save some permanent data in JSON, for future use.
    So this, below block of code, saves data in JSON file.
    """
    fullname = get_first_name + get_surname
    fullname = fullname.lower()
    new_json_data = {
        fullname: {
            'First Name': get_first_name,
            'Middle Name': get_middle_name,
            'Surname': get_surname,
            'Phone No': get_phone_no,
            'Email': get_email,
            'Relative Phone No': get_relative_phone,
            'Last Visit Symptoms': [get_symptoms_cough, get_symptoms_fever, get_symptoms_cold, get_symptoms_body_pain,
                                    get_other_symptoms],
            'Birth Date': get_birth_date,
            'Blood Group': get_blood_group,
            'Gender': person_gender,
            'Sugar Level': get_sugar_level,
            'Blood Pressure': get_blood_pressure,
            'Exercise Status': exercise_status,
            'Weight': get_weight,
            'Height': get_height,
            'Food': food_type,
            'Vision Problem': vision_prob_,
            'Address': get_address,
        }
    }
    """This code doesn't save new data below old data, this opens old data, read it.
     then if same data name available, then save it"""
    with open('bank_data.json', 'r') as data_json:
        # Read Old Data
        read_data = json.load(data_json)
        # Updating Old Data with new Data
        read_data.update(new_json_data)

    with open('bank_data.json', 'w') as data:
        # Saving The Updated Data
        json.dump(read_data, data, indent=4)
        # json.dump(new_json_data, data, indent=4)
# -------------------------------- Clear Content From Entry Field --------------------------------------------------- #
    """ After saving entries, this entries serves no purpose, so delete these values instead"""
    first_name_entry.delete(0, END)
    middle_name_entry.delete(0, END)
    surname_entry.delete(0, END)
    relative_phone_number_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    other_symptoms_entry.delete(0, END)
    birth_date_entry.delete(0, END)
    blood_group_entry.delete(0, END)
    sugar_level_entry.delete(0, END)
    blood_pressure_entry.delete(0, END)
    weight_kg_entry.delete(0, END)
    height_entry.delete(0, END)
    address_entry.delete(0, END)

# ------------------------------------------------- Setting Window -------------------------------------------------- #


window = Tk()
window.title("Shivam Hospital Data Base")
window.maxsize(width=1366, height=768)
window.minsize(width=1366, height=768)
# --------------------------------------------------- Header Row ---------------------------------------------------- #
header = Label(text='Shivam Hospital and Medicals', font=FONT_HEADER)
header.grid(row=0, column=0, columnspan=8, sticky='w')
# --------------------------------------------------- First Row ----------------------------------------------------- #
# Display Function
# First Row
first_name = Label(text="First Name :", font=FONT, padx=PADX, pady=PADY, width=12)
first_name_entry = Entry(font=FONT, width=24)
first_name_entry.focus()
first_name_entry.insert(0, 'Shivam')
middle_name = Label(text="Middle Name :", font=FONT, padx=PADX, pady=PADY, width=12)
middle_name_entry = Entry(font=FONT)
surname = Label(text="Surname :", font=FONT, padx=PADX, pady=PADY, width=12)
surname_entry = Entry(font=FONT, width=30)
# Grid Functions
first_name.grid(row=1, column=0, sticky='w', padx=PADX, pady=PADY)
first_name_entry.grid(row=1, column=1, columnspan=2, sticky='w', padx=PADX, pady=PADY)
middle_name_entry.grid(row=1, column=4, padx=PADX, pady=PADY)
middle_name.grid(row=1, column=3, padx=PADX, pady=PADY)
surname.grid(row=1, column=5, padx=PADX, pady=PADY)
surname_entry.grid(row=1, column=6, columnspan=3, sticky='w', padx=PADX, pady=PADY)
# --------------------------------------------------- Second Row ---------------------------------------------------- #
# Display Function
# Second Row
phone_number = Label(text="Phone No :", font=FONT, padx=PADX, pady=PADY, width=12)
phone_number_entry = Entry(font=FONT, width=24)
email = Label(text="Email :", font=FONT, padx=PADX, pady=PADY, width=12)
email_entry = Entry(font=FONT)
relative_phone_number = Label(text="Relative Ph. No. :", font=FONT, padx=PADX, pady=PADY, width=12)
relative_phone_number_entry = Entry(font=FONT, width=30)

# Grid Functions
phone_number.grid(row=2, column=0, sticky='w', padx=PADX, pady=PADY)
relative_phone_number.grid(row=2, column=5)
email.grid(row=2, column=3)
email_entry.grid(row=2, column=4)
phone_number_entry.grid(row=2, column=1, columnspan=2, sticky='w', padx=PADX, pady=PADY)
relative_phone_number_entry.grid(row=2, column=6, columnspan=3, sticky='w', padx=PADX, pady=PADY)

# --------------------------------------------------- Third Row ----------------------------------------------------- #
symptom_var_cough = BooleanVar()
symptom_var_fever = BooleanVar()
symptom_var_cold = BooleanVar()
symptom_var_bodyPain = BooleanVar()

# Display Functions
# Third Row
symptoms = Label(text="Symptoms", font=FONT, padx=PADX, pady=PADY, width=12)
cough_CB = Checkbutton(text="Cough", font=FONT, width=11, variable=symptom_var_cough)
fever_CB = Checkbutton(text="Fever", font=FONT, width=11, variable=symptom_var_fever)
cold_CB = Checkbutton(text="Cold", font=FONT, width=11, variable=symptom_var_cold)
body_pain_CB = Checkbutton(text="Body Pain", font=FONT, width=11, variable=symptom_var_bodyPain)
other_symptoms = Label(text="Other Symptoms :", font=FONT, padx=PADX, pady=PADY, width=12)
other_symptoms_entry = Entry(font=FONT, width=30)

# Grid Functions
symptoms.grid(row=3, column=0, padx=PADX, pady=PADY)
cough_CB.grid(row=3, column=1, sticky='w')
fever_CB.grid(row=3, column=2, sticky='w')
cold_CB.grid(row=3, column=3, sticky='w')
body_pain_CB.grid(row=3, column=4, sticky='w')
other_symptoms.grid(row=3, column=5)
other_symptoms_entry.grid(row=3, column=6, columnspan=3, sticky='w', padx=PADX, pady=PADY)

# --------------------------------------------------- Fourth Row ---------------------------------------------------- #
var_gender = IntVar()
# Display Function
birth_date = Label(text="Birth Date :", font=FONT, padx=PADX, pady=PADY, width=12)
birth_date_entry = DateEntry(font=FONT, selectmode='year')
blood_group = Label(text="Blood Group :", font=FONT, padx=PADX, pady=PADY, width=12)
blood_group_entry = Entry(font=FONT)
gender = Label(text="Gender :", font=FONT, padx=PADX, pady=PADY, width=12)
male = Radiobutton(text='Male', variable=var_gender, value=1, font=FONT, width=6)
female = Radiobutton(text='Female', variable=var_gender, value=2, font=FONT, width=6)
other = Radiobutton(text='Other', variable=var_gender, value=3, font=FONT, width=6)
# num = int(year) - get_year()get_year
age = Label(text=f"Age : ", font=FONT, padx=PADX, pady=PADY, width=12)

# Grid Functions
birth_date.grid(row=4, column=0, sticky='w', padx=PADX, pady=PADY)
birth_date_entry.grid(row=4, column=1)
age.grid(row=4, column=2)
blood_group.grid(row=4, column=3)
blood_group_entry.grid(row=4, column=4)
gender.grid(row=4, column=5)
male.grid(row=4, column=6, sticky='w')
female.grid(row=4, column=7, sticky='w')
other.grid(row=4, column=8, sticky='w')

# --------------------------------------------------- Fifth Row ----------------------------------------------------- #
var_exercise = IntVar()
# Display Functions
sugar_level = Label(text="Sugar Level :", font=FONT, padx=PADX, pady=PADY, width=12)
sugar_level_entry = Entry(font=FONT, width=24)
blood_pressure = Label(text="Blood Pressure :", font=FONT, padx=PADX, pady=PADY, width=12)
blood_pressure_entry = Entry(font=FONT)
exercise = Label(text="Exercise :", font=FONT, padx=PADX, pady=PADY, width=12)
exercise_yes = Radiobutton(text='Yes', variable=var_exercise, value=1, font=FONT, width=6)
exercise_no = Radiobutton(text='No', variable=var_exercise, value=2, font=FONT, width=6)
exercise_sometimes = Radiobutton(text='Sometimes', variable=var_exercise, value=3, font=FONT, width=8)

# Grid Functions
sugar_level.grid(row=5, column=0, sticky='w', padx=PADX, pady=PADY)
sugar_level_entry.grid(row=5, column=1, columnspan=2, sticky='w', padx=PADX, pady=PADY)
blood_pressure_entry.grid(row=5, column=4)
blood_pressure.grid(row=5, column=3)
exercise.grid(row=5, column=5)
exercise_yes.grid(row=5, column=6, sticky='w')
exercise_no.grid(row=5, column=7, sticky='w')
exercise_sometimes.grid(row=5, column=8, sticky='w')

# --------------------------------------------------- Sixth Row ----------------------------------------------------- #
var_food = IntVar()
# Display Function
weight_kg = Label(text="Weight In Kg :", font=FONT, padx=PADX, pady=PADY, width=12)
weight_kg_entry = Entry(font=FONT, width=24)
bmi = Label(text="Food:", font=FONT, padx=PADX, pady=PADY, width=12)
height = Label(text="Height (CM):", font=FONT, padx=PADX, pady=PADY, width=12)

height_entry = Entry(font=FONT)
food_veg = Radiobutton(text='Veg', variable=var_food, value=1, font=FONT, width=8)
food_non_veg = Radiobutton(text='Non-Veg', variable=var_food, value=2, width=8, font=FONT)
food_vegan = Radiobutton(text='Vegan', variable=var_food, value=3, width=8, font=FONT)

# Grid Function
weight_kg.grid(row=6, column=0, sticky='w', padx=PADX, pady=PADY)
bmi.grid(row=6, column=5)
height.grid(row=6, column=3)
weight_kg_entry.grid(row=6, column=1, columnspan=2, sticky='w', padx=PADX, pady=PADY)
height_entry.grid(row=6, column=4)
food_veg.grid(row=6, column=6, sticky='w')
food_non_veg.grid(row=6, column=7, sticky='w')
food_vegan.grid(row=6, column=8, sticky='w')

# --------------------------------------------------- Seventh Row --------------------------------------------------- #
cov_pos_var = IntVar()
vaccine_var = IntVar()
# Display Functions
covid_positive = Label(text="Covid Positive :", font=FONT, padx=PADX, pady=PADY, width=12)
covid_positive_yes = Radiobutton(text='Yes', variable=cov_pos_var, value=1, font=FONT, width=8)
covid_positive_no = Radiobutton(text='No', variable=cov_pos_var, value=2, font=FONT, width=8)
vaccinated = Label(text="Vaccinated :", font=FONT, padx=PADX, pady=PADY, width=12)
vaccinated_first = Radiobutton(text='First', variable=vaccine_var, value=1, font=FONT, width=8)
vaccinated_second = Radiobutton(text='Second', variable=vaccine_var, value=2, font=FONT, width=8)
vaccinated_no = Radiobutton(text='No', variable=vaccine_var, value=3, font=FONT, width=8)

# Grid Functions
covid_positive.grid(row=7, column=0, sticky='w', padx=PADX, pady=PADY)
covid_positive_yes.grid(row=7, column=1, padx=PADX, pady=PADY)
covid_positive_no.grid(row=7, column=2, padx=PADX, pady=PADY)
vaccinated.grid(row=7, column=5)
vaccinated_first.grid(row=7, column=6)
vaccinated_second.grid(row=7, column=7)
vaccinated_no.grid(row=7, column=8)

# --------------------------------------------------- Eighth Row ---------------------------------------------------- #
vision_prob = IntVar()
color_B_var = IntVar()


def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    print(color_code)


# Display Functions
vision_problem = Label(text="Vision Problem :", font=FONT, padx=PADX, pady=PADY, width=12)
vision_prob_yes = Radiobutton(text='Yes', variable=vision_prob, value=1, font=FONT, width=8)
vision_prob_no = Radiobutton(text='No', variable=vision_prob, value=2, font=FONT, width=8)
color_B = Label(text="Blindness :", font=FONT, padx=PADX, pady=PADY, width=12)
color_B_yes = Radiobutton(text='Yes', variable=color_B_var, value=1, font=FONT, width=8)
color_B_no = Radiobutton(text='No', variable=color_B_var, value=2, font=FONT, width=8)
color_selector = Button(window, text="Color", command=choose_color, font=FONT)

# Grid Functions
vision_problem.grid(row=8, column=0, sticky='w', padx=PADX, pady=PADY)
vision_prob_no.grid(row=8, column=2, padx=PADX, pady=PADY)
vision_prob_yes.grid(row=8, column=1, padx=PADX, pady=PADY)
color_B.grid(row=8, column=5, sticky='w', padx=PADX, pady=PADY)
color_selector.grid(row=8, column=6)
color_B_yes.grid(row=8, column=7, sticky='w')
color_B_no.grid(row=8, column=8, sticky='w')

# --------------------------------------------------- Final Row ----------------------------------------------------- #
# Display Functions
# Ninth Row
address = Label(text="Address :", font=FONT, padx=PADX, pady=PADY, width=12)
address_entry = Entry(font=FONT, width=40)
save_button = Button(text="Save Data", width=10, font=FONT, command=save_data)
search_button = Button(text="Search", width=10, font=FONT, command=search_user)
clear_button = Button(text="Clear", width=10, font=FONT, command=clear)
save_to_excel_button = Button(text="To Excel", width=10, font=FONT, command=save_to_csv)
get_saved_date = read_saved_date()
last_saved = Label(text=get_saved_date, font=FONT_SAVED)

# Grid Functions
address.grid(row=9, column=0, sticky='w', padx=PADX, pady=PADY)
address_entry.grid(row=9, column=1, columnspan=4, rowspan=2, sticky='w')
save_button.grid(row=9, column=5, padx=PADX, pady=PADY)
search_button.grid(row=9, column=6, padx=PADX, pady=PADY)
clear_button.grid(row=9, column=4, padx=PADX, pady=PADY, sticky='e')
save_to_excel_button.grid(row=9, column=7, padx=PADX, pady=PADY)
last_saved.grid(row=9, column=8)

window.mainloop()
