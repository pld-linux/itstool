Summary:	ITS-based XML translation tool
Summary(pl.UTF-8):	Narzędzie do tłumaczenia XML-a oparte na ITS
Name:		itstool
Version:	2.0.6
Release:	2
License:	GPL v3+
Group:		Applications/Text
Source0:	http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2
# Source0-md5:	4306eeba4f4aee6b393d14f9c3c57ca1
Patch0:		%{name}-fix-crash-wrong-encoding.patch
URL:		http://itstool.org/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-libxml2
Requires:	python >= 1:2.6
Requires:	python-libxml2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ITS Tool allows you to translate XML documents with PO files, using
rules from the W3C Internationalization Tag Set (ITS) to determine
what to translate and how to separate it into PO file messages.

%description -l pl.UTF-8
ITS Tool pozwala na tłumaczenie dokumentów XML przy użyciu plików PO,
z wykorzystaniem reguł ITS (W3C Internationalization Tag Set) do
określania, co ma być tłumaczone i jak powinno być rozdzielone na
komunikaty w pliku PO.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	PYTHON="%{__python}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_bindir}/itstool
%{_datadir}/itstool
%{_mandir}/man1/itstool.1*
