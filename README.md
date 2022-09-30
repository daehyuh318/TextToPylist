# python-tip

```python
# txt to py-list
file_path = "새 텍스트 문서.txt"
with open(file_path, 'rt', encoding='UTF8') as f:
    lines = f.readlines()

print(list(map(lambda s: s.strip(), lines)))
```
