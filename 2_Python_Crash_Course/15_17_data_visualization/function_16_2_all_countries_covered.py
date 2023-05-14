# 16-5 涵盖所有国家 ：本节制作人口地图时，对于大约12个国家，
# 程序不能自动确定其两个字母的国别码。请找出这些国家，
# 在字典COUNTRIES 中找到它们的国别码；然后，对于每个这样的国家，
# 都在get_country_code() 中添加一个if-elif 代码块，以返回其国别码

from pygal_maps_world.i18n import COUNTRIES
import json

# def national_judgements(country_name):
#     # 判断传入的国家参数是否在两位国家集中
#     if country_name in COUNTRIES.values():
#         return country_name

def get_country_code(country_name):
    """根据给定的国家返回两个字母的国别码"""
    # if national_judgements(country_name):
    for code,name in COUNTRIES.items():
        if country_name == name:
            return code
        # 手动把那几个国家找到然后再找出对应的两位国家代码真的好死亡
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        elif country_name == 'Dominica':
            return 'do'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Yemen, Rep.':
            return 'ye'
    
# def main():
#     # 载入国家人口的json文件，将读取得到的数据放入一个list中
#     filename = r"2_Python_Crash_Course\15_17_data_visualization\res\population_data.json"
    
#     with open(filename) as j_s:
#         pop_data = json.load(j_s)
    
#     # 遍历国家人口数据的list，取出2010年的数据
#     cc_pop = []
#     for pop_dict in pop_data:
#         if pop_dict["Year"] == "2010":
#             country_name = pop_dict["Country Name"]
#             name = get_country_code(country_name)
#             if name:
#                 cc_pop.append(name)
#     print(cc_pop,len(cc_pop))

# if __name__ == "__main__":
#     main()

















