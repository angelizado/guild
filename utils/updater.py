import aiohttp
import asyncio
from rich.console import Console

console = Console()

async def update(guild_id, token):
    url = 'https://discord.com/api/v9/users/@me/clan'
    payload = {"identity_guild_id": guild_id, "identity_enabled": True}
    headers = {"Authorization": token, "Content-Type": "application/json"}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(url, json=payload, headers=headers) as response:
                if response.status == 200:
                    tag = (await response.json()).get('clan', {}).get('tag')
                    console.print(f"[bold][green]⟳[/green][/bold] | Clan updated for [yellow]{tag}[/yellow]")
                else:
                    console.print(f"[bold][yellow]⚠[/yellow][/bold] | Failed to update clan for Guild ID {guild_id}: {await response.text()}")
    except Exception as e:
        console.print(f"[bold][yellow]⚠[/yellow][/bold] | Error updating clan for Guild ID {guild_id}: {e}")

async def updater(config):
    current = 0
    while True:
        guild_id = config["guild_ids"][current]
        await update(guild_id, config["token"])
        current = (current + 1) % len(config["guild_ids"])
        await asyncio.sleep(config["interval"] / 1000)

async def start(config):
    await updater(config)
