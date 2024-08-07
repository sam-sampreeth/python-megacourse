ft_in = input("Enter feet and inches: ")


def convert(ft_in_local):
    parts = ft_in_local.split(' ')
    ft = float(parts[0])
    inc = float(parts[1])
    mtrs = ft * 0.3048 + inc * 0.0254
    return mtrs


res = convert(ft_in)
if res < 1.0:
    print("Not allowed")
else:
    print("Allowed")
