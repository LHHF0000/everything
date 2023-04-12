import requests

url = "https://search.douban.com/movie/subject_search?search_text=%E9%9F%A9%E5%AD%9D%E5%91%A8&cat=1002"

payload={}
headers = {
  'Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'same-site',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  'Referer': 'https://movie.douban.com/',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'll="108088"; bid=v6qsYXyxEtw; __gads=ID=b9ab4685ef1f3fe4-2252d7ecaecc00f5:T=1634737465:RT=1634737465:S=ALNI_MY8Q_KL2f_2lwTPBbBKkdTMiclSIw; douban-fav-remind=1; viewed="27080946"; gr_user_id=67ba6299-120d-4ca6-a6a7-c340c857ab20; __gpi=UID=000008e48d3770ab:T=1661179894:RT=1661393288:S=ALNI_MbFdhkmr1AvZ3yyKGALNwttg9dQoA; _pk_ref.100001.2939=%5B%22%22%2C%22%22%2C1661595780%2C%22https%3A%2F%2Fmovie.douban.com%2F%22%5D; _pk_id.100001.2939=e33eb2cb535e8397.1636174675.2.1661595875.1636174678.; __utma=30149280.1632434926.1645448101.1661595771.1661607970.8; __utmb=30149280.0.10.1661607970; __utmc=30149280; __utmz=30149280.1661607970.8.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0'
}
proxies = { "http": None, "https": None}
response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=proxies)

print(response.text)
