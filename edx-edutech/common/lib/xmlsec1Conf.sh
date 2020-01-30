#
# Configuration file for using the XML library in GNOME applications
#
prefix="/home/css/edx-edutech/common"
exec_prefix="${prefix}"
libdir="${exec_prefix}/lib"
includedir="${prefix}/include"

XMLSEC_LIBDIR="${exec_prefix}/lib"
XMLSEC_INCLUDEDIR=" -D__XMLSEC_FUNCTION__=__func__ -DXMLSEC_NO_SIZE_T -DXMLSEC_NO_GOST=1 -DXMLSEC_NO_GOST2012=1 -DXMLSEC_DL_LIBLTDL=1 -I${prefix}/include/xmlsec1   -I/home/css/edx-edutech/common/include/libxml2  -I/home/css/edx-edutech/common/include -I/home/css/edx-edutech/common/include/libxml2  -I/home/css/edx-edutech/common/include  -DXMLSEC_CRYPTO_OPENSSL=1"
XMLSEC_LIBS="-L${exec_prefix}/lib -lxmlsec1-openssl -lxmlsec1 -lltdl  -L/home/css/edx-edutech/common/lib -lxml2  -L/home/css/edx-edutech/common/lib -lxslt -lxml2 -lz -liconv -lm -ldl -lm -lxml2  -L/home/css/edx-edutech/common/lib -lssl -lcrypto "
MODULE_VERSION="xmlsec-1.2.28-openssl"

