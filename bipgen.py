import os
import random
import binascii
import mnemonic

num_wallets = 99999
with open('wallets.txt', 'w') as f:
    for i in range(num_wallets):
        entropy = os.urandom(32)
        m = mnemonic.Mnemonic('english')
        wallet = m.to_mnemonic(entropy)
        f.write(wallet + '\n')
