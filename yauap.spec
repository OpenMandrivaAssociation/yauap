Name:           yauap
Summary:        Commandline Audio Player
Version:        0.2.2
Release:        %mkrel 4
Url:            http://www.nongnu.org/yauap/
License:        LGPL v2+
Group:          Sound
BuildRequires:  dbus-glib-devel
BuildRequires:  libgstreamer-plugins-base-devel
Requires:       libgstreamer0.10
Requires:       gstreamer0.10-plugins-base 
Requires:       gstreamer0.10-plugins-good 
Requires:       dbus-x11
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.gz


%description
yauap is a simple commandline audio player based on GStreamer.

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/yauap

#--------------------------------------------------------------------

%prep
%setup -q


%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%make

%install
%makeinstall

%clean
%{__rm} -rf "%{buildroot}"


