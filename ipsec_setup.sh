sudo yum update -y
sudo yum install git make wget gcc gmp-devel bison flex -y

git clone https://github.com/xelerance/Openswan.git
cd Openswan
sudo make programs
sudo make install

sudo service ipsec start
sudo service ipsec status
