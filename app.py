from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# 1. Санасан тоог таах тоглоом
number_to_guess = random.randint(1, 10)
@app.route('/guess_number', methods=['GET', 'POST'])
def guess_number():
    message = ''
    global number_to_guess
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess == number_to_guess:
            message = 'Баяр хүргэе! Та зөв таалаа!'
            number_to_guess = random.randint(1, 10)
        elif guess < number_to_guess:
            message = 'Илүү өндөр тоо байна.'
        else:
            message = 'Илүү бага тоо байна.'
    return render_template('guess_number.html', message=message)

# 2. Хайч, Чулуу, Даавуу
@app.route('/rps', methods=['GET', 'POST'])
def rps():
    result = ''
    if request.method == 'POST':
        player = request.form['choice']
        computer = random.choice(['Чулуу', 'Даавуу', 'Хайч'])
        if player == computer:
            result = 'Тэнцээ!'
        elif (player == 'Чулуу' and computer == 'Хайч') or (player == 'Даавуу' and computer == 'Чулуу') or (player == 'Хайч' and computer == 'Даавуу'):
            result = f'Та хожлоо! Компьютер: {computer}'
        else:
            result = f'Та хожигдлоо! Компьютер: {computer}'
    return render_template('rps.html', result=result)

# 3. Зураг таах (хамгийн энгийн хувилбар, зөвхөн текстээр асуулт өгнө, зураг оруулах бол нэмж болно)
@app.route('/image_guess', methods=['GET', 'POST'])
def image_guess():
    correct_answer = 'нохой'
    message = ''
    if request.method == 'POST':
        answer = request.form['answer'].lower()
        if answer == correct_answer:
            message = 'Зөв!'
        else:
            message = 'Буруу!'
    return render_template('image_guess.html', message=message)

# 4. Фибоначчигийн таавар
@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    result = ''
    if request.method == 'POST':
        n = int(request.form['number'])
        a, b = 0, 1
        sequence = []
        for _ in range(n):
            sequence.append(a)
            a, b = b, a + b
        result = ', '.join(map(str, sequence))
    return render_template('fibonacci.html', result=result)

# 5. Төөрдөг байшин (simple text based)
@app.route('/maze', methods=['GET', 'POST'])
def maze():
    message = ''
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == 'зүүн':
            message = 'Таныг баривчиллаа! Тоглоом дуусав.'
        elif choice == 'баруун':
            message = 'Та гарцыг оллоо! Амжилттай!'
        else:
            message = 'Зөв замаа сонгоно уу.'
    return render_template('maze.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
