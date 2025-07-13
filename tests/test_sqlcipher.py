import asyncio


from tortoise import Tortoise, fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"


pwd = "\"x'adfaxcv1245764qzxcvbre'\""


async def init():
    print(f"sqlcipher://test.db?journal_mode=WAL&key={pwd}&cipher_hmac_algorithm=HMAC_SHA256")
    await Tortoise.init(
        # db_url=f"sqlcipher://test.db?journal_mode=WAL&key={pwd}&cipher_hmac_algorithm=HMAC_SHA256",  # 数据库连接字符串
        db_url="sqlcipher://fdb.db?journal_mode=WAL&key=\"x'c5DJeTTNz#QTjf5Y6br6KhDunzxM@QwKSCRZ'\"&busy_timeout=1000",
        modules={"models": ["__main__"]},  # 包含模型的模块
        use_tz=False,
        # timezone="Asia/Shanghai",
    )

    # await Tortoise.init(
    #     {
    #         "apps": {"models": {"default_connection": "default", "models": ["__main__"]}},
    #         "connections": {
    #             "default": {
    #                 "credentials": {
    #                     # "driver": "aiosqlcipher",
    #                     "file_path": "test.db",
    #                     "journal_mode": "WAL",
    #                     "journal_size_limit": 16384,
    #                     "key": "123",
    #                 },
    #                 "engine": "tortoise.backends.sqlcipher",
    #             }
    #         },
    #     }
    # )
    await Tortoise.generate_schemas()


async def main():
    await init()

    # 创建用户
    user = await User.create(username="test", email="test@example.com")
    print(f"Created user: {user.username}")

    # 查询用户
    users = await User.all()
    for u in users:
        print(f"User: {u.username}, Email: {u.email}")

    await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(main())
