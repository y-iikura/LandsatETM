LandsatETM
======================
ランドサット７号ETM+(Level 1T)から指定した範囲を切り出します。位相限定相関法を用いて、数値標高モデルから作成した陰影画像との位置ズレの評価も行えます。

使い方
------
ターミナルで以下のようなコマンドを入力します。
<pre>
$ extraction.py scene\_name area\_file　new\_folder 
$ displacement.py scene\_name dem.tif　
</pre>

* extraction.pyで対象とするデータが入っているフォルダ(scene\_name)の可視・近赤外バンド画像からarea_fileで以下のように指定された範囲を切り出し、バンド毎のgeotifファイルをnew\_folderに生成します。
* 追加のキーワードパラメータを設定する事（dx=dx0　dy=dy0)により位置ズレを補正できます。位置ズレはdisplacement.pyにより推定します。
* displacement.pyでは、数値標高モデル（dem.tif）と衛星撮影時の太陽高度・方位から作成される太陽入射角の余弦を参照画像として利用します。


### area_fileの書き方 ###
例(template.txt)がアップされています。  
UTM座標系(単位はメートル）
<pre>
xs= 406200.0　　西端
xe= 442200.0　　東端
dx= 30.0　　　　 画素サイズ
ys= 4460750.0　 南端
ye= 4496750.0　 北端
dy= 30.0　　　　 画素サイズ
</pre>


必要なデータ
----------------
[EarthExplore][link]
を利用して、衛星データ（オルソ補正済み）を入手して下さい。以下の二つのデータセットタイプに適用可能です。

* Landsat Archive/ L7 ETM+ SLC-on (1999-2003)  
* Landsat Legacy/ ETM+(1999-2003)
[link]: http://earthexplorer.usgs.gov
---
* ファイルは付属情報（\*.metまたは\*/MTL.txt)も含めて、シーン毎に一つのフォルダ(scned\_name)にまとめて入れます。　　
* displacement.pyではgGEOTIF形式の数値標高モデルを利用します。KibanDemを用いて作成する事ができます。
* 位置ズレの同定にはopencvの位相限定相関法（phaseCorrelate)を利用します。

利用するライブラリ
--------
Python2.7で動作を確認しています。

1. sys,numpy,scipy,cv2,osgeoが必要です。
2. 自作のライブラリを利用します。  
　　1.proj\_util  投影法変換とGEOTIFFの読み書きなど  
　　2.convert\_util 付属情報の読み出し、変換パラメータの設定

参考文献など
--------
* 飯倉善和：数値標高モデルを用いたランドサットTM画像の幾何補正の最適化、日本リモートセンシング学会誌、22(2)、pp.189-195、200２

ライセンス
----------
Copyright &copy; 2016 Yoshikazu Iikura  
Distributed under the [MIT License][mit].

[MIT]: http://www.opensource.org/licenses/mit-