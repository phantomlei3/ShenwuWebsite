from flask import Flask, redirect, url_for, render_template, request, session
import csv

app = Flask(__name__)

with open("info_data/public_info.csv", "r", encoding="utf-8") as f:
    public_info = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]

public_info = sorted(public_info, key=lambda info: info['time'], reverse=True)
info_id_dict = {info['id']: info for info in public_info}

announce_info = [info for info in public_info if info['type'] == "公告"]
event_info = [info for info in public_info if info['type'] == "活动"]
news_info = [info for info in public_info if info['type'] == "新闻"]


# 首页
@app.route('/')
@app.route('/index')
def index():

    # visualization limitation: 10
    return render_template("index.html", public_info=public_info[:10],
                            announce_info=announce_info[:10], event_info=event_info[:10], news_info=news_info[:10])

# 游戏公告
@app.route('/announcements')
def announcements():
    banner = "announcement"
    return render_template("info.html", banner=banner, all_info=announce_info)

# 活动专区
@app.route('/events')
def events():
    banner = "event"
    return render_template("info.html", banner=banner, all_info=event_info)

# 新闻资讯
@app.route('/news')
def news():
    banner = "news"
    return render_template("info.html", banner=banner, all_info=news_info)


@app.route('/article', methods=['GET'])
def article():
    # 获取article id
    id = str(request.args.get('id')).lower()
    # 设置banner
    if 'a' in id:
        banner = "announcement"
    elif 'e' in id:
        banner = "event"
    else:
        banner = "news"

    article = info_id_dict[id]

    return render_template("article.html", banner=banner, article=article)




# 神武图书馆
@app.route('/wiki')
def wiki():
    return "wiki"

# 游戏论坛
@app.route('/forum')
def infolibrary():
    return "forum"


# 游戏下载
@app.route('/download')
def download():
    return render_template("download.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5001", debug=True)