# שאלון "איפה התיקון שלכם נתקע"

שאלון אבחון קצר שמזהה באיזו תחנה ברצף התיקון הזוגי נתקעים, ומפנה להרצאת "הקאמבק".

- `index.html` — הדף החי. **נבנה אוטומטית, לא לערוך ידנית**
- `src/quiz.template.html` — המקור. כאן עורכים טקסטים, שאלות וקישורים
- `build.py` — מטמיע את פונט Polin ומייצר את `index.html`
- `docs/spec.md` — האפיון המלא: שאלות, ניקוד, לוגיקה וטקסטים

## לעדכן

```bash
cd ~/repair-quiz
# עורכים את src/quiz.template.html
python3 build.py
git add -A && git commit -m "עדכון" && git push
```

הקישורים למוצרים נמצאים בראש הסקריפט ב-`src/quiz.template.html`, באובייקט `LINKS`.
