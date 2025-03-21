from flask import Flask, render_template, redirect, url_for
import requests
import config

app = Flask(__name__)

def get_student_data():
    params = {'name': config.STUDENT_NAME}
    try:
        response = requests.get(config.API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print("Ошибка при запросе к API:", e)
        return {"age": "N/A"}

def make_resume():
    data = get_student_data()
    achievements = [
        "Успешное выполнение учебных проектов",
        "Участие в олимпиадах",
        "Разработка собственного проекта",
        "Победы на хакатонах",
        "Публикации в профильных изданиях"
    ]
    return {
        "name": config.STUDENT_NAME,
        "age": data.get("age", "N/A"),
        "achievements": achievements
    }

@app.route('/')
def home():
    resume_data = make_resume()
    return render_template('resume.html', **resume_data)

@app.route('/update')
def update():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
