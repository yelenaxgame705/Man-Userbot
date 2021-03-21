#Recode by @mrismanaziz

from datetime import datetime
import time
from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, StartTime
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.keping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**『⍟𝐊𝐎𝐍𝐓𝐎𝐋』**")
    await pong.edit("**◆◈𝐊𝐀𝐌𝐏𝐀𝐍𝐆◈◆**")
    await pong.edit("**𝐏𝐄𝐂𝐀𝐇𝐊𝐀𝐍 𝐁𝐈𝐉𝐈 𝐊𝐀𝐔 𝐀𝐒𝐔**")
    await pong.edit("**☬𝐒𝐈𝐀𝐏 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐄𝐍𝐔𝐌𝐁𝐔𝐊 𝐀𝐒𝐔☬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**✲ 𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙻𝙴𝙳𝚄𝙶** "
                    f"\n ⫸ ᴷᵒⁿᵗᵒˡ `%sms` \n"
                    f"**✲ 𝙱𝙸𝙹𝙸 𝙿𝙴𝙻𝙴𝚁** "

                    f"\n ⫸ ᴷᵃᵐᵖᵃⁿᵍ『`{ALIVE_NAME}`』 \n" % (duration))

@register(outgoing=True, pattern="^.kping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`KONTOLL....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**NGENTOT!! 🐨**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration))


@register(outgoing=True, pattern='^.usange(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit("**Informasi Dyno ★**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n" f"-> `Penggunaan Dyno` **{ALIVE_NAME}**:\n" f" ❉ **10 Jam - " f"51 Menit - 0%**" "\n ◐━─━─━─━─━──━─━─━─━─━◐\n" "-> `Sisa Dyno Bulan Ini`:\n" f" ❉ **9989 Jam - 9948 Menit " f"- 99%**\n" "╰━━━━━━━━━━━━━━━━━━━━╯"
                     )
# @mixiologist


CMD_HELP.update({
    "fakedyno":
    "`.usange`\
\nUsage: Dynos tipu tipu anjeeeng."
})
