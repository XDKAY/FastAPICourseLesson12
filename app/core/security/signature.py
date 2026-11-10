from itsdangerous import HMACAlgorithm, Signer

__all__ = ("signature", )


# == Нельзя оставлять секретные ключи и другие важные данные в коде ==
# Здесь сделано в рамках проекта
# В лучшем случае закинуть это в .env файл

SECRET_KEY = "fastapi course lesson 12"


class Signature(Signer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            secret_key=SECRET_KEY,
            algorithm=HMACAlgorithm(),
        )

    def generate(self, value: str | bytes) -> str:
        return super().get_signature(value).decode("utf-8")

    def verify(self, value: str | bytes, signature: str | bytes) -> bool:
        return super().verify_signature(value, signature)


signature = Signature()
