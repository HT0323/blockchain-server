from ecdsa import SigningKey
from ecdsa import SECP256k1


def main():
    # 秘密鍵の作成
    secret_key = SigningKey.generate(curve=SECP256k1)
    # 公開鍵の作成
    public_key = secret_key.verifying_key
    # 秘密鍵を16進数文字列に変換
    secret_key_str = secret_key.to_string().hex()
    # 公開鍵を16進数文字列に変換
    public_key_str = public_key.to_string().hex()

    key = {"secret_key_str": secret_key_str, "public_key_str": public_key_str}
    print(key)


if __name__ == "__main__":
    main()
