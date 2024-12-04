# Методы работы со словарями

**Создания словаря**

```python
student = {
    'name': 'Alice',
    'age': 22,
    'major': 'Mathematics'
}
```

1. `get()`

Метод `get()` возвращает значение, связанное с ключом. Если ключ не найден, можно задать значение по умолчанию.

```python
# Получение значения по ключу
major = student.get('major')
print(major)  # 'Mathematics'

# Если ключа нет, вернётся значение по умолчанию
gpa = student.get('gpa', 'Not Available')
print(gpa)  # 'Not Available'
```

2. `update()`

Метод `update()` позволяет обновить существующие значения или добавить новые пары ключ-значение в словарь.

```python
# Обновление и добавление значений
student.update({'age': 23, 'gpa': 3.8})
print(student)
# {'name': 'Alice', 'age': 23, 'major': 'Mathematics', 'gpa': 3.8}
```

3. `keys()`

Метод `keys()` возвращает объект представления всех ключей словаря.

```python
# Получение всех ключей
keys = student.keys()
print(keys)  # dict_keys(['name', 'age', 'major', 'gpa'])
```

4. `values()`

Метод `values()` возвращает объект представления всех значений словаря.

```python
# Получение всех значений
values = student.values()
print(values)  # dict_values(['Alice', 23, 'Mathematics', 3.8])
```

5. `items()`

Метод `items()` возвращает объект представления всех пар "ключ-значение" в виде кортежей.

```python
# Получение всех пар ключ-значение
items = student.items()
print(items)
# dict_items([('name', 'Alice'), ('age', 23), ('major', 'Mathematics'), ('gpa', 3.8)])
```

6. `pop()`

Метод `pop()` удаляет элемент по ключу и возвращает его значение. Если ключ не найден, можно задать значение по умолчанию, которое будет возвращено вместо ошибки.

```python
# Удаление элемента по ключу
age = student.pop('age')
print(age)  # 23
print(student)
# {'name': 'Alice', 'major': 'Mathematics', 'gpa': 3.8}
```

7. `popitem()`

Метод `popitem()` удаляет последнюю добавленную пару "ключ-значение" из словаря и возвращает её.

```python
# Удаление последней добавленной пары
last_item = student.popitem()
print(last_item)  # ('gpa', 3.8)
print(student)
# {'name': 'Alice', 'major': 'Mathematics'}
```

8. `clear()`

Метод `clear()` удаляет все элементы из словаря, оставляя его пустым.

```python
# Очистка словаря
student.clear()
print(student)  # {}
```

9. `copy()`

Метод `copy()` создаёт поверхностную копию словаря.

```python
# Создание копии словаря
student_copy = student.copy()
print(student_copy)
# {'name': 'Alice', 'major': 'Mathematics'}
```

10. `fromkeys()`

Метод `fromkeys()` создаёт новый словарь с заданными ключами и значением по умолчанию для всех ключей.

```python
# Создание словаря с одинаковыми значениями для всех ключей
keys = ['name', 'age', 'major']
default_value = 'Unknown'
new_student = dict.fromkeys(keys, default_value)
print(new_student)
# {'name': 'Unknown', 'age': 'Unknown', 'major': 'Unknown'}
```

11. `setdefault()`

Метод `setdefault()` возвращает значение по ключу, если ключ уже существует. Если его нет, добавляет ключ с указанным значением по умолчанию.

```python
# Получение значения существующего ключа
major = student.setdefault('major', 'Not Assigned')
print(major)  # 'Mathematics'

# Добавление нового ключа, если его не было
gpa = student.setdefault('gpa', 3.5)
print(gpa)  # 3.5
print(student)
# {'name': 'Alice', 'major': 'Mathematics', 'gpa': 3.5}
```

12. Проверка наличия ключа `(in)`

Для проверки, существует ли ключ в словаре, можно использовать оператор `in`.

```python
# Проверка наличия ключа
if 'name' in student:
    print("Key 'name' exists.")
```
