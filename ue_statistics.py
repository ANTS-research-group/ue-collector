from configparser import ConfigParser
import json
import socket
import time
import modules.defines as defines

from prometheus_client import Gauge, start_http_server


parser = ConfigParser()
parser.read('config.ini')
log_file_path = parser["LoggingConfig"]["log_file_path"]
address_listen = parser["ServerConfig"]["address"]
port_listen = int(parser["ServerConfig"]["port"])
prometheus_address = parser["PrometheusConfig"]["address"]
prometheus_port = int(parser["PrometheusConfig"]["port"])

start_http_server(int(prometheus_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', int(port_listen)))
sock.settimeout(60) #timeout 60 seconds
#init 
end_time = 0
start_time = 0
gauges_list = {}
packet_statistics_before = {}



while True:
    # sock.sendto(bytes("hello", "utf-8"), ip_co)
    defines.log.debug(f'\nwaiting to receive a new message on {port_listen}...\n')
    
    try:
        data, addr = sock.recvfrom(5120)
    except Exception:
        continue
    
    defines.log.debug(f'message received from {addr}')
    info = json.loads(data.decode("utf-8"))

    if (not info["static"] or not info["dynamic"]):
        
        defines.log.error("empty static or dynamic info")
        time.sleep(10)
        continue
    
    defines.log.debug(f"new data received")
    
    try:
        static_info = info["static"]
        dynamic_info = info["dynamic"]
        imei = static_info["dms_value_imei"]
    except:
        continue
    
    if imei not in gauges_list:

        gauges = {}

        for elem in defines.StatisticsListToPrometheus:
            g = Gauge(f"{elem}_{imei}", 'info')
            gauges.update({f"{elem}_{imei}":g})

        defines.log.info(f"new imei was found: {imei} and will be save into the gauge list")

        gauges_list.update({imei:gauges})

    gauges = gauges_list.get(imei)

    for gauge_name in gauges:
        
        parts = gauge_name.rsplit('_', 1)
        name = '_'.join(parts[:-1])
        if (name not in dynamic_info):
            continue
            
        value = dynamic_info[name]
        
        if (value is None):
            continue

        g = gauges[gauge_name]
        g.set_to_current_time()
        g.set(value)

        defines.log.debug(f'{gauge_name}: {value}')

    defines.log.info("received: OK\n")