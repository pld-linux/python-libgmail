%define 	module	libgmail

Summary:	libgmail . Python binding for Google's Gmail service
Name:		python-%{module}
Version:	0.0.8
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tgz
# Source0-md5:	6bfd82f39b959a6e92fa73fa19ed4eba
URL:		http://libgmail.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libgmail project is a pure Python binding to provide access to
Google's Gmail web-mail service.

%prep
%setup -q -n %{module}-%{version}

%build
python -c "import compiler;compiler.compileFile('libgmail.py')"
python -c "import compiler;compiler.compileFile('constants.py')"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install constants.pyc $RPM_BUILD_ROOT%{py_sitescriptdir}
install libgmail.pyc $RPM_BUILD_ROOT%{py_sitescriptdir}

install demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc [A-R]*
%{py_sitescriptdir}/*.py[co]
%{_examplesdir}/%{name}-%{version}
