def parse(ft_in_local):
    parts = ft_in_local.split(' ')
    ft = float(parts[0])
    inc = float(parts[1])
    return {"feet": ft, "inches": inc}


def convert(ft, inc):
    mtrs = ft * 0.3048 + inc * 0.0254
    return mtrs
