cd package

zip -r ../hello_world_deploy.zip .

cd ..

zip hello_world_deploy lambda_function.py

mv hello_world_deploy.zip ../../deploy

