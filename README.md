# 数当てゲームの作成

自作したRosパッケージを動かす際の説明です。

プログラムにlicenseを追加する。

# 動作環境

以下の環境にて動作確認を行っています。

- raspberry pi 4 (8GB)
- OS: Ubuntu 20.04.1 LTS
- ROS: Noetic

# インストール方法

ターミナル
```sh
cd ~/catkin_ws/src/
git clone https://github.com/knr2/mypkg.git
cd ..
catkin_make
source ~/.bashrc
```

# 実行方法

以下のコマンドで実行ができます。

ターミナルが2つ開ける場合は、76,84行目をコメントアウトすると求めたい答えが見やすくなります。

ターミナル１
```sh
roscore &
rosrun mypkg number_hit_game.py
```

エラーが出る場合
-/usr/bin/env: `python3\r': そのようなファイルやディレクトリはありません

以下のコマンドを打って、もう一度ターミナル1のコマンドを打ってください。

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

2つ開ける際は以下のコマンドを打ってください。

ターミナル２
```sh
rostopic echo /game
```

#### Videos

後でURLを変更
[![数当てゲーム](http://img.youtube.com/vi/UDOO2g307oI/hqdefault.jpg)](https://youtu.be/UDOO2g307oI)


# バグ利用
Ctrl + C