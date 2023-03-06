'''9-12 多个模块 ：将User 类存储在一个模块中，
并将Privileges 和Admin 类存储在另一个模块中。再创建一个文件，
在其中创建一个Admin 实例，并对其调用方法show_privileges() ，
以确认一切都依然能够正确地运行。'''

from function_9_7_Admin import Admin

a_admin = Admin("大","狗子",18,)
a_admin.describe_user()
a_admin.privileges.show_privileges()