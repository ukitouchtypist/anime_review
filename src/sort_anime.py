# coding: utf-8
import re

def main() :
        anime_titles = []
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

def ranked_anime_extract(start_rank, stop_rank) :
    with open("anime_weekly.md", mode="r", encoding="utf_8") as f :
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
    patterns = [re.compile(r"^###\s(.+?)\s第\d{,2}[話幕夜]"), re.compile(r"^###\s(.+?)\sEPISODE\s\d{,2}"), re.compile(r"^###\s(.+?)\sChapter\s\d{,2}"), re.compile(r"###\s(.+?)\s\d{,2}羽目"), re.compile(r"###\s(.+?)\s終わり")]
    for pattern in patterns :
        m = pattern.match(row)
        if m :
            return m.group(1)

if __name__ == '__main__' :
    main()
