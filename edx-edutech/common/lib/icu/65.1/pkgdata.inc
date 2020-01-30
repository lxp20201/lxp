GENCCODE_ASSEMBLY_TYPE=-a gcc
SO=so
SOBJ=so
A=a
LIBPREFIX=lib
LIB_EXT_ORDER=.65.1
COMPILE=gcc -DAI_ADDRCONFIG=0 -I/bitnami/ruby24stack-linux-x64/output/mysql/include -I/home/css/edx-edutech/common/include  -I/bitnami/ruby24stack-linux-x64/output/sqlite/include -I/home/css/edx-edutech/common/include/sasl -I/home/css/edx-edutech/common/include -D_REENTRANT  -DU_HAVE_ELF_H=1 -DU_HAVE_STRTOD_L=1 -DU_HAVE_XLOCALE_H=1  -DU_ATTRIBUTE_DEPRECATED= -fPIC -I/home/css/edx-edutech/common/include -fPIC -I/home/css/edx-edutech/common/include -I/bitnami/ruby24stack-linux-x64/output/mysql/include -I/home/css/edx-edutech/common/include -fPIC -m64 -I/bitnami/ruby24stack-linux-x64/output/ImageMagick/include/ImageMagick-6 -I/bitnami/ruby24stack-linux-x64/output/ImageMagick/include/ImageMagick-6/wand/ -I/bitnami/ruby24stack-linux-x64/output/ImageMagick/include/ImageMagick-6/MagickCore/ -std=c11 -Wall -pedantic -Wshadow -Wpointer-arith -Wmissing-prototypes -Wwrite-strings   -c
LIBFLAGS=-I/home/css/edx-edutech/common/include -DPIC -fPIC
GENLIB=gcc -fPIC -I/home/css/edx-edutech/common/include -fPIC -I/home/css/edx-edutech/common/include -I/bitnami/ruby24stack-linux-x64/output/mysql/include -I/home/css/edx-edutech/common/include -fPIC -m64 -I/bitnami/ruby24stack-linux-x64/output/ImageMagick/include/ImageMagick-6 -I/bitnami/ruby24stack-linux-x64/output/ImageMagick/include/ImageMagick-6/wand/ -I/bitnami/ruby24stack-linux-x64/output/ImageMagick/include/ImageMagick-6/MagickCore/ -std=c11 -Wall -pedantic -Wshadow -Wpointer-arith -Wmissing-prototypes -Wwrite-strings   -L/home/css/edx-edutech/common/lib -L/home/css/edx-edutech/common/lib -L/bitnami/ruby24stack-linux-x64/output/mysql/include -L/bitnami/ruby24stack-linux-x64/output/sqlite/lib -L/home/css/edx-edutech/common/lib -L/bitnami/ruby24stack-linux-x64/output/ImageMagick/lib  -shared -Wl,-Bsymbolic
LDICUDTFLAGS=-nodefaultlibs -nostdlib
LD_SONAME=-Wl,-soname -Wl,
RPATH_FLAGS=
BIR_LDFLAGS=-Wl,-Bsymbolic
AR=ar
ARFLAGS=r
RANLIB=ranlib
INSTALL_CMD=/bin/install -c
