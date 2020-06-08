import os
import requests
import hashlib
import uuid

def download_files(urls):
    #use a set to have unique hashes
    unique_hashes = set()
  
    #download files
    for url in urls:
        r = requests.get(url, allow_redirects=True)
            ##calculate hash
        h = hashlib.sha256(r.content).hexdigest()

        ##check if not already exists
        if h not in unique_hashes:
            #put the hash and save file
            unique_hashes.add(h)
            file = str(uuid.uuid4())
            open(file, 'wb').write(r.content)

def child():
    ##this is the child process
    urls = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]
    ##download all
    download_files(urls)


##fork a process
child_pid = os.fork()

#if child_pid id 0 this is the child
if child_pid == 0:
    child()
else:
    #this is the parent
    print(f"Child pid is {child_pid}")
    #wait for the child using os.wait
    os.wait()
    #child exited
    print("Child exited")