# coding: utf-8
import re

def main() :
    sorted_anime_titles = []
    with open("anime_weekly.md", mode="r", encoding="utf_8") as f :
        article_rows = [l.strip() for l in f.readlines()]
        anime_titles = []
        extract_title_pattern = re.compile(
            r"^###\s(.+?)\s第\d{,2}[話幕夜]|" +
            r"^###\s(.+?)\sEPISODE\s\d{,2}|" +
            r"^###\s(.+?)\sChapter\s\d{,2}")

if __name__ == '__main__' :
    main()
