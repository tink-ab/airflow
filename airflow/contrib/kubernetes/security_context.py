# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


class SecurityContext:
    """Defines Kubernetes Security Context"""

    def __init__(self, run_as_non_root=None, read_only_root_filesystem=None,  run_as_user=None, run_as_group=None, fs_group=None):
        """Initialize a Kubernetes Security context for a pod.
        :param run_as_non_root: If container shall run as non root.
        :type run_as_non_root: bool
        :param read_only_root_filesystem: If container root filesystem shall be readonly.
        :type read_only_root_filesystem: bool
        :param run_as_user: uid to run container as.
        :type run_as_user: int
        :param run_as_group: gid to run container as.
        :type run_as_group: int
        :param fs_group: group owner (guid) of files.
        :type fs_group: int
        """
        self.run_as_non_root = run_as_non_root
        self.read_only_root_filesystem = read_only_root_filesystem
        self.run_as_user = run_as_user
        self.run_as_group = run_as_group
        self.fs_group = fs_group
