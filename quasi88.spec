Name:         quasi88
License:      GPL
Group:        Emulators
Version:      0.6.3
Release:      %mkrel 1
Summary:      NEC PC-8801 Emulator
Source:       %name-%version.tgz
Patch:        %name-%version.dif
Patch1:       %name-rpmlint.patch
BuildRequires: SDL-devel gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Needs ROM images in ~/.quasi88/rom. You can use the corresponding MESS rom set (pc88srl.zip).

%prep
%setup
%patch
%patch1

%build
CFLAGS="$RPM_OPT_FLAGS" make %{?jobs:-j%jobs} \
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

