import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并且存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=star"
r = requests.get(url)
print("status code: ", r.status_code)

# 将API的相应存储到一个变量中
response_dict = r.json()

print("total repositories: ", response_dict["total_count"])

# 研究有关的仓库信息
repo_dicts = response_dict['items']
print("Number of items: ", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        "value":repo_dict["stargazers_count"],
        "label":repo_dict['description'],
        # 在点击柱状图时显示仓库的全名
        "xlink":repo_dict["html_url"]
        # 在点击图像的柱状图时直接到链接到对应的连接地址
    }
    
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
# 将较长的项目名缩短为15个字符
my_config.show_y_guides = False
# 隐藏图表中的水平线
my_config.width = 1000

chart = pygal.Bar(my_config, style = my_style)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "most_starred python projects on github"
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file(r"2_Python_Crash_Course\15_17_data_visualization\img\python_repos_2.svg")

























