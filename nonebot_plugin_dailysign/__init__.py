from nonebot import require, on_fullmatch
from nonebot.log import logger
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import GroupMessageEvent as V11MessageEvent
from nonebot.adapters.onebot.v12 import GroupMessageEvent as V12MessageEvent

from .config import Config
from .data_source import get_sign_in

require("nonebot_plugin_tortoise_orm")
from nonebot_plugin_tortoise_orm import add_model

add_model("nonebot_plugin_dailysign.models")

__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_dailysign",
    description="简单的签到插件",
    usage="发送 签到 即可",
    type="application",
    homepage="https://github.com/kexue-z/nonebot-plugin-dailysign",
    config=Config,
    supported_adapters={"~onebot.v11"},
)

sign = on_fullmatch("签到", priority=5, block=False)


@sign.handle()
async def _(event: V11MessageEvent | V12MessageEvent):
    user_id = int(event.user_id)
    group_id = int(event.group_id)
    logger.debug(f"群 group_id: 用户 {user_id} 签到")
    msg = await get_sign_in(user_id, group_id)
    await sign.finish(msg, at_sender=True)
