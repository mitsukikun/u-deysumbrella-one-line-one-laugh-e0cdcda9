import os

line = ("I asked the mirror who the fairest of them all was. "
        "It said, 'That's a question for my lawyer.'")

# Entry must stay within the 140-character limit.
assert len(line) <= 140

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
