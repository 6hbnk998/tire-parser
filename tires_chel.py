
import requests
import json

headers ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'X-Is-Ajax-Request': 'X-Is-Ajax-Request',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json, text/javascript, */*; q=0.01'
}



def get_data():
    url = 'https://skinport.com/ru/market?cat=Knife'
    r = requests.get(url=url, headers=headers)

    # with open('tires_chel.html', 'w') as file:
    #     file.write(r.text)
    # with open('tires.json', 'a', encoding='utf-8') as file:
    #     json.dump(r.json(), file, indent=4 ,ensure_ascii=False)

    pages_count = r.json()['pageCount']

    data_list = []

    for i in range(1, 2):
        url = f'https://roscarservis.ru/catalog/legkovye/?isAjax=true&PAGEN_1={pages_count}'
        
        r =requests.get(url=url,headers=headers)
        data = r.json()
        items = data["items"]

        possible_stores = ['discountStores','fortochkiStores','commonStores']
        total_amount = 0

        for item in items:
            item_name = item["name"]
            item_price = item["price"]
            item_img = 'https://roscarservis.ru'+item["imgSrc"]
            item_url = 'https://roscarservis.ru'+item['url']


        


            stores = []
            for ps in possible_stores:
                if ps in item:
                    if item[ps] is None or len(item[ps]) <1:
                        continue
                    else:
                        for store in item[ps]:
                            store_name = store['STORE_NAME']
                            store_price = store ['PRICE']
                            store_amount = store['AMOUNT']
                            total_amount += int(store['AMOUNT'])

                            stores.append(
                                {
                                    "store_name": store_name,
                                    "store_price": store_price,
                                    "store_amount": store_amount
                                }
                            )


            data_list.append(
                        {
                            "name": item_name,
                            "price": item_price,
                            "url": item_url,
                            "img_url": item_img,
                            "stores": stores,
                            "total_amount": total_amount
                        }
                    )

    print(f"[INFO] Обработал {i}/{pages_count}")

    with open("data_1.json", "a") as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)



def main():
    get_data()
if __name__=="__main__":
    main()