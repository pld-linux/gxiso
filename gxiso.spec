Summary:	Program to extract or upload Xbox ISO images to an Xbox
Summary(pl):	Program do wyci±gania i wrzucania obrazów Xbox ISO do Xboksa
Name:		gxiso
Version:	1.2
Release:	1
License:	GPL
Group:		Networking
Source0:	http://kassoulet.free.fr/files/%{name}-%{version}.tar.gz
# Source0-md5:	869e6fe121f16e57ff8ad84f4b5db201
URL:		http://gxiso.berlios.de/
BuildRequires:	python-devel
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
