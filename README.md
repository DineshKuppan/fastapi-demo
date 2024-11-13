


docker build -t kuppandinesh/fastapi-redis-app .
docker push kuppandinesh/fastapi-redis-app


kubectl apply -f https://raw.githubusercontent.com/bitnami/charts/master/bitnami/redis/redis-deployment.yaml


kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml