# Blockchain

```sh
python3 run.py 5000
python3 run.py 5001

curl -X GET http://localhost:5000/mine
curl -X GET http://localhost:5001/mine

curl -X GET http://localhost:5000/chain
curl -X GET http://localhost:5001/chain

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "your-adress",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"
curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "your-adress",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5001/transactions/new"

curl -X POST -H "Content-Type: application/json" -d '{
 "nodes": ["http://127.0.0.1:5001"]
}' "http://localhost:5000/nodes/register"
curl -X POST -H "Content-Type: application/json" -d '{
 "nodes": ["http://127.0.0.1:5000"]
}' "http://localhost:5001/nodes/register"

curl -X GET http://localhost:5000/nodes/resolve
curl -X GET http://localhost:5001/nodes/resolve
```

