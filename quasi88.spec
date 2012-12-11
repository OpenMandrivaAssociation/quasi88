Name:         quasi88
License:      GPL
Group:        Emulators
Version:      0.6.3
Release:      %mkrel 2
Summary:      NEC PC-8801 Emulator
URL:          http://www.117.ne.jp/~show/pc8801/pc88emu.html
Source0:      http://www.117.ne.jp/~show/pc8801/%name-%version.tgz
Patch0:       %name-compile.patch
Patch1:       %name-rpmlint.patch
Patch2:       %name-Werror.patch
BuildRequires: SDL-devel gcc-c++

%description
Needs ROM images in ~/.quasi88/rom. You can use the corresponding MESS rom set (pc88srl.zip).

%prep
%setup
%patch0 -p1 -b .config~
%patch1 -p0 -b .rpmlint~
%patch2 -p1 -b .Werror~

%build
CFLAGS="$RPM_OPT_FLAGS" make \
%ifarch %ix86 x86_64 ia64 %arm
LSB_FIRST=1
%else

%endif
cd tools
make CFLAGS="$RPM_OPT_FLAGS"

%install
install -D -m 755 quasi88.sdl $RPM_BUILD_ROOT%{_bindir}/quasi88
install -m 755 tools/*88 $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(-,root,root)
%doc document/* *.ini *.rc tools/*.txt
%{_bindir}/*88



%changelog
* Wed Jan 04 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.6.3-2mdv2011.0
+ Revision: 755571
- Use -p1 when applying patch0
- Add URL to upstream sources in Source tag
- Make it build with the standard -Werror flags
- Fix build/linkage issues

  + Zombie Ryushu <ryushu@mandriva.org>
    - Bad patch
    - Spec Cleanups
    - Spec Cleanups
    - imported package quasi88


* Thu Nov 27 2008 - uli@suse.de
- fixed bugs found by rpmlint
