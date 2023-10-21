%global major_ver 6
%global minor_ver 6
%global patch_ver 0
%global rc_ver    rc6
%global rel_ver   0

Name: kernel-rc

%global src_dir linux-%{major_ver}.%{minor_ver}-rc%{rc_ver}

Source0: https://git.kernel.org/torvalds/t/linux-%{major_ver}.%{minor_ver}-%{rc_ver}.tar.gz
Source1: kernel-common.inc
%include %{SOURCE1}
