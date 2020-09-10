import requests, math
from tqdm import tqdm

# message 슬랙전송
from slacker import Slacker
token = 'xoxp-222764622535-221133094001-222766712423-d34410402edc94c2b8664a93d631c92c'
slack = Slacker(token)

def pywget(url):

    # 파라미터들을 추출한다
    filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    total_size, block_size = int(r.headers.get('content-length', 0)), 4096

    # 크기정보 출력
    if int(total_size) > 10 ** 6:
        size_info = "{:,} mb".format(int(int(total_size) / 10 ** 6))
    elif int(total_size) > 10 ** 3:
        size_info = "{:,} kb".format(int(int(total_size) / 10 ** 3))
    else:
        size_info = "{:,} byte".format(int(total_size))

    start_msg = "{:6} Start : {} ".format(size_info, filename)
    slack.chat.post_message('#general', start_msg)

    # Download 작업을 시작한다
    try:
        with open(filename, 'wb') as f:
            for data in tqdm(r.iter_content(block_size),
                             total=math.ceil(total_size // block_size),
                             unit='KB', unit_scale=True):
                f.write(data)
    except:
        broken_msg = "{} Broken".format(filename)
        slack.chat.post_message('#general', broken_msg)

    complete_msg = "{} Complete".format(filename)
    slack.chat.post_message('#general', complete_msg)
    return None


links = {"Khongloi-Kernel-Note8-Note5.zip(112Mb)" : "https://qc1.androidfilehost.com/dl/7u9tj_VtgLidEEZnALq5uQ/1544893252/817906626617935034/Khongloi-Kernel-Note8-Note5.zip",
 "V11-Update_1.zip(225Mb)" : "https://qc1.androidfilehost.com/dl/PJgiGQRwNS7mb8PVDtIi4w/1544893819/817550096634775809/V11-Update_1.zip",
 "Khongloi-Kernel-Nougat-Note5-V11.zip(108Mb)" :"https://qc1.androidfilehost.com/dl/pTTarA_oqKFKrV9R_JAPyw/1544893874/817550096634774347/Khongloi-Kernel-Nougat-Note5-V11.zip",
 "KHONGLOI_CSC_OMC_Note5_V11.zip(1.5Gb)":"https://qc1.androidfilehost.com/dl/pxZ4Sz-XJtxW3JikwqDLwQ/1544893945/817550096634774820/KHONGLOI_CSC_OMC_Note5_V11.zip",
 "KHONGLOI-NOUGAT-V11-Note5.zip(2Gb)":"https://ca1.androidfilehost.com/dl/CTmneLYGhdiAumtQJyNGQA/1544894009/673368273298960434/KHONGLOI-NOUGAT-V11-Note5.zip"
}

linklist = list(links.values())

if __name__ == "__main__" :
    for file_url in linklist:
        pywget(file_url)
    slack.chat.post_message('#general', "Process is Done")