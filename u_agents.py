#first do pip install pip install user-agents

from user_agents import parse

# iPhone's user agent string
ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
user_agent = parse(ua_string)

# Accessing user agent's browser attributes
print(user_agent.browser)  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
print(user_agent.browser.family)  # returns 'Mobile Safari'
print(user_agent.browser.version)  # returns (5, 1)
print(user_agent.browser.version_string)   # returns '5.1'

# Accessing user agent's operating system properties
print(user_agent.os)  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
print(user_agent.os.family)  # returns 'iOS'
print(user_agent.os.version)  # returns (5, 1)
print(user_agent.os.version_string)  # returns '5.1'

# Accessing user agent's device properties
print(user_agent.device)  # returns Device(family=u'iPhone', brand=u'Apple', model=u'iPhone')
print(user_agent.device.family)  # returns 'iPhone'
print(user_agent.device.brand) # returns 'Apple'
print(user_agent.device.model) # returns 'iPhone'

# Viewing a pretty string version
print(str(user_agent)) # returns "iPhone / iOS 5.1 / Mobile Safari 5.1"

# Can also identify properties like is_mobile, is_tablet, is_pc, is_touch_capable, is_bot (a web crawler)

# Touch capable Windows 8 device
ua_string = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)'
user_agent = parse(ua_string)
print(user_agent.is_mobile) # returns False
print(user_agent.is_tablet) # returns False
print(user_agent.is_touch_capable) # returns True
print(user_agent.is_pc) # returns True
print(user_agent.is_bot) # returns False
print(str(user_agent)) # returns "PC / Windows 8 / IE 10"