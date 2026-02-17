import ijson

INPUT_FILE = "conversations.json"
TMP_FILE = "conv_tmp.tsv"

with open(INPUT_FILE, "rb") as f, open(TMP_FILE, "w", encoding="utf-8") as out:
    # 欄位：create_time \t update_time \t title
    for conv in ijson.items(f, "item"):
        ct = conv.get("create_time")
        if ct is None:
            continue
        ut = conv.get("update_time") or ""
        title = (conv.get("title") or "(No Title)").replace("\t", " ").replace("\n", " ")
        out.write(f"{ct}\t{ut}\t{title}\n")

print("Done:", TMP_FILE)
