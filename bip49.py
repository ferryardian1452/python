from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip44Changes, Bip49, Bip49Coins

ADDR_NUM: int = 9999

mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
print(f"{mnemonic}")

seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

bip49_mst_ctx = Bip49.FromSeed(seed_bytes, Bip49Coins.LITECOIN)

bip49_acc_ctx = bip49_mst_ctx.Purpose().Coin().Account(0)

bip49_chg_ctx = bip49_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

for i in range(ADDR_NUM):
    bip49_addr_ctx = bip49_chg_ctx.AddressIndex(i)
    print(f"{bip49_addr_ctx.PublicKey().ToAddress()}",f"{bip49_addr_ctx.PrivateKey().ToWif()}")
