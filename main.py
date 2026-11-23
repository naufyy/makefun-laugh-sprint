import os

LINE = "My houseplant has survived three years of my care — less a plant now, more a hostage with excellent negotiation skills."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
