def split_and_join(line):
    a = line.split(" ")
    b = "-".join(a)
    return(b)
if _name_ == '_main_':
    line = input()
    result = split_and_join(line)
    print(result)
