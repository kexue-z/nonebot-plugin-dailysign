# 一个签到

发送 `签到` 来签到

有什么用？

可以获取金币

然后呢？

就没了

因为是写着玩练手的

因为是用了刚刚摸鱼的 `nonebot_plugin_tortoise_orm` 来弄数据库啦

[https://github.com/kexue-z/nonebot-plugin-tortoise-orm](https://github.com/kexue-z/nonebot-plugin-tortoise-orm)

可以开发插件来获取金币？

## 插件使用

```python

from nonebot_plugin_dailysign.models import DailySign

await DailySign.get_gold(user_id, group_id)
# 获取金币

await DailySign.adjust_gold(adjust, user_id, group_id)
# 更改金币数量 adjust 正负均可

```

## 计划

- [ ] 用来减少 `SETU NOW` 插件的 CD
