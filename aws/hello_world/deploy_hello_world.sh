cd package
zip -r ../my_deployment_package.zip .

cd ..
zip my_deployment_package.zip lambda_function.py

mv my_deployment_package.zip ../../deploy

