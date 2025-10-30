# Create a function called format_name() that takes two inputs: f_name and `l_name'.
# Use the title() function to modify the f_name and l_name parameters into Title Case.

def format_name(f_name, l_name):
    full_name = f"{f_name.title()} {l_name.title()}"
    return full_name

formatted_name = format_name("RenZO", "MIYATERA")
print(formatted_name)
