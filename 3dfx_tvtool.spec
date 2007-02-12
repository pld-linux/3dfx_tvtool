Summary:	The 3dfx TV Out Tool - GUI on setting the BT869 chip on the VooDoo3
Summary(pl.UTF-8):   3dfx TV Out Tool - narzędzie do ustawiania chipu BT869 z kart VooDoo3
Name:		3dfx_tvtool
Version:	0.0.3
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://7of9.are-b.org/~node/3dfx_tvtool/%{name}-%{version}.tar.bz2
# Source0-md5:	41dbd44e9a398e3ae883dd6d621b9adf
Source1:	%{name}.desktop
URL:		http://7of9.are-b.org/~node/3dfx_tvtool/
BuildRequires:	gtk+2-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 3dfx TV Out Tool is a userfriendly GUI on setting all the settings
found on the BT869 chip on the VooDoo3. It tries to be the well-known
'TV Tool' for the 3dfx VooDoo3 cards. It might work on other cards
based on the bt869 chip, since it uses the bt869 lm_sensors module.

%description -l pl.UTF-8
3dfx TV Out Tool jest przyjaznym dla użytkownika GUI do ustawiania
wszystkich ustawień, jakie są na chipie BT869 w kartach VooDoo3. Stara
się być dobrze znanym "narzędziem TV" do kart VooDoo3 firmy 3dfx. Może
pracować na innych kartach opartych o chip bt869, jeżeli używają one
modułu bt869 z lm_sensors.

%prep
%setup -q

%build
CC="%{__cc}"
export CC
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{BUGS,ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
