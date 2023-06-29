from pydantic import BaseModel


class SignData(BaseModel):
    all_gold: int
    today_gold: int
    sign_times: int
    streak: int
