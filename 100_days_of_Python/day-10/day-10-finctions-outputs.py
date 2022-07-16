#functions with outputs


def format_name(f_name, l_name):
    formated_f_name = print(f_name.title())
    formated_l_name = print(l_name.title())
    return f"Result: {formated_f_name } {formated_l_name}"
    
print(format_name(input("What is your first name?: "), input("What is your last name?: ")))  
