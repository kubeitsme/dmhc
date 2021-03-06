# how to run?
```
gunicorn app:api
```
# query params
### paging
default: _pager_start = 0  
default: _pager_num = 50  
_pager_start: bước nhảy của _pager_num  
ex: 0 -> 50 -> 100 -> 150 ->...  
_pager_number: số phần tử mỗi trang  
```
?_pager_start=75&_pager_num=25
```
### sort
default: _sort_key = id  
default: _sort_dir = desc  
_sort_key: column name  
_sort_dir: asc or desc  
```
?_sort_key=id&_sort_dir=desc
```

# WIP
- GETHandler districts with province_id
```
/quan-huyen/ma-so/2?ma_so_tinh_thanh=2
```
- GETHandler wards with district_id
```
/phuong-xa/ma-so/2?ma_so_quan_huyen=2
```
- GETHandler with all child level (province, district)
```
/tinh-thanh/ma-so/2?phan_cap=true
/quan-huyen/ma-so/2?phan_cap=true
```

# Next update?
- Authentication with token
- CreateHandler
- UpdateHandler
- DeleteHandler


```
sudo apt-get update
sudo apt-get -y install nginx git-core libmysqlclient-dev mysql-server python3-pip
sudo mysql -u root -p dhmc < dhmc_2018-05-01.sql  # import DB
sudo mysql_secure_installation # setting password for mysql-server
sudo apt-get update
sudo apt-get -y upgrade
python3 -V # check python version
python3 -m virtualenv venv # install virtualenv
source venv/bin/activate
pip install falcon gunicorn mysqlclient
```

```
connect mysql without sudo
$ sudo mysql -u root -p
[mysql] use mysql;
[mysql] update user set plugin='' where User='root';
[mysql] flush privileges;
[mysql] \q 
```

```
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04
```

```
config nginx
sudo nano /etc/nginx/conf.d/virtual.conf

server {
    listen       80;
    server_name  lamgidayta.com www.lamgidayta.com;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

sudo nginx -t && sudo service nginx restart

gunicorn app:api

```
adding subdomain
following step
https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04
and create dns
=> google console

```

```
pkill gunicorn

gunicorn app:api
```
