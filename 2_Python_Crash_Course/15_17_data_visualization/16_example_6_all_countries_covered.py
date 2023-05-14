import json
from function_16_2_all_countries_covered import get_country_code
import pygal_maps_world.maps
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# 将数据加载到一个list中
filename = r'2_Python_Crash_Course\15_17_data_visualization\res\population_data.json'

# 将数据加载到一个list中
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口数量将国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 打印每个分组的国家数量
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3),)

wm = pygal_maps_world.maps.World()
# wm_style =RS("#336699", base_style = LCS)
wm_style = pygal.style.RotateStyle("#3366AA", base_style = pygal.style.LightColorizedStyle)

wm.title = 'world population in 2010, by country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bm', cc_pops_2)
wm.add('> 1bm', cc_pops_3)
# Pygal根据这些数字自动给不同国家着以深浅不一的颜色
# （人口最少的国家颜色最浅，人口最多的国家颜色最深）

wm.render_to_file(r'2_Python_Crash_Course\15_17_data_visualization\img\world_population_all_country.svg')

