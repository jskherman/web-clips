import os

snapshots_dir = os.path.join(os.getcwd(), "snapshots")

html_files_with_non_ascii = [
    f
    for f in os.listdir(snapshots_dir)
    if f.endswith(".html") and any(ord(c) > 127 for c in f)
]

if html_files_with_non_ascii:
    print("@@@@@@@@@@ WARNING!!! @@@@@@@@@@")
    print("These HTML files have non-ASCII characters in their filenames:")
    print(html_files_with_non_ascii)
else:
    print("All HTML files have proper ASCII filenames.")
