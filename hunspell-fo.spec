Name: hunspell-fo
Summary: Faroese hunspell dictionaries
Version: 0.4.1
Release: 4%{?dist}
Source: http://fo.speling.org/filer/myspell-fo-%{version}.tar.bz2
Group: Applications/Text
URL: http://fo.speling.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Faroese hunspell dictionaries.

%prep
%setup -q -n myspell-fo-%{version}

%build
for i in Copyright contributors README; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README Copyright contributors COPYING
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4.1-4
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.4.1-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May 22 2011 Caolán McNamara <caolanm@redhat.com> - 0.4.0-1
- latest version

* Fri Mar 18 2011 Caolán McNamara <caolanm@redhat.com> - 0.2.44-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Caolán McNamara <caolanm@redhat.com> - 0.2.43-1
- latest version

* Mon Oct 04 2010 Caolán McNamara <caolanm@redhat.com> - 0.2.42-1
- latest version

* Wed Jul 28 2010 Caolán McNamara <caolanm@redhat.com> - 0.2.41-1
- latest version

* Fri May 28 2010 Caolán McNamara <caolanm@redhat.com> - 0.2.40-1
- latest version

* Mon Jan 04 2010 Caolán McNamara <caolanm@redhat.com> - 0.2.39-1
- latest version

* Thu Nov 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.2.38-1
- latest version

* Fri Sep 04 2009 Caolán McNamara <caolanm@redhat.com> - 0.2.37-1
- latest version

* Mon Aug 10 2009 Caolán McNamara <caolanm@redhat.com> - 0.2.36-4
- .gz -> .bz2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.2.36-2
- tidy spec

* Tue May 19 2009 Caolán McNamara <caolanm@redhat.com> - 0.2.36-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Caolán McNamara <caolanm@redhat.com> - 0.2.35-1
- latest version

* Mon Sep 08 2008 Caolán McNamara <caolanm@redhat.com> - 0.2.34-1
- latest version

* Mon Jul 07 2008 Caolán McNamara <caolanm@redhat.com> - 0.2.33-1
- latest version

* Thu Mar 27 2008 Caolán McNamara <caolanm@redhat.com> - 0.2.32-1
- initial version
