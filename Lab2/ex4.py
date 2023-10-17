def camel_case_to_snake_case(input_str):
    output_str = ""
    
    for char in input_str:
        if char.isupper():
            output_str += "_"
            output_str += char.lower()
        else:
            output_str += char
    
    if output_str.startswith("_"):
        output_str = output_str[1:]
    
    return output_str

input_str = input("Introduceți un șir în UpperCamelCase: ")
snake_case_str = camel_case_to_snake_case(input_str)

print(f"Șirul în snake_case este: {snake_case_str}")
