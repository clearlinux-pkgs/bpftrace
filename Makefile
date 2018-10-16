PKG_NAME := bpftrace
URL = https://github.com/iovisor/bpftrace/archive/51500dfbe2529823a261af2ab2879d3fb7cd8bf9.tar.gz
ARCHIVES = https://github.com/iovisor/bcc/archive/v0.7.0.tar.gz 3rdparty/bcc https://github.com/google/googletest/archive/release-1.8.1.tar.gz 3rdparty/gtest

include ../common/Makefile.common
