# get_map_texture 


### はじめに
- 国土地理院の[地理院タイル](https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html)から、任意の場所・範囲の画像を引っ張ってくる。
- 範囲が大きくなると画像の枚数がやばいから一枚に合成する。
- タイルは256x256のイメージデータで、標準地図や白地図、空中写真などの種類がある。
- タイルにはレベルという概念があり、レベル0が世界全体で、レベルが1上がるごとに解像度が縦横それぞれ2倍になる。
- レベルは最大18で、この場合タイルの一片の長さは北緯35度では約125mになるらしい。
- PLATEAUの3次メッシュが、地理院タイルの15レベルに対応している
- [ライセンス](https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html)


### 使い方
- [タイル座標確認ページ](https://maps.gsi.go.jp/development/tileCoordCheck.html#15/35.6673/139.7314)にアクセスする。
- 欲しい範囲の左上のタイルの座標見つける。
---
- プログラムを実行↓
- x座標を入力
- y座標を入力
- タイルの数を入力
    - "4"  →  右下に向かって"4*4"のタイルを持ってくる
- タイルのレベルを入力(1~18)
    - 18が一番細かくて高解像度
- 実行ファイルのディレクトリに"export"フォルダを生成してその中に出力される





### Ref  

- PLATEAUのDEMファイルに空中写真のテクスチャを貼りたい
  - [https://qiita.com/yoshikawa-hiroyuki/items/6935a9705b3144774fd1](https://qiita.com/yoshikawa-hiroyuki/items/6935a9705b3144774fd1)  