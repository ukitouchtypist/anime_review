# coding: utf-8
import re

def main() :
    new_rows = []
    with open("anime_weekly.md", mode="r", encoding="utf_8") as f :
        article_rows = [l.strip() for l in f.readlines()]
        include_pattern = re.compile(
            r"^評価:\s[A-F]{,3}\s→(\s[A-F]{,3})?$|" +
            r"^評価:(\s[A-F]{,3})?$|" +
            r"^#|" +
            r"^\[←前回\]|" +
            r"\)\s次回→$|" +
            r"^次回→$|" +
            r"^\*\*\*$")
        end = "## 切った"
        end_index = article_rows.index(end)
        for row in article_rows :
            if row == end :
                break
            if include_pattern.match(row) :
                new_rows.append(row)
        new_rows.extend(article_rows[end_index:])
    with open("anime_weekly.md", mode="w", encoding="utf-8", newline="\n") as f :
        for row in new_rows :
            f.write(row + "\n")

if __name__ == '__main__' :
    main()
