# 数当てゲーム

自作したROSパッケージを動かす際の説明です。

# 目次

- [概要](#概要)
- [動作環境](#動作環境)
- [使用したもの](#使用したもの)
- [デモ動画](#デモ動画)
- [インストール方法](#インストール方法)
- [使用方法](#使用方法)
- [不具合](#不具合)
- [ライセンス](#ライセンス)

# 概要

数字当てゲームのやり方。

このゲームのクリア条件は出力される数値が目標の数値と同じになるようにすることです。

ただし、入力された数値が一定の規則に乗っ取り変化するので、まずは法則性を探します。

![image](https://user-images.githubusercontent.com/60230025/103792326-dab3fa80-5086-11eb-92c4-8d174ffc64ee.png)

その法則性から何を入力したら目標の数値になるかを考察して数値を入力し、あっていればクリアです。

(もしも、上記の法則性で目標が97ならば48を入力すればクリア)

ミス回数がカウントされているのでその回数が小さいほど高スコアです！


# 動作環境

以下の環境にて動作確認を行っています。

- Raspberry Pi 4 (8GB)
- OS: Ubuntu 20.04.1 LTS
- ROS: Noetic


# 使用したもの

- Raspberry Pi 4 (8GB)
- Micro SD Card (Gigastone : 16GB)

※必須ではありません。Ubuntuが使えればWindows上でも問題なく動きます。


# デモ動画

[![数当てゲーム](http://img.youtube.com/vi/MDfyllj7h1Q/hqdefault.jpg)](https://youtu.be/MDfyllj7h1Q)


# インストール方法

ターミナル
```sh
cd ~/catkin_ws/src/
git clone https://github.com/knr2/mypkg.git
cd ..
catkin_make
source ~/.bashrc
```

# 使用方法

以下のコマンドで使用できます。

ターミナル１
```sh
roscore &
rosrun mypkg number_hit_game.py
```

2つ開ける際は以下のコマンドを打ってください。

現在のミス回数が見られます。

ターミナル２
```sh
rostopic echo /game
```

# 不具合

- エラー

プログラムを実行した際に「-/usr/bin/env: `python3\r': そのようなファイルやディレクトリはありません」と表示される。

対処法

以下のコマンドを打って、もう一度ターミナル1でrosrunから始まるコマンドを打ってください。

ターミナル1
```sh
cd ~/catkin_ws/src/mypkg/scripts
vi number_hit_game.py
```

Vim
```sh
:set ff=unix
:wq
```
- バグ

実行中に「Ctrl + C」と入力すると、自動でクリアになる。

# ライセンス

BSD 3-Clause License
