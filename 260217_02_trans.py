from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))
IN_FILE = "conv_sorted.tsv"
OUT_FILE = "conversation_list_sorted.csv"

def fmt(ts):
    if ts == "" or ts is None:
        return ""
    return datetime.fromtimestamp(float(ts), JST).strftime("%Y-%m-%d %H:%M:%S")

with open(IN_FILE, "r", encoding="utf-8") as f, open(OUT_FILE, "w", encoding="utf-8") as out:
    out.write("No,Title,Create Time (JST),Update Time (JST)\n")
    for i, line in enumerate(f, start=1):
        ct, ut, title = line.rstrip("\n").split("\t", 2)
        out.write(f'{i},"{title}",{fmt(ct)},{fmt(ut)}\n')

print("Done:", OUT_FILE)
