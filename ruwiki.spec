Summary:	A Wiki written in Ruby
Summary(pl.UTF-8):	Wiki napisane w Ruby
Name:		ruwiki
Version:	0.9.3
Release:	2
License:	Ruby License
Group:		Applications/WWW
Source0:	http://rubyforge.org/frs/download.php/2314/%{name}-%{version}.tar.gz
# Source0-md5:	f5538cc2a723438954b1466edd6dfbed
Source1:	setup.rb
URL:		http://rubyforge.org/projects/ruwiki/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Requires:	ruby-Diff-LCS
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_cgibindir	/home/services/httpd/cgi-bin

%description
Ruwiki is a simple, extensible Wiki-clone written in Ruby, supporting
CGI and WEBrick interfaces, templates, CSS formatting, namespaces, and
internationalisation. A focus on antispam techniques has been applied.

%description -l pl.UTF-8
Ruwiki to prosty, rozszerzalny klon Wiki napisany w Ruby. Obsługuje
skrypty CGI oraz interfejsy WEBrick, skórki, formatowanie przy użyciu
CSS a także internacjonalizacje. Posiada mechanizmy antyspamowe.

%prep
%setup -q
install %{SOURCE1} .
mkdir share/ruwiki -p
mv data share/ruwiki/data
mv templates share/ruwiki/templates
mv share data
mkdir cgi-bin
mv bin/ruwiki.cgi cgi-bin
rm bin/ruwiki_service.rb

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_ridir},%{_cgibindir}}
install cgi-bin/%{name}.cgi $RPM_BUILD_ROOT%{_cgibindir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

rdoc -o rdoc lib --inline-source

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_cgibindir}/*
%{ruby_rubylibdir}/*
%{_datadir}/%{name}
