%global with_check 0
%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global goipath github.com/containers/podman-tui
Version: 0.2.0
%global tag v0.2.0
%gometa

%global goname podman-tui

%global common_description %{expand:
%{goname} is a terminal user interface for Podman v3 (>= 3.1).
it is using podman.socket service to communicate with podman machine.
}

%global golicenses LICENSE
%global godocs CODE-OF-CONDUCT.md CONTRIBUTING.md README.md

%global godevelheader %{expand:
Requires:  %{name} = %{version}-%{release}
}

Name: %{goname}
Release: 1%{?dist}
Summary: Podman Terminal User Interface
License: ASL 2.0
URL: %{gourl}
Source0: %{gosource}

BuildRequires: gcc
BuildRequires: golang >= 1.16.6
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: glibc-static
BuildRequires: git-core
BuildRequires: go-rpm-macros
BuildRequires: make
BuildRequires: gpgme-devel
BuildRequires: device-mapper-devel
BuildRequires: libassuan-devel
%if ! 0%{?centos}
BuildRequires: btrfs-progs-devel
%endif
%if 0%{?fedora} >= 35
BuildRequires: shadow-utils-subid-devel
%endif
BuildRequires: golang-github-docker-distribution-devel
BuildRequires: golang-github-docker-devel
BuildRequires: golang-github-docker-units-devel
BuildRequires: golang-github-pkg-errors-devel
BuildRequires: golang-github-rs-zerolog-devel
BuildRequires: golang-github-sirupsen-logrus-devel
BuildRequires: golang-github-spf13-cobra-devel
# indirect requirements
BuildRequires: golang-github-moby-term-devel
BuildRequires: golang-github-burntsushi-toml-devel
BuildRequires: golang-github-rivo-uniseg-devel
BuildRequires: golang-github-protobuf-devel
BuildRequires: golang-github-gorilla-mux-devel
BuildRequires: golang-github-gorilla-schema-devel
BuildRequires: golang-github-gdamore-encoding-devel
BuildRequires: golang-github-klauspost-compress-devel
BuildRequires: golang-github-xeipuuv-gojsonschema-devel
BuildRequires: golang-github-xeipuuv-gojsonreference-devel
BuildRequires: golang-github-xeipuuv-gojsonpointer-devel
BuildRequires: golang-github-vishvananda-netlink-devel
BuildRequires: golang-github-vishvananda-netns-devel
BuildRequires: golang-github-ulikunitz-xz-devel
BuildRequires: golang-github-syndtr-gocapability-devel
BuildRequires: golang-github-miekg-pkcs11-devel
BuildRequires: golang-github-modern-reflect2-devel
BuildRequires: golang-github-lucasb-eyer-colorful-devel
BuildRequires: golang-github-klauspost-pgzip-devel
BuildRequires: golang-github-mattn-shellwords-devel
BuildRequires: golang-github-manifoldco-promptui-devel
BuildRequires: golang-github-inconshreveable-mousetrap-devel
BuildRequires: golang-github-imdario-mergo-devel
BuildRequires: golang-github-hpcloud-tail-devel
BuildRequires: golang-github-hashicorp-multierror-devel
BuildRequires: golang-github-hashicorp-errwrap-devel
BuildRequires: golang-github-google-uuid-devel
BuildRequires: golang-github-groupcache-devel
BuildRequires: golang-github-gogo-protobuf-devel
BuildRequires: compat-golang-github-godbus-dbus-5-devel
BuildRequires: golang-github-ghodss-yaml-devel
BuildRequires: golang-gopkg-yaml-2-devel
BuildRequires: golang-github-fsnotify-devel
BuildRequires: golang-github-docker-metrics-devel
BuildRequires: golang-github-docker-connections-devel
BuildRequires: golang-github-cyphar-filepath-securejoin-devel
BuildRequires: compat-golang-github-coreos-systemd-v22-devel
BuildRequires: golang-github-beorn7-perks-devel
BuildRequires: golang-github-acarl005-stripansi-devel
BuildRequires: golang-github-containerd-cgroups-devel
BuildRequires: golang-github-containernetworking-plugins-devel
BuildRequires: golang-github-containernetworking-cni-devel
BuildRequires: golang-gopkg-square-jose-2-devel
BuildRequires: golang-github-vbatts-tar-split
BuildRequires: golang-github-tchap-patricia-devel
BuildRequires: golang-github-stefanberger-pkcs11uri-devel
BuildRequires: golang-github-opencontainers-selinux-devel
BuildRequires: golang-github-modern-concurrent-devel
BuildRequires: golang-github-blang-semver-devel
BuildRequires: golang-github-json-iterator-devel
BuildRequires: golang-github-prometheus-common-devel
BuildRequires: golang-github-prometheus-client-devel
BuildRequires: golang-github-prometheus-client-model-devel
BuildRequires: golang-github-prometheus-procfs-devel
BuildRequires: golang-github-moby-sys-devel
BuildRequires: golang-github-docker-credential-helpers-devel
BuildRequires: compat-golang-github-chzyer-readline-devel
BuildRequires: golang-github-cespare-xxhash-devel
BuildRequires: golang-github-matttproud-protobuf-extensions-devel
BuildRequires: golang-github-mistifyio-zfs-devel
BuildRequires: golang-github-opencontainers-digest-devel
BuildRequires: golang-github-opencontainers-image-spec-devel
BuildRequires: golang-github-opencontainers-runc-devel
BuildRequires: golang-github-opencontainers-runtime-spec-devel
BuildRequires: golang-github-opencontainers-runtime-tools-devel
BuildRequires: golang-github-containerd-stargz-snapshotter-estargz-devel

# bundled libraries - not available in fedora packages
Provides: bundled(golang(github.com/containerd/containerd)) = v1.5.7
Provides: bundled(golang(github.com/containers/buildah)) = v1.23.1
Provides: bundled(golang(github.com/containers/common)) = v0.44.4
Provides: bundled(golang(github.com/containers/image/v5)) = v5.17.0
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20190913040956_14b96171aa3b
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.2
Provides: bundled(golang(github.com/containers/podman/v3)) = v3.4.4
Provides: bundled(golang(github.com/containers/psgo)) = v1.7.1
Provides: bundled(golang(github.com/containers/storage)) = v1.37.0
Provides: bundled(golang(github.com/cri_o/ocicni)) = v0.2.1_0.20210621164014_d0acc7862283
Provides: bundled(golang(github.com/disiqueira/gotree/v3)) = v3.0.2
Provides: bundled(golang(github.com/gdamore/tcell/v2)) = v2.4.1_0.20210905002822_f057f0a857a1
Provides: bundled(golang(github.com/google/go_intervals)) = v0.0.2
Provides: bundled(golang(github.com/jinzhu/copier)) = v0.3.2
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.13
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.8.22
Provides: bundled(golang(github.com/mtrmac/gpgme)) = v0.1.2
Provides: bundled(golang(github.com/navidys/tvxwidgets)) = v0.1.0
Provides: bundled(golang(github.com/navidys/vtterm)) = v0.1.0
Provides: bundled(golang(github.com/ostreedev/ostree_go)) = v0.0.0_20190702140239_759a8c1ac913
Provides: bundled(golang(github.com/rivo/tview)) = v0.0.0_20220106183741_90d72bc664f5
Provides: bundled(golang(github.com/vbauerster/mpb/v7)) = v7.1.5
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0

%description
%{common_description}

%prep
%goprep

mkdir _depbundle
pushd _depbundle
/usr/bin/gzip -dc %{SOURCE0} | /usr/bin/tar -xof -
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
install -m 0755 -vd %{gobuilddir}/src/github.com/
install -m 0755 -vd %{gobuilddir}/src/github.com/vbauerster/mpb/
install -m 0755 -vd %{gobuilddir}/src/github.com/rivo
install -m 0755 -vd %{gobuilddir}/src/github.com/ostreedev
install -m 0755 -vd %{gobuilddir}/src/github.com/disiqueira/gotree
install -m 0755 -vd %{gobuilddir}/src/github.com/navidys
install -m 0755 -vd %{gobuilddir}/src/github.com/mtrmac
install -m 0755 -vd %{gobuilddir}/src/github.com/Microsoft
install -m 0755 -vd %{gobuilddir}/src/github.com/mattn
install -m 0755 -vd %{gobuilddir}/src/github.com/jinzhu
install -m 0755 -vd %{gobuilddir}/src/github.com/disiqueira/gotree
install -m 0755 -vd %{gobuilddir}/src/github.com/containers
install -m 0755 -vd %{gobuilddir}/src/github.com/cri-o
install -m 0755 -vd %{gobuilddir}/src/github.com/containerd/stargz-snapshotter
install -m 0755 -vd %{gobuilddir}/src/github.com/google
install -m 0755 -vd %{gobuilddir}/src/github.com/gdamore

# copy required bundled libraries
/bin/cp -rp %{goname}-%{version}/vendor/github.com/VividCortex %{gobuilddir}/src/github.com/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/vbauerster/mpb/v7 %{gobuilddir}/src/github.com/vbauerster/mpb/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/rivo/tview %{gobuilddir}/src/github.com/rivo/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/ostreedev/ostree-go %{gobuilddir}/src/github.com/ostreedev/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/navidys/tvxwidgets %{gobuilddir}/src/github.com/navidys/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/navidys/vtterm %{gobuilddir}/src/github.com/navidys/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/mtrmac/gpgme %{gobuilddir}/src/github.com/mtrmac/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/Microsoft/hcsshim %{gobuilddir}/src/github.com/Microsoft/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/Microsoft/go-winio %{gobuilddir}/src/github.com/Microsoft/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/mattn/go-runewidth %{gobuilddir}/src/github.com/mattn/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/jinzhu/copier %{gobuilddir}/src/github.com/jinzhu/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/google/go-intervals %{gobuilddir}/src/github.com/google/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/gdamore/tcell %{gobuilddir}/src/github.com/gdamore/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/disiqueira/gotree/v3 %{gobuilddir}/src/github.com/disiqueira/gotree/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/containers/storage %{gobuilddir}/src/github.com/containers/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/containers/psgo %{gobuilddir}/src/github.com/containers/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/containers/ocicrypt %{gobuilddir}/src/github.com/containers/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/containers/libtrust %{gobuilddir}/src/github.com/containers/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/containers/image %{gobuilddir}/src/github.com/containers/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/containers/common %{gobuilddir}/src/github.com/containers/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/containers/buildah %{gobuilddir}/src/github.com/containers/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/containers/podman %{gobuilddir}/src/github.com/containers/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/cri-o/ocicni %{gobuilddir}/src/github.com/cri-o/
/bin/cp -rp %{goname}-%{version}/vendor/github.com/containerd/containerd %{gobuilddir}/src/github.com/containerd/

popd
/bin/rm -rf _depbundle

%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}/

%install
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if 0%{?with_check}
%check
%gocheck
%endif

%files
%license %{golicenses}
%doc     
%{_bindir}/*

%changelog
%autochangelog