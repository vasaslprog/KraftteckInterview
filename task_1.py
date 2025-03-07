# Задача 1
# У нас есть 2 таблицы: Users – таблица пользователей и Orders – таблица с заказами пользователей. Таблицы имеют такую структуру:
#
# Users (
# id INTEGER PRIMARY KEY,
# name TEXT,
# email TEXT
# );
#
# Orders (
# id INTEGER PRIMARY KEY,
# user_id INTEGER,
# total_amount REAL,
# FOREIGN KEY (user_id) REFERENCES Users(id)
# );
#
# Требуется написать один SQL-запрос к базе данных, который вернёт:
# name всех пользователей, которые оформили заказов (Orders) на общую сумму (total_amount) более 1000руб.
# Если у вас получилось, то дополните запрос таким образом
# чтобы он помимо name возвращал общую сумму всех заказов пользователя.

