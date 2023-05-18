import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)

chart.title = "python projects"

chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
 {'value': 16101, 'label': 'Description of httpie.'},
{'value': 15028, 'label': 'Description of django.'},
{'value': 14798, 'label': 'Description of flask.'},
]
# 使用与'label' 相关联的字符串给条形创建工具提示。
chart.add('', plot_dicts)
chart.render_to_file(r'2_Python_Crash_Course\15_17_data_visualization\img\bar_descriptions.svg')











