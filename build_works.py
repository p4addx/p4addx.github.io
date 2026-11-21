# Строит works/works.json из картинок в works/.
# Имя файла: Категория__Название.jpg  (без "__" — работа без категории)
import json, os, re, urllib.parse
exts = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.avif'}
out = []
for n in sorted(os.listdir('works')):
    b, e = os.path.splitext(n)
    if e.lower() not in exts:
        continue
    cat, _, title = b.partition('__')
    if not title:
        cat, title = '', b
    title = re.sub(r'^\d+[-_.]\s*', '', title).replace('_', ' ').replace('-', ' ').strip()
    w = {'src': 'works/' + urllib.parse.quote(n), 'title': title}
    if cat:
        w['cat'] = cat.replace('_', ' ').strip()
    out.append(w)
json.dump(out, open('works/works.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'works')
