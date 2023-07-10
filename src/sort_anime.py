# coding: utf-8
import re
import argparse

def main() :
        any_rank_animes = []
        ranks = ["AAA", "AA", "A", "B", "C", "D", "E", "F"]
        any_rank_animes.append(list(dict.fromkeys(ranked_anime_extract("AAA", "AA"))))
        any_rank_animes.append(list(dict.fromkeys(ranked_anime_extract("AA", "A"))))
        any_rank_animes.append(list(dict.fromkeys(ranked_anime_extract("A", "B"))))
        any_rank_animes.append(list(dict.fromkeys(ranked_anime_extract("B", "C"))))
        any_rank_animes.append(list(dict.fromkeys(ranked_anime_extract("C", "D"))))
        any_rank_animes.append(list(dict.fromkeys(ranked_anime_extract("D", "E"))))
        any_rank_animes.append(list(dict.fromkeys(ranked_anime_extract("E", "F"))))
        any_rank_animes.append(list(dict.fromkeys(ranked_anime_extract("F", "切った"))))
        for i in range(len(any_rank_animes)) :
            print_rank_and_count(any_rank_animes[i], ranks[i])
            print_ranked_animes(any_rank_animes[i])

def print_ranked_animes(ranked_animes) :
    ranked_and_split_animes = [ranked_animes[i:i+3] for i in range(0, len(ranked_animes), 3)]
    for line in ranked_and_split_animes :
        for title in line :
            print("「" + title + "」", end="")
        print()

def print_rank_and_count(ranked_animes, rank) :
    print("## {rank}({count}作品)".format(rank=rank, count=str(len(ranked_animes))))

def fetch_file_name_from_args() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type=str, default="anime_weekly.md")
    return parser.parse_args().i

def ranked_anime_extract(start_rank, stop_rank) :
    file_name = fetch_file_name_from_args()
    with open(file_name, mode="r", encoding="utf_8") as f :
        article_rows = [l.strip() for l in f.readlines()]
        ranked_anime_titles = []
        article_end_pattern = re.compile(r"^## 切った$")
        start_row = "## " + start_rank
        start_index = article_rows.index(start_row)
        stop_row = "## " + stop_rank
        stop_index = article_rows.index(stop_row)
        for row in article_rows[start_index:stop_index] :
            if article_end_pattern.match(row) :
                return ranked_anime_titles
            title = extract_title(row)
            if title :
                ranked_anime_titles.append(title)
        return ranked_anime_titles


def extract_title(row) :
    patterns = [
        re.compile(r"^###\s(.+?)\s第\d{,2}[話幕夜場]"),
        re.compile(r"^###\s(.+?)\s第[壱一弐二参三肆四伍五陸六漆七捌八玖九拾十陌百阡千萬万億兆京]{,2}[話幕夜場]"),
        re.compile(r"^###\s(.+?)\s\d{,2}缶め"),
        re.compile(r"^###\s(.+?)\sEPISODE[\\.\s]\d{,2}"),
        re.compile(r"^###\s(.+?)\sシフト[\\.\s]\d{,2}"),
        re.compile(r"^###\s(.+?)\sLv[\\.\s]\d{,2}"),
        re.compile(r"^###\s(.+?)\s【karte\d{,2}】"),
        re.compile(r"^###\s(.+?)\sMISSION:\d{,2}"),
        re.compile(r"^###\s(.+?)\sChapter[\\.\s]\d{,2}"),
        re.compile(r"^###\s(.+?)\sScene[\\.\s]\d{,2}"),
        re.compile(r"^###\s(.+?)\schapter[\s]\d{,2}"),
        re.compile(r"###\s(.+?)\s\d{,2}羽目"),
        re.compile(r"###\s(.+?)\s【すてっぷ[①-⑫]】"),
        re.compile(r"###\s(.+?)\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\."),
        re.compile(r"^###\s(.+)"),
    ]
    for pattern in patterns :
        m = pattern.match(row)
        if m :
            return m.group(1)

if __name__ == '__main__' :
    main()
