## Croomba-ROS-HectorSLAM Setup

# What does the software do? 

To set up the Croomba, use ROS, and use Hector SLAM for mapping of an environment, multiple command terminals are used, also known as shell programming. Below, all steps for setting up the Croomba to work with ROS, Combined_Code.py, and the Wireless Access Point are discussed. To minimize error, follow the command terminal scripts below in chronological order. 

# Dependencies 

The following shell scripts require a Windows master remote machine with Windows Remote Desktop. The Raspberry Pi 4B requires the installation of Ubuntu 20.04 (Server), Light Ubuntu Desktop GUI, XRDP, python3.7, ROS Noetic, ROS Navigation Stack, ROS Hector SLAM, ROS RPlidar, and RVIZ. 

# How to Install? 

To install the previously mentioned dependencies, enter the shown commands into the Ubuntu terminal on the Raspberry Pi 4B. This is a long installation process, however, all of the following information is important for the code to execute. Note, the current version of the Croomba has everything installed so the installation step can be skipped of using the current version of the Croomba.  

Setting Up Wifi (TTU Wifi EagleNet As Example): 

sudo apt update 

sudo apt upgrade 

sudo apt install python3.7 

python –version 

sudo apt-get -y install python3-pip 

cd /etc/netplan/50-cloud-init.yaml 

Remove the # in front of EagleNet and password, place a # in front of Capstone_Robot_Team1 and password.  

Control, shift, x  

Y 

sudo netplan –debug generate 

sudo netplan –debug apply 

ifconfig 

Check that ip4 address is in the format of “10.0……”, if so continue, if not trouble shoot wifi network name and password to make sure that you are connected to EagleNet (Internet) 

Installing XRDP for Windows Desktop Remote:

sudo apt install xrdp 

sudo adduser ubuntu 

sudo ufw allow from “IP Address of Master Windows Machine” 

Installing ROS Noetic, ROS Navigation Stack, ROS RPlidar, RVIZ, and ROS Hector SLAM 

sudo sh -c ‘echo “deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main” 

sudo apt install ros-noetic-desktop 

sudo apt-get install ros-noetic-navigation 

sudo apt-get install build-essential 

echo “source /opt/ros/noetic/setup.bash” >> ~/.bashrc 

source ~/.bashrc 

mkdir -p ~/catkin_ws/src 

cd ~/catkin_ws/ 

catkin_init_workspace 

echo “source $HOME/catkin_ws/devel/setup.bash” >> ~/.bashrc 

cd src 

sudo git clone https://github.com/Slamtec/rplidar_ros.git 

sudo git clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git 

cd ~/catkin_ws/ 

catkin_make 

# How to Run? 

To run these scripts for an actual test, follow the below shell programming command terminal scripts in chronological order. Again, since ROS is very dependent on shell programming, multiple terminals are needed and will be specified when needed below.  

Setting Up Wireless Access Point (Connect Back To WAP): 

cd /etc/netplan/50-cloud-init.yaml 

Remove the # in front of Capstone_Robot_Team1 and password, place a # in front of EagleNet and password. 

Control, shift, x  

Y 

sudo netplan –debug generate 

sudo netplan –debug apply 

ifconfig 

Check that ip4 address is in the format of “192.168.0.100 or 192.168.0.101 or etc…” if so continue, if not trouble shoot wifi network name and password to make sure that you are connected to the wireless access point (WAP). 

Ifconfig 

Record IP address shown here, this will be the IP address that is used to connect to the Croomba wirelessly. Connect Windows master machine to WAP, ipconfig in terminal, record IP address of Windows machine.  

sudo ufw allow from “IP Address of Master Windows Machine” 

Connect to the Raspberry Pi 4B through Windows Remote Desktop by entering Raspberry Pi 4B address. User will then be prompted to enter the username and password of the Raspberry Pi 4B and user will then be able to remotely control the Croomba. 

On the Raspberry Pi 4B through the Windows Remote Desktop:

Ifconfig 

Record the current IP Address of the Croomba 

sudo nano ~/.bashrc 

Add the following lines to the bashrc file: 

ROS_MASTER_URI=http://”IP of Raspberry Pi 4B”:11311 

ROS_HOSTNAME=”IP of Raspberry Pi 4B” 

Save and exit the bashrc file then enter the following commands: 

source ~/.bashrc 

roscore 

Now, open a new command terminal for the following commands: 

cd catkin_ws 

source devel/setup.bash 

roslaunch rplidar_ros rplidar.launch 

Now, open a new command terminal for the following commands: 

cd catkin_ws 

source devel/setup.bash 

roslaunch hector_slam_launch tutorial.launch 

The RVIZ window should now be open. Click “add” in the bottom left, click “by topic”, select “Laser Scan”, and finally click add.  

Now, open a new command terminal for the following commands (will be utilizing the Combined_Code.py script, follow setup for that code): 

python filepath/Combined_Code.py 

Once robot has stopped moving, open another command terminal and enter: 

cd catkin_ws 

source devel/setup.bash 

rosrun map_server map_saver -f “file name” 
