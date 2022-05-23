from random import randint
from datetime import date

from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Message, MessageSegment

from .models import DailySign


async def get_sign_in(user_id: int, group_id: int) -> Message:
    msg = Message()
    last_sign = await DailySign.get_last_sign(user_id, group_id)
    # 判断是否已签到
    today = date.today()
    logger.debug(f"last_sign: {last_sign}")
    logger.debug(f"today: {today}")
    if today == last_sign:
        msg += Message("你今天已经签到了，不要贪心噢。")
        return msg

    # 签到名次
    sign_num = await DailySign.filter(group_id=group_id, last_sign=today).count() + 1

    # 设置签到
    data = await DailySign.sign_in(
        user_id=user_id,
        group_id=group_id,
        gold_base=100,
        lucky_gold=randint(1, 10),
        today_lucky=randint(1, 10) - randint(1, 10),
    )

    msg_txt = f"本群第 {sign_num} 位 签到完成\n"
    msg_txt += f"获得金币：+{data.today_gold} (总金币：{data.all_gold})\n"
    msg_txt += f"累计签到次数：{data.sign_times}"
    msg += MessageSegment.text(msg_txt)

    return msg
