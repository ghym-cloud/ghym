kubeadm join 172.16.0.8:6443 --v=9 --token mx9e4a.i7494th4272ymnrl --discovery-token-ca-cert-hash sha256:d77cb3d8f786b0cb8d9c51577b564a03e4e055d9d9d9ad19638e338aa01540af

kubeadm join 172.16.0.8:6443 --v=9 --token 4xbqtr.6qvh4oszwh9tez71 --discovery-token-ca-cert-hash sha256:d77cb3d8f786b0cb8d9c51577b564a03e4e055d9d9d9ad19638e338aa01540af

kubectl label nodes ae-dc1-cp1 dclocation=ae1
kubectl label nodes ae-dc1-cp1 nodetype=cp
kubectl label nodes ae-dc1-cp1 host=ae-dc1-2

convert creatind nodes from cmd to file
