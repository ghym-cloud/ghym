# Run as ./CreateVM.py VMNAME USERNAME USERPASSWORD
import os, sys, shutil, crypt
# Name of Virtual Machine and Username from CLI arguments
vmname = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
# Folder of Virtual Machine
directory = "/home/hdd/"
file_tmp = "/tmp/" + vmname
file_ssh_key = "/home/max/.ssh/" + vmname
file_meta_data = file_tmp + "/Template/meta-data"
file_user_data = file_tmp + "/Template/user-data"
hdd = directory + vmname + ".qcow2"
image = "/home/template/ae-dc1-cp1.qcow2"
# Create "mata-data" file with content
meta_data = open(file_meta_data, "r")
meta_data_content = meta_data.read()
meta_data_content = meta_data_content.replace("VMNAME", vmname)
meta_data.close()
meta_data = open(file_meta_data, "w")
meta_data.write(meta_data_content)
meta_data.close()
# Create SSH key
os.system("ssh-keygen -t rsa -f " + file_ssh_key + " -N ''")
# Create hash of password
pwd = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512, rounds=4096))
# Get SSH key data
ssh_key = open(file_ssh_key + ".pub", "r")
ssh_key_content = ssh_key.read()
ssh_key.close()
# Get file user-data cantent
user_data = open(file_user_data, "r")
user_data_content = user_data.read()
# Replace VMNAME, USERNAME and SSHKEY
user_data_content = user_data_content.replace("USERNAME", username)
user_data_content = user_data_content.replace("VMNAME", vmname)
user_data_content = user_data_content.replace("SSHKEY", ssh_key_content)
user_data_content = user_data_content.replace("USERPASSWORD", pwd)
# Reopen file to write changes
user_data.close()
user_data = open(file_user_data, "w")
# Rewrite with actual VMNAME, USERNAME and SSHKEY
user_data.write(user_data_content)
# Safe file
user_data.close()
# Copy HDD image
shutil.copyfile(image, hdd)
#qemu-img create -f qcow2 -o preallocation=metadata $VM.new.image 60G
#virt-resize --quiet --expand /dev/sda1 $VM.qcow2 $VM.new.image
os.system("mkisofs -o " + file_tmp + "/Template/" + vmname + ".iso -V cidata -J -r " +file_user_data + " " + file_meta_data)
# Create a storage pool for Virtual Machine
#os.system("virsh pool-create-as --name " + hdd + " --type dir --target " + directory)
# Deploy Virtual Machine
os.system("virt-install --import --name " + vmname + " --memory 2048 --vcpu 2 --cpu host --disk " + hdd +",format=qcow2,bus=virtio --disk " + file_tmp + "/Template/" + vmname + ".iso,device=cdrom --network bridge=br0,model=virtio --os-type=linux --graphics=vnc")
# Eject CD-Rom
os.system("virsh change-media " + vmname + " hda --eject --config")
# Delete temporary files
shutil.rmtree(file_tmp)
