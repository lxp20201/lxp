#!/bin/sh
echo $PATH | egrep "/home/css/edx-edutech/common" > /dev/null
if [ $? -ne 0 ] ; then
PATH="/home/css/edx-edutech/apps/edx/edx-platform/node_modules/.bin:/home/css/edx-edutech/apps/edx/bin:/home/css/edx-edutech/postgresql/bin:/home/css/edx-edutech/git/bin:/home/css/edx-edutech/perl/bin:/home/css/edx-edutech/nodejs/bin:/home/css/edx-edutech/java/bin:/home/css/edx-edutech/erlang/bin:/home/css/edx-edutech/ruby/bin:/home/css/edx-edutech/python/bin:/home/css/edx-edutech/elasticsearch/bin:/home/css/edx-edutech/memcached/bin:/home/css/edx-edutech/mongodb/bin:/home/css/edx-edutech/sqlite/bin:/home/css/edx-edutech/mysql/bin:/home/css/edx-edutech/letsencrypt/:/home/css/edx-edutech/apache2/bin:/home/css/edx-edutech/common/bin:$PATH"
export PATH
fi
echo $LD_LIBRARY_PATH | egrep "/home/css/edx-edutech/common" > /dev/null
if [ $? -ne 0 ] ; then
LD_LIBRARY_PATH="/home/css/edx-edutech/ruby/lib/ruby/gems/2.4.0/gems/passenger-5.3.7/lib:/home/css/edx-edutech/postgresql/lib:/home/css/edx-edutech/git/lib:/home/css/edx-edutech/perl/lib:/home/css/edx-edutech/perl/lib/5.16.3/x86_64-linux-thread-multi/CORE:/home/css/edx-edutech/java/lib/amd64/server:/home/css/edx-edutech/java/lib/amd64/headless:/home/css/edx-edutech/java/lib/amd64/jli:/home/css/edx-edutech/java/lib/amd64:/home/css/edx-edutech/erlang/lib:/home/css/edx-edutech/ruby/lib:/home/css/edx-edutech/python/lib:/home/css/edx-edutech/memcached/lib:/home/css/edx-edutech/mongodb/lib:/home/css/edx-edutech/sqlite/lib:/home/css/edx-edutech/mysql/lib:/home/css/edx-edutech/apache2/lib:/home/css/edx-edutech/common/lib:/home/css/edx-edutech/common/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export LD_LIBRARY_PATH
fi

TERMINFO=/home/css/edx-edutech/common/share/terminfo
export TERMINFO
##### GIT ENV #####
GIT_EXEC_PATH=/home/css/edx-edutech/git/libexec/git-core/
export GIT_EXEC_PATH
GIT_TEMPLATE_DIR=/home/css/edx-edutech/git/share/git-core/templates
export GIT_TEMPLATE_DIR
GIT_SSL_CAINFO=/home/css/edx-edutech/common/openssl/certs/curl-ca-bundle.crt
export GIT_SSL_CAINFO


PERL5LIB="/home/css/edx-edutech/git/lib/site_perl/5.16.3:$PERL5LIB"
export PERL5LIB
GITPERLLIB="/home/css/edx-edutech/git/lib/site_perl/5.16.3"
export GITPERLLIB
                    ##### GHOSTSCRIPT ENV #####
GS_LIB="/home/css/edx-edutech/common/share/ghostscript/fonts"
export GS_LIB
##### IMAGEMAGICK ENV #####
MAGICK_HOME="/home/css/edx-edutech/common"
export MAGICK_HOME

MAGICK_CONFIGURE_PATH="/home/css/edx-edutech/common/lib/ImageMagick-6.9.8/config-Q16:/home/css/edx-edutech/common/"
export MAGICK_CONFIGURE_PATH

MAGICK_CODER_MODULE_PATH="/home/css/edx-edutech/common/lib/ImageMagick-6.9.8/modules-Q16/coders"
export MAGICK_CODER_MODULE_PATH

##### FONTCONFIG ENV #####
FONTCONFIG_PATH="/home/css/edx-edutech/common/etc/fonts"
export FONTCONFIG_PATH
SASL_CONF_PATH=/home/css/edx-edutech/common/etc
export SASL_CONF_PATH
SASL_PATH=/home/css/edx-edutech/common/lib/sasl2 
export SASL_PATH
LDAPCONF=/home/css/edx-edutech/common/etc/openldap/ldap.conf
export LDAPCONF
##### PERL ENV #####
PERL5LIB="/home/css/edx-edutech/perl/lib/5.16.3:/home/css/edx-edutech/perl/lib/site_perl/5.16.3:/home/css/edx-edutech/perl/lib/5.16.3/x86_64-linux-thread-multi:/home/css/edx-edutech/perl/lib/site_perl/5.16.3/x86_64-linux-thread-multi"
export PERL5LIB
##### NODEJS ENV #####

export NODE_PATH=/home/css/edx-edutech/nodejs/lib/node_modules

            ##### JAVA ENV #####
JAVA_HOME=/home/css/edx-edutech/java
export JAVA_HOME

##### RUBY ENV #####
GEM_HOME="/home/css/edx-edutech/ruby/lib/ruby/gems/2.4.0"
GEM_PATH="/home/css/edx-edutech/ruby/lib/ruby/gems/2.4.0"
RUBY_HOME="/home/css/edx-edutech/ruby"
RUBYLIB="/home/css/edx-edutech/ruby/lib/ruby/site_ruby/2.4.0:/home/css/edx-edutech/ruby/lib/ruby/site_ruby/2.4.0/x86_64-linux:/home/css/edx-edutech/ruby/lib/ruby/site_ruby/:/home/css/edx-edutech/ruby/lib/ruby/vendor_ruby/2.4.0:/home/css/edx-edutech/ruby/lib/ruby/vendor_ruby/2.4.0/x86_64-linux:/home/css/edx-edutech/ruby/lib/ruby/vendor_ruby/:/home/css/edx-edutech/ruby/lib/ruby/2.4.0:/home/css/edx-edutech/ruby/lib/ruby/2.4.0/x86_64-linux:/home/css/edx-edutech/ruby/lib/ruby/:/home/css/edx-edutech/ruby/lib"
BUNDLE_CONFIG="/home/css/edx-edutech/ruby/.bundler/config"
export GEM_HOME
export GEM_PATH
export RUBY_HOME
export RUBYLIB
export BUNDLE_CONFIG
if [ -n "$(grep 'BUNDLE_DEFAULT' "$BUNDLE_CONFIG")" ]; then
    export RUBYLIB="$GEM_PATH/gems/bundler-$(grep 'BUNDLE_DEFAULT' "$BUNDLE_CONFIG" | awk -F '"' '{print $2}')/lib:/home/css/edx-edutech/ruby/lib/ruby/site_ruby/2.4.0:/home/css/edx-edutech/ruby/lib/ruby/site_ruby/2.4.0/x86_64-linux:/home/css/edx-edutech/ruby/lib/ruby/site_ruby/:/home/css/edx-edutech/ruby/lib/ruby/vendor_ruby/2.4.0:/home/css/edx-edutech/ruby/lib/ruby/vendor_ruby/2.4.0/x86_64-linux:/home/css/edx-edutech/ruby/lib/ruby/vendor_ruby/:/home/css/edx-edutech/ruby/lib/ruby/2.4.0:/home/css/edx-edutech/ruby/lib/ruby/2.4.0/x86_64-linux:/home/css/edx-edutech/ruby/lib/ruby/:/home/css/edx-edutech/ruby/lib"
fi
            ##### MEMCACHED ENV #####
		
      ##### MONGODB ENV #####

      ##### SQLITE ENV #####
			
##### MYSQL ENV #####

##### APACHE ENV #####

##### CURL ENV #####
CURL_CA_BUNDLE=/home/css/edx-edutech/common/openssl/certs/curl-ca-bundle.crt
export CURL_CA_BUNDLE
##### SSL ENV #####
SSL_CERT_FILE=/home/css/edx-edutech/common/openssl/certs/curl-ca-bundle.crt
export SSL_CERT_FILE
OPENSSL_CONF=/home/css/edx-edutech/common/openssl/openssl.cnf
export OPENSSL_CONF
OPENSSL_ENGINES=/home/css/edx-edutech/common/lib/engines
export OPENSSL_ENGINES


. /home/css/edx-edutech/scripts/build-setenv.sh
PYTHON_EGG_CACHE=/home/css/edx-edutech/.tmp
export PYTHON_EGG_CACHE
