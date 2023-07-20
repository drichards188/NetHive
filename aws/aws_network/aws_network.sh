cd package

zip -r ../aws_network_deploy.zip .

cd ..

zip aws_network_deploy.zip lambda_function.py

mv aws_network_deploy.zip ../../deploy

