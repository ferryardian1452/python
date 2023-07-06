from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip44Changes, Bip86, Bip86Coins

ADDR_NUM: int = 9999

mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
print(f"{mnemonic}")

seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

bip86_mst_ctx = Bip86.FromSeed(seed_bytes, Bip86Coins.BITCOIN)

bip86_acc_ctx = bip86_mst_ctx.Purpose().Coin().Account(0)

bip86_chg_ctx = bip86_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

for i in range(ADDR_NUM):
    bip86_addr_ctx = bip86_chg_ctx.AddressIndex(i)
    print(f"{bip86_addr_ctx.PublicKey().ToAddress()}",f"{bip86_addr_ctx.PrivateKey().ToWif()}")
