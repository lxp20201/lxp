#!/bin/sh
LDFLAGS="-L/home/css/edx-edutech/common/lib $LDFLAGS"
export LDFLAGS
CFLAGS="-I/home/css/edx-edutech/common/include/ImageMagick -I/home/css/edx-edutech/common/include $CFLAGS"
export CFLAGS
CXXFLAGS="-I/home/css/edx-edutech/common/include $CXXFLAGS"
export CXXFLAGS
		    
PKG_CONFIG_PATH="/home/css/edx-edutech/common/lib64/pkgconfig:/home/css/edx-edutech/common/lib/pkgconfig"
export PKG_CONFIG_PATH
