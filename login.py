#creat a login in bash
#!/bin/bash

read -p "Enter your username: " username
read -p "Enter your password: " password

if [ $username == "admin" && $password == "123456" ]; then
    echo "Login successful"
else
    echo "Login failed"
fi