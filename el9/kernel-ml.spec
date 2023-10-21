# Define the version of the Linux Kernel Archive tarball.
%global major_ver 6
%global minor_ver 5
%global patch_ver 8
%global LKAver %{major_ver}.%{minor_ver}.%{patch_ver}
%global pkg_version %{LKAver}

# Define the buildid, if required.
#global buildid .local

# Set pkg_release.
%global pkg_release 1%{?buildid}%{?dist}

%global KVERREL %{pkg_version}-%{pkg_release}.%{_target_cpu}

Name: kernel-ml

%include kernel-common.inc
