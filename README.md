```sh
# deploy
gcloud functions deploy nhansproxy\
         --runtime python37\
         --trigger-http\
         --region=asia-east2

# delete
gcloud functions delete nhansproxy --region=asia-east2
```
