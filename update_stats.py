import requests
from collections import Counter
import os

USERNAME = "chanho99"
README_PATH = "README.md"

def fetch_solved_problems(username):
    problems = []
    page = 1
    while True:
        url = f"https://solved.ac/api/v3/search/problem?query=solved_by:{username}&page={page}"
        res = requests.get(url)
        if res.status_code != 200:
            break
        data = res.json()
        problems += data["items"]
        if data["count"] < 50:
            break
        page += 1
    return problems

def count_difficulty(problems):
    level_map = {
        0: "Unrated", 1: "Bronze V", 2: "Bronze IV", 3: "Bronze III", 4: "Bronze II", 5: "Bronze I",
        6: "Silver V", 7: "Silver IV", 8: "Silver III", 9: "Silver II", 10: "Silver I",
        11: "Gold V", 12: "Gold IV", 13: "Gold III", 14: "Gold II", 15: "Gold I",
        16: "Platinum V", 17: "Platinum IV", 18: "Platinum III", 19: "Platinum II", 20: "Platinum I",
        21: "Diamond V", 22: "Diamond IV", 23: "Diamond III", 24: "Diamond II", 25: "Diamond I",
        26: "Ruby V", 27: "Ruby IV", 28: "Ruby III", 29: "Ruby II", 30: "Ruby I"
    }
    level_counter = Counter(p["level"] for p in problems)
    return {level_map[k]: v for k, v in sorted(level_counter.items())}

def count_tags(problems):
    tag_counter = Counter()
    for p in problems:
        for tag in p["tags"]:
            tag_counter[tag["key"]] += 1
    return dict(tag_counter.most_common(10))  # 상위 10개만

def inject_into_readme(difficulty_data, tag_data):
    def format_table(title, data_dict):
        table = f"\n### {title}\n\n| 항목 | 문제 수 |\n|------|---------|\n"
        for k, v in data_dict.items():
            table += f"| {k} | {v} |\n"
        return table

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = "<!-- STATS_START -->"
    end_tag = "<!-- STATS_END -->"

    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)

    if start_idx == -1 or end_idx == -1:
        raise ValueError("README.md에 <!-- STATS_START --> 와 <!-- STATS_END --> 태그를 포함시켜주세요.")

    stats_section = format_table("📊 난이도 분포", difficulty_data) + format_table("🏷️ 태그 분포", tag_data)

    new_content = (
        content[:start_idx + len(start_tag)]
        + "\n" + stats_section + "\n"
        + content[end_idx:]
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    problems = fetch_solved_problems(USERNAME)
    diff = count_difficulty(problems)
    tags = count_tags(problems)
    inject_into_readme(diff, tags)

if __name__ == "__main__":
    main()
