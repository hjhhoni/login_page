from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.secret_key = 'QWERTYUIOP'  # 对用户信息加密


@app.route('/signin', methods=['GET', "POST"])  # 路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
def login():
    if request.method == 'GET':
        return render_template('signin.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'admin' and pwd == '123':  # 这里可以根据数据库里的用户和密码来判断，因为是最简单的登录界面，数据库学的不是很好，所有没用。
        session['user_info'] = user
        return render_template('hello.html', greeting=f"您好！{user}")
    else:
        return render_template('signin.html', msg='用户名或密码输入错误')



if __name__ == "__main__":
    app.run()