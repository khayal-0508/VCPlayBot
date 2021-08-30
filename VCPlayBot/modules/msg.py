import os
from VCPlayBot.config import SOURCE_CODE
from VCPlayBot.config import ASSISTANT_NAME
from VCPlayBot.config import PROJECT_NAME
from VCPlayBot.config import SUPPORT_GROUP
from VCPlayBot.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Salam 👋 [{}](tg://user?id={})!**\n\n🤖 Mən qrupunuzun səsli söhbətində musiqi dinləməyiniz üçün @tag1y3v tərəfindən yaradılmış bir botam.\n\n✅ Daha çox məlumat üçün /help yazın."
      HELP_MSG = [
        ".",
f"""
**Hey 👋 {PROJECT_NAME} -a yenidən xoş gəldiniz

⚪️ {PROJECT_NAME} Sizin səsli söhbətinizdə musiqi dinləməyiniz üçündür

⚪️ Assistantın adı >> @{ASSISTANT_NAME}\n\nTəlimatlar üçün növbəti düyməsini basın**
""",

f"""
**Quraşdırmaq**

1) Mənə qrupunuzda adminlik verin.
2) Səsli söhbət başladın.
3) Assistantın qrupa qoşulması üçün adminlərdən biri /play və ya /userbotjoin əmrini işlətsin
*) @{ASSISTANT_NAME} qrupa qoşulmasa @tag1y3v ilə kontakta keçin.
""",
f"""
**Əmrlər**

**=>> Musiqi oxutmaq 🎧**

- /play: İstədiyiniz mahnının adını yazaraq qoymaq
- /play [yt url] : Verilmiş YouTube linki ilə mahnı qoşmaq
- /play [fayla yanıt verərək]: Yanıt verdiyiniz faylı səsli söhbətdə oxutmaq
- /ytplay: Youtube Music vasitəsilə mahnı qoşmaq

**=>> Oxunmaq ⏯**

- /player: Player menyusunu açmaq
- /skip: Oxunan musiqinu dəyişdirmək
- /pause: Oxunan musiqiyə pauza vermək
- /resume: Pauza verilən musiqiyə davam etmək
- /end: Musiqini dayandırmaq
- /current: Oxunn musiqiyə baxmaq
- /playlist: Playlistə baxmaq

*Player əmrləri və /play, /current, /playlist  istisna olmaqla digər əmrləri yalnız qrup adminləri yerinə yetirə bilər.
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Admin listi yeniləmək
- /userbotjoin: @{ASSISTANT_NAME} -ı qrupa dəvət etmək
""",
f"""
**=>> Musiqi yükləmək🎸**

- /video [video adı]: YouTube-dan video yükləmək
- /song [mahnı adı]: YouTube-dan mahnı yükləmək

**=>> Axtarış funksiyları 📄**

- /search [mahnı adı]: YouTube-dan link almaq
- /lyrics [mahnı adı]: Mahnının sözlərini tapmaq
""",

f"""
**=>> Bot sahibi üçün olan əmrlər ⚔️**

 - /userbotleaveall - Assistantı bütün qruplardan çıxarmaq
 - /broadcast <yanıt verilən mesaj> - Yanıt verilən mesajı bütün qruplara göndərmək
 - /pmpermit [on/off] - enable/disable Şəxsi mesajlar
*Bot sahibi bütün əmrləri bütün qruplarda icra edə bilir.

"""
      ]
