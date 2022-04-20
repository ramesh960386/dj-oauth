import json
import redis

rds = redis.StrictRedis(port=6379, db=0)


class OTPData:

    def set_otp(self, email, otp):
        if email and otp:
            rds.set(email, otp)
        return True
    
    def get_otp(self, email):
        otp_info = rds.get(email)
        if otp_info:
            return otp_info
        return False


class Red:

    def set(cache_key, data):
        data = json.dumps(data)
        rds.set(cache_key, data)
        return True

    def get(cahe_key):
        cahe_data = rds.get(cahe_key)
        if not cahe_data:
            return False
        # cahe_data = cahe_data.decode("utf-8")
        # cahe_data = json.loads(cahe_data)
        return cahe_data

def responsedata(status, message, code, data={}):
    return {"success": status, "data": data, "code": code, "message": message}