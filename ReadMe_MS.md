#Python microservices

user-service/
├── app.py
├── requirements.txt
└── Dockerfile

#step1
docker build --no-cache -t user-service:1.0 .

#step2
docker run -d -p 8000:8000 --name user-service user-service:1.0
           



#step3
Health check: http://localhost:8000/health/
Root endpoint (if defined): http://localhost:8000/
Swagger UI: http://localhost:8000/docs
OpenAPI JSON: http://localhost:8000/openapi.json

# check JWT token

TOKEN=$(curl -s -X POST http://127.0.0.1:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}' | python3 -c "import sys,json;print(json.load(sys.stdin)['access_token'])")

curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:8000/usersJwt
