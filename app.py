import platform
from datetime import datetime, timezone


def get_system_status():
    return {
        "status": "HEALTHY",
        "application": "Infrastructure Health API",
        "version": "1.0.0",
        "platform": platform.system(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    system = get_system_status()

    for key, value in system.items():
        print(f"{key}: {value}")
