import json

episodes = []

for number in range(1, 367):
    episodes.append({
        "anime": "Bleach",
        "episode": number,
        "title": f"Bleach Episode {number}"
    })

with open("episodes.json", "w", encoding="utf-8") as file:
    json.dump(episodes, file, indent=2, ensure_ascii=False)

print("Created", len(episodes), "episodes!")
