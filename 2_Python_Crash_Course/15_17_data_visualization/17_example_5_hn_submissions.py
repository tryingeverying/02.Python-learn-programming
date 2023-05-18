import requests
from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

print("status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
print(submission_ids[:5])
child_dicts = []
for submission_id in submission_ids[:30]:
    # 获取上个url中的数据,用以组合成新的child_url
    child_url = ('https://hacker-news.firebaseio.com/v0/item/' +
                str(submission_id) + '.json')
    child_r = requests.get(child_url)
    print(child_r.status_code)
    child_respose_dict = child_r.json()

    child_dict = {
        "title": child_respose_dict["title"],
        "link":'http://news.ycombinator.com/item?id=' + str(submission_id),
        "comments":child_respose_dict.get("descendants",0)
        # .get("descendants",0)在指定的键(descendants)不存在时返回你指定的值(0)
    }
    child_dicts.append(child_dict)

child_dicts = sorted(child_dicts, key=itemgetter("comments"), reverse=True)
# operator 中的函数itemgetter() 向这个函数传递了键'comments' ，
# 因此它将从这个列表的每个字典中提取与键'comments' 相关联的值。
# 这样，函数sorted() 将根据这种值对列表进行排序。
for child_dict in child_dicts:
    print("\nTitle:", child_dict["title"])
    print("Discussion link:", child_dict["link"])
    print("comment:",child_dict["comments"])













