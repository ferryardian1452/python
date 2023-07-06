from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip44Changes, Bip84, Bip84Coins

ADDR_NUM: int = 9999

mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
print(f"{mnemonic}")

seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

bip84_mst_ctx = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN)

bip84_acc_ctx = bip84_mst_ctx.Purpose().Coin().Account(0)

bip84_chg_ctx = bip84_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

for i in range(ADDR_NUM):
    bip84_addr_ctx = bip84_chg_ctx.AddressIndex(i)
    print(f"{bip84_addr_ctx.PublicKey().ToAddress()}",f"{bip84_addr_ctx.PrivateKey().ToWif()}")
