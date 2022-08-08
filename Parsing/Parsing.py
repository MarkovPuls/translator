import json
from bs4 import BeautifulSoup
import requests

# a = open('webinars.json', 'r', encoding='utf-8')
# b = json.load(a)
# var = [i['name'] for i in b]
# print(*var, sep='|')

# g = open('skillbox.html', 'r', encoding='utf-8')
# html = g.read()
# soup = BeautifulSoup(html, features="html.parser")
# links = soup.findAll('a')
# print(*[i.string.strip() for i in links], sep='\n')

# pro = requests.get('https://yandex.ru/')
# yat = BeautifulSoup(pro.content, features="html.parser")
# water = yat.findAll(class_='direct-desktop__logo')
# print(water.string.strip())

""" Парсим сайт auto.ru и получаем данные о машине """


def fetch(url, params):  # params = {method, headers, body}
    headers = params["headers"]
    body = params["body"]
    method = params["method"]

    if method == "POST":
        return requests.post(url, headers=headers, data=body)

    if method == "GET":
        return requests.get(url, headers=headers)


car = fetch("https://auto.ru/-/ajax/desktop/listing/", {
    "headers": {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "same-origin",
        "sec-fetch-site": "same-origin",
        "x-client-app-version": "95.0.9767920",
        "x-client-date": "1658942334011",
        "x-csrf-token": "098cf57581bc3406ca6ec8ea2f52c730a4289c0045fb93b2",
        "x-kl-ajax-request": "Ajax_Request",
        "x-page-request-id": "2ec04167ea90e27ea63a20040e9ab1a5",
        "x-requested-with": "XMLHttpRequest",
        "x-retpath-y": "https://auto.ru/moskva/cars/plymouth/all/",
        "x-yafp": "{\"a1\":\"YtIs26HgPmaOFw==;0\",\"a2\":\"9xbmEsxorsQmzzJh2s+bsViFbMiPiQ==;1\","
                  "\"a3\":\"XAZUXdmg6wtN8FNgCmIIXQ==;2\","
                  "\"a4\":\"h6/l9xTFusG2Vs5i779/Y+lQfsHOPMbIDjK0ccVybvRcsw==;3\",\"a5\":\"ORYIXSzLvciFFg==;4\","
                  "\"a6\":\"RWE=;5\",\"a7\":\"f/SzMjSF18ZOyA==;6\",\"a8\":\"Gh1010RJtfo=;7\","
                  "\"a9\":\"saEIlLtw8+e6YA==;8\",\"b1\":\"8D55UFKmIXI=;9\",\"b2\":\"6UTJTguvQsqYnA==;10\","
                  "\"b3\":\"7vXeroGqng5A1g==;11\",\"b4\":\"mKWX/izAWp0=;12\",\"b5\":\"G7iRIkviLo2ouA==;13\","
                  "\"b6\":\"k2Mm0xP0gr06QA==;14\",\"b7\":\"JCoD/6ole/CxtQ==;15\",\"b8\":\"ko9pTnBQw7jiqQ==;16\","
                  "\"b9\":\"3Gzhnr0pt76pQw==;17\",\"c1\":\"r/ZV3w==;18\",\"c2\":\"VqTumvkOtTCd/IZKylacKebq;19\","
                  "\"c3\":\"vj60fsmjfBhF67RL6pxuBSRV;20\",\"c4\":\"ARcjKjK15SY=;21\",\"c5\":\"dm+180bOENw=;22\","
                  "\"c6\":\"rSr3ag==;23\",\"c7\":\"yY1WfWggY2Y=;24\",\"c8\":\"Cfs=;25\",\"c9\":\"OXcUKEfwMuM=;26\","
                  "\"d1\":\"nl4vf6/CN3w=;27\",\"d2\":\"wC4=;28\",\"d3\":\"3UZ1KJYG7iJbtg==;29\","
                  "\"d4\":\"DBxWNMiIY2k=;30\",\"d5\":\"mkaIlaKGqlU=;31\",\"d7\":\"W8k01PHi18c=;32\","
                  "\"d8\":\"BQXacXUMTlYGRNS495fNa+GZXfVvPyHfYiY=;33\",\"d9\":\"Bw3FG0CthnI=;34\","
                  "\"e1\":\"HMJjLvaiNGxbpg==;35\",\"e2\":\"2Yvf0Fm4Ak4=;36\",\"e3\":\"5iRVRwxYXDY=;37\","
                  "\"e4\":\"DNTwiIobmDU=;38\",\"e5\":\"lQlo58ZFCV06cw==;39\",\"e6\":\"2SImXnZysus=;40\","
                  "\"e7\":\"TuPrnBZWz0FyPQ==;41\",\"e8\":\"0DdXx1k9GN0=;42\",\"e9\":\"XmYJSmqGzUU=;43\","
                  "\"f1\":\"HoCXCpZSXTK1lg==;44\",\"f2\":\"TBCgdLM8RJ4=;45\",\"f3\":\"/eruSt+pymOU3A==;46\","
                  "\"f4\":\"wP4lPFFgr4s=;47\",\"f5\":\"k2NiuLXj8kbyaQ==;48\",\"f6\":\"2ORfMNnCIgFO7g==;49\","
                  "\"f7\":\"ACDNszqynPtF/w==;50\",\"f8\":\"UeuuBCUhtDBqrA==;51\",\"f9\":\"5X7r+3p83EM=;52\","
                  "\"g1\":\"VVWUIjnaVkcDRw==;53\",\"g2\":\"o9avbI0yDiMZUw==;54\",\"g3\":\"iPB9yQR0Dcc=;55\","
                  "\"g4\":\"guBc+5yVwSh0Sw==;56\",\"g5\":\"1fC3iIAvB+8=;57\",\"g6\":\"+p/KeTYOXzc=;58\","
                  "\"g7\":\"fo/LE6+9QqQ=;59\",\"g8\":\"wFyy+ZqdXhQ=;60\",\"g9\":\"3KCIc5u/YXA=;61\","
                  "\"h1\":\"TbCe42W7ipnLhg==;62\",\"h2\":\"LRlsbdSbAntPog==;63\",\"h3\":\"zFF+YmqTIvRegA==;64\","
                  "\"h4\":\"M0OwV0mYlbR1Og==;65\",\"h5\":\"m1VKjNf3JB4=;66\",\"h6\":\"vU+6l/DqngoQiw==;67\","
                  "\"h7\":\"5ufLo06VOr92rRE4sZZfV/bgVmAmh7kDcYjVGjLQf/P+j/z/;68\",\"h8\":\"unwI979BX4xR5g==;69\","
                  "\"h9\":\"fP3MT7ptXQ25FA==;70\",\"i1\":\"2B76SteyevY=;71\",\"i2\":\"UM3z3iyhO4jf/w==;72\","
                  "\"i3\":\"W7DOxHyTR5Iztw==;73\",\"i4\":\"Wk2VVM/+na4BoA==;74\",\"i5\":\"rsHg/guPoG6f9g==;75\","
                  "\"z1\":\"kBVaUIGpsP+0umT+9/s82JaXR/ZFc9HuLgnh+sMDwpHIHdtWl9VzOpdJQN6BTyuVCn7eK6rtpBXD2d7UqW50Uw"
                  "==;76\","
                  "\"z2\":\"jDhYkGmy3o8N3NkIlqkWyGfke0DW0KvBj3cOcdUKvIq9S1MOp7TKn7q1XN5mfxoVVvrWNhkKt3FhtP7tDWWsdA"
                  "==;77\",\"y2\":\"ZZ95PbHbmas16Q==;78\",\"y3\":\"b6wjL6R9urfWLQ==;79\","
                  "\"y6\":\"8ph/Wze0o44OEw==;80\",\"y8\":\"K0DAUkZ5LJtmCw==;81\",\"x4\":\"tBACNyx3vPnnIg==;82\","
                  "\"z5\":\"gDFUzCa8puc=;83\",\"z4\":\"lY2KhITKsm33gw==;84\",\"z6\":\"mMMLkkprgHltNS1O;85\","
                  "\"z7\":\"KLiBOqlvpv84wrNI;86\",\"z8\":\"lZ+uhIDva/5EupvPHrA=;87\",\"z9\":\"JgoEmIEvYyQkgXld;88\","
                  "\"y1\":\"+NmAZ8+/w2AqIQFb;89\",\"y4\":\"bT+4kuRG2b+aJKRO;90\",\"y5\":\"Nx03BU5JkRB0j6OjPdU=;91\","
                  "\"y7\":\"hoj29CpK20TSSFei;92\",\"y9\":\"UdEjrT97SzmdOlMIjqw=;93\","
                  "\"y10\":\"5m/BGt0+Jnq1b2zGYSY=;94\",\"x1\":\"fsfE0nMXFwUwOWCn;95\","
                  "\"x2\":\"FqqJ6cb+Gs6bO1X/lyE=;96\",\"x3\":\"VCcjEAlBuY3iOjBH;97\",\"x5\":\"wZEBahwQn8oL3Hly;98\","
                  "\"z3\":\"D2GC3ADoqQTo2KYQaIUr2Th7y0TSqw9xUFoAiS/TIbU=;99\",\"v\":\"6.3.1\","
                  "\"pgrdt\":\"fRKHOZT0gKYwIu/XmWeix+b6tl0=;100\","
                  "\"pgrd\":\"i41b/3pML9YQqkBXtsWo7EjPGKYoqFYASDA7QqrQ/9I9agiP93iT+6nHd5OVgYgeUnbQJ0"
                  "+5XFiEqKo7THvOf6i4enWdgLM1MsNXmEYldOIKJKo7M2DJterw5tj/aY1ImxLdsf/fv0q8KRn3yalQthK"
                  "/nkvpKYJxAt3lQkhSbS/TcqcmV6A17LcSoGjS9bw+aV+pakE3225YJUfVdBngFZ/9QEQ=\"}",
        "cookie": "_csrf_token=098cf57581bc3406ca6ec8ea2f52c730a4289c0045fb93b2; "
                  "autoru_sid=a%3Ag62e16fb7226tnif6ce4tah17ao2av2r.f249fc70c03b87d22d47c93eafc282b9%7C1658941367717"
                  ".604800.Q2rCBbaWo9rwTsOmuVo6Ng.j6aC8jrhcTt_5mH2CfMAkMmuHnbLWdKUYuK3p-es8b4; "
                  "autoruuid=g62e16fb7226tnif6ce4tah17ao2av2r.f249fc70c03b87d22d47c93eafc282b9; "
                  "suid=5dc327a76b678606ef90050d2957ac5a.271e97e79162269a30d760f28bf2942a; from=morda; "
                  "salon_phone_utms=utm_medium%3D%26utm_source%3Dmain_stripe_big%26utm_campaign%3D%26utm_content%3D; "
                  "yuidlt=1; yandexuid=1123147201654537767; my=YwA%3D; Session_id=noauth:1658941369; yandex_login=; "
                  "ys=wprid.1658648333590510-10849291738702308974-sas6-5250-e7c-sas-l7-balancer-8080-BAL-3257"
                  "%23c_chck.2416974469#c_chck.2560554081; "
                  "i=PXPPgugq9eY31rer5SeTtZ9kGpiPq5+I57RBn30Updjbb//Kxg4OSCHzONDN+LSrfBHx9XWiWcXCLvyvet/qh22AaWs=; "
                  "mda2_beacon=1658941369240; gdpr=0; sso_status=sso.passport.yandex.ru:synchronized; "
                  "_ym_uid=1658941370619440438; _ym_isad=2; _yasc=y4npKcQpED1pklbo6bsSu0vMRjD8ipOdzOEMfLlxkkjV0Tn6; "
                  "_ym_d=1658941437; from_lifetime=1658941437844",
        "Referer": "https://auto.ru/moskva/cars/plymouth/all/",
        "Referrer-Policy": "no-referrer-when-downgrade"
    },
    "body": "{\"catalog_filter\":[{\"mark\":\"PLYMOUTH\"}],\"section\":\"all\",\"category\":\"cars\","
            "\"output_type\":\"list\",\"geo_radius\":200,\"geo_id\":[213]}",
    "method": "POST"
});

# Вставляем данные из "Node.js fetch". Далее отбираемся по json по любым параметрам.

car_data = car.json()
print('Всего машин:', len(car_data['offers']))
for i in car_data['offers']:
    print(
        f'Car {i["vehicle_info"]["tech_param"]["human_name"]}, '
        f'Mileage: {i["state"]["mileage"]}, Price: {i["price_info"]["EUR"]}')
