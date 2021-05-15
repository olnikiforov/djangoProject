"""Fill posts module by beautifulsoup."""

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from main.models import Post
import requests


class Command(BaseCommand):
    """Parse random posts from doroshenkoaa."""

    url = "https://doroshenkoaa.ru/med/"

    def handle(self, *args, **options):
        """Parse url."""
        Post.objects.all().delete()
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        link_lst = []
        for lst in soup.findAll("a", {"class": "more"}):
            link_lst.append(lst.get('href'))
        for lst in link_lst:
            r = requests.get(lst)
            soup = BeautifulSoup(r.text, "html.parser")
            for con in soup.findAll("div", {"itemprop": "articleBody"}):
                content = con.text
            for tit in soup.findAll("h1", {"itemprop": "headline"}):
                title = tit.text.strip()
            Post.objects.create(title=title, content=content)
