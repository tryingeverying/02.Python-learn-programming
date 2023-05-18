import requests
import json

# 执行API调用并储存响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars'"
r = requests.get(url)
print("status code: ", r.status_code)

# 将API响应储存在一个变量中
response_dict = r.json()
# 由于预先在网页中得知返回的数据为json格式，
# 因此使用.json方法把json数据转换为python的dict

# 将得到的json数据写入到文件中
with open(r"2_Python_Crash_Course\15_17_data_visualization\res\response_data.json","w") as write_f:
    write_f.write(json.dumps(response_dict))


print("total repositories: " , response_dict["total_count"])


# 处理仓库的信息
repo_dicts = response_dict["items"]
print("Repositories returned:", len(repo_dicts))

print("\nSelected information about first repository:")

for repo_dict in repo_dicts:
    # 遍历所有的仓库信息
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])


print("\nkeys:" , len(repo_dicts))
for key in sorted(repo_dict.keys()):
    print(key)
# 处理结果
print(response_dict.keys())












