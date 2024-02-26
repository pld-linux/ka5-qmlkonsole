#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		qmlkonsole
Summary:	A terminal application built for touch
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	985263e65aab74a0fb03b5f7399c4d0c
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Network-devel >= 5.15.10
BuildRequires:	Qt6Qml-devel >= 5.15.10
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.101.0
BuildRequires:	kf6-kconfig-devel >= 5.101.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.101.0
BuildRequires:	kf6-ki18n-devel >= 5.101.0
BuildRequires:	kf6-kirigami-devel >= 5.101.0
BuildRequires:	kf6-kwindowsystem-devel >= 5.101.0
BuildRequires:	kirigami-addons-devel >= 0.6
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	qmltermwidget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A terminal application built for touch, based on
[qmltermwidget](https://github.com/Swordfish90/qmltermwidget).

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,zh_CN}

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qmlkonsole
%{_desktopdir}/org.kde.qmlkonsole.desktop
%{_datadir}/config.kcfg/terminalsettings.kcfg
%{_iconsdir}/hicolor/scalable/apps/org.kde.qmlkonsole.svg
%{_datadir}/metainfo/org.kde.qmlkonsole.appdata.xml
