Summary:	Program to extract or upload Xbox ISO images to an Xbox
Summary(pl):	Program do wyci±gania i wrzucania obrazów Xbox ISO do Xboksa
Name:		gxiso
Version:	1.3
Release:	1
License:	GPL
Group:		Networking
Source0:	http://kassoulet.free.fr/files/%{name}-%{version}.tar.gz
# Source0-md5:	9736a3eefb3ddc9eee93b5d7aee783e6
URL:		http://gxiso.berlios.de/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	gettext-devel
Requires:	python-pygtk-gtk
Requires:	python-pygtk-glade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gXiso is GTK+2 program to extract or upload Xbox ISO images to an
Xbox.

%description -l pl
gXiso to program GTK+2 do wyci±gania i wrzucania obrazów Xbox ISO do
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
