import sys
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    """
    Escaneia a rede usando requisições ARP para encontrar dispositivos ativos.
    :param ip_range: Ex: "192.168.1.0/24"
    :return: Lista de dicionários com IP e MAC dos dispositivos encontrados.
    """
    print(f"[+] Iniciando o escaneamento na rede: {ip_range}\n")
    
    # Cria um pacote ARP solicitando o IP de destino e um quadro Ethernet de broadcast
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    # Envia o pacote e aguarda a resposta (timeout de 2 segundos)
    # srp() envia e recebe pacotes na camada 2 (Data Link Layer)
    answered_list = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in answered_list:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def display_results(devices):
    print("Dispositivos encontrados na rede:")
    print("-" * 50)
    print(f"{'Endereço IP':<20} | {'Endereço MAC'}")
    print("-" * 50)
    
    for device in devices:
        print(f"{device['ip']:<20} | {device['mac']}")
    
    print("-" * 50)
    print(f"Total de dispositivos encontrados: {len(devices)}")

if __name__ == "__main__":
    # Defina a faixa de IP da sua rede (substitua pelo IP correto da sua sub-rede)
    # Exemplo comum: "192.168.0.0/24" ou "192.168.1.0/24"
    target_ip = "192.168.1.0/24"
    
    try:
        active_devices = scan_network(target_ip)
        display_results(active_devices)
    except PermissionError:
        print("[-] Erro: Permissões insuficientes. Execute o script como Administrador (sudo no Linux/macOS).")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Ocorreu um erro inesperado: {e}")