![FH AACHEN](https://www.testa-fid.de/upload/mediapool/Kunden/FH-Aachen.jpg)

<br />

# TB3_TurtleBot
Team Turbo

<br />

## Launch tb3_hardware via SSH on Turtlebot
<br />
Following Packages need to be installed and build on the Robot: 

```
apriltag_msgs
apriltag_ros
tb3_hardware
Launch on system 1. 

```
$ ros2 launch tb3_description tb3_description.launch.py use_sim_time:=false
```
```

Launching the Lidarsensor 

```
$ sudo chmod 0666 /dev/ttyUSB0
$ ros2 launch tb3_hardware rplidar.launch.py
```

Launching the Webcam
```
$ ros2 launch usb_cam demo_launch.py
```

Launch Apriltag Detections
```
$ ros2 launch apriltag_ros track.launch.py
```
Launching the Robot Interface
```
$ sudo chmod 0666 /dev/ttyACM0
$ TURTLEBOT3_MODEL=waffle ros2 launch tb3_hardware robot.launch.py 
```
<br />

## Launch on System
<br />

```
$ ros2 run tb3_teleop teleop
$ ros2 launch my_robot_slam localization.launch.py use_sim_time:=false
$ ros2 launch my_robot_navigation robot_nav.launch.py use_sim_time:=false
$ ros2 run my_robot_navigation auto_explorer
``` 

<br />

## Autonomous Drive in Gazebo 
<br />

```
$ ros2 launch tb3_gazebo tb3_arena.launch.py 
$ ros2 launch my_robot_slam localization.launch.py
$ ros2 launch my_robot_navigation robot_nav.launch.py
$ ros2 run my_robot_navigation auto_explorer 
```

## Zum erstellen der Map braucht man...
- odometire
- tf three
- slamtoolbox

## Hinweis: using simtime muss für Gazebo bei allen auf **ture** gesetzt werden

<br />
<br />

## Languages and Tools

<img align="left" alt="Visual Studio Code" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" style="padding-right:10px;" />
<img align="left" alt="Python" width="26px" src="https://www.inovex.de/wp-content/uploads/2021/04/training-python.png" style="padding-right:10px;" />
<img align="left" alt="C++" width="26px" src="https://www.vectorsoft.de/wp-content/uploads/2019/10/C_API.png" style="padding-right:10px;" />
<img align="left" alt="ROS" width="26px" src="https://picknik.ai/assets/images/blog_posts/ROS2/ros2.png" style="padding-right:10px;" />
<img align="left" alt="Gazebo" width="26px" src="https://upload.wikimedia.org/wikipedia/en/5/5e/Gazebo_logo_without_text.svg" style="padding-right:10px;" />
<img align="left" alt="GitLab" width="26px" src="https://iffmd.fz-juelich.de/uploads/upload_44b1fe64823271caf566fc904ad5e5f2.png" style="padding-right:10px;" />
<img align="left" alt="Git" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" style="padding-right:10px;" />
<img align="left" alt="GitHub" width="26px" src="https://user-images.githubusercontent.com/3369400/139448065-39a229ba-4b06-434b-bc67-616e2ed80c8f.png" style="padding-right:10px;" />
<img align="left" alt="Ubuntu" width="26px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Logo-ubuntu_cof-orange-hex.svg/1200px-Logo-ubuntu_cof-orange-hex.svg.png" style="padding-right:10px;


<br />
<br />


## Was ist noch zu machen?

- zum laufen Bringen des Roboters
- Kamera und Lidarsensor publishen und auf remote PC empfangen
- Feierabendbier trinken 