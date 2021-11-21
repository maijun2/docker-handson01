# これは何？
Dockerfileとdocker composeを組み合わせたハンズオン用のソースファイルです。

## 構成
app
- flaskでjsonデータを返答するappサーバー（https化済）

web
- nginx + Vue.jsで作ったフロントエンド。appサーバーと通信します