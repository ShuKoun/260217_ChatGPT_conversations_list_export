import ijson

INPUT_FILE = "/Users/user01/Library/Mobile Documents/com~apple~CloudDocs/20231225_inbox/260212_01_chatgpt01_backup_01/b33a994df128ffad992db1bfac6de93f0411465f4d13bfb4377bc6c0e9c6227f-2026-02-10-14-26-34-b7a4dedae62048369f9e6409c22f54e1/conversations.json"
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
