import requests
from bs4 import BeautifulSoup
import json
import os


def stage1():
    url = input("Input the URL: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "content" in data:
                print(data["content"])
            else:
                print("Invalid quote resource!")
        else:
            print("Invalid quote resource!")
    except Exception:
        print("Invalid quote resource!")


def stage2():
    url = input("Input the URL: ")
    try:
        headers = {'Accept-Language': 'en-US,en;q=0.5'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200 and "title" in url:
            soup = BeautifulSoup(response.content, 'html.parser')
            title_tag = soup.find('title')
            title = ""
            if title_tag is not None:
                title = title_tag.text.strip()
                if " - IMDb" in title:
                    title = title.replace(" - IMDb", "")
            meta_desc = soup.find('meta', {'name': 'description'})
            description = ""
            if meta_desc is not None:
                description = meta_desc.get('content', "").strip()
            if title and description:
                result = {"title": title, "description": description}
                print(json.dumps(result))
            else:
                print("Invalid movie page!")
        else:
            print("Invalid movie page!")
    except Exception:
        print("Invalid movie page!")


def stage3():
    url = input("Input the URL: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("source.html", "wb") as file:
                file.write(response.content)
            print("Content saved.")
        else:
            print(f"The URL returned {response.status_code}!")
    except Exception:
        print("The URL returned error!")


def stage4():
    base_url = "https://www.nature.com/nature/articles"
    params = {
        "sort": "PubDate",
        "year": "2022",
        "page": "3"
    }
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('article')
            saved_files = []
            for article in articles:
                type_span = article.find('span', {'data-test': 'article.type'})
                if type_span and "News" in type_span.text:
                    link = article.find('a', {'data-track-action': 'view article'})
                    if link:
                        article_url = "https://www.nature.com" + link.get('href', '')
                        article_response = requests.get(article_url)
                        if article_response.status_code == 200:
                            article_soup = BeautifulSoup(article_response.content, 'html.parser')
                            body_div = article_soup.find('div', {'class': 'c-article-body'})
                            if body_div:
                                title = link.text.strip()
                                for p in '.,!?;:()[]{}"\'':
                                    title = title.replace(p, '')
                                title = title.replace(' ', '_')
                                filename = f"{title}.txt"
                                with open(filename, "w", encoding="utf-8") as f:
                                    f.write(body_div.text.strip())
                                saved_files.append(filename)
            print(f"Saved articles: {saved_files}")
        else:
            print("Failed to fetch articles")
    except Exception:
        print("Failed to fetch articles")


def stage5():
    try:
        num_pages = int(input())
        article_type = input()

        for page in range(1, num_pages + 1):
            os.makedirs(f"Page_{page}", exist_ok=True)
            base_url = "https://www.nature.com/nature/articles"
            params = {
                "sort": "PubDate",
                "year": "2022",
                "page": str(page)
            }
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                articles = soup.find_all('article')
                for article in articles:
                    type_span = article.find('span', {'data-test': 'article.type'})
                    if type_span and article_type in type_span.text:
                        link = article.find('a', {'data-track-action': 'view article'})
                        if link:
                            article_url = "https://www.nature.com" + link.get('href', '')
                            article_response = requests.get(article_url)
                            if article_response.status_code == 200:
                                article_soup = BeautifulSoup(article_response.content, 'html.parser')
                                body_div = article_soup.find('div', {'class': 'c-article-body'})
                                if not body_div:
                                    body_div = article_soup.find('div', {'class': 'article__body'})
                                if body_div:
                                    title = link.text.strip()
                                    for p in '.,!?;:()[]{}"\'':
                                        title = title.replace(p, '')
                                    title = title.replace(' ', '_')
                                    filename = f"Page_{page}/{title}.txt"
                                    with open(filename, "w", encoding="utf-8") as f:
                                        f.write(body_div.text.strip())
        print("Saved all articles.")
    except Exception:
        print("Error occurred")


def main():
    print("Choose stage (1-5):")
    stage = input("> ")
    if stage == "1":
        stage1()
    elif stage == "2":
        stage2()
    elif stage == "3":
        stage3()
    elif stage == "4":
        stage4()
    elif stage == "5":
        stage5()
    else:
        print("Invalid stage")


if __name__ == "__main__":
    main()