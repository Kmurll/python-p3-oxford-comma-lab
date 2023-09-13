def oxford_comma(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return f"{arr[0]} and {arr[1]}"
    else:
        oxford_string = ', '.join(arr[:-1])
        oxford_string += f", and {arr[-1]}"
        return oxford_string
