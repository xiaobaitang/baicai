
import hashlib
import base64
import os
import sys
from aes import AEScoder
import uuid
if __name__ == "__main__":
    env_dist = os.environ #
    if 'ENCKEY' in env_dist:
        key = env_dist['ENCKEY']
    else:
        key = str(uuid.uuid4());
        key=key.replace("-","",100);
    # key =  env_dist["cookiekey"]
    print("您的config 加密密码(请添加到环境变量 ENCKEY):\n")
    print(key);

    t = AEScoder(key);
    p = open("/".join([sys.path[0], "config_of_mine.json"])).read();
    e = t.encrypt(p);
    text_file = open("config_of_mine.json.enc", "w")
    text_file.write(e);
    text_file.close()
    p2 = t.decrypt(e);
    print ("",p2 == p );
    