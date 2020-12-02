import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None                      # disable host key checking

host = "ftp2.markedskraft.com"       #hard-coded
password = "XXXX"               #hard-coded
username = "mathias.skreden"                #hard-coded

with pysftp.Connection(host, username=username, password=password, cnopts=cnopts) as sftp:
    files = sftp.listdir_attr(".")
    for f in files:
        print(f)
    sftp.get_d('.', localdir='./data/')