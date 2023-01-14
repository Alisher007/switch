from django.test import TestCase

# {{ post.get_absolute_url }}
# @shared_task(name='test55')
# def hello():
#     devices = Device.objects.all()
#     for device in devices:
#         device_ping = ping(device.name)
#         device.status = device_ping

#     Device.objects.bulk_update(devices, ['status'])




# def ping(host):
#     """
#     Returns True if host (str) responds to a ping request.
#     Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
#     """

#     # Option for the number of packets as a function of
#     param = '-n' if platform.system().lower()=='windows' else '-c'

#     # Building the command. Ex: "ping -c 1 google.com"
#     command = ['ping', param, '1', host]

#     return subprocess.call(command) == 0



