%define tarball xf86-video-vmware
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:    Xorg X11 vmware video driver
Name:	    xorg-x11-drv-vmware
Version:    10.16.7
Release:    2.1%{?dist}
URL:	    http://www.x.org
License:    MIT
Group:	    User Interface/X Hardware Support
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:    vmware.xinf
Patch0: abi.patch
Patch1: abi2.patch

ExclusiveArch: %{ix86} x86_64 ia64

%if 0%{?gitdate}
BuildRequires: autoconf automake libtool
%endif
BuildRequires: xorg-x11-server-sdk >= 1.4.99.1

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 vmware video driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p1 -b .abi
%patch1 -p1 -b .abi2

%build
%if 0%{?gitdate}
autoreconf -v --install || exit 1
%endif
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/vmware_drv.so
%{_datadir}/hwdata/videoaliases/vmware.xinf
%{_mandir}/man4/vmware.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 10.16.7-2.1
- Rebuilt for RHEL 6

* Fri Aug 07 2009 Adam Jackson <ajax@redhat.com> 10.16.7-2
- fix for symbol list removal.

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 10.16.7-1
- vmware 10.16.7 + new abi patch

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.16.0-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 10.16.0-4.1
- ABI bump

* Tue Jun 23 2009 Dave Airlie <airlied@redhat.com> 10.16.0-4
- abi.patch: patch for new server ABI

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Dave Airlie <airlied@redhat.com> 10.16.0-2
- bump build for new server API

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 10.16.0-1
- Latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 10.15.2-100.1
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Adam Jackson <ajax@redhat.com> 10.15.2-99.1
- Update to git snapshot for pciaccess conversion. (#428613)

* Thu Oct 11 2007 Adam Jackson <ajax@redhat.com> 10.15.2-1
- xf86-video-vmware 10.15.2

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 10.15.1-1
- xf86-video-vmware 10.15.1

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 10.14.1-3
- Rebuild for build ID

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 10.14.1-2
- Update Requires and BuildRequires.  Disown the module directories.  Add
  Requires: hwdata.

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 10.14.1-1.fc7
- Update to 10.14.1

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 10.13.0-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 10.13.0-1
- Update to 10.13.0 from 7.1RC1.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 10.11.1.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 10.11.1.3-1
- Updated xorg-x11-drv-vmware to version 10.11.1.3 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 10.11.1.2-1
- Updated xorg-x11-drv-vmware to version 10.11.1.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 10.11.1-1
- Updated xorg-x11-drv-vmware to version 10.11.1 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 10.11.0.1-1
- Updated xorg-x11-drv-vmware to version 10.11.0.1 from X11R7 RC1
- Fix *.la file removal.

* Tue Oct 4 2005 Mike A. Harris <mharris@redhat.com> 10.10.2-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64, ia64

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 10.10.2-0
- Initial spec file for vmware video driver generated automatically
  by my xorg-driverspecgen script.
