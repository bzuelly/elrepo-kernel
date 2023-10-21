%global major_ver 6
%global minor_ver 1
%global patch_ver 59
%global rel_ver   1

Name: kernel-lt

%global src_dir linux-%{major_ver}.%{minor_ver}.%{patch_ver}

Source1: kernel-common.inc
%include %{SOURCE1}
