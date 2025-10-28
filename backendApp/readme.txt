cd C:\Users\nitro\OneDrive\Desktop\API
$env:FLASK_APP = "backendApp.app:create_app"
flask db init
flask db migrate -m "init"
flask db upgrade
flask run

Use these to finally get the app running via CMD

Once its running, either use POSTMAN or cmc

curl http://127.0.0.1:5000/api/notes/
curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"Test Note\",\"content\":\"This is a test\"}" http://127.0.0.1:5000/api/notes/
curl -X DELETE http://127.0.0.1:5000/api/notes/1
