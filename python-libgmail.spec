%define 	module	libgmail

Summary:	libgmail - Python binding for Google's Gmail service
Summary(pl):	libgmail - wi�zania Pythona do us�ugi Google Gmail
Name:		python-%{module}
Version:	0.0.8
Release:	0.9
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tgz
# Source0-md5:	6bfd82f39b959a6e92fa73fa19ed4eba
Patch0:		%{name}-path.patch
URL:		http://libgmail.sourceforge.net/
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libgmail project is a pure Python binding to provide access to
Google's Gmail web-mail service.

%description -l pl
Projekt libgmail umo�liwia uzyskanie dost�pu do us�ugi Google Gmail w
programach pisanych w Pythonie.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
%{py_comp} .
%{py_ocomp} .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_bindir},%{_examplesdir}/%{name}-%{version},%{_datadir}/%{name}}

install libgmail.py[co] $RPM_BUILD_ROOT%{py_sitescriptdir}

install mkconstants.py $RPM_BUILD_ROOT%{_bindir}
install constants.py $RPM_BUILD_ROOT%{_datadir}/%{name}

install demos/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGELOG README
%{_bindir}/mkconstants.py
%{py_sitescriptdir}/*.py[co]
%{_datadir}/%{name}
%{_examplesdir}/%{name}-%{version}
