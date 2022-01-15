# zappaでapigateway + lambda

## 前提

python3.9

aws cli

## pythonの仮想環境を作成(zappaは仮想環境じゃないと動かないらしい)

### 仮想環境の設定を作るフォルダに移動(たぶんどこでもいい)

```
cd /vagrant/prj
```

### 仮想環境の作成

```
python3 -m venv zappa_env
```

### 仮想環境を起動(?)する

```
. zappa_env/bin/activate
```

### 仮想環境を終了する場合

```
deactivate
```

## zappaをインストール。activateしている状態で行う。(サンプルではflaskを使っているので一緒にインストール)

```
pip install flask zappa
pip install flask-cors
```

## デプロイ

### 対象のファイルがあるフォルダに移動

```
cd /path/to/serverlessCMS/testApp
```

### zappaを初期化

```
zappa init
```

### zappa initするといくつか入力を求められる。以下以外はdefaultでOK

Where is your app's function?: my_app.app

### 初回デプロイ

```
zappa deploy dev
```

### 2回目以降デプロイ
```
zappa update dev
```
