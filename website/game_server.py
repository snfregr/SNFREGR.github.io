from flask import Flask, request, redirect, render_template
from flask_cors import CORS

app = Flask(__name__, static_url_path="", static_folder="static")
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return redirect('/hub/')

@app.route('/game/snake/')
def snake_choice():
    return render_template('snake_choice.html')

@app.route('/game/snake/', methods=['POST'])
def start_snake_game():
    difficulty = request.form.get('difficulty')
    if difficulty == 'easy':
        return redirect('/game/snake/easy/')
    elif difficulty == 'hard':
        return redirect('/game/snake/hard/')
    else:
        return 'Invalid difficulty.'

@app.route('/game/snake/easy/')
def snake_easy():
    return render_template('snake_easy.html')

@app.route('/game/snake/hard/')
def snake_hard():
    return render_template('snake_hard.html')

@app.route('/game/hub/')
def game_hub():
    return render_template('game_hub.html')

@app.route('/hub/')
def hub():
    return render_template('hub.html')

# 添加 /study/hub 路由，将其渲染到 study_hub.html 模板文件
@app.route('/study/hub/')
def study_hub():
    return render_template('study_hub.html')

# 添加 /study/easy 路由，将其渲染到 number.html 模板文件
@app.route('/study/easy/')
def study_easy():
    return render_template('number.html')

# 添加 /study/hard 路由，将其渲染到 number2.html 模板文件
@app.route('/study/hard/')
def study_hard():
    return render_template('number2.html')

@app.route('/game/tower/')
def tower_game():
    return render_template('tower.html')

@app.route('/game/wuziqi/')
def wuziqi_game():
    return render_template('wuziqi.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)