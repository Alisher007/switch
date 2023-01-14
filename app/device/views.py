from django.shortcuts import render, get_object_or_404
from .models import Device
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def home(request):
    return render(request, 'home.html')

def deviceListView(request):
    devices = Device.objects.all()
    context = {
        'object_list': devices,
        }
    return render(request, 'device/device-list.html', context)

def deviceDetailView(request, id):
    device = get_object_or_404(Device, id = id)
    context = {
        'object': device,
        }
    return render(request, 'device/device-detail.html', context)

def deviceTestView(request):

    devices = Device.objects.all()
    for device in devices:
        device_ping = ping(device.name)
        device.status = device_ping

    Device.objects.bulk_update(devices, ['status'])
    # google.com
    # github.com
    # office.com
    # linkedin.com


    context = {
        'object': 'test',
        }
    return render(request, 'device/device-test.html', context)
