import pprint

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")
# print(soup.a) Retrieves links
# print(soup.find('a'))find first item
# print(soup.find(id="score_37989875"))
# print(soup.select("#score_37989875"))  # selecting using id in css
# print(soup.select(".score"))  # selecting using class in css

links = soup.select(".titleline")  # [0] get first item in the wbe page
subtext = soup.select(".subtext")
# votes = soup.select(".score")


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


# print(votes[0].get("id"))
def creat_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 200:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


pprint.pprint(creat_custom_hn(links, subtext))
