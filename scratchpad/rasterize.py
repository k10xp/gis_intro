import json
from pathlib import Path
import matplotlib.pyplot as plt

geojson_path = Path(".", "data", "australia.json")
map_png_export_path = Path(".", "data", "australia.png")

with geojson_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

# shapes = [(feature["geometry"], 1) for feature in data["features"]]
# print(shapes)

# recreate grass gis output
fig, ax = plt.subplots(figsize=(6, 6))

for feature in data["features"]:
    geom = feature["geometry"]
    if geom["type"] == "MultiPolygon":
        for polygon in geom["coordinates"]:
            # polygon is list of linear rings, take exterior ring
            ring = polygon[0]
            xs = [pt[0] for pt in ring]
            ys = [pt[1] for pt in ring]
            ax.fill(xs, ys, facecolor="lightblue", edgecolor="blue")

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_aspect("equal", adjustable="box")
ax.set_title("Australia continent")
ax.axis("off")

plt.tight_layout()
plt.savefig(map_png_export_path, dpi=200)
plt.close()
