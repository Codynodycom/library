# Методы списков

`append()`
Добавляет элемент в конец списка.

```python
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)  # ['apple', 'banana', 'orange']
```

`insert()`
Вставляет элемент на определённую позицию.

```python
fruits = ['apple', 'banana']
fruits.insert(1, 'cherry')
print(fruits)  # ['apple', 'cherry', 'banana']
```

`remove()`
Удаляет первое вхождение элемента.

```python
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)  # ['apple', 'cherry']
```

`pop()`
Удаляет и возвращает элемент по индексу. Если индекс не указан, удаляется последний элемент.

```python
fruits = ['apple', 'banana', 'cherry']
last_fruit = fruits.pop()
print(fruits)  # ['apple', 'banana']
print(last_fruit)  # 'cherry'
```

`clear()`
Удаляет все элементы из списка.

```python
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)  # []
```

`index()`
Возвращает индекс первого вхождения указанного элемента.

```python
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))  # 1
```

`count()`
Возвращает количество вхождений элемента в списке.

```python
fruits = ['apple', 'banana', 'apple']
print(fruits.count('apple'))  # 2
```

`sort()`
Сортирует список по возрастанию (по умолчанию).

```python
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # [1, 2, 3]
```

Можно отсортировать по убыванию, если передать аргумент `reverse=True`

```python
numbers.sort(reverse=True)
print(numbers)  # [3, 2, 1]
```

`reverse()`
Разворачивает порядок элементов в списке.

```python
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # ['cherry', 'banana', 'apple']
```

`copy()`
Создаёт поверхностную копию списка.

```python
fruits = ['apple', 'banana', 'cherry']
new_fruits = fruits.copy()
print(new_fruits)  # ['apple', 'banana', 'cherry']
```

`extend()`
Расширяет список, добавляя все элементы переданного итерируемого объекта.

```python
fruits = ['apple', 'banana']
more_fruits = ['cherry', 'orange']
fruits.extend(more_fruits)
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
```

