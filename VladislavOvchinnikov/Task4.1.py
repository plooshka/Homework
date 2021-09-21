def change_quotation_marks(input_str: str) -> str:
    """The function which receives a string and replaces all " symbols with ' and vise versa"""

    changed_string = ""
    for char in input_str:
        if char == "'":
            changed_string += "\""
        elif char == "\"":
            changed_string += "'"
        else:
            changed_string += char
    return changed_string


print(change_quotation_marks("'Привет' '''\"машина \"BMW\"!!!"))
