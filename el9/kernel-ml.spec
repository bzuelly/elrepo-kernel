%global major_ver 6
%global minor_ver 5
%global patch_ver 8
%global rel_ver   1

Name: kernel-ml

%global src_dir linux-%{major_ver}.%{minor_ver}.%{patch_ver}

Source1: kernel-common.inc
%include %{SOURCE1}
