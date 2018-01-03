# 讓你三餐不無聊bot

可以幫你決定三餐，給菜單讓你參考。
甚至幫你找、推薦音樂給你聽喔~。

## Setup

### Prerequisite

* Python 3

#### Install Dependency

```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](https://github.com/BroLeaf/TOC-Project-2017/blob/master/img/show-fsm.png)

## Usage

一開始進入 `user` 後會馬上跳到 `choose`，不用任何input，也不會跳回來。

當到達 `search` or `recommend` 給完結果就會直接跳回 `choose`

* choose	
在這個state會跟據你輸入哪一餐

來推薦你要吃什麼

如果不想吃東西也可以聽聽想要的音樂

	* Input: "吃早餐" 進入 `breakfast`
		* Reply: 會回覆 黑色香蕉 加上 他的菜單

	* Input: "吃午餐" 進入 `lunch`
		* Reply: 會回覆 麥當勞 加上 他的菜單

	* Input: "吃晚餐" 進入 `dinner`
		* Reply: 會回覆 肯得基 加上 他的菜單

	* Input: "聽音樂" 進入 `satisfied`
		* Reply: 會回覆 要搜尋還是推薦

* breakfast, lunch, dinner

只吃東西一定會太無聊

所以還有這個固定的模式 就是讓你聽音樂啦~

	* Input: "飽了" or "聽音樂" 進入 `satisfied`
		* Reply: 會回覆 要搜尋還是推薦

* satisfied
如果要聽音樂

可以輸入關鍵字bot會去youtube幫你找

或是輸入 推薦 來獲得很讚的內容

但如果不想聽 直接輸入 不要 就可以回到一開始選吃或聽的地方了

	* Input: "推薦" 進入 `recommend`
		* Reply: 固定回覆，會給 gfriend 的 youtube 聯結 （超讚ㄉ）

	* Input: "不要" 進入（回到） `choose`
		* Reply: 會問你要吃還是聽音樂
	
	* Input: 除了 "推薦" 和 "不要" 都會進入 `search`
		* Reply: 會直接把input丟到youtube搜尋 然後給超聯結



