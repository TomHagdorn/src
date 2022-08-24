import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

# detect only 16h5 tags with id=0 from compressed image stream (ensure image transport plugins and image common exist/ build from source)
cfg_16h5 = {
    #required params
    "image_transport": "raw",
    "family": "16h5",
    "size": 0.162,
    "z_up": True,

    #optional detection tuning params
    "max_hamming": 0,
    "decimate": 1.0,
    "blur": 0.9,
    #"refine-edges": 1,
    #"threads": 1,
    #"debug": 0,

    #optional customization of tag list/display
     "tag_ids": [0,1,2,3,4,5,6,7,8,9,10],
     "tag_frames": ["marker0","marker1","marker2","marker3","marker4","marker5","marker6","marker7","marker8","marker9","marker10"],
    
}

def generate_launch_description():
    composable_node = ComposableNode(
        name='apriltag',
        package='apriltag_ros', plugin='AprilTagNode',
        remappings=[("/apriltag/image", "/image_raw"), ("/apriltag/camera_info", "/camera_info")],
        parameters=[cfg_16h5])
    container = ComposableNodeContainer(
        name='tag_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[composable_node],
        output='screen'
    )

    return launch.LaunchDescription([container])