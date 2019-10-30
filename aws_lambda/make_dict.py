from datetime import datetime

def make_dict(parsed_ua, user):
    ua_dict = {}
    ua_dict['ua_string'] = parsed_ua.ua_string
    brows_dict = {}
    brows_dict['family'] = parsed_ua.browser.family
    brows_dict['version'] = parsed_ua.browser.version
    brows_dict['version_string'] = parsed_ua.browser.version_string
    ua_dict['browser'] = brows_dict
    os_dict = {}
    os_dict['family'] = parsed_ua.os.family
    os_dict['version'] = parsed_ua.os.version
    os_dict['version_string'] = parsed_ua.os.version_string
    ua_dict['os'] = os_dict
    device_dict = {}
    device_dict['family'] = parsed_ua.device.family
    device_dict['brand'] = parsed_ua.device.brand
    device_dict['model'] = parsed_ua.device.model
    ua_dict['device'] = device_dict
    ua_dict['is_mobile'] = parsed_ua.is_mobile
    ua_dict['is_tablet'] = parsed_ua.is_tablet
    ua_dict['is_touch_capable'] = parsed_ua.is_touch_capable
    ua_dict['is_pc'] = parsed_ua.is_pc
    ua_dict['is_bot'] = parsed_ua.is_bot
    ua_dict['time'] = str(datetime.now())
    ua_dict['user'] = user
    return ua_dict
