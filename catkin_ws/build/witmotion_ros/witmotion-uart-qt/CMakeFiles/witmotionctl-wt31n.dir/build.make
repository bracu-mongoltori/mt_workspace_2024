# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mtbase/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mtbase/catkin_ws/build

# Include any dependencies generated for this target.
include witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/depend.make

# Include the progress variables for this target.
include witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/progress.make

# Include the compile flags for this target's objects.
include witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/flags.make

witmotion_ros/witmotion-uart-qt/include/witmotion/moc_wt31n-uart.cpp: /home/mtbase/catkin_ws/src/witmotion_ros/witmotion-uart-qt/include/witmotion/wt31n-uart.h
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/mtbase/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating include/witmotion/moc_wt31n-uart.cpp"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt/include/witmotion && /usr/lib/qt5/bin/moc @/home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt/include/witmotion/moc_wt31n-uart.cpp_parameters

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.o: witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/flags.make
witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.o: witmotion_ros/witmotion-uart-qt/witmotionctl-wt31n_autogen/mocs_compilation.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mtbase/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.o"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.o -c /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt/witmotionctl-wt31n_autogen/mocs_compilation.cpp

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.i"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt/witmotionctl-wt31n_autogen/mocs_compilation.cpp > CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.i

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.s"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt/witmotionctl-wt31n_autogen/mocs_compilation.cpp -o CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.s

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.o: witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/flags.make
witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.o: witmotion_ros/witmotion-uart-qt/include/witmotion/moc_wt31n-uart.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mtbase/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.o"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.o -c /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt/include/witmotion/moc_wt31n-uart.cpp

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.i"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt/include/witmotion/moc_wt31n-uart.cpp > CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.i

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.s"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt/include/witmotion/moc_wt31n-uart.cpp -o CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.s

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.o: witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/flags.make
witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.o: /home/mtbase/catkin_ws/src/witmotion_ros/witmotion-uart-qt/src/wt31n-control.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mtbase/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.o"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.o -c /home/mtbase/catkin_ws/src/witmotion_ros/witmotion-uart-qt/src/wt31n-control.cpp

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.i"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mtbase/catkin_ws/src/witmotion_ros/witmotion-uart-qt/src/wt31n-control.cpp > CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.i

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.s"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mtbase/catkin_ws/src/witmotion_ros/witmotion-uart-qt/src/wt31n-control.cpp -o CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.s

# Object files for target witmotionctl-wt31n
witmotionctl__wt31n_OBJECTS = \
"CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.o" \
"CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.o" \
"CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.o"

# External object files for target witmotionctl-wt31n
witmotionctl__wt31n_EXTERNAL_OBJECTS =

/home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n: witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/witmotionctl-wt31n_autogen/mocs_compilation.cpp.o
/home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n: witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/include/witmotion/moc_wt31n-uart.cpp.o
/home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n: witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/src/wt31n-control.cpp.o
/home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n: witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/build.make
/home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n: /home/mtbase/catkin_ws/devel/lib/libwitmotion-wt31n.so
/home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n: /home/mtbase/catkin_ws/devel/lib/libwitmotion-uart.so
/home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n: /usr/lib/x86_64-linux-gnu/libQt5SerialPort.so.5.12.8
/home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n: /usr/lib/x86_64-linux-gnu/libQt5Core.so.5.12.8
/home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n: witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mtbase/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX executable /home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n"
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/witmotionctl-wt31n.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/build: /home/mtbase/catkin_ws/devel/lib/witmotion_ros/witmotionctl-wt31n

.PHONY : witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/build

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/clean:
	cd /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt && $(CMAKE_COMMAND) -P CMakeFiles/witmotionctl-wt31n.dir/cmake_clean.cmake
.PHONY : witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/clean

witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/depend: witmotion_ros/witmotion-uart-qt/include/witmotion/moc_wt31n-uart.cpp
	cd /home/mtbase/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mtbase/catkin_ws/src /home/mtbase/catkin_ws/src/witmotion_ros/witmotion-uart-qt /home/mtbase/catkin_ws/build /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt /home/mtbase/catkin_ws/build/witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : witmotion_ros/witmotion-uart-qt/CMakeFiles/witmotionctl-wt31n.dir/depend

