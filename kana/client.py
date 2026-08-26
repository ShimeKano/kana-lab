class KanaClient:
    """Transport-neutral interface for an authorized Kana integration.

    The concrete transport is intentionally not guessed until an allowed,
    documented or normally observable interface is identified.
    """

    def __init__(self) -> None:
        self.connected = False

    async def connect(self) -> None:
        raise NotImplementedError("Kana transport has not been identified yet")

    async def send_command(self, command: str) -> None:
        raise NotImplementedError("Kana transport has not been identified yet")

    async def close(self) -> None:
        self.connected = False
