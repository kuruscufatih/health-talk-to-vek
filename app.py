from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get(
    "ms_token", "NMyZ1u0chqSXkDevs7Cdu_fO4nyVXCH_s0wrbHGfx5_j2cobwauU_wAwalAc186ALXIeUa2gA86Txny9U11-oUSoFcihbcS2WeOx6xpm9S3cDdksHIZoNyZ_QRlmj8RhD09_vqdl-GZd3xywLA4pNJwtkQ=="
)  # set your own ms_token, think it might need to have visited a profile


async def user_example():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "webkit"))
        user = api.user("therock")
        user_data = await user.info()
        print(user_data)

        async for video in user.videos(count=30):
            print(video)
            print(video.as_dict)

        async for playlist in user.playlists():
            print(playlist)


if __name__ == "__main__":
    asyncio.run(user_example())