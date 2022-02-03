#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bpftrace
Version  : 0.14.1
Release  : 19
URL      : https://github.com/iovisor/bpftrace/archive/v0.14.1/bpftrace-0.14.1.tar.gz
Source0  : https://github.com/iovisor/bpftrace/archive/v0.14.1/bpftrace-0.14.1.tar.gz
Summary  : High-level tracing language for Linux eBPF
Group    : Development/Tools
License  : Apache-2.0
Requires: bpftrace-bin = %{version}-%{release}
Requires: bpftrace-data = %{version}-%{release}
Requires: bpftrace-license = %{version}-%{release}
Requires: bpftrace-man = %{version}-%{release}
BuildRequires : bcc-dev
BuildRequires : bison-dev
BuildRequires : buildreq-cmake
BuildRequires : cereal-dev
BuildRequires : flex
BuildRequires : flex-dev
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : libxml2-dev
BuildRequires : llvm-dev
BuildRequires : llvm-staticdev
BuildRequires : pkgconfig(libelf)
Patch1: 0001-Don-t-use-asciidoctor.patch

%description
# bpftrace
[![Build Status](https://github.com/iovisor/bpftrace/workflows/CI/badge.svg?branch=master)](https://github.com/iovisor/bpftrace/actions?query=workflow%3ACI+branch%3Amaster)
[![IRC#bpftrace](https://img.shields.io/badge/IRC-bpftrace-blue.svg)](https://webchat.oftc.net/?channels=bpftrace)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/iovisor/bpftrace.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/iovisor/bpftrace/alerts/)

%package bin
Summary: bin components for the bpftrace package.
Group: Binaries
Requires: bpftrace-data = %{version}-%{release}
Requires: bpftrace-license = %{version}-%{release}

%description bin
bin components for the bpftrace package.


%package data
Summary: data components for the bpftrace package.
Group: Data

%description data
data components for the bpftrace package.


%package license
Summary: license components for the bpftrace package.
Group: Default

%description license
license components for the bpftrace package.


%package man
Summary: man components for the bpftrace package.
Group: Default

%description man
man components for the bpftrace package.


%prep
%setup -q -n bpftrace-0.14.1
cd %{_builddir}/bpftrace-0.14.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643913084
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DBUILD_TESTING=OFF \
-DBUILD_SHARED_LIBS=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1643913084
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bpftrace
cp %{_builddir}/bpftrace-0.14.1/LICENSE %{buildroot}/usr/share/package-licenses/bpftrace/2b8b815229aa8a61e483fb4ba0588b8b6c491890
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bpftrace

%files data
%defattr(-,root,root,-)
/usr/share/bpftrace/tools/bashreadline.bt
/usr/share/bpftrace/tools/biolatency.bt
/usr/share/bpftrace/tools/biosnoop.bt
/usr/share/bpftrace/tools/biostacks.bt
/usr/share/bpftrace/tools/bitesize.bt
/usr/share/bpftrace/tools/capable.bt
/usr/share/bpftrace/tools/cpuwalk.bt
/usr/share/bpftrace/tools/dcsnoop.bt
/usr/share/bpftrace/tools/doc/bashreadline_example.txt
/usr/share/bpftrace/tools/doc/biolatency_example.txt
/usr/share/bpftrace/tools/doc/biosnoop_example.txt
/usr/share/bpftrace/tools/doc/biostacks_example.txt
/usr/share/bpftrace/tools/doc/bitesize_example.txt
/usr/share/bpftrace/tools/doc/capable_example.txt
/usr/share/bpftrace/tools/doc/cpuwalk_example.txt
/usr/share/bpftrace/tools/doc/dcsnoop_example.txt
/usr/share/bpftrace/tools/doc/execsnoop_example.txt
/usr/share/bpftrace/tools/doc/gethostlatency_example.txt
/usr/share/bpftrace/tools/doc/killsnoop_example.txt
/usr/share/bpftrace/tools/doc/loads_example.txt
/usr/share/bpftrace/tools/doc/mdflush_example.txt
/usr/share/bpftrace/tools/doc/naptime_example.txt
/usr/share/bpftrace/tools/doc/oomkill_example.txt
/usr/share/bpftrace/tools/doc/opensnoop_example.txt
/usr/share/bpftrace/tools/doc/pidpersec_example.txt
/usr/share/bpftrace/tools/doc/runqlat_example.txt
/usr/share/bpftrace/tools/doc/runqlen_example.txt
/usr/share/bpftrace/tools/doc/setuids_example.txt
/usr/share/bpftrace/tools/doc/statsnoop_example.txt
/usr/share/bpftrace/tools/doc/swapin_example.txt
/usr/share/bpftrace/tools/doc/syncsnoop_example.txt
/usr/share/bpftrace/tools/doc/syscount_example.txt
/usr/share/bpftrace/tools/doc/tcpaccept_example.txt
/usr/share/bpftrace/tools/doc/tcpconnect_example.txt
/usr/share/bpftrace/tools/doc/tcpdrop_example.txt
/usr/share/bpftrace/tools/doc/tcplife_example.txt
/usr/share/bpftrace/tools/doc/tcpretrans_example.txt
/usr/share/bpftrace/tools/doc/tcpsynbl_example.txt
/usr/share/bpftrace/tools/doc/threadsnoop_example.txt
/usr/share/bpftrace/tools/doc/vfscount_example.txt
/usr/share/bpftrace/tools/doc/vfsstat_example.txt
/usr/share/bpftrace/tools/doc/writeback_example.txt
/usr/share/bpftrace/tools/doc/xfsdist_example.txt
/usr/share/bpftrace/tools/execsnoop.bt
/usr/share/bpftrace/tools/gethostlatency.bt
/usr/share/bpftrace/tools/killsnoop.bt
/usr/share/bpftrace/tools/loads.bt
/usr/share/bpftrace/tools/mdflush.bt
/usr/share/bpftrace/tools/naptime.bt
/usr/share/bpftrace/tools/oomkill.bt
/usr/share/bpftrace/tools/opensnoop.bt
/usr/share/bpftrace/tools/pidpersec.bt
/usr/share/bpftrace/tools/runqlat.bt
/usr/share/bpftrace/tools/runqlen.bt
/usr/share/bpftrace/tools/setuids.bt
/usr/share/bpftrace/tools/statsnoop.bt
/usr/share/bpftrace/tools/swapin.bt
/usr/share/bpftrace/tools/syncsnoop.bt
/usr/share/bpftrace/tools/syscount.bt
/usr/share/bpftrace/tools/tcpaccept.bt
/usr/share/bpftrace/tools/tcpconnect.bt
/usr/share/bpftrace/tools/tcpdrop.bt
/usr/share/bpftrace/tools/tcplife.bt
/usr/share/bpftrace/tools/tcpretrans.bt
/usr/share/bpftrace/tools/tcpsynbl.bt
/usr/share/bpftrace/tools/threadsnoop.bt
/usr/share/bpftrace/tools/vfscount.bt
/usr/share/bpftrace/tools/vfsstat.bt
/usr/share/bpftrace/tools/writeback.bt
/usr/share/bpftrace/tools/xfsdist.bt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bpftrace/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/bashreadline.8.gz
/usr/share/man/man8/biolatency.8.gz
/usr/share/man/man8/biosnoop.8.gz
/usr/share/man/man8/biostacks.8.gz
/usr/share/man/man8/bitesize.8.gz
/usr/share/man/man8/capable.8.gz
/usr/share/man/man8/cpuwalk.8.gz
/usr/share/man/man8/dcsnoop.8.gz
/usr/share/man/man8/execsnoop.8.gz
/usr/share/man/man8/gethostlatency.8.gz
/usr/share/man/man8/killsnoop.8.gz
/usr/share/man/man8/loads.8.gz
/usr/share/man/man8/mdflush.8.gz
/usr/share/man/man8/naptime.8.gz
/usr/share/man/man8/oomkill.8.gz
/usr/share/man/man8/opensnoop.8.gz
/usr/share/man/man8/pidpersec.8.gz
/usr/share/man/man8/runqlat.8.gz
/usr/share/man/man8/runqlen.8.gz
/usr/share/man/man8/setuids.8.gz
/usr/share/man/man8/statsnoop.8.gz
/usr/share/man/man8/swapin.8.gz
/usr/share/man/man8/syncsnoop.8.gz
/usr/share/man/man8/syscount.8.gz
/usr/share/man/man8/tcpaccept.8.gz
/usr/share/man/man8/tcpconnect.8.gz
/usr/share/man/man8/tcpdrop.8.gz
/usr/share/man/man8/tcplife.8.gz
/usr/share/man/man8/tcpretrans.8.gz
/usr/share/man/man8/tcpsynbl.8.gz
/usr/share/man/man8/threadsnoop.8.gz
/usr/share/man/man8/vfscount.8.gz
/usr/share/man/man8/vfsstat.8.gz
/usr/share/man/man8/writeback.8.gz
/usr/share/man/man8/xfsdist.8.gz
