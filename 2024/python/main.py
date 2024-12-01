from sys import argv
import git
from requests import get

day = argv[1]
example = len(argv) > 2

def get_input():
    url = f"https://adventofcode.com/2024/day/{day}/input"
    with open(f"{root}/token.txt", "r") as token:
        day_input = get(url, headers={"Cookie": "session=" + token.read()}).text

        return day_input


if __name__ == "__main__":
    git_repo = git.Repo(".", search_parent_directories=True)
    root = git_repo.working_tree_dir
    package_name = f'day{day if len(day) > 1 else "0" + day}'
    package_day = __import__(package_name)
    if example:
        package_day.test()
    else:
        day_input = get_input()
        package_day.run(day_input)
