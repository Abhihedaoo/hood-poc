# Create namespaces
kubectl create ns nginx
kubectl create ns common

kubectl create serviceaccount common --namespace common



helm3 install nginx stable/nginx-ingress --namespace nginx --set rbac.create=true --set controller.publishService.enabled=true


helm3 repo add bitnami https://charts.bitnami.com/bitnami

helm3 install postgres bitnami/postgresql --namespace common --set global.postgresql.postgresqlDatabase=kubernetes --set global.postgresql.postgresqlUsername=postgres --set global.postgresql.postgresqlPassword=postgres




###########
NAME: postgres
LAST DEPLOYED: Mon Apr 20 09:34:25 2020
NAMESPACE: common
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
** Please be patient while the chart is being deployed **
PostgreSQL can be accessed via port 5432 on the following DNS name from within your cluster:
    postgres-postgresql.common.svc.cluster.local - Read/Write connection
To get the password for "postgres" run:
    export POSTGRES_PASSWORD=$(kubectl get secret --namespace common postgres-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode)
To connect to your database run the following command:
    kubectl run postgres-postgresql-client --rm --tty -i --restart='Never' --namespace common --image docker.io/bitnami/postgresql:11.7.0-debian-10-r73 --env="PGPASSWORD=$POSTGRES_PASSWORD" --comm
and -- psql --host postgres-postgresql -U postgres -d postgres -p 5432
To connect to your database from outside the cluster execute the following commands:
    kubectl port-forward --namespace common svc/postgres-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432


