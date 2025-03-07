# Задача 2
# На сервере Flask реализована вот такая обработка маршрута:
# @app.route('/api/people', methods=['GET'])
# def hi_people():
# name = request.args.get('name')
# age = request.args.get('age')
# return {"message": f"Привет, {name}, тебе {age} лет."}
#
# Напишите url, перейдя по которому мы передадим на сервер следующую информацию:
# Имя – «Олег», возраст – «33».
# Сервер использует 3000 порт.