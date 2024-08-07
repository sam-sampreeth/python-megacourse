from subfiles.b14modules import parse, convert

ft_in = input("Enter feet and inches: ")
parsed = parse(ft_in)
res = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches = {res}")
if res < 1.0:
    print("Not allowed")
else:
    print("Allowed")
