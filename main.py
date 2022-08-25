import json

import requests

url = "https://graphql.haraj.com.sa/?queryName=initialPosts&lang=en&token=&clientId=IYKP8glX-meFM-Bg2V-K1P6-U464UA4UoTbov3&version=8.2.1%20,%202%2022%20-%208%20-%2022/"

payload = "{\"query\":\"query($city:String,$page:Int) { posts( city:$city, page:$page) {\\n\\t\\titems {\\n\\t\\t\\tid status authorUsername title city postDate updateDate hasImage thumbURL authorId\\n\\t\\t}\\n\\t\\tpageInfo {\\n\\t\\t\\thasNextPage\\n\\t\\t}\\n\\t\\t} }\",\"variables\":{\"city\":\"الرياض\",\"page\":2}}".encode("UTF-8")
headers = {
  # 'Content-Type':'text/plain; charset=utf-8',
  'Referer':'https://haraj.com.sa/',
  'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
  'sec-ch-ua-mobile':'?0',
  'sec-ch-ua-platform':'"Windows"',
  'trackId':'eyJjaXR5Ijoi2KfZhNix2YrYp9i2In0=',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
  'Cookie': 'AWSALB=9vWJwMcaBaZ6w9ct99Gb4hebC4vf4+Gl5rggU+2/OXnk3Tw9gV1htdAsplnaAM58txFY35f6cZfcr7wcdnhQ/ESnosRU8VZFkb0qEb7NIdAJjvOIBZ5XR2YNOgxG; AWSALBCORS=9vWJwMcaBaZ6w9ct99Gb4hebC4vf4+Gl5rggU+2/OXnk3Tw9gV1htdAsplnaAM58txFY35f6cZfcr7wcdnhQ/ESnosRU8VZFkb0qEb7NIdAJjvOIBZ5XR2YNOgxG; AWSALBTG=FxAoiZFloV8Avy/y+L6pZ7FzgA/dG+zzd/Mr5Wuy0fhDRZbbUAcsziZvovRv/O7spOlNq23JXp+6Hh3ERFMri3042VfYf8KLB2ZYxoyLs3g/Wu/UV2pubqSbcxedxstRq2bc3pDVx4j+vedK2sSE/sYznCTBSraewTifI+KxUoNdMpyYuWM=; AWSALBTGCORS=FxAoiZFloV8Avy/y+L6pZ7FzgA/dG+zzd/Mr5Wuy0fhDRZbbUAcsziZvovRv/O7spOlNq23JXp+6Hh3ERFMri3042VfYf8KLB2ZYxoyLs3g/Wu/UV2pubqSbcxedxstRq2bc3pDVx4j+vedK2sSE/sYznCTBSraewTifI+KxUoNdMpyYuWM='
}

response = requests.request("POST", url, headers=headers, data=payload)


json_data = json.loads(response.text)
print(json_data)


items = {}

# data.posts.items[0].id

for data in json_data['data']['posts']['items']:
  id = data['id']
  authorUsername = data['authorUsername']

  items['id'] = id
  items['authorUsername'] = authorUsername
  print(items)


def hello():
  print("Vrushabh")

if __name__ == '__main__':
    hello()

