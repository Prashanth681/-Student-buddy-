from flask import Flask, render_template, request, redirect, url_for
from student_buddy.data_manager import load_data, save_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    data = load_data()
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            data['tasks'].append(task)
            save_data(data)
        return redirect(url_for('tasks'))
    return render_template('tasks.html', tasks=data['tasks'])

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    data = load_data()
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            data['notes'].append(note)
            save_data(data)
        return redirect(url_for('notes'))
    return render_template('notes.html', notes=data['notes'])

@app.route('/timetable', methods=['GET', 'POST'])
def timetable():
    data = load_data()
    if request.method == 'POST':
        day = request.form.get('day')
        subject = request.form.get('subject')
        if day and subject:
            data['timetable'].setdefault(day, []).append(subject)
            save_data(data)
        return redirect(url_for('timetable'))
    return render_template('timetable.html', timetable=data['timetable'])

@app.route('/study_hours', methods=['GET', 'POST'])
def study_hours():
    data = load_data()
    if request.method == 'POST':
        try:
            hours = float(request.form.get('hours'))
            if hours > 0:
                data['study_hours'].append(hours)
                save_data(data)
        except (ValueError, TypeError):
            # just ignore invalid input
            pass
        return redirect(url_for('study_hours'))

    total_hours = sum(data['study_hours'])
    return render_template('study_hours.html', study_hours=data['study_hours'], total_hours=total_hours)

if __name__ == '__main__':
    app.run(debug=True)
