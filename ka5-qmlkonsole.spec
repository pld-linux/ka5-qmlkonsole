#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	23.08.5
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		qmlkonsole
Summary:	A terminal application built for touch
Summary(pl.UTF-8):	Aplikacja terminala dla ekranów dotykowych
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	204daca108b2822cddc1366324cf9942
URL:		https://apps.kde.org/qmlkonsole/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Network-devel >= 5.15.10
BuildRequires:	Qt5Qml-devel >= 5.15.10
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.101.0
BuildRequires:	kf5-kconfig-devel >= 5.101.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.101.0
BuildRequires:	kf5-ki18n-devel >= 5.101.0
BuildRequires:	kf5-kirigami2-devel >= 5.101.0
BuildRequires:	kf5-kirigami-addons-devel >= 0.6
BuildRequires:	kf5-kwindowsystem-devel >= 5.101.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	qmltermwidget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A terminal application built for touch, based on qmltermwidget
<https://github.com/Swordfish90/qmltermwidget>.

%description -l pl.UTF-8
Aplikacja terminala dla ekranów dotykowych, oparta na qmltermwidget
<https://github.com/Swordfish90/qmltermwidget>.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qmlkonsole
%{_desktopdir}/org.kde.qmlkonsole.desktop
%{_datadir}/config.kcfg/terminalsettings.kcfg
%{_iconsdir}/hicolor/scalable/apps/org.kde.qmlkonsole.svg
%{_datadir}/metainfo/org.kde.qmlkonsole.appdata.xml
