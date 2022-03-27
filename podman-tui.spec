%global with_check 0
%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global goipath github.com/containers/podman-tui
Version: 0.3.0
%global tag v0.3.0
%gometa

%global goname podman-tui

%global common_description %{expand:
%{goname} is a terminal user interface for Podman v4.
%{goname} is using podman.socket service to communicate with podman environment
and SSH to connect to remote podman machines.
}

%global golicenses LICENSE
%global godocs CODE-OF-CONDUCT.md CONTRIBUTING.md README.md

%global godevelheader %{expand:
Requires:  %{name} = %{version}-%{release}
}

Name: %{goname}
Release: %autorelease
Summary: Podman Terminal User Interface
License: ASL 2.0 and BSD and ISC and MIT and MPLv2.0
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
BuildRequires: golang-github-beorn7-perks-devel
BuildRequires: golang-github-acarl005-stripansi-devel
BuildRequires: golang-github-containerd-cgroups-devel
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
Provides: bundled(golang(github.com/containerd/containerd)) = v1.5.9
Provides: bundled(golang(github.com/containers/buildah)) = v1.24.1
Provides: bundled(golang(github.com/containers/common)) = v0.47.5
Provides: bundled(golang(github.com/containers/image/v5)) = v5.19.1
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20190913040956_14b96171aa3b
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.2
Provides: bundled(golang(github.com/containers/podman/v4)) = v4.0.2
Provides: bundled(golang(github.com/containers/psgo)) = v1.7.2
Provides: bundled(golang(github.com/containers/storage)) = v1.38.2
Provides: bundled(golang(github.com/disiqueira/gotree/v3)) = v3.0.2
Provides: bundled(golang(github.com/gdamore/tcell/v2)) = v2.4.1_0.20210905002822_f057f0a857a1
Provides: bundled(golang(github.com/google/go_intervals)) = v0.0.2
Provides: bundled(golang(github.com/jinzhu/copier)) = v0.3.5
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.13
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.9.2
Provides: bundled(golang(github.com/navidys/tvxwidgets)) = v0.1.0
Provides: bundled(golang(github.com/navidys/vtterm)) = v0.1.0
Provides: bundled(golang(github.com/ostreedev/ostree_go)) = v0.0.0_20190702140239_759a8c1ac913
Provides: bundled(golang(github.com/rivo/tview)) = v0.0.0_20220307222120_9994674d60a8
Provides: bundled(golang(github.com/vbauerster/mpb/v7)) = v7.3.2
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/beorn7/perks)) = v1.0.1
Provides: bundled(golang(github.com/proglottis/gpgme)) = v0.1.1
Provides: bundled(golang(github.com/sylabs/sif/v2)) = v2.3.1

%description
%{common_description}

%prep
%goprep

mkdir _depbundle
pushd _depbundle
/usr/bin/gzip -dc %{SOURCE0} | /usr/bin/tar -xof -
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/vbauerster/mpb/
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/rivo
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/ostreedev
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/disiqueira/gotree
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/navidys
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/Microsoft
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/mattn
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/jinzhu
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/disiqueira/gotree
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/containers
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/containerd/stargz-snapshotter
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/google
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/gdamore
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/beorn7
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/proglottis
%{__install} -m 0755 -vd %{gobuilddir}/src/github.com/sylabs

# copy required bundled libraries
%{__cp} -rp %{goname}-%{version}/vendor/github.com/VividCortex %{gobuilddir}/src/github.com/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/vbauerster/mpb/v7 %{gobuilddir}/src/github.com/vbauerster/mpb/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/rivo/tview %{gobuilddir}/src/github.com/rivo/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/ostreedev/ostree-go %{gobuilddir}/src/github.com/ostreedev/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/navidys/tvxwidgets %{gobuilddir}/src/github.com/navidys/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/navidys/vtterm %{gobuilddir}/src/github.com/navidys/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/Microsoft/hcsshim %{gobuilddir}/src/github.com/Microsoft/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/Microsoft/go-winio %{gobuilddir}/src/github.com/Microsoft/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/mattn/go-runewidth %{gobuilddir}/src/github.com/mattn/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/jinzhu/copier %{gobuilddir}/src/github.com/jinzhu/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/google/go-intervals %{gobuilddir}/src/github.com/google/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/gdamore/tcell %{gobuilddir}/src/github.com/gdamore/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/disiqueira/gotree/v3 %{gobuilddir}/src/github.com/disiqueira/gotree/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/containers/storage %{gobuilddir}/src/github.com/containers/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/containers/psgo %{gobuilddir}/src/github.com/containers/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/containers/ocicrypt %{gobuilddir}/src/github.com/containers/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/containers/libtrust %{gobuilddir}/src/github.com/containers/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/containers/image %{gobuilddir}/src/github.com/containers/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/containers/common %{gobuilddir}/src/github.com/containers/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/containers/buildah %{gobuilddir}/src/github.com/containers/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/containers/podman %{gobuilddir}/src/github.com/containers/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/containerd/containerd %{gobuilddir}/src/github.com/containerd/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/beorn7/perks %{gobuilddir}/src/github.com/beorn7/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/proglottis/gpgme %{gobuilddir}/src/github.com/proglottis/
%{__cp} -rp %{goname}-%{version}/vendor/github.com/sylabs/sif %{gobuilddir}/src/github.com/sylabs/

popd
%{_bindir}/rm -rf _depbundle

%build
%gobuild -o %{gobuilddir}/bin/%{goname} %{goipath}/

%install
%{__install} -m 0755 -vd %{buildroot}%{_bindir}
%{__install} -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

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