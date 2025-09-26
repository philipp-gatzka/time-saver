import json
import os
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Issue:
    title: str
    body: str
    labels: List[str]
    milestone: str
    inserted: bool

def read_issues(filepath: str) -> List[Issue]:
    with open(filepath, 'r') as f:
        data = json.load(f)
        return [Issue(**issue) for issue in data]

def write_body_to_file(body: str, filepath: str = "temp.md"):
    with open(filepath, "w") as f:
        f.write(body)

def main():
    issues = read_issues('issues.json')
    non_inserted_issues = [issue for issue in issues if not issue.inserted]
    for issue in non_inserted_issues:
        write_body_to_file(issue.body)
        labels = ','.join(issue.labels)

        command = f"gh issue create --title \"{issue.title}\" --body-file \"temp.md\" --assignee \"@me\" --project \"Timesaver\" --milestone \"{issue.milestone}\" --label \"{labels}\""
        if os.system(command) == 0:
            issue.inserted = True
            with open('issues.json', 'w') as f:
                json.dump([vars(i) for i in issues], f, indent=2)

if __name__ == "__main__":
    main()
