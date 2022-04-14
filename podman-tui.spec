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
# vendored libraries
# awk '{print "Provides: bundled(golang("$1")) = "$2}' go.mod | sort | uniq | sed -e 's/-/_/g' -e '/bundled(golang())/d' -e '/bundled(golang(go\|module\|replace\|require))/d'
Provides: bundled(golang(github.com/acarl005/stripansi)) = v0.0.0_20180116102854_5a71ef0e047d
Provides: bundled(golang(github.com/Azure/go_ansiterm)) = v0.0.0_20210617225240_d185dfc1b5a1
Provides: bundled(golang(github.com/beorn7/perks)) = v1.0.1
Provides: bundled(golang(github.com/blang/semver)) = v3.5.1+incompatible
Provides: bundled(golang(github.com/BurntSushi/toml)) = v0.4.1
Provides: bundled(golang(github.com/cespare/xxhash/v2)) = v2.1.2
Provides: bundled(golang(github.com/chzyer/readline)) = v0.0.0_20180603132655_2972be24d48e
Provides: bundled(golang(github.com/containerd/cgroups)) = v1.0.1
Provides: bundled(golang(github.com/containerd/containerd)) = v1.5.7
Provides: bundled(golang(github.com/containerd/stargz_snapshotter/estargz)) = v0.9.0
Provides: bundled(golang(github.com/containernetworking/cni)) = v0.8.1
Provides: bundled(golang(github.com/containernetworking/plugins)) = v0.9.1
Provides: bundled(golang(github.com/containers/buildah)) = v1.23.1
Provides: bundled(golang(github.com/containers/common)) = v0.44.4
Provides: bundled(golang(github.com/containers/image/v5)) = v5.17.0
Provides: bundled(golang(github.com/containers/libtrust)) = v0.0.0_20190913040956_14b96171aa3b
Provides: bundled(golang(github.com/containers/ocicrypt)) = v1.1.2
Provides: bundled(golang(github.com/containers/podman/v3)) = v3.4.4
Provides: bundled(golang(github.com/containers/psgo)) = v1.7.1
Provides: bundled(golang(github.com/containers/storage)) = v1.37.0
Provides: bundled(golang(github.com/coreos/go_systemd/v22)) = v22.3.2
Provides: bundled(golang(github.com/cri_o/ocicni)) = v0.2.1_0.20210621164014_d0acc7862283
Provides: bundled(golang(github.com/cyphar/filepath_securejoin)) = v0.2.3
Provides: bundled(golang(github.com/disiqueira/gotree/v3)) = v3.0.2
Provides: bundled(golang(github.com/docker/distribution)) = v2.7.1+incompatible
Provides: bundled(golang(github.com/docker/docker_credential_helpers)) = v0.6.4
Provides: bundled(golang(github.com/docker/docker)) = v20.10.12+incompatible
Provides: bundled(golang(github.com/docker/go_connections)) = v0.4.0
Provides: bundled(golang(github.com/docker/go_metrics)) = v0.0.1
Provides: bundled(golang(github.com/docker/go_units)) = v0.4.0
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = v1.5.1
Provides: bundled(golang(github.com/gdamore/encoding)) = v1.0.0
Provides: bundled(golang(github.com/gdamore/tcell/v2)) = v2.4.1_0.20210905002822_f057f0a857a1
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/godbus/dbus/v5)) = v5.0.6
Provides: bundled(golang(github.com/gogo/protobuf)) = v1.3.2
Provides: bundled(golang(github.com/golang/groupcache)) = v0.0.0_20210331224755_41bb18bfe9da
Provides: bundled(golang(github.com/golang/protobuf)) = v1.5.2
Provides: bundled(golang(github.com/google/go_intervals)) = v0.0.2
Provides: bundled(golang(github.com/google/uuid)) = v1.3.0
Provides: bundled(golang(github.com/gorilla/mux)) = v1.8.0
Provides: bundled(golang(github.com/gorilla/schema)) = v1.2.0
Provides: bundled(golang(github.com/hashicorp/errwrap)) = v1.0.0
Provides: bundled(golang(github.com/hashicorp/go_multierror)) = v1.1.1
Provides: bundled(golang(github.com/hpcloud/tail)) = v1.0.0
Provides: bundled(golang(github.com/imdario/mergo)) = v0.3.12
Provides: bundled(golang(github.com/inconshreveable/mousetrap)) = v1.0.0
Provides: bundled(golang(github.com/jinzhu/copier)) = v0.3.2
Provides: bundled(golang(github.com/json_iterator/go)) = v1.1.12
Provides: bundled(golang(github.com/klauspost/compress)) = v1.13.6
Provides: bundled(golang(github.com/klauspost/pgzip)) = v1.2.5
Provides: bundled(golang(github.com/lucasb_eyer/go_colorful)) = v1.2.0
Provides: bundled(golang(github.com/manifoldco/promptui)) = v0.9.0
Provides: bundled(golang(github.com/mattn/go_runewidth)) = v0.0.13
Provides: bundled(golang(github.com/mattn/go_shellwords)) = v1.0.12
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = v1.0.2_0.20181231171920_c182affec369
Provides: bundled(golang(github.com/Microsoft/go_winio)) = v0.5.0
Provides: bundled(golang(github.com/Microsoft/hcsshim)) = v0.8.22
Provides: bundled(golang(github.com/miekg/pkcs11)) = v1.0.3
Provides: bundled(golang(github.com/mistifyio/go_zfs)) = v2.1.2_0.20190413222219_f784269be439+incompatible
Provides: bundled(golang(github.com/moby/sys/mountinfo)) = v0.4.1
Provides: bundled(golang(github.com/moby/term)) = v0.0.0_20210619224110_3f7ff695adc6
Provides: bundled(golang(github.com/modern_go/concurrent)) = v0.0.0_20180306012644_bacd9c7ef1dd
Provides: bundled(golang(github.com/modern_go/reflect2)) = v1.0.2
Provides: bundled(golang(github.com/mtrmac/gpgme)) = v0.1.2
Provides: bundled(golang(github.com/navidys/tvxwidgets)) = v0.1.0
Provides: bundled(golang(github.com/navidys/vtterm)) = v0.1.0
Provides: bundled(golang(github.com/opencontainers/go_digest)) = v1.0.0
Provides: bundled(golang(github.com/opencontainers/image_spec)) = v1.0.2_0.20210819154149_5ad6f50d6283
Provides: bundled(golang(github.com/opencontainers/runc)) = v1.0.2
Provides: bundled(golang(github.com/opencontainers/runtime_spec)) = v1.0.3_0.20210326190908_1c3f411f0417
Provides: bundled(golang(github.com/opencontainers/runtime_tools)) = v0.9.0
Provides: bundled(golang(github.com/opencontainers/selinux)) = v1.9.1
Provides: bundled(golang(github.com/ostreedev/ostree_go)) = v0.0.0_20190702140239_759a8c1ac913
Provides: bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides: bundled(golang(github.com/prometheus/client_golang)) = v1.7.1
Provides: bundled(golang(github.com/prometheus/client_model)) = v0.2.0
Provides: bundled(golang(github.com/prometheus/common)) = v0.10.0
Provides: bundled(golang(github.com/prometheus/procfs)) = v0.6.0
Provides: bundled(golang(github.com/rivo/tview)) = v0.0.0_20220106183741_90d72bc664f5
Provides: bundled(golang(github.com/rivo/uniseg)) = v0.2.0
Provides: bundled(golang(github.com/rs/zerolog)) = v1.26.1
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.8.1
Provides: bundled(golang(github.com/spf13/cobra)) = v1.3.0
Provides: bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides: bundled(golang(github.com/stefanberger/go_pkcs11uri)) = v0.0.0_20201008174630_78d3cae3a980
Provides: bundled(golang(github.com/syndtr/gocapability)) = v0.0.0_20200815063812_42c35b437635
Provides: bundled(golang(github.com/tchap/go_patricia)) = v2.3.0+incompatible
Provides: bundled(golang(github.com/ulikunitz/xz)) = v0.5.10
Provides: bundled(golang(github.com/vbatts/tar_split)) = v0.11.2
Provides: bundled(golang(github.com/vbauerster/mpb/v7)) = v7.1.5
Provides: bundled(golang(github.com/vishvananda/netlink)) = v1.1.1_0.20201029203352_d40f9887b852
Provides: bundled(golang(github.com/vishvananda/netns)) = v0.0.0_20200728191858_db3c7e526aae
Provides: bundled(golang(github.com/VividCortex/ewma)) = v1.2.0
Provides: bundled(golang(github.com/xeipuuv/gojsonpointer)) = v0.0.0_20190809123943_df4f5c81cb3b
Provides: bundled(golang(github.com/xeipuuv/gojsonreference)) = v0.0.0_20180127040603_bd5ef7bd5415
Provides: bundled(golang(github.com/xeipuuv/gojsonschema)) = v1.2.0

%description
%{common_description}

%prep
%goprep

mkdir _depbundle
pushd _depbundle
/usr/bin/gzip -dc %{SOURCE0} | /usr/bin/tar -xof -
/usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
%{__install} -m 0755 -vd %{gobuilddir}/src/
# copy required bundled libraries
%{__cp} -rp %{goname}-%{version}/vendor/* %{gobuilddir}/src/
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