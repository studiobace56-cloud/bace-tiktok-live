"""Free best-effort TikTok LIVE checks; never fabricate statuses or viewer counts."""
import asyncio, json, datetime
from pathlib import Path
from TikTokLive import TikTokLiveClient

HANDLES = ['lo6iq_pi4','kristiqnagenova','vivi_love350']

async def check(handle):
    client = TikTokLiveClient(unique_id='@'+handle)
    try:
        # A failed request must NOT be interpreted as offline.
        live = await asyncio.wait_for(client.is_live(), timeout=22)
        if type(live) is not bool:
            return {'handle':handle,'status':'unknown','viewers':None}
        return {'handle':handle,'status':'live' if live else 'offline','viewers':None}
    except Exception as exc:
        print('Check failed for',handle,type(exc).__name__)
        return {'handle':handle,'status':'unknown','viewers':None}
    finally:
        try:
            await client.disconnect()
        except Exception:
            pass

async def main():
    profiles = await asyncio.gather(*(check(h) for h in HANDLES))
    result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'profiles':profiles}
    Path('live-status.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(result)

if __name__=='__main__':
    asyncio.run(main())
