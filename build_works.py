# Строит works/works.json из картинок в works/.
# Имя файла: Категория__Название.jpg  (без "__" — работа без категории)
# Для файлов с латинскими именами подписи берутся из works/titles.json
import json, os, re, urllib.parse
exts = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.avif'}
ORDER = ['Фирменный стиль', 'Логотипы', 'Ретушь']  # порядок категорий в галерее
try:
    meta = json.load(open('works/titles.json', encoding='utf-8'))
except Exception:
    meta = {}
mk = list(meta)

def cat_of(n):
    if n in meta:
        return meta[n].get('cat', '')
    return n.split('__')[0].replace('_', ' ').strip() if '__' in n else ''

def key(n):
    c = cat_of(n)
    return (ORDER.index(c) if c in ORDER else len(ORDER),
            mk.index(n) if n in meta else 1000, os.path.splitext(n)[0])

out = []
for n in sorted(os.listdir('works'), key=key):
    b, e = os.path.splitext(n)
    if e.lower() not in exts:
        continue
    if n in meta:
        cat, title = meta[n].get('cat', ''), meta[n].get('title', b)
    else:
        cat, _, title = b.partition('__')
        if not title:
            cat, title = '', b
        title = re.sub(r'^\d+[-_.]\s*', '', title).replace('_', ' ').replace('-', ' ').strip()
        cat = cat.replace('_', ' ').strip()
    w = {'src': 'works/' + urllib.parse.quote(n), 'title': title}
    if cat:
        w['cat'] = cat
    out.append(w)
json.dump(out, open('works/works.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'works')
