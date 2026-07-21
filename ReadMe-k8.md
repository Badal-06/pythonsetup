#k8 deployment
kind create cluster --config kind-config.yml
kind get clusters

-- Load Image in kind
kind load docker-image user-service:1.0

kubectl apply -f deployment.yml
kubectl get pods

kubectl apply -f service.yml
kubectl get svc

kubectl port-forward service/user-service 8000:8000

http://localhost:8000/docs

#-- --------------------------------------
kubectl delete -f deployment.yml 
kubectl delete -f service.yml 
kubectl describe pod user-service-996755b5-tcmxs

-- test pod deployment
curl http://localhost:8000/health

#----------------------------------------------------replicA SET

kubectl scale deployment user-service --replicas=2
kubectl get replicasets
kubectl get rs
kubectl describe rs user-service-996755b5



#configmap----------------
kubectl apply -f configmap.yml
kubectl get configmap
kubectl describe configmap user-service-config
kubectl get configmap user-service-config -o yaml


#  secret------------
echo -n "admin" | base64



#k8 verify
kubectl get pods
kubectl get deployments
kubectl get svc
kubectl get svc user-service



