from configparser import ConfigParser
import logging
import sys, os


""" Config Logging """



parser = ConfigParser()
parser.read('config.ini')
log_file_path = parser["LoggingConfig"]["log_file_path"]
log_max_debug_level_file = parser["LoggingConfig"]["log_max_debug_level"]
log_debug_level_file = parser["LoggingConfig"]["log_debug_level_file"]
log_debug_level_console = parser["LoggingConfig"]["log_debug_level_console"]

# create log file if not exists
if not os.path.exists(log_file_path):
    with open(log_file_path, 'w') as archivo:
        archivo.write("")

    print(f'file {log_file_path} not found so it was created')

log_file_handler_format = logging.Formatter('%(asctime)s - %(levelname)s - [line %(lineno)d in %(filename)s] %(message)s ')

log_file_handler = logging.FileHandler(filename=log_file_path, encoding='utf-8')
log_file_handler.setLevel(log_debug_level_file)
log_file_handler.setFormatter(log_file_handler_format)
log_file_handler.mode = 'w'

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setLevel(log_debug_level_console)
consoleHandler.setFormatter(log_file_handler_format)

log = logging.getLogger("statistic_receipting")
log.setLevel(log_max_debug_level_file)
log.addHandler(consoleHandler)
log.addHandler(log_file_handler)

StatisticsListToPrometheus = [
    'dms_value_imei',
    'nas_value_io',
    'nas_value_sinr',
    'nas_value_5g_signal_strength_rsrp',
    'nas_value_5g_signal_strength_snr',
    'nas_value_5g_signal_strength_extended',
    'nas_value_rx_chain_0_info_rx_power',
    'nas_value_rx_chain_0_info_ecio',
    'nas_value_rx_chain_0_info_rscp',
    'nas_value_rx_chain_0_info_rsrp',
    'nas_value_rx_chain_0_info_phase',
    'nas_value_rx_chain_1_info_rx_power',
    'nas_value_rx_chain_1_info_ecio',
    'nas_value_rx_chain_1_info_rscp',
    'nas_value_rx_chain_1_info_rsrp',
    'nas_value_rx_chain_1_info_phase',
    'nas_value_rx_chain_2_info_rx_power',
    'nas_value_rx_chain_2_info_ecio',
    'nas_value_rx_chain_2_info_rscp',
    'nas_value_rx_chain_2_info_rsrp',
    'nas_value_rx_chain_2_info_phase',
    'nas_value_rx_chain_3_info_rx_power',
    'nas_value_rx_chain_3_info_ecio',
    'nas_value_rx_chain_3_info_rscp',
    'nas_value_rx_chain_3_info_rsrp',
    'nas_value_rx_chain_3_info_phase',
    'wds_value_tx_packets_ok',
    'wds_value_rx_packets_ok',
    'wds_value_tx_packets_error',
    'wds_value_rx_packets_error',
    'wds_value_tx_overflows',
    'wds_value_rx_overflows',
    'wds_value_tx_bytes_ok',
    'wds_value_rx_bytes_ok',
    'wds_value_tx_packets_dropped',
    'wds_value_rx_packets_dropped',
    'wds_value_channel_rates_channel_tx_rate_bps'
    "nas_value_nr5g_arfcn",
    "nas_value_nr5g_cell_information_global_cell_id",
    "nas_value_nr5g_cell_information_physical_cell_id",
    "nas_value_nr5g_cell_information_plmn",
    "nas_value_nr5g_cell_information_rsrp",
    "nas_value_nr5g_cell_information_rsrq",
    "nas_value_nr5g_cell_information_snr",
    "nas_value_nr5g_cell_information_tracking_area_code"
    'gpsd_sky_timestamp',
    'gpsd_sky_hdop',
    'gpsd_sky_pdop',
    'gpsd_tpv_timestamp',
    'gpsd_tpv_lat',
    'gpsd_tpv_lon',
    'gpsd_tpv_alt',
    'gpsd_tpv_althae',
    'gpsd_tpv_epx',
    'gpsd_tpv_epy',
    'gpsd_tpv_epv',
    'gpsd_tpv_speed',
    'gpsd_tpv_eps',
    'throughput_upload_kb',
    'throughput_download_kb',
    'throughput_upload_speed_kbps',
    'throughput_download_speed_kbps',
]