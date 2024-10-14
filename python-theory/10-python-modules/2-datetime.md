# Модуль `datetime` в Python

`datetime` в Python позволяет работать с датой и временем. С его помощью можно узнать текущую дату и время, сравнивать их, добавлять или вычитать дни, часы, минуты и многое другое.

Представь, что у тебя есть волшебный календарь, который всегда показывает правильную дату и время. Модуль `datetime` — это как раз такой календарь в Python, который умеет работать с датами и временем и помогает тебе с ними взаимодействовать.


### Получение текущей даты и времени

Чтобы получить текущую дату и время, можно использовать функцию `datetime.now()`.

```python
import datetime

current_time = datetime.datetime.now()
print("Текущая дата и время:", current_time)
```

Этот код выведет на экран текущую дату и время, например, что-то вроде: `2024-10-13 15:30:00`.

### Получение только текущей даты или времени

Иногда нужно отдельно получить только дату или только время. Для этого есть функции `date()` и `time()`.

```python
import datetime

current_date = datetime.datetime.now().date()
current_time = datetime.datetime.now().time()

print("Текущая дата:", current_date)
print("Текущее время:", current_time)
```

Этот код выведет отдельно дату и время.

### Форматирование даты и времени

Модуль `datetime` позволяет форматировать дату и время в нужный тебе формат. Для этого используется метод `strftime()`.

```python
import datetime

now = datetime.datetime.now()
formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
print("Форматированное время:", formatted_time)
```

В этом примере дата и время будут выведены в формате день/месяц/год часы:минуты:секунды. Например: `13/10/2024 15:30:00`.

### Разбор строк в формат даты и времени

Иногда нужно преобразовать строку в формат даты и времени. Для этого используется метод `strptime()`.

```python
import datetime

date_string = "13/10/2024 15:30:00"
date_object = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
print("Преобразованная дата:", date_object)
```

Этот код преобразует строку в объект `datetime`, который уже можно использовать для вычислений и других операций.

### Работа с timedelta (разница во времени)

Модуль `datetime` позволяет вычитать и прибавлять дни, часы, минуты и другие временные интервалы с помощью объекта `timedelta`.

```python
import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
print("Завтра:", tomorrow)
```

Этот код вычисляет дату завтрашнего дня, прибавляя один день к сегодняшней дате.

### Разница между двумя датами

Ты можешь вычислить разницу между двумя датами. Например, чтобы узнать, сколько дней осталось до какого-то события.

```python
import datetime

today = datetime.date.today()
event_date = datetime.date(2024, 12, 31)
days_left = event_date - today
print("Дней до Нового года:", days_left.days)
```

Этот код покажет, сколько дней осталось до 31 декабря 2024 года.

