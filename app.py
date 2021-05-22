from flask import Flask, redirect, url_for, render_template, request, session


app = Flask(__name__)


# 首页
@app.route('/')
@app.route('/index')
def index():
    return render_template("base.html", )

# 游戏公告
@app.route('/announcements')
def announcements():
    return "announcements"

# 活动专区
@app.route('/events')
def events():
    return "events"

# 更新资讯
@app.route('/news')
def news():
    return "news"

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
    return 'download'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5001", debug=True)