from urllib.request import urlopen

target_url = "https://artsandculture.google.com/search/asset/?p=van-gogh-museum&em=m015xrq&categoryId=art-movement"

page = urlopen(target_url)

