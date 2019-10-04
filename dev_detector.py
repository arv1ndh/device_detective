from device_detector import DeviceDetector

ua = 'Mozilla/5.0 (Linux; Android 4.3; C5502 Build/10.4.1.B.0.101) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36'

# Parse UA string and load data to dict of 'os', 'client', 'device' keys
device = DeviceDetector(ua).parse()

# Use helper methods to extract data by attribute

print(device.is_bot())      # >>> False

print(device.os_name())     # >>> Android
print(device.os_version())  # >>> 4.3
print(device.engine())      # >>> WebKit

print(device.device_brand_name())  # >>> Sony
print(device.device_brand())       # >>> SO
print(device.device_model())       # >>> Xperia ZR
print(device.device_type())        # >>> smartphone

# For much faster performance, skip Bot and Device Hardware Detection
# and extract get OS / App details only.
from device_detector import SoftwareDetector

ua = 'Mozilla/5.0 (Linux; Android 6.0; 4Good Light A103 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36'
device = SoftwareDetector(ua).parse()

print(device.client_name())        # >>> Chrome Mobile
print(device.client_short_name())  # >>> CM
print(device.client_type())        # >>> browser
print(device.client_version())     # >>> 58.0.3029.83

print(device.os_name())     # >>> Android
print(device.os_version())  # >>> 6.0
print(device.engine())      # >>> WebKit

print(device.device_brand_name())  # >>> ''
print(device.device_brand())       # >>> ''
print(device.device_model())       # >>> ''
print(device.device_type())        # >>> ''

# Many mobile browser UA strings contain the app info of the APP that's using the browser 
ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 EtsyInc/5.22 rv:52200.62.0'
device = DeviceDetector(ua).parse()

print(device.secondary_client_name())     # >>> EtsyInc
print(device.secondary_client_type())     # >>> generic
print(device.secondary_client_version())  # >>> 5.22