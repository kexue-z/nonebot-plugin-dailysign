from nonebot import on_regex
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import GROUP, GroupMessageEvent
from nonebot_plugin_tortoise_orm import add_model

from .data_source import get_sign_in

add_model("nonebot_plugin_dailysign.models")

sign = on_regex(r"^签到$", permission=GROUP, priority=5, block=True)


@sign.handle()
async def _(event: GroupMessageEvent):
    user_id = event.user_id
    group_id = event.group_id
    logger.opt(colors=True).info(f"群 <y>{group_id}</y> : 用户 <y>{user_id}</y> 签到")
    msg = await get_sign_in(user_id, group_id)
    await sign.finish(msg)
