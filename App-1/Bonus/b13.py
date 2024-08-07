ft_in = input("Enter feet and inches: ")


def parse(ft_in_local):
    parts = ft_in_local.split(' ')
    ft = float(parts[0])
    inc = float(parts[1])
    return {"feet": ft, "inches": inc}


def convert(ft, inc):
    mtrs = ft * 0.3048 + inc * 0.0254
    return mtrs


parsed = parse(ft_in)
res = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} = {res}")
if res < 1.0:
    print("Not allowed")
else:
    print("Allowed")
