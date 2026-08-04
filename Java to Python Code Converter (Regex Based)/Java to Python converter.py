import re

with open("input.java", "r") as file:
    code = file.read()


def convert_print_statement(code):
    """converts Java print statements into Python"""

    pattern = r'System\.out\.print(ln)?\((.+?)\);'

    def replacer(match):
        println = match.group(1)
        content = match.group(2).strip()

        if println:
            return f"print({content})"
        else:
            return f'print({content}, end="")'

    return re.sub(pattern, replacer, code)


def convert_loops(loop):
    """converts Java for loops into Python"""

    pattern = r'for\s*\(\s*(?:int\s+)?(\w+)\s*=\s*(\d+);\s*\1\s*<\s*(\d+);\s*\1\+\+\s*\)'

    def replacer(match):
        var_name = match.group(1)
        start = int(match.group(2))
        end = int(match.group(3))

        return f'for {var_name} in range({start}, {end}):'

    return re.sub(pattern, replacer, loop)


l = convert_loops(code)
print(l)

p = convert_print_statement(code)
print(p)