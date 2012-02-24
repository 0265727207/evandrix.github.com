###
# This assumes you have Xcode on a Mac. (It is not
# possible to compile for iPad without a Mac.)
##
/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/gcc  -arch armv7 -Wall -O3 -DIPAD -isysroot   /Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS5.0.sdk  -o ipadhashfunctionreal hashfunctionsreal.c

/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/gcc  -arch armv7 -Wall -O3  -isysroot   /Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS5.0.sdk  -o ipadhashfunction32 hashfunctions32.c

/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/gcc  -arch armv7 -Wall -funroll-loops -O3 -DIPAD -isysroot   /Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS5.0.sdk  -o ipadhashfunctionrealunroll hashfunctionsreal.c

/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/gcc  -arch armv7 -Wall -funroll-loops -O3  -isysroot   /Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS5.0.sdk  -o ipadhashfunction32unroll hashfunctions32.c

# 
# You then have to copy the executable on the iPad. This can 
# be achieved by jailbreaking the iPad and installing an ssh
# server on it. The default password on a rooted iPad is often
# "alpine".
