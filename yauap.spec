Name:           yauap
Summary:        Commandline Audio Player
Version:        0.2.4
Release:        2
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
Source0:        http://mirrors.zerg.biz/nongnu/yauap/%{name}-%{version}.tar.gz


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




%changelog
* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.2.4-1mdv2010.0
+ Revision: 444884
- Update to new version 0.2.4

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.2.3-1mdv2009.1
+ Revision: 332958
- New upstream release

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.2-4mdv2009.0
+ Revision: 262788
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.2-3mdv2009.0
+ Revision: 257933
- rebuild

* Tue Mar 18 2008 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.2-1mdv2008.1
+ Revision: 188683
- import yauap


