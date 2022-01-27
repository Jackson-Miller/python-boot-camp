from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(response, "html.parser")

# find the JSON data at the end of the code
json_data = soup.find(name="script", type="application/json").getText()

# convert the JSON data into a dictionary
json_data_dict = json.loads(json_data)

# dive deep into the data and get hold of the titleText :O)
title_list = []
for counter in range(0, 100):
    title_list.append(json_data_dict["props"]["pageProps"]["data"]["getArticleByFurl"]
                      ["_layout"][7]["content"]["images"][counter]["titleText"])

title_list_reversed = title_list[::-1]

with open("movie_list_top100.txt", "w") as file:
    file.writelines("%s\n" % title for title in title_list_reversed)