# DevOps_CaseStudy_02

sudo yum update -y

sudo yum install python -y

# In this case study: We will write a Shell script which runs a Python phone book application



#!/bin/bash
echo -e "###########\t WELCOME TO GROUPPROFFESOR CASE STUDY_2\t ############"
user=$(whoami | tr a-z A-Z)
echo "HI $user, to start, lets install git, openssl11"
sudo yum install -y git openssl11 1>/tmp/process.txt
echo "Wait a moment for system preparation"
sleep 3
read -p "$user , Please enter your password:" password  #mkpasswd --method=SHA-512 --stdin

function passwordChecker { #compare typed password with hashed one in the system for validation

    userHashedPassword=$(sudo cat /etc/shadow | grep -i $user | cut -d":" -f2)
    hashType=$(echo $userHashedPassword | cut -d"$" -f2) #Get the hash function type
    salt=$(sudo cat /etc/shadow | grep -i $user | cut -d"$" -f3) #Get the salt for hash function
    hashed_password=$(openssl11 passwd -$hashType -salt $salt  $password) || $(openssl passwd -$hashType -salt $salt  $password) #hash user password (AMAZON uses openssl11)
    
    if [ "$hashed_password" == "$userHashedPassword" ] # check if the user password is correct
    then
        return 0
    else
        return 1
    fi
}

if passwordChecker # call passwordChecker function
then
    printf " "
    echo -e "#######################\t Welcome $user\t #########################" # If the user knows the root password, then echo a welcome message with the name of the user
    printf " "

    if [ -e AccessLog.txt ] # Then check if AccessLog.txt file exists in the current directory
    then
    count=$(grep -ic $user AccessLog.txt)
    echo -e "###############\t Access Log Details\t #########################"
    echo -e "$user\t $(date)\t $((++count))" >> AccessLog.txt  # If the file exists, then append the name of the user, the date and the number of the record starting by 1 to the file
    cat AccessLog.txt # print out AccessLog file
    else 
    echo -e "###############\t Access Log Details\t #########################"
    touch AccessLog.txt; echo -e "$user\t $(date)\t 1"  >> AccessLog.txt # If the file doesn't exist, create it in the current directory
    cat AccessLog.txt # print out AccessLog file
    fi
    
    if [[ $(apt list --installed 2>/dev/null | grep python3) || $(yum list installed | grep python3) ]];#     Later on, check if you have installed Python
    then
        echo -e ">>>>>>>>\t Python3 installed already\t <<<<<<<<<<<"
        printf ""

        if [[ $(find ./ -name "phone_book.py" | wc -l) -gt 0 ]]; # if file exists line number should 1, so TRUE
        then
        cd GProf/case_study #change directory to default for phone_book.py
        python3 phone_book.py # If the script finds the application, it should run it
        else
        git clone https://github.com/daveMillerAWS/GProf.git 2>/dev/null # it should clone it from your git repository which already has your application in it and run the application
        
        find ./ -name "phone_book.py" -exec python3 {} \;
         
        fi      
         
    else #     If Python is not installed, install it within your script
         echo -e "!!!!  Python3 has not installed yet"
         sudo apt install python3.8 2>/dev/null || sudo yum install -y python3 1>/tmp/process.txt
        
        if [[ $(find ./ -name "phone_book.py" | wc -l) -gt 0 ]]; # if file exists line number should 1, so TRUE
        then
        
        python3 phone_book.py # If the script finds the application, it should run it
        else
        git clone https://github.com/daveMillerAWS/GProf.git 2>/dev/null # it should clone it from your git repository which already has your application in it and run the application
        
        find ./ -name "phone_book.py" -exec python3 {} \;
         
        fi      
    
    fi

else
    echo '!!! WRONG PASSWORD  !!!'
    echo "Goodbye $user" 
fi