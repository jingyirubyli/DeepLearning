# project name
PROJECT(KSWEntropy)
# requirement of cmake version
cmake_minimum_required(VERSION 3.5)

# set the directory of executable files
#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${KSWEntropy_SOURCE_DIR}/bin)

# find required opencv
set(OpenCV_DIR F:\\OpenCV\\opencv-3.2.0\\build-opencv-3.2.0)
find_package(OpenCV REQUIRED)

# directory of opencv headers
include_directories(${OpenCV_INCLUDE_DIRS})
# name of executable file and path of source file
add_executable(KSWEntropy main.cpp )
# directory of opencv library
link_directories(${OpenCV_LIBRARY_DIRS})
# opencv libraries
target_link_libraries(KSWEntropy ${OpenCV_LIBS})
