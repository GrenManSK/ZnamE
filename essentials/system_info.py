import os
import wmi
import GPUtil
import psutil
import platform
import cpuinfo
import socket
import sys
import tabulate
import re
import uuid
from .writing import to_info, printnlog


def system_info(logger, screensize, verzia, datelog):
    try:
        os.makedirs("C:/Users/" + os.getlogin() +
                    "/AppData/Local/ZnámE/")
    except FileExistsError:
        pass
    open("C:/Users/" + os.getlogin() +
         "/AppData/Local/ZnámE/info.txt", "x")
    logger.stay(to_info(datelog, verzia.read(), end='',
                file='version', mode='w', toprint=False))
    logger.stay(printnlog(datelog, 'Getting system information', toprint=False))
    logger.next(to_info(datelog, 'Resolution: ' +
                        str(screensize[0]) + 'x' + str(screensize[1]) + '\n', toprint=False))
    computer1 = wmi.WMI()
    computer_info: list[str] = computer1.Win32_ComputerSystem()[0]
    os_info: list[str] = computer1.Win32_OperatingSystem()[0]
    proc_info: list[str] = computer1.Win32_Processor()[0]
    gpu_info: list[str] = computer1.Win32_VideoController()[0]

    def get_size1(bytes: int | float, suffix: str = "B"):
        """
        It takes a number of bytes and returns a string with the number of bytes and the appropriate
        unit

        :param bytes: The number of bytes to convert
        :param suffix: The suffix to be appended to the size, defaults to B (optional)
        """
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor: int = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    "Printing and logging user PC info; !! info is send to none server"

    my_system = platform.uname()
    my_cpuinfo = cpuinfo.get_cpu_info()
    pc = wmi.WMI()
    svmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    gpus = GPUtil.getGPUs()
    partitions = psutil.disk_partitions()
    disk_io = psutil.disk_io_counters()
    if_addrs = psutil.net_if_addrs()
    net_io = psutil.net_io_counters()
    os_info = pc.Win32_operatingSystem()[0]
    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    cpufreq = psutil.cpu_freq()
    os_version: str = ' '.join([os_info.Version, os_info.BuildNumber])
    logger.stay(to_info(datelog, os_info, toprint=False))
    system_ram = float(os_info.TotalVisibleMemorySize) / \
        1048576  # KB to GB
    logger.stay(to_info(datelog, 'OS Name: {0}'.format(os_name), toprint=False))
    logger.stay(
        to_info(datelog, f"Device Name: {my_system.node}", toprint=False))
    logger.stay(
        to_info(datelog, f"Architecture: {my_system.machine}", toprint=False))
    logger.stay(
        to_info(datelog, f"Processor: {my_system.processor}", toprint=False))
    logger.stay(to_info(datelog, 'CPU: {0}'.format(
        proc_info.Name), toprint=False))
    logger.stay(to_info(datelog, "="*40 + "CPU Info" + "="*40, toprint=False))
    logger.stay(
        to_info(datelog, f"CPU architecture: {my_cpuinfo['arch']}", toprint=False))
    logger.stay(to_info(datelog, "Physical cores:" +
                str(psutil.cpu_count(logical=False)), toprint=False))
    logger.stay(to_info(datelog, "Total cores:" +
                str(psutil.cpu_count(logical=True)), toprint=False))
    logger.stay(
        to_info(datelog, f"Max Frequency: {cpufreq.max:.2f}Mhz", toprint=False))
    logger.stay(
        to_info(datelog, f"Min Frequency: {cpufreq.min:.2f}Mhz", toprint=False))
    logger.stay(
        to_info(datelog, f"Current Frequency: {cpufreq.current:.2f}Mhz", toprint=False))
    logger.stay(to_info(datelog, "CPU Usage Per Core:", toprint=False))
    logger.next('')
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        to_info(datelog, f"Core {i}: {percentage}%")
    logger.prev(to_info(datelog, pc.Win32_Processor()[0], toprint=False))
    logger.stay(
        to_info(datelog, f"Total CPU Usage: {psutil.cpu_percent()}%", toprint=False))
    logger.stay(
        to_info(datelog, 'RAM: {0} GB'.format(system_ram), toprint=False))
    logger.stay(
        to_info(datelog, "="*40 + "Memory Information" + "="*40, toprint=False))
    logger.stay(
        to_info(datelog, f"Total: {get_size1(svmem.total)}", toprint=False))
    logger.stay(
        to_info(datelog, f"Available: {get_size1(svmem.available)}", toprint=False))
    logger.stay(
        to_info(datelog, f"Used: {get_size1(svmem.used)}", toprint=False))
    logger.stay(
        to_info(datelog, f"Percentage: {svmem.percent}%", toprint=False))
    logger.stay(to_info(datelog, "="*20 + "SWAP" + "="*20, toprint=False))
    logger.stay(
        to_info(datelog, f"Total: {get_size1(swap.total)}", toprint=False))
    logger.stay(
        to_info(datelog, f"Free: {get_size1(swap.free)}", toprint=False))
    logger.stay(
        to_info(datelog, f"Used: {get_size1(swap.used)}", toprint=False))
    logger.stay(to_info(datelog, f"Percentage: {swap.percent}%", toprint=False))
    logger.stay(to_info(datelog, 'Graphics Card: {0}'.format(
        gpu_info.Name), toprint=False))
    logger.stay(
        to_info(datelog, "="*40 + "GPU Details" + "="*40, toprint=False))
    list_gpus: list = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    logger.stay(to_info(datelog, tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                                     "temperature", "uuid")), toprint=False))
    logger.stay(to_info(datelog, 
        f'IP Adress: {socket.gethostbyname(socket.gethostname())}', toprint=False))
    logger.stay(to_info(datelog, 
        f"MAC Adress: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}, toprint=False"))
    logger.stay(
        to_info(datelog, "="*40 + "Disk Information" + "="*40, toprint=False))
    logger.stay(to_info(datelog, "Partitions and Usage:", toprint=False))
    logger.next('')
    for partition in partitions:
        logger.stay(
            to_info(datelog, f"=== Device: {partition.device} ===", toprint=False))
        logger.stay(
            to_info(datelog, f"  Mountpoint: {partition.mountpoint}", toprint=False))
        logger.stay(
            to_info(datelog, f"  File system type: {partition.fstype}", toprint=False))
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        logger.stay(
            to_info(datelog, f"  Total Size: {get_size1(partition_usage.total)}", toprint=False))
        logger.stay(
            to_info(datelog, f"  Used: {get_size1(partition_usage.used)}", toprint=False))
        logger.stay(
            to_info(datelog, f"  Free: {get_size1(partition_usage.free)}", toprint=False))
        logger.stay(
            to_info(datelog, f"  Percentage: {partition_usage.percent}%", toprint=False))
    logger.prev(
        to_info(datelog, f"Total read: {get_size1(disk_io.read_bytes)}", toprint=False))
    logger.stay(
        to_info(datelog, f"Total write: {get_size1(disk_io.write_bytes)}", toprint=False))
    logger.stay(
        to_info(datelog, "="*40 + "Network Information" + "="*40, toprint=False))
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            logger.next(
                to_info(datelog, f"=== Interface: {interface_name} ===", toprint=False))
            if str(address.family) == 'AddressFamily.AF_INET':
                logger.next(
                    to_info(datelog, f"  IP Address: {address.address}", toprint=False))
                logger.stay(
                    to_info(datelog, f"  Netmask: {address.netmask}", toprint=False))
                logger.stay(
                    to_info(datelog, f"  Broadcast IP: {address.broadcast}", toprint=False))
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                logger.next(
                    to_info(datelog, f"  MAC Address: {address.address}", toprint=False))
                logger.stay(
                    to_info(datelog, f"  Netmask: {address.netmask}", toprint=False))
                logger.stay(
                    to_info(datelog, f"  Broadcast MAC: {address.broadcast}", toprint=False))
            logger.prev('', by=1)
    logger.prev('')
    logger.stay(
        to_info(datelog, f"Total Bytes Sent: {get_size1(net_io.bytes_sent)}", toprint=False))
    logger.stay(
        to_info(datelog, f"Total Bytes Received: {get_size1(net_io.bytes_recv)}", toprint=False))
    logger.stay(to_info(datelog, pc.Win32_VideoController()[0], toprint=False))
    logger.stay(to_info(datelog, "User Current Version:-" +
                str(sys.version), toprint=False))
    logger.stay(printnlog(datelog, '\nDONE\n', toprint=False))
