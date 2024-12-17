# Примеры

### Алгоритм поиска наиболее частого элемента (использование `Counter`)

С помощью `Counter` можно легко определить наиболее часто встречающийся элемент в списке, строке или другом итерируемом объекте. Это часто используется в задачах обработки данных, текстов или логов.

```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Использование Counter для подсчета частоты каждого элемента
count = Counter(numbers)

# Нахождение наиболее частого элемента
most_common_element = count.most_common(1)[0]  # [(4, 4)] -> первый элемент списка
print(f"Наиболее частый элемент: {most_common_element[0]} (встречается {most_common_element[1]} раз)")
```

###### Вывод:

```python
Наиболее частый элемент: 4 (встречается 4 раз)
```

#### Реализация очереди с `deque` (алгоритм BFS)

Deque подходит для реализации алгоритмов, где требуется двусторонняя очередь. Например, алгоритм поиска в ширину (BFS) использует очередь для обхода графа.

```python
from collections import deque

def bfs(graph, start):
    # Создаем очередь и добавляем начальную вершину
    queue = deque([start])
    visited = set()  # множество посещенных вершин

    while queue:
        # Извлекаем вершину из очереди
        node = queue.popleft()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            # Добавляем все смежные вершины в очередь
            queue.extend(graph[node])

# Пример графа (как словарь)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Выполняем BFS
bfs(graph, 'A')
```

###### Вывод:

```python
A B C D E F
```

### Группировка данных по ключу (использование `defaultdict`)

При обработке данных часто требуется группировать элементы по определённым ключам. `defaultdict` позволяет автоматически создавать списки для каждого ключа и добавлять туда значения, не проверяя заранее, существует ли ключ.

```python
from collections import defaultdict

students_courses = [
    ('Alice', 'Math'),
    ('Bob', 'Physics'),
    ('Alice', 'Physics'),
    ('Charlie', 'Math'),
    ('Bob', 'Math'),
]

# Группировка студентов по курсам
course_students = defaultdict(list)

for student, course in students_courses:
    course_students[course].append(student)

# Вывод сгруппированных данных
for course, students in course_students.items():
    print(f"{course}: {', '.join(students)}")
```

###### Вывод:

```python
Math: Alice, Charlie, Bob
Physics: Bob, Alice
```

### LRU-кэш (Least Recently Used) с использованием `OrderedDict`

С помощью `OrderedDict` можно реализовать кэш, где элементы, которые не использовались дольше всего, будут удаляться первыми.

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            # Если элемент существует, перемещаем его в конец
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Если ключ уже существует, обновляем его и перемещаем в конец
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            # Удаляем первый элемент (наименее используемый)
            self.cache.popitem(last=False)

# Пример использования LRUCache
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Возвращает 1
cache.put(3, 3)  # Удаляет ключ 2
print(cache.get(2))  # Возвращает -1 (ключ 2 был удален)
cache.put(4, 4)  # Удаляет ключ 1
print(cache.get(1))  # Возвращает -1 (ключ 1 был удален)
print(cache.get(3))  # Возвращает 3
print(cache.get(4))  # Возвращает 4
```

###### Вывод:

```python
1
-1
-1
3
4
```

### Подсчёт пар слов с `Counter`

При обработке текстов или данных часто возникает необходимость подсчёта пар элементов. Например, подсчёт двусловных фраз (биграмм) в тексте может использоваться для анализа данных.

```python
from collections import Counter

text = "this is a simple example of a simple text with simple words"
words = text.split()

# Создаем список биграмм
bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]

# Подсчитываем частоту биграмм
bigram_counts = Counter(bigrams)

# Наиболее частые биграммы
most_common_bigrams = bigram_counts.most_common(3)
print(most_common_bigrams)
```

###### Вывод:

```python
[(('simple', 'example'), 1), (('example', 'of'), 1), (('of', 'a'), 1)]
```

### Нахождение разницы в списках с использованием `Counter`

Иногда необходимо найти разницу между двумя списками, учитывая количество вхождений каждого элемента. `Counter` может помочь в таких задачах.

```python
from collections import Counter

list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 3, 4, 5]

# Подсчитываем количество вхождений элементов в каждом списке
counter1 = Counter(list1)
counter2 = Counter(list2)

# Элементы, которые были удалены
removed = counter1 - counter2
print(f"Удаленные элементы: {removed}")

# Элементы, которые были добавлены
added = counter2 - counter1
print(f"Добавленные элементы: {added}")
```

###### Вывод:

```python
Удаленные элементы: Counter({1: 1, 2: 1})
Добавленные элементы: Counter({3: 1, 5: 1})
```
