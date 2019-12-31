import hashlib

SECRET = 'извращенец'

patients = [{
        'user': 'Ivanov',
        'card_number': '449445454'
    }, {
        'user': 'Petrov',
        'card_number': '023167194'
    }, {
        'user': 'Sidorov',
        'card_number': '217989437'
    }
]


class MyHash:
    @staticmethod
    def hash(msg):
        md5_hash = int(hashlib.md5(msg.encode()).hexdigest(), 16)

        return str(md5_hash)[-9:]

    @staticmethod
    def check_patient(patient):
        if MyHash.hash(SECRET) == patient['card_number']:
            print('Patient ' + patient['user'] + ' is the same pervert')
        print('Patient card number: ' + patient['card_number'])


def main():
    print('Secret is: ' + SECRET)
    print('Secret hash: ' + MyHash.hash(SECRET))
    for i in range(0, len(patients)):
        article = patients[i]

        MyHash.check_patient(article)


if __name__ == '__main__':
    main()
