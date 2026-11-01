from datetime import datetime, timedelta
from json import dumps, loads
from pathlib import Path

file = Path("views.json")
if not file.exists():
    file.write_text("{}")


def set_view(ip: str | None = None) -> tuple[int, int, int]:
    views = loads(file.read_text())
    if ip:
        print(ip)
        views[ip] = datetime.now().timestamp()
        file.write_text(dumps(views))
    else:
        print("no ip")
    return (
        len(views),
        len(
            [
                v
                for v in views.values()
                if datetime.fromtimestamp(v) > datetime.now() - timedelta(hours=24)
            ]
        ),
        len(
            [
                v
                for v in views.values()
                if datetime.fromtimestamp(v) > datetime.now() - timedelta(weeks=1)
            ]
        )
    )
