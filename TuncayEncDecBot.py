import os, time, base64, marshal, random, zlib, re, requests, telebot, ast, subprocess, json
from telebot import types
from io import StringIO
from contextlib import redirect_stdout
hackerhıhı = "\033[100m"
batu = "\033[94m"
hehe = "\033[0m"
hackerbatu = """⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰⠂⠀
⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅⡀⠀
⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⢠⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⣿⠇⠀⠀⠀⠀⢸⡇⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠖⡾⠁⠀⠀⣿⠀⠀⠀⠀⠀⠘⣿⠀⠀⠙⡇⢸⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠄⠀
⠀⠀⢻⣷⡦⣤⣤⣤⡴⠶⠿⠛⠉⠁⠀⢳⠀⢠⡀⢿⣀⠀⠀⠀⠀⣠⡟⢀⣀⢠⠇⠀⠈⠙⠛⠷⠶⢦⣤⣤⣤⢴⣾⡏⠀⠀
⠀⠀⠈⣿⣧⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢊⣙⠛⠒⠒⢛⣋⡚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⣾⡿⠀⠀⠀
⠀⠀⠀⠘⣿⣇⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠁⣼⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣦⠀⠻⣿⣷⣦⣤⣤⣶⣶⣶⣿⣿⣿⣿⠏⠀⠀⠻⣿⣿⣿⣿⣶⣶⣶⣦⣤⣴⣿⣿⠏⢀⣼⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣷⣄⠙⠻⠿⠿⠿⠿⠿⢿⣿⣿⣿⣁⣀⣀⣀⣀⣙⣿⣿⣿⠿⠿⠿⠿⠿⠿⠟⠁⣠⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣯⠙⢦⣀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⣠⠴⢋⣾⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠈⠉⠒⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⠒⠉⠁⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
CISTAK = input("Lütfen Telegram bot token'ınızı girin: ")
YONETICI_ID = int(input("Lütfen yönetici ID'nizi girin: "))
bot = telebot.TeleBot(CISTAK)
if os.path.exists("amkoe.json"):
    try:
        with open("amkoe.json", "r", encoding="utf-8") as fp:
            amkoeBanlar = set(json.load(fp))
    except Exception as e:
        print("amkoe.json yüklenemedi, yeni dosya oluşturuluyor. Hata:", e)
        amkoeBanlar = set()
else:
    amkoeBanlar = set()
if os.path.exists("kullanicilar.json"):
    try:
        with open("kullanicilar.json", "r", encoding="utf-8") as fp:
            data = json.load(fp)
            if isinstance(data, dict):
                amkoeUyeler = data
            else:
                print("kullanicilar.json formatı hatalı, dict bekleniyordu. Yeni dict kullanılıyor.")
                amkoeUyeler = {}
    except Exception as e:
        print("kullanicilar.json yüklenemedi, yeni dosya oluşturuluyor. Hata:", e)
        amkoeUyeler = {}
else:
    amkoeUyeler = {}

amkoeSecimler = {}

siktirZip = lambda veri: zlib.compress(veri)
base64la = lambda veri: base64.b64encode(veri)
base32la = lambda veri: base64.b32encode(veri)
base16la = lambda veri: base64.b16encode(veri)
marshalla = lambda veri: marshal.dumps(compile(veri, 'modul', 'exec'))
amkoe_baslik = "# Geliştirici @batukurucu | Kanal @batutool\n\n"
amkoe_son = "\n\n# Geliştirici @TuncayXodayev | Kanal @TuncayTOOL\n"
amkoeKlasor = "TuncayTOOL"
if not os.path.exists(amkoeKlasor):
    os.makedirs(amkoeKlasor)
amkoeArapKlasor = "/storage/emulated/0/TuncayTOOL/"
os.makedirs(amkoeArapKlasor, exist_ok=True)
def temizAdYap(ad):
    ad = os.path.splitext(ad)[0]
    ad = re.sub(r'\W+', '_', ad)
    return ad + ".py"
def smsKoduAl():
    url = "https://raw.githubusercontent.com/muhammadkaracak/Sms/refs/heads/main/Sms.py"
    yanit = requests.get(url)
    yanit.raise_for_status()
    return yanit.text
def smsCalistir(giris, cikis):
    kod = smsKoduAl()
    with open("gecici_sms.py", "w", encoding="utf-8") as dosya:
        dosya.write(kod)
    islem = subprocess.Popen(
        ["python", "gecici_sms.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    cikti, _ = islem.communicate(f"{giris}\n{cikis}\n")
    os.remove("gecici_sms.py")
    return cikti
def ilet(mesaj):
    if mesaj.content_type != 'text' or not hasattr(mesaj, 'data'):
        icerik = f"Mesajı gönderen: {mesaj.from_user.id}\n\n"
        bot.send_message(YONETICI_ID, icerik)
        try:
            bot.forward_message(YONETICI_ID, mesaj.chat.id, mesaj.message_id)
        except Exception as hata:
            print("İleti hata:", hata)
def banla(mesaj):
    if mesaj.from_user.id != YONETICI_ID:
        return
    try:
        parts = mesaj.text.split()
        if len(parts) < 2:
            bot.reply_to(mesaj, "Lütfen banlanacak kullanıcı ID'sini belirtin. Örnek: /ban 123456789")
            return
        ban_id = int(parts[1])
        amkoeBanlar.add(ban_id)
        with open("amkoe.json", "w", encoding="utf-8") as fp:
            json.dump(list(amkoeBanlar), fp)
        bot.reply_to(mesaj, f"Kullanıcı {ban_id} banlandı.")
    except Exception as e:
        bot.reply_to(mesaj, f"Hata: {e}")
def unbanla(mesaj):
    if mesaj.from_user.id != YONETICI_ID:
        return
    try:
        parts = mesaj.text.split()
        if len(parts) < 2:
            bot.reply_to(mesaj, "Lütfen banı kaldırılacak kullanıcı ID'sini belirtin. Örnek: /unban 123456789")
            return
        unban_id = int(parts[1])
        if unban_id in amkoeBanlar:
            amkoeBanlar.remove(unban_id)
            with open("amkoe.json", "w", encoding="utf-8") as fp:
                json.dump(list(amkoeBanlar), fp)
            bot.reply_to(mesaj, f"Kullanıcı {unban_id} banı kaldırıldı.")
        else:
            bot.reply_to(mesaj, f"Kullanıcı {unban_id} zaten banlı değil.")
    except Exception as e:
        bot.reply_to(mesaj, f"Hata: {e}")
def listUsers(mesaj):
    if mesaj.from_user.id != YONETICI_ID:
        return
    kullanici_list = "\n".join(str(uid) for uid in amkoeUyeler.keys())
    if kullanici_list == "":
        kullanici_list = "Kayıtlı kullanıcı yok."
    bot.reply_to(mesaj, f"Kayıtlı kullanıcılar:\n{kullanici_list}")
@bot.message_handler(commands=['ban'])
def komut_ban(mesaj):
    banla(mesaj)
@bot.message_handler(commands=['unban'])
def komut_unban(mesaj):
    unbanla(mesaj)
@bot.message_handler(commands=['list_users'])
def komut_listUsers(mesaj):
    listUsers(mesaj)
@bot.message_handler(commands=['start'])
def komut_start(mesaj):
    ilet(mesaj)
    uid = mesaj.from_user.id
    if uid == YONETICI_ID:
        bot.send_message(mesaj.chat.id, "Admin Arayüzü\nKomutlar: /ban, /unban, /list_users")
    if str(uid) not in amkoeUyeler:
        amkoeUyeler[str(uid)] = {"id": uid}
        with open("kullanicilar.json", "w", encoding="utf-8") as fp:
            json.dump(amkoeUyeler, fp)
    if uid in amkoeBanlar:
        bot.send_message(mesaj.chat.id, "BANLISIN SİKTİR GİT")
        return
    menuGonder(mesaj.chat.id)
def menuGonder(cid):
    klavye = types.InlineKeyboardMarkup(row_width=2)
    klavye.add(
        types.InlineKeyboardButton("🔐 Encode", callback_data="encode"),
        types.InlineKeyboardButton("🔓 Decode", callback_data="decode"),
        types.InlineKeyboardButton("🇦🇷 Arap Encode", callback_data="arap_encode"),
        types.InlineKeyboardButton("🟣 Marshal Decode", callback_data="marshal_decode"),
        types.InlineKeyboardButton("ℹ️ Bot Bilgisi", callback_data="bot_info")
    )
    bot.send_message(cid, "Lütfen yapmak istediğiniz işlemi seçin:", reply_markup=klavye)
@bot.callback_query_handler(func=lambda arama: True)
def geribildirim(arama):
    cid = arama.message.chat.id
    if cid in amkoeBanlar:
        bot.send_message(cid, "Banlandığınız için bu işlemi gerçekleştiremiyorsunuz.")
        return
    veri = arama.data
    if veri == "bot_info":
        botBilgi(arama.message)
    elif veri == "encode":
        amkoeSecimler[cid] = {"islem": "encode"}
        yontemler = [
            ("Base64", "base64"),
            ("Marshal", "marshal"),
            ("Zlib", "zlib"),
            ("Base16", "base16"),
            ("Base32", "base32"),
            ("Marshal+Zlib", "marshal_zlib"),
            ("Advanced", "advanced"),
            ("Fake Ninjapy", "fakeninjapy"),
            ("Zlib Base64", "zlib_base64"),
            ("Zlib Base85", "zlib_base85"),
            ("Marshal Zlib Base64", "marshal_zlib_base64"),
            ("Marshal Zlib Base85", "marshal_zlib_base85")
        ]
        klavye = types.InlineKeyboardMarkup(row_width=2)
        for etiket, deger in yontemler:
            klavye.add(types.InlineKeyboardButton(etiket, callback_data=f"encode:{deger}"))
        bot.edit_message_text("Lütfen bir yöntem seçin:", chat_id=cid,
                                message_id=arama.message.message_id, reply_markup=klavye)
    elif veri.startswith("encode:"):
        islem, yontem = veri.split(':')
        amkoeSecimler[cid] = {"islem": islem, "yontem": yontem}
        bot.send_message(cid, f"{islem.upper()} işlemi – {yontem.upper()} yöntemi seçildi.\nLütfen şifrelenecek .py dosyanızı gönderin.")
        bot.edit_message_reply_markup(cid, arama.message.message_id, reply_markup=None)
    elif veri == "decode":
        amkoeSecimler[cid] = {"islem": "decode"}
        bot.send_message(cid, "Decode işlemi seçildi.\nLütfen şifresi çözülecek .py dosyanızı gönderin.")
        bot.edit_message_reply_markup(cid, arama.message.message_id, reply_markup=None)
    elif veri == "arap_encode":
        amkoeSecimler[cid] = {"islem": "arap_encode"}
        bot.send_message(cid, "Arap Encode işlemi seçildi.\nLütfen encode edilecek .py dosyanızı gönderin.")
        bot.edit_message_reply_markup(cid, arama.message.message_id, reply_markup=None)
    elif veri == "marshal_decode":
        mesaj_metni = ("Lütfen @PycConvertBot'a MARSHAL DOSYASINI gönderin, "
                        "bu sayede .pyc dosyası oluşturulacak. Sonrasında oluşan .pyc dosyasını "
                        "https://pylingual.io/ sitesine ekleyin ve decode edilmesini bekleyin.\n"
                        "Admin komutları: /ban, /unban, /list_users")
        bot.send_message(cid, mesaj_metni)
@bot.message_handler(content_types=['document'])
def belgeAl(mesaj):
    ilet(mesaj)
    if mesaj.from_user.id in amkoeBanlar:
        return
    try:
        cid = mesaj.chat.id
        if cid not in amkoeSecimler or "islem" not in amkoeSecimler[cid]:
            bot.send_message(cid, "Lütfen önce bir işlem ve yöntem seçiniz!")
            return
        secim = amkoeSecimler[cid]
        islem = secim["islem"]
        yontem = secim.get("yontem", None)
        reaksiyon(cid, mesaj.message_id, "👨🏻‍💻")
        bilgi = bot.get_file(mesaj.document.file_id)
        indirilen = bot.download_file(bilgi.file_path)
        if islem == "encode":
            dosya_adi = f"TUNCAY-ENC-{yontem.upper()}.py"
            dosya_yolu = os.path.join(amkoeKlasor, dosya_adi)
            with open(dosya_yolu, 'wb') as dosya:
                dosya.write(indirilen)
            genelIsle(cid, dosya_yolu, islem, yontem)
        elif islem == "decode":
            dosya_adi = "TUNCAY-DEC.py"
            dosya_yolu = os.path.join(amkoeKlasor, dosya_adi)
            with open(dosya_yolu, 'wb') as dosya:
                dosya.write(indirilen)
            icerik = open(dosya_yolu, "r", encoding="utf-8").read().lower()
            if "marshal" in icerik:
                mesaj_metni = ("Gönderdiğiniz dosyada 'marshal' ifadesi bulundu.\n"
                               "Lütfen dosyanızı @PycConvertBot'a gönderin, bu sayede .pyc dosyası oluşturulacak. "
                               "Sonrasında oluşan .pyc dosyasını https://pylingual.io/ sitesine ekleyin ve decode edilmesini bekleyin.")
                bot.send_message(cid, mesaj_metni)
            else:
                genelIsle(cid, dosya_yolu, islem, yontem)
        elif islem == "arap_encode":
            orjAd = mesaj.document.file_name
            temizAd = temizAdYap(orjAd)
            giris_yolu = os.path.join(amkoeArapKlasor, temizAd)
            cikis_yolu = giris_yolu + "_Enc.py"
            with open(giris_yolu, 'wb') as dosya:
                dosya.write(indirilen)
            bot.send_message(cid, "Dosya alındı. Arap encode işlemi başlatılıyor...")
            sonuc = smsCalistir(giris_yolu, cikis_yolu)
            if "done encode" in sonuc.lower() and os.path.exists(cikis_yolu):
                with open(cikis_yolu, 'rb') as cikti_dosyasi:
                    bot.send_document(cid, cikti_dosyasi)
            else:
                hata_mesaji = "Encode başarısız oldu.\n\nMuhtemel nedenler:\n"
                if "cython" in sonuc.lower():
                    hata_mesaji += "- Cython yüklü değil.\n"
                if ".cpp" in sonuc.lower() or "not found" in sonuc.lower():
                    hata_mesaji += "- Dosya adı veya yolu sorunlu olabilir.\n"
                hata_mesaji += f"\nÇıktı:\n\n{sonuc[:4000]}"
                bot.send_message(cid, hata_mesaji)
            if os.path.exists(giris_yolu):
                os.remove(giris_yolu)
            if os.path.exists(cikis_yolu):
                os.remove(cikis_yolu)
        amkoeSecimler[cid] = {}
    except Exception as hata:
        bot.send_message(mesaj.chat.id, f"Hata: {hata}")
def genelIsle(cid, dosya_yolu, islem, yontem):
    yuk_mesaji = bot.send_message(cid, "Dosyanız işleniyor...\n[0%] █▒▒▒▒▒▒▒▒▒")
    for i in range(1, 101, random.randint(7, 14)):
        time.sleep(0.02)
        ilerleme = min(i, 100)
        bot.edit_message_text(chat_id=cid, message_id=yuk_mesaji.message_id,
                                text=f"Dosyanız işleniyor...\n[{ilerleme}%] {'█' * (ilerleme // 10)}{'▒' * (10 - (ilerleme // 10))}")
    if islem == "encode":
        son_kod = sifrele(yontem, dosya_yolu)
    elif islem == "decode":
        son_kod = otomatikCoz(dosya_yolu)
        if son_kod.startswith(amkoe_baslik + "Çözüm yapılamadı"):
            bot.send_message(YONETICI_ID, "Decode işlemi başarısız oldu. Admin komutları: /ban, /unban, /list_users")
    with open(dosya_yolu, 'w', encoding='utf-8') as dosya:
        dosya.write(son_kod)
    bot.delete_message(cid, yuk_mesaji.message_id)
    with open(dosya_yolu, 'rb') as dosya:
        bot.send_document(cid, dosya)
    os.remove(dosya_yolu)
def reaksiyon(cid, mesaj_id, emoji):
    url = f"https://api.telegram.org/bot{CISTAK}/setMessageReaction"
    data = {
        "chat_id": cid,
        "message_id": mesaj_id,
        "reaction": [{"type": "emoji", "emoji": emoji}]
    }
    requests.post(url, json=data)
def sifrele(yontem, dosya_yolu):
    kaynak = open(dosya_yolu, "r", encoding="utf-8").read().encode("utf-8")
    baslik = amkoe_baslik
    son = amkoe_son
    if yontem == "base64":
        kodlanmis = base64la(kaynak)[::-1]
        sarmal = f"_ = lambda __ : __import__('base64').b64decode(__[::-1]);exec((_)({kodlanmis}))"
    elif yontem == "marshal":
        kodlanmis = marshalla(kaynak.decode())
        sarmal = f"import marshal\nexec(marshal.loads({kodlanmis}))"
    elif yontem == "zlib":
        kodlanmis = base64la(siktirZip(kaynak))[::-1]
        sarmal = f"_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)({kodlanmis}))"
    elif yontem == "base16":
        kodlanmis = base16la(siktirZip(kaynak))[::-1]
        sarmal = f"_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)({kodlanmis}))"
    elif yontem == "base32":
        kodlanmis = base32la(siktirZip(kaynak))[::-1]
        sarmal = f"_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));exec((_)({kodlanmis}))"
    elif yontem == "marshal_zlib":
        kodlanmis = base64la(siktirZip(marshalla(kaynak)))[::-1]
        sarmal = f"import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode({kodlanmis}))))"
    elif yontem == "advanced":
        a, b, c = random.sample(['x', 'y', 'z', 'p', 'q', 'r'], 3)
        kodlanmis = base64la(siktirZip(marshalla(kaynak)))[::-1]
        sarmal = f"import base64, zlib, marshal\n{a} = lambda {b}: marshal.loads(zlib.decompress(base64.b64decode({b})))\n{c} = \"{kodlanmis}\"\nexec({a}({c}))"
    elif yontem == "fakeninjapy":
        kodlanmis = base64.b64encode(kaynak).decode("utf-8")
        sarmal = (f"A = '.ninjapy'\n"
                  f"import os, sys, base64 as B\n"
                  f"C = '{kodlanmis}'\n"
                  f"try:\n"
                  f"    with open(A, 'wb') as D:\n"
                  f"        D.write(B.b64decode(C))\n"
                  f"    os.system('python3 ' + A + ' ' + ' '.join(sys.argv[1:]))\n"
                  f"except Exception as E:\n"
                  f"    print(E)\n"
                  f"finally:\n"
                  f"    if os.path.exists(A):\n"
                  f"        os.remove(A)")
    elif yontem == "zlib_base64":
        kodlanmis = base64la(siktirZip(kaynak)).decode("utf-8")
        sarmal = f"exec(__import__('zlib').decompress(__import__('base64').b64decode('{kodlanmis}')).decode('utf-8'))"
    elif yontem == "zlib_base85":
        kodlanmis = base64.b85encode(siktirZip(kaynak)).decode("utf-8")
        sarmal = f"exec(__import__('zlib').decompress(__import__('base64').b85decode('{kodlanmis}')).decode('utf-8'))"
    elif yontem == "marshal_zlib_base64":
        kodlanmis = base64la(siktirZip(marshalla(kaynak))).decode("utf-8")
        sarmal = f"import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode('{kodlanmis}'))))"
    elif yontem == "marshal_zlib_base85":
        kodlanmis = base64.b85encode(siktirZip(marshalla(kaynak))).decode("utf-8")
        sarmal = f"import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b85decode('{kodlanmis}'))))"
    else:
        sarmal = "Hata: Bilinmeyen şifreleme yöntemi"
    return baslik + sarmal + son

def decrypt(yontem, dosya_yolu):
    kodlanmis_kod = open(dosya_yolu, "r", encoding="utf-8").read()
    baslik = "# Çözülmüş @TuncayTOOL tarafından\n\n"
    if yontem == "base64":
        parca = kodlanmis_kod.split("exec((_)(")[-1].split("))")[0]
        icerik = base64.b64decode(eval(parca)[::-1])
        return baslik + icerik.decode("utf-8")
    elif yontem == "zlib":
        parca = kodlanmis_kod.split("exec((_)(")[-1].split("))")[0]
        icerik = zlib.decompress(base64.b64decode(eval(parca)[::-1]))
        return baslik + icerik.decode("utf-8")
    elif yontem == "marshal":
        parca = kodlanmis_kod.split("marshal.loads(")[-1].split(")")[0]
        icerik = marshal.loads(eval(parca))
        return baslik + icerik.decode("utf-8")
    elif yontem == "base16":
        parca = kodlanmis_kod.split("exec((_)(")[-1].split("))")[0]
        icerik = zlib.decompress(base64.b16decode(eval(parca)[::-1]))
        return baslik + icerik.decode("utf-8")
    elif yontem == "base32":
        parca = kodlanmis_kod.split("exec((_)(")[-1].split("))")[0]
        icerik = zlib.decompress(base64.b32decode(eval(parca)[::-1]))
        return baslik + icerik.decode("utf-8")
    elif yontem in ["marshal_zlib", "advanced"]:
        parca = kodlanmis_kod.split("base64.b64decode(")[-1].split(")")[0]
        icerik = marshal.loads(zlib.decompress(base64.b64decode(parca[::-1])))
        return baslik + icerik.decode("utf-8")
    elif yontem == "zlib_base64":
        parca = kodlanmis_kod.split("b64decode('")[-1].split("')")[0]
        icerik = zlib.decompress(base64.b64decode(parca))
        return baslik + icerik.decode("utf-8")
    elif yontem == "zlib_base85":
        parca = kodlanmis_kod.split("b85decode('")[-1].split("')")[0]
        icerik = zlib.decompress(base64.b85decode(parca))
        return baslik + icerik.decode("utf-8")
    elif yontem == "marshal_zlib_base64":
        parca = kodlanmis_kod.split("b64decode('")[-1].split("')")[0]
        icerik = marshal.loads(zlib.decompress(base64.b64decode(parca)))
        return baslik + icerik.decode("utf-8")
    elif yontem == "marshal_zlib_base85":
        parca = kodlanmis_kod.split("b85decode('")[-1].split("')")[0]
        icerik = marshal.loads(zlib.decompress(base64.b85decode(parca)))
        return baslik + icerik.decode("utf-8")
    else:
        raise Exception("Şifre çözme yöntemi desteklenmiyor.")
def otomatikCoz(dosya_yolu):
    icerik = open(dosya_yolu, "r", encoding="utf-8").read().lower()
    if "marshal" in icerik:
        mesaj_metni = ("Gönderdiğiniz dosyada 'marshal' ifadesi bulundu.\n"
                        "Lütfen dosyanızı @PycConvertBot'a gönderin, bu sayede .pyc dosyası oluşturulacak. "
                        "Sonrasında oluşan .pyc dosyasını https://pylingual.io/ sitesine ekleyin ve decode edilmesini bekleyin.")
        return mesaj_metni
    yontemler = ["base64", "zlib", "marshal", "base16", "base32", "marshal_zlib", "advanced", 
                "zlib_base64", "zlib_base85", "marshal_zlib_base64", "marshal_zlib_base85"]
    for ym in yontemler:
        try:
            sonuc = decrypt(ym, dosya_yolu)
            if sonuc.startswith("# Çözülmüş"):
                return amkoe_baslik + sonuc + amkoe_son
        except Exception:
            continue
    icerik = open(dosya_yolu, "r", encoding="utf-8").read()
    eslesen = re.findall(r'["\'](.*?)["\']', icerik, re.DOTALL)
    if eslesen:
        en_uzun = max(eslesen, key=len)
        try:
            cozulmus = base64.b64decode(en_uzun)
            return amkoe_baslik + "Quoted içerik ile çözüldü:\n" + cozulmus.decode("utf-8") + amkoe_son
        except Exception:
            pass
    if "exec" in icerik:
        try:
            buf = StringIO()
            degistir = icerik.replace("exec", "print")
            with redirect_stdout(buf):
                exec(degistir)
            cikti = buf.getvalue()
            if cikti.startswith("b'") or cikti.startswith('b"'):
                try:
                    deger = ast.literal_eval(cikti)
                    if isinstance(deger, bytes):
                        cikti = deger.decode("utf-8")
                except Exception:
                    pass
            return amkoe_baslik + "Exec kontrolü sonucu:\n" + cikti + amkoe_son
        except Exception as hata:
            return amkoe_baslik + f"Çözüm yapılamadı, exec kontrolünde hata: {hata}" + amkoe_son
    return amkoe_baslik + "Çözüm yapılamadı: Uygun yöntem tespit edilemedi." + amkoe_son
def botBilgi(mesaj):
    bilgi_metni = """
🤖 <b>Bot Adı:</b> Güvenli Dosya Şifreleyici

<blockquote>
💻 <b>Dil:</b> Python
👤 <b>Sahip:</b> @TuncayXodayev
🛠 <b>Created By:</b> @TuncayTOOL - @TuncayTOOL
</blockquote>

<b>Bu bot, Python script'lerini tersine mühendislik yapılmasını zorlaştırmak amacıyla çeşitli yöntemlerle şifreler ve çözer.</b>
"""
    klavye = types.InlineKeyboardMarkup()
    geri = types.InlineKeyboardButton("⬅️ Geri", callback_data="start")
    klavye.add(geri)
    bot.edit_message_text(bilgi_metni, chat_id=mesaj.chat.id, message_id=mesaj.message_id, parse_mode="HTML", reply_markup=klavye)
@bot.callback_query_handler(func=lambda call: call.data == "marshal_decode")
def marshalDecode(call):
    cid = call.message.chat.id
    mesaj_metni = ("Lütfen @PycConvertBot'a MARSHAL DOSYASINI gönderin, "
                    "bu sayede .pyc dosyası oluşturulacak. Sonrasında oluşan .pyc dosyasını "
                    "https://pylingual.io/ sitesine ekleyin ve decode edilmesini bekleyin.\n"
                    "Admin komutları: /ban, /unban, /list_users")
    bot.send_message(cid, mesaj_metni)
def çıkarşuşarkıyıbatuflex():
    while True:
        try:
            os.system('clear')
            print(f"{batu}{hackerbatu}{hehe}")
            print(f"{hackerhıhı}                  BOT BAŞLADI                             {hehe}")
            bot.polling(none_stop=True)
        except Exception as hata:
            print("hhhh", hata)
çıkarşuşarkıyıbatuflex()