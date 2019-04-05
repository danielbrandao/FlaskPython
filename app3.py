from flask import Flask, render_template, json, request
from werkzeug import generate_password_hash, check_password_hash
# pip install flask-mysql (Mac/Linux)
# pip install Flask-MySQL (Windows)
from flaskext.mysql import MySQL


mysql = MySQL()
app = Flask(__name__)

# MySQL setup
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'webapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _nome = request.form['inputNome']
        _email = request.form['inputEmail']
        _senha = request.form['inputSenha']

        # Valida os dados recebidos
        if _name and _email and _password:
            
            with closing(mysql.connect()) as conn:
                with closing(conn.cursor()) as cursor:
            
                    _hashed_password = generate_password_hash(_password)
                    cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
                    data = cursor.fetchall()

                    if len(data) is 0:
                        conn.commit()
                        return json.dumps({'message':'User criado com sucesso!'})
                    else:
                        return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>preencha os campos requeridos</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})

if __name__ == "__main__":
    app.run(port=5002)