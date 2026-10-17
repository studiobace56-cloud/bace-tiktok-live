НАСТРОЙКА НА БЕЗПЛАТНИЯ МОНИТОР — GitHub

1. Създай БЕЗПЛАТЕН GitHub акаунт, ако нямаш.
2. Натисни New repository, име например bace-tiktok-live, Public, Create repository.
3. Разархивирай ТОЗИ ZIP. Качи check_live.py, requirements.txt, live-status.json и папката .github/workflows/ в корена на хранилището.
   Важно: папката .github е скрита на някои компютри; не я пропускай.
4. GitHub > Repository > Settings > Actions > General > Workflow permissions: Read and write permissions > Save.
5. GitHub > Actions > TikTok LIVE status > Run workflow.
6. Изчакай да завърши. В корена отвори live-status.json и виж checked_at.
7. В ZIP на САЙТА редактирай agency/live-free-config.js и замени OWNER с GitHub потребителското си име и REPO с името на хранилището.
8. Публикувай ZIP на сайта в съществуващия Netlify проект.
9. Тествай www.bacebg.com/agency/ след като GitHub workflow е минал успешно.

Проверка през 5 минути е приблизителна: GitHub може да забавя или спира графика.
TikTokLive е неофициална библиотека и може да не работи при блокиране/промени.
Броят зрители засега остава празен (не измисляме стойности).
Не са нужни TikTok пароли.
