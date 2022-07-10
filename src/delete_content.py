# coding: utf-8
import re

def main() :
    new_rows = []
    with open("anime_weekly.md", mode="r", encoding="utf_8") as f :
        article_rows = [l.strip() for l in f.readlines()]
        include_pattern = re.compile(r"(^評価:\s[A-F]{,3}\s→\s[A-F]{,3}$|^評価:(\s[A-F]{,3})?$|^#{,3}\s[A-F]{,3}|^\[←前回\]|\)\s次回→$)")
        end_pattern = re.compile(r"^## 切った$")
        for row in article_rows :
            if end_pattern.match(row):
                break
            if include_pattern.match(row) :
                new_rows.append(row)
    with open("anime_weekly.md", mode="w", encoding="utf-8") as f :
        for row in new_rows :
            f.write(row + "\n")

if __name__ == '__main__' :
    main()
