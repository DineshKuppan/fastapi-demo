## FastAPI-REDIS-APP

### Fastapi quick deploy to ArgoCD Gitops tools

```
docker build -t kuppandinesh/fastapi-redis-app .
docker push kuppandinesh/fastapi-redis-app
```

#### Redis Deployment

```
kubectl apply -f https://raw.githubusercontent.com/bitnami/charts/master/bitnami/redis/redis-deployment.yaml
```

#### Kubernetes Deployment and Service file

```
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml
```