from nonebot import get_driver
from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    daily_sign_base: int = 100
    """签到基础点数"""
    daily_sign_multiplier: float = 0.2
    """连续签到加成比例"""
    daily_sign_max_lucky: int = 10
    """最大幸运值"""


plugin_config = Config.parse_obj(get_driver().config)
BASE = plugin_config.daily_sign_base
MULTIPLIER = plugin_config.daily_sign_multiplier
MAX_LUCKY = plugin_config.daily_sign_max_lucky
