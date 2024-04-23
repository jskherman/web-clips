import os

snapshots_dir = os.path.join(os.getcwd(), "snapshots")

html_files_with_non_ascii = [
    f
    for f in os.listdir(snapshots_dir)
    if f.endswith(".html") and any(ord(c) > 127 for c in f)
]

if len(html_files_with_non_ascii) > 0:
    print("@@@@@@@@@@ WARNING!!! @@@@@@@@@@")
    print("These HTML files have non-ASCII characters in their filenames:\n")
    for f in html_files_with_non_ascii:
        print(f)
    print("\n\nPlease rename them to ASCII characters before proceeding.")
else:
    print("All HTML files have proper ASCII filenames.")
