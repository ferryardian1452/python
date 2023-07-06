from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip44, Bip44Changes, Bip44Coins

ADDR_NUM: int = 9999

mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
print(f"{mnemonic}")

seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)

bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)

bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

for i in range(ADDR_NUM):
    bip44_addr_ctx = bip44_chg_ctx.AddressIndex(i)
    print(f"{bip44_addr_ctx.PublicKey().ToAddress()}",f"{bip44_addr_ctx.PrivateKey().ToWif()}")
