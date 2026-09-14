# amit = {'python' , 'java' , 'git' , 'linux'}

# rahul = {'sql' ,'c++','python','java'}

# priya = {'sql' , 'python' , 'machinlearning','java'}

# unique = amit |  rahul
# print(unique)

# unique2 = unique ^ priya
# print(unique2)



# # output = {machinlearning ,c++,git,linux}

# import requests

# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9,hi;q=0.8,gu;q=0.7',
#     'cache-control': 'max-age=0',
#     'if-modified-since': 'Wed, 08 Feb 2023 21:02:32 GMT',
#     'if-none-match': 'W/"63e40de8-c85e"',
#     'priority': 'u=0, i',
#     'sec-ch-ua': '"Google Chrome";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'none',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36',
# }

# response = requests.get('https://books.toscrape.com/', headers=headers)
# print(response.status_code)
# print(response.text)