import requests,os
# 获取数据包和网页的信息
url = 'https://www.pearvideo.com/video_1762639'
contid = url.split('_')[1]
data_pag_url = f'https://www.pearvideo.com/videoStatus.jsp?contId={contid}&mrd=0.30432358432497475'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
    'Referer': url
}

res = requests.get(data_pag_url,headers=header)
dict = res.json()
srcUrl = dict['videoInfo']['videos']['srcUrl']
systemTime = dict['systemTime']

# 合成正确的视频链接

download_url = srcUrl.replace(systemTime,f'cont-{contid}')

download_res = requests.get(download_url)
# 下载视频
with open('a.mp4','wb') as f:
    f.write(download_res.content)
print('下载完成')
download_res.close()
res.close()

















