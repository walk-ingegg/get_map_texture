import urllib.request
import os
import skimage.io
import skimage.util
import shutil

# ORIGINAL_URL(seamlessphoto) = "https://cyberjapandata.gsi.go.jp/xyz/{t}/{z}/{x}/{y}.{ext}"

X_COORDINATE = int(input("左上のタイルのx座標を入力 : "))
Y_COORDINATE = int(input("左上のタイルのy座標を入力 : "))
TILE_COUNT = int(input("タイルの数 : "))
ZOOM_LEVEL = input("ズームレベル(max 18) : ")
TILE_EXPORT_PATH = "export_tile"
FIN_EXPORT_PATH = "export"

DATE_TYPE = "seamlessphoto"
DATE_EXT = "jpg"

# 出力先のフォルダを作成
os.makedirs(TILE_EXPORT_PATH, exist_ok=True)
os.makedirs(FIN_EXPORT_PATH, exist_ok=True)

x_coordinates = []
y_coordinates = []
image_names = []
image_paths = []

# とってくるタイルの配列を作る
for num in range(TILE_COUNT):
    x_coordinates.append(X_COORDINATE + num)
    y_coordinates.append(Y_COORDINATE + num)

# サイトから画像をとってきて"TILE_EXPORT_PATH"に出力
for y in y_coordinates:
    for x in x_coordinates:
        f = open(f"{TILE_EXPORT_PATH}/{str(x)}_{str(y)}.{DATE_EXT}", "wb")
        image_names.append(f"{TILE_EXPORT_PATH}/{str(x)}_{str(y)}.{DATE_EXT}")
        f.write(urllib.request.urlopen(f"https://cyberjapandata.gsi.go.jp/xyz/{DATE_TYPE}/{ZOOM_LEVEL}/{str(x)}/{str(y)}.{DATE_EXT}").read())
        f.close()

# ダウンロードしてきたファイルをくっつける下準備
for i in image_names:
    image_paths.append(skimage.io.imread(i))

# 画像をくっつけて保存
fin_image = skimage.util.montage(image_paths, multichannel=True)
skimage.io.imsave(f"{FIN_EXPORT_PATH}/{DATE_TYPE}_{ZOOM_LEVEL}_{str(X_COORDINATE)}_{str(Y_COORDINATE)}.{DATE_EXT}", fin_image)

# いらないファイルの消去
shutil.rmtree(TILE_EXPORT_PATH)