from login import login
from create import createUser

domain=input('please enter your domain name(example.test): ')
username_domain=input('please enter your username of domain: ')
password_domain=input('please enter your password of domain: ')

f_users=input('please enter address file of usernames for emails: ')
f_passwords=input('please enter address file of passwords for emails: ')

try:
    f_u=open(f_users,'r').readlines()
    f_p=open(f_passwords,'r').readlines()
    
    print('Go to create file ... ')
    for i in range(len(f_u)):
        s=login(domain,username_domain,password_domain)
        createUser(s,domain,f_u[i],f_p[i])
        print('create : ',i+1)
except:
    print('Some things is wrong!')
