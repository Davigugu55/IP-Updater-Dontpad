from requests import get
import dontpad

ipDontpad = dontpad.read("dontpadExtHERE")
ipAtual = get('https://api.ipify.org').text + ':25565'

print('IP Antigo:\t' + ipDontpad)
print('IP Atual:\t' + ipAtual)

if ipDontpad != ipAtual:
    print('\nAtualizando IP...\n')
    dontpad.write("dontpadExtHERE", ipAtual)
