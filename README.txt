پکیج نهایی سایت برای بارگذاری در GitHub Pages
نام کاربری GitHub: kamalvand110-bit

فایل‌ها:
- index.html
- profile.jpg (placeholder; اگر می‌خواهید عکس خودتان را بگذارید، این فایل را جایگزین کنید)
- profile_round.png (تصویر دایره‌ای برای هدر)
- profile_thumb.jpg (256x256)
- sitemap.xml (الگو - دامنهٔ خود را جایگزین کنید)
- articles/index.json
- articles/chidamane-shimi-ai.html
- README.txt (این فایل)

راهنمای سریع (رابط وب):
1. به https://github.com برو و وارد حساب خود شوید.
2. بالا سمت راست ➕ → New repository. نام مخزن را مثلاً kamalvandm110-bit/mohamadalikamalvand448.github.io قرار دهید تا سایت در URL https://kamalvandm110-bit/mohamadalikamalvand448.github.io منتشر شود.

3. ایجاد مخزن. سپس روی Add file → Upload files کلیک کنید و همهٔ فایل‌ها را از این بسته بارگذاری کنید (index.html و پوشه articles و تصاویر).
4. Commit changes. پس از چند دقیقه سایت در https://kamalvandm110-bit/mohamadalikamalvand448.github.io در دسترس خواهد بود.

روش با git (خط فرمان):
```
cd /path/to/extracted/site-folder
git init
git add .
git commit -m "Initial site upload for kamalvand110-bit"
git branch -M main
git remote add origin  https://kamalvandm110-bit/mohamadalikamalvand448.github.io
git push -u origin main
```

اضافه کردن مقالهٔ جدید:
- مقاله را به صورت فایل HTML یا Markdown داخل پوشهٔ articles قرار دهید.
- سپس آیتمی به articles/index.json اضافه کنید تا در صفحهٔ اصلی نمایش داده شود. مثال:
{ "id": "new-id", "title": "عنوان مقاله", "description": "خلاصه کوتاه", "url": "articles/new-article.html", "date": "2025-10-09", "tags": ["نمونه"] }

اتصال دامنه اختصاصی:
- دامنه را بخرید و رکورد DNS را طبق راهنمای GitHub Pages تنظیم کنید. سپس نام دامنه را در تنظیمات مخزن → Pages → Custom domain وارد کنید.
