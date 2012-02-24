### 
#
# Download the Android NDK, install it at a place like ~/android-ndk-r6
#
# *) use the corresponding script to generate a 
#    custom toolchain
#     ~/android-ndk-r6/build/tools/make-standalone-toolchain.sh  --platform=android-9
#
# *) This generate a tar ball at 
#   /tmp/ndk-lemire/arm-linux-androideabi-4.4.3.tar.bz2
#  copy it at ~/myandroid
#      cp /tmp/ndk-lemire/arm-linux-androideabi-4.4.3.tar.bz2 ~/myandroid/
# and open it
#  tar xjvf arm-linux-androideabi-4.4.3.tar.bz2 
#  cd ~/myandroid/
#
####

ANDROIDNDK=/Users/lwy08/Documents/AndroidSDK/android-ndk-r6
PATH=/Users/lwy08/Documents/AndroidSDK/arm-linux-androideabi-4.4.3/bin/:$PATH

# defaults to armv7 according to arm-linux-androideabi-gcc -dumpspecs.
# this matches the instruction set on the machine
arm-linux-androideabi-gcc  -Wall  -O3  -o androidhashfunctionsreal -DLITTLEMEMORY hashfunctionsreal.c

arm-linux-androideabi-gcc  -Wall  -O3  -o androidhashfunctions32 hashfunctions32.c

arm-linux-androideabi-gcc  -Wall -funroll-loops -O3  -o androidhashfunctionsrealunroll -DLITTLEMEMORY hashfunctionsreal.c

arm-linux-androideabi-gcc  -Wall -funroll-loops -O3  -o androidhashfunctions32unroll  hashfunctions32.c

#
#
# you can then copy it to an android machine. SSH would do. But
# maybe it is simpler to get the Android SDK. Run the "android" program
# and get it to install platform-tools, this will download several programs
# including a small executable called adb. You can  upload software
# to an android device connected to the USB port with adb push,
# and you can run stuff with adb shell. Notice that for this to
# work, you might have to enable USB debugging in Settings > Applications.
#
# SSH might be more convenient, but you need to root the device first,
# then install something like SSHDroid.
