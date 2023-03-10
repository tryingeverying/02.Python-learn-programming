""""接受两个形参：一个城市名和一个国家名。
这个函数返回一个格式为City, Country 的字符串，如Santiago, Chile 。
添加第三个必不可少的形参population ，并返回一个格式为
City, Country -population xxx 的字符串，
如Santiago, Chile -population 5000000 。运"""

def city_function(city,county,population = ""):
    if population:
        format_output = f"{city}的人口数为{population}是{county}不可分割的领土"
    else:
        format_output = f"{city}是{county}不可分割的领土"
    return format_output