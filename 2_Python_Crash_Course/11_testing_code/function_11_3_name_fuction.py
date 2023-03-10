'''函数添加中间名的判断'''
def get_formatted_name(first,last,middle = ''):
    '''将姓和名组合在一起'''
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()