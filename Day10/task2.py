# Create a function called format_name() that takes two inputs: f_name and `l_name'.
# Use the title() function to modify the f_name and l_name parameters into Title Case.
# Create a return when the user doesn't provide any value, and at the end of the function to return the formatted name
# Create a Docstring for this function

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("RenZO", "MIYATERA"))
print(format_name("", ""))
