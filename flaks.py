from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'dein_geheimes_schlüssel'

# Beispiel-Anmeldedaten
valid_username = "admin"
valid_password = "password123"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == valid_username and password == valid_password:
            session['loggedin'] = True
            return redirect(url_for('calendar'))
        else:
            return "Ungültiger Benutzername oder Passwort."
    return render_template('login.html')

@app.route('/calendar')
def calendar():
    if 'loggedin' in session:
        return render_template('calendar.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
