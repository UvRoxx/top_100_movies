import requests
from bs4 import BeautifulSoup

site = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
site = site.text
soup = BeautifulSoup(site, "html.parser")
print(soup.prettify())
titles = soup.find_all(name="h3", class_="title")
print(titles)
save_titles = [f"{title.text}\n" for title in titles]
save_titles[-1] = f"1) {save_titles[-1]}"
save_titles.reverse()
with open("top_100_movies.txt", "w") as file:
    file.writelines(save_titles)
print("Done 🤖")