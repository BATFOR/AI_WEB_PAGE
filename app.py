
from flask import Flask,send_from_directory,render_template

# 创建Flask应用程序实例
app = Flask(__name__)

# 定义一个路由和对应的视图函数
@app.route('/<page_path>')
def page(page_path):
    return render_template(page_path)

@app.route('/data/<data_name>', methods=['GET', 'POST'])
def get_data(data_name):
    return send_from_directory("static", data_name)

@app.route('/')
def index():
    return render_template("index.html")


# 运行应用程序
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
