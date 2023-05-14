# 制作地图前，还需要解决数据存在的最后一个问题。
# Pygal中的地图制作工具要求数据为特定的格式：
# 用国别码表示国家，以及用数字表示人口数量。
# 处理地理政治数据时，经常需要用到几个标准化国别码集。
# population_data.json中包含的是三个字母的国别码，
# 但Pygal使用两个字母的国别码。我们需要想办法根据国家名获取两个字母的国别码

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据给定的国家返回两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果不存在该国家返回空值
    return None


















