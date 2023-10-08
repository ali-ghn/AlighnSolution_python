class Web3ClientHelper:
    def __int__(self, mnemonic: str, secret: str, ethereum_node_provider_key: str, test: bool = False):
        self.mnemonic = mnemonic
        self.secret = secret

