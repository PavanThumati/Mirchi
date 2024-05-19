# Mirchi
The system aims to develop an automated red chili sorting system using advanced
 computer vision technology and an IoT setup. This system will revolutionize the sorting
 process by accurately identifying and segregating red chilies based on their color and quality,
 ensuring only high-quality chilies proceed for further processing. The system will leverage
 the YOLO (You Only Look Once) object detection algorithm for chili classification and
 integrate it with an IoT-controlled conveyor belt mechanism.
The system consists of several key components. First, a computer vision module
 utilizes the YOLO object detection algorithm to analyze images captured by a camera
 positioned above the conveyor belt. The YOLO model is trained to detect and classify red
 chilies based on their color and quality. Second, an IoT setup controls the conveyor belt
 mechanism based on the output of the computer vision module.
The IoT system communicates with the conveyor belt motors to regulate the movement of chilies
 along the conveyor belt. Third, the IoT system that needs to be integrated with the previous work.
 Finally, upon classification, chilies are sorted into different bins based on their quality (good
 or bad). This sorting mechanism ensures that only high-quality chilies proceed for further
 processing, while low-quality chilies are discarded.
The system presents several challenges that need to be addressed during
 implementation. Firstly, training the YOLO model to accurately detect and classify red
 chilies based on color and quality requires a diverse dataset and rigorous algorithm tuning.
 Secondly, integrating the computer vision module with the IoT setup seamlessly poses
 challenges in data communication and synchronization between different components in real
 time. Lastly, ensuring the reliability and stability of the conveyor belt mechanism and
 integrating it with an IoT system constructed from Arduino, motors, and cardboard requires
 meticulous design and testing to prevent mechanical failures.
