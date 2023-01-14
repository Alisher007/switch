from celery import shared_task
from .models import Device
import os


def ping(host):
    response = os.system("ping -c 1 " + host)

    return response == 0

@shared_task
def sample_task2():
    devices = Device.objects.all()
    if devices:
        for device in devices:
            device_ping = ping(device.name)
            device.status = device_ping

        Device.objects.bulk_update(devices, ['status'])

