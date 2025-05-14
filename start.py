import os
import subprocess
import time
import webbrowser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")

# اجرای سرور جنگو
try:
    # سرور رو توی subprocess اجرا می‌کنیم
    server = subprocess.Popen(["python", "manage.py", "runserver"])
    
    # چند ثانیه صبر می‌کنیم تا سرور کامل بالا بیاد
    time.sleep(3)

    # باز کردن مرورگر
    webbrowser.open("http://127.0.0.1:8000")

    # منتظر می‌مونیم تا سرور بسته بشه
    server.wait()

except Exception as e:
    print("خطا در اجرای سرور:", e)

input("برای خروج Enter بزنید...")
