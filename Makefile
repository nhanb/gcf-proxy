deploy:
	gcloud functions deploy nhansproxy\
		--runtime python37\
		--trigger-http\
		--region=asia-east2\
		--env-vars-file .env.yaml

undeploy:
	gcloud functions delete nhansproxy --region=asia-east2
