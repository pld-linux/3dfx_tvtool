Summary:	The 3dfx TV Out Tool - GUI on setting the BT869 chip on the VooDoo3
Summary(pl):	3dfx TV Out Tool - narzêdzie do ustawiania chipu BT869 z kart VooDoo3
Name:		3dfx_tvtool
Version:	0.0.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://131.155.224.79/~node/3dfx_tvtool/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://131.155.224.79/~node/3dfx_tvtool/
BuildRequires:	gtk+2-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
The 3dfx TV Out Tool is a userfriendly GUI on setting all the settings
found on the BT869 chip on the VooDoo3. It tries to be the well-known
'TV Tool' for the 3dfx VooDoo3 cards. It might work on other cards
based on the bt869 chip, since it uses the bt869 lm_sensors module.

%description -l pl
3dfx TV Out Tool jest przyjaznym dla u¿ytkownika GUI do ustawiania
wszystkich ustawieñ, jakie s± na chipie BT869 w kartach VooDoo3. Stara
siê byæ dobrze znanym "narzêdziem TV" do kart VooDoo3 firmy 3dfx. Mo¿e
pracowaæ na innych kartach opartych o chip bt869, je¿eli u¿ywaj± one
modu³u bt869 z lm_sensors.

%prep
%setup -q

%build
CC=%{__cc}
export CC
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%{__make} DESTDIR=$RPM_BUILD_ROOT \
		BINDIR=%{_bindir} install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{BUGS,ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_applnkdir}/Multimedia/*.desktop
