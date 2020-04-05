import os

stream = os.popen("diff -u .github/workflows/cached_results/results.json results/*.json")
diff = stream.read()
print(diff)

diff = diff.replace('\n', '\\n')
print(f"::set-output name=JSON_OUTPUT::{diff}")
