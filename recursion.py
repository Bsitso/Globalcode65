>>> word = ["hello", "my", "name", "is", "sam"]
>>> word[0].upper()
'HELLO'
'''>>> word[0].upper(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: upper() takes no arguments (1 given)
>>> word[1].upper()
'MY'
>>> word[2].upper()
'NAME'
>>> word[3].upper()
'IS'
>>> word[4].upper()

>>> word = ["hello", "my", "name", "is", "sam"]
>>> length = [len(word)for word in word]
>>> word = [word.upper()for word in word]
>>> tuple(zip(word, length))
(('HELLO', 5), ('MY', 2), ('NAME', 4), ('IS', 2), ('SAM', 3))'''

>>> 