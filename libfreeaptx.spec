%global sonamebase 0

Name:           libfreeaptx
Version:        %{sonamebase}.1.1
Release:        1%{?dist}
Summary:        Open Source implementation of Audio Processing Technology codec (aptX)

License:        LGPLv2+
URL:            https://github.com/iamthehorker/%{name}
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package        tools
Summary:        %{name} encoder and decoder utilities
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description
This is Open Source implementation of Audio Processing Technology codec (aptX)
derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec is
mainly used in Bluetooth A2DP profile.

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description    tools
The %{name}-tools package contains freeaptxenc encoder and freeaptxdec decoder
command-line utilities.

%prep
%autosetup

%build
# Skip building static binaries
# Environment variable CFLAGS are overridden in makefile so we override that
%make_build STATIC_UTILITIES= ANAME= LDFLAGS="%{build_ldflags}" CFLAGS="%{optflags}"

%install
# Skip build in install phase
%make_install BUILD= PREFIX= LIBDIR="%{_libdir}" INCDIR="%{_includedir}" BINDIR="%{_bindir}" ANAME=

%files
%license COPYING
%{_libdir}/%{name}.so.%{sonamebase}
%{_libdir}/%{name}.so.%{version}

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}.so
%{_includedir}/freeaptx.h
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/freeaptxenc
%{_bindir}/freeaptxdec

%changelog
* Thu Jul 29 2021 Markus Frey <mfrey@mailbox.org> - 0.1.1-1
- Initial packaging
