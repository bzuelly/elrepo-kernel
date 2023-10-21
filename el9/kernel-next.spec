%global major_ver 6
%global minor_ver 6
%global patch_ver 0
%global next_snapshot_date 20231020
%global rel_ver   1

Name: kernel-next

%global src_dir linux-next-next-%{next_snapshot_date}

Source0: https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/snapshot/linux-next-next-%{next_snapshot_date}.tar.gz
Source1: kernel-common.inc
%include %{SOURCE1}
