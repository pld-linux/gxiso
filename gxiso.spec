Summary:	Program to extract or upload Xbox ISO images to an Xbox
Summary(pl.UTF-8):	Program do wyciągania i wrzucania obrazów Xbox ISO do Xboksa
Name:		gxiso
Version:	1.5
Release:	1
License:	GPL
Group:		Networking
Source0:	http://download.berlios.de/gxiso/%{name}-%{version}.tar.gz
# Source0-md5:	c5e8e24b57ca6fe652ddc24f7e8ca4ba
URL:		http://gxiso.berlios.de/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	gettext-tools
Requires:	python-pygtk-gtk
Requires:	python-pygtk-glade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gXiso is GTK+2 program to extract or upload Xbox ISO images to an
Xbox.

%description -l pl.UTF-8
gXiso to program GTK+2 do wyciągania i wrzucania obrazów Xbox ISO do
Xboksa.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*py[co]
