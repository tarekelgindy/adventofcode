import sys
import requests
day = sys.argv[1]
headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'cookie':'_ga=GA1.2.2109716982.1606792659; _gid=GA1.2.1723703142.1606792659; session=53616c7465645f5f2733974bd807f5fdcd0a0aabb1eb558a26249e8b1a01328ff640d0213d13a4660255a2e5eab4b2f8',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'cache-control': 'max-age=0'
}
res = requests.get(f'https://adventofcode.com/2020/day/{day}/input', headers=headers)
print(res.text)
