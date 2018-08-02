# Blockchain

```sh
python3 run.py 5000
# * Running on http://127.0.0.1:5000/

curl -X GET http://localhost:5001/mine

curl -X GET http://localhost:5001/chain

curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "your-adress",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"
```

