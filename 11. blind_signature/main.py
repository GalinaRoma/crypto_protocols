from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from random import SystemRandom

print('Generate RSA key...', end="\n\n")
priv = RSA.generate(3072)
pub = priv.publickey()

COUNT_FOR_TRUST = 2


class Bank:
    def __init__(self):
        self.last_amount = -1
        self.cur_trust = COUNT_FOR_TRUST

    def sign(self, msg_blinded):
        if self.cur_trust > 0:
            return 'err', 'No trust yet, content needed'

        print('Bank unseeingly signed content')
        return 'ok', priv.sign(msg_blinded, 0)

    def sign_with_open(self, text):
        print('Bank read the contents of the account: ' + str(text))

        if text['amount'] == self.last_amount:
            print('The degree of confidence of the bank has increased!')
            self.cur_trust -= 1
        else:
            print('The bank remembered the new amount:' + str(text['amount']))
            self.last_amount = text['amount']
            self.cur_trust = COUNT_FOR_TRUST

        print("Bank saw id. We will not send a letter")
        print()


class User:
    def __init__(self):
        self.r = None
        self.accounts = [
            {
                'id': 1,
                'amount': 100,
            },
            {
                'id': 2,
                'amount': 100,
            },
            {
                'id': 3,
                'amount': 100,
            },
            {
                'id': 4,
                'amount': 100,
            }
        ]

    def blind_msg(self, msg):
        self.r = SystemRandom().randrange(pub.n >> 10, pub.n)

        hash = SHA256.new()
        hash.update(msg)
        msgDigest = hash.digest()

        return pub.blind(msgDigest, self.r)

    def unblind_msg(self, blinded):
        return pub.unblind(blinded[0], self.r)

    def check_msg(self, msg, blinded):
        msg_sign = self.unblind_msg(blinded)

        hash = SHA256.new()
        hash.update(msg)
        msgDigest = hash.digest()

        print("Validation passed? ", pub.verify(msgDigest, (msg_sign,)))

    def send_accounts(self, bank):
        for i in range(0, len(self.accounts)):
            account = self.accounts[i]

            msg = str(account).encode()
            msg_blinded = self.blind_msg(msg)

            status, msg_blinded_sign = bank.sign(msg_blinded)
            if status != 'ok':
                bank.sign_with_open(account)
                continue

            self.check_msg(msg, msg_blinded_sign)


def main():
    bank = Bank()
    user = User()

    user.send_accounts(bank)


if __name__ == '__main__':
    main()
