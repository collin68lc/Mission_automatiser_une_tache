import requests
import csv
import os

from bs4 import BeautifulSoup
from urllib.parse import urljoin


base_url = 'https://books.toscrape.com/index.html'


def get_product(url):
    """
    Return informations about one book from given url.
    """
    response = requests.get(url)
    with open ('index.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    soup = BeautifulSoup(response.content, "html.parser")
     
    
    upc = soup.find('td').string
    title = soup.find('li', class_="active" ).text
    price_ttc = soup.find('p', class_='price_color').text
    price_ht = soup.find_all('td')[2].text
    availability = soup.find('p', class_='instock availability').text.strip()
    product_description = soup.find_all("p")[3].text
    category = soup.find("ul", class_="breadcrumb").find_all("a")[2].text
    review_rating = soup.find("p", class_= "star-rating")
    classes = review_rating['class']
    image_url = soup.find("div", class_= "item active").find("img")['src']
    image_url_absolute = urljoin(url, image_url)
    # conversion letter number in number
    ratings = {
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5
    }
    review_rating_number=ratings[classes[1]]

    infos = {
        "upc" : upc,
        "title" : title,
        "price ttc": price_ttc,
        "price ht" : price_ht,
        "availability": availability,
        "product_description": product_description,
        "category": category,
        "review_rating": review_rating_number,
        "image_url": image_url_absolute
    }
    return infos


def get_category_urls(category_url):
    """
    Return all book urls from one category.
    """
    urls_category = []
    current_url = category_url   # Scraped url changed from next page
    
    while True:
        response = requests.get(current_url)
        with open ('index.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        # find all book url in one category and add to the list
        book = soup.find("ol", class_='row').find_all("h3")
        for links in book:
            urls = links.a['href']
            urls_absolute = urljoin(category_url, urls) # urljoin give the absolute url
            urls_category.append(urls_absolute)
        # find "next button" for having the next page url and stop if "next button" is not present
        next_page = soup.find('li', class_='next')
        if next_page is None : break
        next_href = next_page.a['href']
        current_url = urljoin(current_url, next_href)


    return (urls_category)    
    
    
def get_categories(base_url):
  
    """
    Return url of all category
    """
    categories_dict = {}

    response = requests.get(base_url)
    with open ('index.html', 'w', encoding='utf-8') as f:
       f.write(response.text)
    soup = BeautifulSoup(response.content, "html.parser")

     
    liens = soup.find("ul", class_="nav nav-list").find_all("a")
    for lien in liens[1:]:   
        category_name = lien.text.strip()          # le texte affiché du lien, nettoyé des espaces
        category_href = lien["href"]                # le href relatif
        category_url = urljoin(base_url, category_href)   # transformé en absolu
        
        categories_dict[category_name] = category_url    # on ajoute la paire au dictionnaire

    return categories_dict


def csv_file(products, category_name):
    """
    Save informations of books in a list 
    """
    with open("products informations"+category_name+".csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)


def download_image(image_url, filename):
    """
    downloading books pictures
    """
    os.makedirs("pictures", exist_ok= True)
    response = requests.get(image_url)
    path_file = os.path.join("pictures", filename + ".jpg")
    with open (path_file, 'wb') as f:
           f.write(response.content)


def main():
    categories = get_categories(base_url)
    
    for nom_categorie, url_categorie in categories.items():
        print(f"Scraping catégorie : {nom_categorie}")
        urls_produits = get_category_urls(url_categorie)
        
        products = []

        for actual_url in urls_produits:
            infos = get_product(actual_url)
            clean_title = infos["title"].replace("/", "-").replace("#", "-")
            products.append(infos)
            image = download_image(infos["image_url"], clean_title +"("+infos["upc"]+")"+".jpg")
        csv_file(products, nom_categorie)
    
            





if __name__ == '__main__':
    main()
