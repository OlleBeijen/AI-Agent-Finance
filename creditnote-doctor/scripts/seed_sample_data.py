
# Kopieer sample_data naar data/
import shutil
from pathlib import Path

src = Path("sample_data")
dst = Path("data")
dst.mkdir(exist_ok=True, parents=True)
for p in src.glob("*.csv"):
    shutil.copy(p, dst / p.name)
print("Sample data gekopieerd naar ./data")
